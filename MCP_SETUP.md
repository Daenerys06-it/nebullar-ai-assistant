# MCP (Model Context Protocol) 配置指南

## 安装依赖

```bash
pip install mcp>=1.0.0
```

## 启动 MCP Server

### 方式1: stdio 模式 (推荐，用于 Claude Desktop)

```bash
# 直接运行
python src/mcp_server.py

# 或带环境变量
LLM_PROVIDER=kimi python src/mcp_server.py
```

### 方式2: SSE 模式 (HTTP服务)

```bash
python src/mcp_server.py --transport sse --port 8000
```

## Claude Desktop 配置

编辑 `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac)
或 `%APPDATA%/Claude/claude_desktop_config.json` (Windows):

```json
{
    "mcpServers": {
        "nebullar": {
            "command": "python",
            "args": [
                "D:/Nebullar-ai-assistant/src/mcp_server.py"
            ],
            "env": {
                "LLM_PROVIDER": "kimi",
                "KIMI_BASE_URL": "http://10.10.5.136:8080",
                "KIMI_API_KEY": "sk-your-key",
                "KIMI_MODEL": "kimi-k2.5"
            }
        }
    }
}
```

## 可用工具列表

| 工具名 | 功能描述 | 示例调用 |
|--------|----------|----------|
| `search_docs` | 搜索技术文档 | search_docs("Scanner初始化") |
| `lookup_error` | 查询错误码 | lookup_error("0xC0060003") |
| `search_cases` | 搜索历史案例 | search_cases("P18刷机超时") |
| `translate` | 中英翻译 | translate("Hello", "zh") |
| `get_device_flash_guide` | 设备刷机指南 | get_device_flash_guide("D0551") |
| `list_available_tools` | 列出所有工具 | list_available_tools() |

## 测试 MCP Server

```python
# test_mcp_client.py
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test():
    params = StdioServerParameters(
        command="python",
        args=["src/mcp_server.py"],
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 列出工具
            tools = await session.list_tools()
            print("可用工具:", [t.name for t in tools.tools])

            # 调用工具
            result = await session.call_tool(
                "get_device_flash_guide",
                {"device_model": "D0551"}
            )
            print(result)

asyncio.run(test())
```

## 重新索引文档 (使用新Chunking)

```bash
# 1. 删除旧索引（可选）
rm -rf chroma_db/

# 2. 重新入库
python src/ingest.py

# 预期输出:
#   [financial_sdk/scanner] 12 chunks (types: {'text', 'code'})
#   ...
# ✅ Done: XXX chunks indexed in 'nebullar_docs'
```

## 架构图

```
┌─────────────────────────────────────────────────────────────┐
│                     Claude Desktop / MCP Client             │
└──────────────────────────┬──────────────────────────────────┘
                           │ stdio / SSE
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    MCP Server (mcp_server.py)               │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────────┐   │
│  │ search_docs │  │ lookup_error │  │ search_cases     │   │
│  └──────┬──────┘  └──────┬───────┘  └────────┬─────────┘   │
│         └─────────────────┼───────────────────┘             │
│                           ▼                                 │
│              ┌─────────────────────────┐                    │
│              │   ChromaDB / Cases DB   │                    │
│              └─────────────────────────┘                    │
└─────────────────────────────────────────────────────────────┘
```
