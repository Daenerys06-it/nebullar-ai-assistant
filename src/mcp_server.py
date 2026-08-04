"""MCP Server: 将Nebullar工具标准化暴露给任意LLM客户端

MCP (Model Context Protocol) 是Anthropic推出的开放协议，
用于标准化LLM与外部工具/数据源的交互。

运行方式:
    1. stdio模式 (本地): python mcp_server.py
    2. SSE模式 (服务): python mcp_server.py --transport sse --port 8000

Claude Desktop配置示例:
    {
        "mcpServers": {
            "nebullar": {
                "command": "python",
                "args": ["/path/to/mcp_server.py"],
                "env": {
                    "LLM_PROVIDER": "kimi",
                    "KIMI_API_KEY": "sk-xxx"
                }
            }
        }
    }
"""

import os
import sys
import json
import asyncio
from typing import Any, Optional
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

# 强制离线模式（公司网络）
os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")

# 将src加入路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "src"))

# MCP SDK
try:
    from mcp.server.fastmcp import FastMCP, Context
    from mcp.types import TextContent, ImageContent
except ImportError:
    print("Error: mcp package not installed. Run: pip install mcp", file=sys.stderr)
    sys.exit(1)

# 项目内部模块
from memory import search_cases as _search_cases, get_all_case_keywords
from retrieve import search as _search_docs
from llm import create_client, complete


# ============ 生命周期管理 ============

class ServerContext:
    """服务器生命周期上下文"""
    def __init__(self):
        self.llm_client = None
        self.llm_model = None
        self.stats = {
            "total_calls": 0,
            "tool_calls": {},
        }

    async def initialize(self):
        """初始化LLM客户端"""
        provider = os.getenv("LLM_PROVIDER", "kimi")
        self.llm_client, self.llm_model = create_client(provider)


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[ServerContext]:
    """应用生命周期管理"""
    ctx = ServerContext()
    await ctx.initialize()
    print(f"[MCP Server] Initialized with model: {ctx.llm_model}", file=sys.stderr)
    try:
        yield ctx
    finally:
        print("[MCP Server] Shutting down...", file=sys.stderr)


# ============ 创建 MCP Server ============

mcp = FastMCP(
    "nebullar-fae-assistant",
    description="Nebullar FAE技术支持助手 - 提供文档检索、错误码查询、案例检索、翻译等工具",
    lifespan=app_lifespan,
)


# ============ 工具定义 ============

@mcp.tool()
async def search_docs(
    query: str,
    top_k: int = 5,
    product: Optional[str] = None,
    ctx: Context = None,
) -> str:
    """搜索Nebullar技术文档，检索SDK使用说明、API文档等。

    Args:
        query: 搜索查询，如"如何初始化Scanner"、"EMV操作流程"
        top_k: 返回结果数量 (1-10)
        product: 限定产品范围，如"financial_sdk"、"terminal_manager_sdk"

    Returns:
        JSON格式的检索结果，包含相关文档片段及其元数据
    """
    if ctx:
        ctx.info(f"Searching docs: {query[:50]}...")

    try:
        results = _search_docs(query, top_k=top_k)

        # 过滤产品（如果指定）
        if product:
            results = [r for r in results if product.lower() in r.get("product", "").lower()]

        # 格式化输出
        formatted = []
        for i, r in enumerate(results, 1):
            formatted.append({
                "rank": i,
                "content": r.get("content", "")[:500],  # 截断长内容
                "product": r.get("product", ""),
                "module": r.get("module", ""),
                "score": r.get("rerank_score", r.get("rrf_score", 0)),
            })

        if ctx:
            ctx.request_context.session

        return json.dumps({
            "query": query,
            "total": len(formatted),
            "results": formatted,
        }, ensure_ascii=False, indent=2)

    except Exception as e:
        return json.dumps({"error": str(e), "query": query}, ensure_ascii=False)


@mcp.tool()
async def lookup_error(
    error_code: str,
    ctx: Context = None,
) -> str:
    """查询错误码的详细说明和解决方案。

    支持的错误码格式:
    - SDK错误码: ERR_SCANNER_TIMEOUT, ERR_CARD_READ_FAILED
    - 系统错误码: 0xC0060003, STATUS_BROM_CMD_SEND_DA_FAIL
    - HTTP状态码: 400, 401, 500

    Args:
        error_code: 错误码字符串

    Returns:
        错误码的详细说明、可能原因和解决方案
    """
    if ctx:
        ctx.info(f"Looking up error code: {error_code}")

    try:
        # 加载错误码表
        error_db_path = os.path.join(BASE_DIR, "data", "error_codes.json")
        if os.path.exists(error_db_path):
            with open(error_db_path, "r", encoding="utf-8") as f:
                error_db = json.load(f)
        else:
            error_db = {}

        # 精确匹配
        if error_code in error_db:
            info = error_db[error_code]
            return json.dumps({
                "found": True,
                "error_code": error_code,
                "description": info.get("description", ""),
                "cause": info.get("cause", ""),
                "solution": info.get("solution", ""),
                "severity": info.get("severity", "unknown"),
            }, ensure_ascii=False, indent=2)

        # 模糊匹配（尝试忽略大小写）
        for key, info in error_db.items():
            if key.lower() == error_code.lower():
                return json.dumps({
                    "found": True,
                    "error_code": key,
                    "description": info.get("description", ""),
                    "cause": info.get("cause", ""),
                    "solution": info.get("solution", ""),
                    "severity": info.get("severity", "unknown"),
                }, ensure_ascii=False, indent=2)

        # 未找到
        return json.dumps({
            "found": False,
            "error_code": error_code,
            "message": f"未找到错误码 '{error_code}' 的信息。请检查拼写或联系技术支持。",
            "available_prefixes": list(set(k.split("_")[0] for k in error_db.keys()))[:10],
        }, ensure_ascii=False, indent=2)

    except Exception as e:
        return json.dumps({"error": str(e), "error_code": error_code}, ensure_ascii=False)


@mcp.tool()
async def search_cases(
    symptom: str,
    top_k: int = 3,
    ctx: Context = None,
) -> str:
    """搜索历史FAE支持案例，获取类似问题的解决方案。

    案例库包含26+条真实技术支持记录，覆盖:
    - 刷机问题 (D5/P18/K1)
    - 写号/配置问题
    - ADB连接问题
    - 设备初始化问题

    Args:
        symptom: 问题症状描述，如"P18刷机超时"、"adb连不上设备"
        top_k: 返回最相似的案例数量 (1-5)

    Returns:
        相似案例列表，包含症状、根本原因和解决方案
    """
    if ctx:
        ctx.info(f"Searching cases: {symptom[:50]}...")

    try:
        results = _search_cases(symptom, top_k=top_k)

        formatted = []
        for i, r in enumerate(results, 1):
            formatted.append({
                "rank": i,
                "case_id": r.get("id", ""),
                "product": r.get("product", ""),
                "module": r.get("module", ""),
                "symptom": r.get("symptom", ""),
                "root_cause": r.get("root_cause", ""),
                "solution": r.get("solution", ""),
                "similarity": r.get("similarity", 0),
                "time_cost": r.get("time_cost_min", 0),
            })

        return json.dumps({
            "query": symptom,
            "total": len(formatted),
            "cases": formatted,
        }, ensure_ascii=False, indent=2)

    except Exception as e:
        return json.dumps({"error": str(e), "query": symptom}, ensure_ascii=False)


@mcp.tool()
async def translate(
    text: str,
    target_language: str = "en",
    ctx: Context = None,
) -> str:
    """中英技术文档互译。

    专为Nebullar SDK技术术语优化，支持:
    - 中文 → 英文 (技术文档、邮件)
    - 英文 → 中文 (客户问题、文档理解)

    Args:
        text: 待翻译文本
        target_language: 目标语言，"en"(英文) 或 "zh"(中文)

    Returns:
        翻译后的文本
    """
    if ctx:
        ctx.info(f"Translating to {target_language}: {text[:50]}...")

    try:
        server_ctx: ServerContext = ctx.request_context.lifespan_context

        if target_language.lower() in ["en", "english", "英文"]:
            system = """你是专业的技术文档翻译，将中文技术内容翻译成英文。
要求：
1. 保留所有技术术语和代码片段不翻译
2. 使用正式的商务英语风格
3. 确保SDK相关术语准确（如 Scanner, EMV, Terminal Manager）
4. 只输出翻译结果，不添加解释"""
        else:
            system = """你是专业的技术文档翻译，将英文技术内容翻译成中文。
要求：
1. 保留所有技术术语和代码片段不翻译
2. 使用简洁的技术文档风格
3. SDK相关术语保持英文（如 Scanner, EMV, Terminal Manager）
4. 只输出翻译结果，不添加解释"""

        result = complete(server_ctx.llm_client, server_ctx.llm_model, system, text)

        return json.dumps({
            "original": text,
            "translated": result.strip(),
            "target_language": target_language,
        }, ensure_ascii=False, indent=2)

    except Exception as e:
        return json.dumps({"error": str(e)}, ensure_ascii=False)


@mcp.tool()
async def get_device_flash_guide(
    device_model: str,
    ctx: Context = None,
) -> str:
    """获取指定设备的刷机/固件升级指南。

    支持设备:
    - D0551/D0552/D5 (使用SP Flash Tool V5)
    - P18 (使用FlashToolSelector)
    - K1 (使用FlashToolSelector)

    Args:
        device_model: 设备型号，如"D0551"、"P18"、"K1"

    Returns:
        该设备的详细刷机步骤和注意事项
    """
    if ctx:
        ctx.info(f"Getting flash guide for: {device_model}")

    guides = {
        "d0551": {
            "tool": "SP Flash Tool V5",
            "mode": "Firmware Upgrade (正常刷机，无需格式化)",
            "steps": [
                "安装驱动：运行 DriverInstall.exe（只需做一次）",
                "打开 SP_Flash_Tool_V5，进入 Download 页面",
                "选择 MTK_AllInOne_DA.bin",
                "选择 scatter file (.txt)",
                "选择 Firmware Upgrade 模式",
                "USB线先连设备（不接电源），点击 Download，再插电脑USB",
                "等待刷机完成",
            ],
            "notes": ["这是正常刷机，不是格式化。失败时才用Format", "D0551支持安卓15和安卓13"],
        },
        "d0552": {
            "tool": "SP Flash Tool V5",
            "mode": "Firmware Upgrade 或 Format",
            "steps": [
                "安装驱动：运行 DriverInstall.exe（只需做一次）",
                "打开 SP_Flash_Tool_V5，进入 Download 页面",
                "选择 MTK_AllInOne_DA.bin",
                "选择 scatter file (.txt)",
                "选择 Firmware Upgrade 模式（如需清空数据选Format）",
                "USB线先连设备（不接电源），点击 Download，再插电脑USB",
                "等待刷机完成",
            ],
            "notes": ["D0552不支持安卓15，只能刷安卓13", "与D0551有互刷机制"],
        },
        "p18": {
            "tool": "FlashToolSelector",
            "mode": "Format 或 固件升级",
            "steps": [
                "安装驱动：运行 DriverInstall.exe（只需做一次）",
                "打开 FlashToolSelector",
                "选择 download_agent 文件夹下的 flash.xml",
                "选择模式：Format（清空数据）或 固件升级（保留数据）",
                "按提示完成刷机",
            ],
            "notes": ["刷机前确保电量充足，避免data_mux超时", "与K1步骤完全相同"],
        },
        "k1": {
            "tool": "FlashToolSelector",
            "mode": "Format 或 固件升级",
            "steps": [
                "安装驱动：运行 DriverInstall.exe（只需做一次）",
                "打开 FlashToolSelector",
                "选择 download_agent 文件夹下的 flash.xml",
                "选择模式：Format（清空数据）或 固件升级（保留数据）",
                "按提示完成刷机",
            ],
            "notes": ["与P18步骤完全相同", "刷机前确保电量充足"],
        },
    }

    key = device_model.lower()
    if key in guides:
        guide = guides[key]
        return json.dumps({
            "device": device_model,
            "found": True,
            "tool": guide["tool"],
            "mode": guide["mode"],
            "steps": guide["steps"],
            "notes": guide["notes"],
        }, ensure_ascii=False, indent=2)
    else:
        return json.dumps({
            "device": device_model,
            "found": False,
            "supported_devices": list(guides.keys()),
            "message": f"暂不支持设备 '{device_model}'，请检查型号或使用 search_cases 搜索相关问题。",
        }, ensure_ascii=False, indent=2)


@mcp.tool()
async def list_available_tools(ctx: Context = None) -> str:
    """列出所有可用工具及其用途。"""
    tools_info = {
        "search_docs": "搜索技术文档 (SDK/API文档)",
        "lookup_error": "查询错误码说明",
        "search_cases": "搜索历史支持案例",
        "translate": "中英技术翻译",
        "get_device_flash_guide": "获取设备刷机指南",
        "list_available_tools": "列出所有工具（本工具）",
    }
    return json.dumps(tools_info, ensure_ascii=False, indent=2)


# ============ 主入口 ============

def main():
    """启动 MCP Server"""
    import argparse

    parser = argparse.ArgumentParser(description="Nebullar MCP Server")
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse"],
        default="stdio",
        help="传输方式: stdio(默认，用于Claude Desktop) 或 sse(HTTP服务)",
    )
    parser.add_argument("--port", type=int, default=8000, help="SSE模式端口")
    parser.add_argument("--host", default="127.0.0.1", help="SSE模式主机")

    args = parser.parse_args()

    if args.transport == "stdio":
        # stdio模式：用于Claude Desktop等本地客户端
        mcp.run(transport="stdio")
    else:
        # SSE模式：作为HTTP服务运行
        print(f"[MCP Server] Starting SSE server on {args.host}:{args.port}", file=sys.stderr)
        mcp.run(transport="sse", host=args.host, port=args.port)


if __name__ == "__main__":
    main()
