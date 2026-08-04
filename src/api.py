"""Nebullar AI Assistant —— FastAPI 后端 + SSE 流式输出

运行：uvicorn src.api:app --reload --port 8501

API 端点：
- POST /chat/stream - SSE 流式对话（打字机效果）
- POST /chat - 非流式对话（一次性返回）
- GET /health - 健康检查
- GET /config - 获取当前配置（模型、提供方）
"""

import json
import asyncio
import os
from typing import AsyncGenerator, List, Dict, Any, Optional
from datetime import datetime

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# 修正导入路径
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agent import MODEL, ask_structured_stream
from llm import PROVIDER


# ========== Pydantic 模型 ==========

class ChatMessage(BaseModel):
    """单条消息"""
    role: str  # "user" | "assistant"
    content: str


class ChatRequest(BaseModel):
    """对话请求"""
    query: str
    history: List[ChatMessage] = []


class ChatResponse(BaseModel):
    """非流式对话响应"""
    answer: str
    tools_used: List[str] = []
    error: Optional[Dict[str, Any]] = None
    cases: List[Dict] = []
    sources: List[Dict] = []


class ConfigResponse(BaseModel):
    """配置信息"""
    model: str
    provider: str
    version: str = "1.0.0"


# ========== FastAPI 应用 ==========

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = FastAPI(
    title="Nebullar AI Assistant API",
    description="部门级 FAE 技术支持助手 - FastAPI 后端",
    version="1.0.0"
)

# 挂载静态文件
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "ok", "timestamp": datetime.now().isoformat()}


@app.get("/config", response_model=ConfigResponse)
async def get_config():
    """获取当前配置"""
    return ConfigResponse(
        model=MODEL,
        provider=PROVIDER
    )


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    非流式对话接口

    示例请求：
    {
        "query": "刷卡返回 -70004 怎么排查？",
        "history": []
    }
    """
    try:
        # 转换 history 格式
        history = [{"role": msg.role, "content": msg.content} for msg in request.history]

        # 调用 Agent
        result = None
        for kind, payload in ask_structured_stream(request.query, history=history):
            if kind == "done":
                result = payload
                break

        if result is None:
            raise HTTPException(status_code=500, detail="Agent 返回结果为空")

        # 确保所有字符串是有效的 UTF-8
        def sanitize(obj):
            if isinstance(obj, str):
                return obj.encode('utf-8', errors='ignore').decode('utf-8')
            elif isinstance(obj, dict):
                return {k: sanitize(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [sanitize(item) for item in obj]
            return obj

        sanitized_result = sanitize(result)

        return ChatResponse(
            answer=sanitized_result["answer"],
            tools_used=sanitized_result.get("tools_used", []),
            error=sanitized_result.get("error"),
            cases=sanitized_result.get("cases", []),
            sources=sanitized_result.get("sources", [])
        )

    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Error in chat: {e}")
        print(error_detail)
        raise HTTPException(status_code=500, detail=f"{str(e)}\n\n{error_detail}")


async def generate_stream(query: str, history: List[Dict]) -> AsyncGenerator[str, None]:
    """
    SSE 流式生成器

    事件类型：
    - progress: 节点进度更新
    - content: 回答内容片段（打字机效果）
    - done: 完成，返回完整结果
    - error: 错误
    """
    try:
        # 发送初始连接确认
        yield json.dumps({"event": "connected", "timestamp": datetime.now().isoformat()}) + "\n"

        result = None

        # 调用 Agent 流式接口
        for kind, payload in ask_structured_stream(query, history=history):
            if kind == "progress":
                # 进度更新
                yield json.dumps({
                    "event": "progress",
                    "data": payload
                }) + "\n"

            elif kind == "done":
                result = payload
                # 发送完成事件
                yield json.dumps({
                    "event": "done",
                    "data": {
                        "answer": result["answer"],
                        "tools_used": result.get("tools_used", []),
                        "error": result.get("error"),
                        "cases": result.get("cases", []),
                        "sources": result.get("sources", [])
                    }
                }) + "\n"

        # 如果没有收到 done 事件，可能是出错
        if result is None:
            yield json.dumps({
                "event": "error",
                "data": "Agent 未返回结果"
            }) + "\n"

    except Exception as e:
        yield json.dumps({
            "event": "error",
            "data": str(e)
        }) + "\n"


@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    """
    SSE 流式对话接口

    前端用 EventSource 连接，实时接收：
    - progress: 节点进度
    - done: 完成 + 完整结果
    - error: 错误信息

    示例：
    const eventSource = new EventSource('/chat/stream');
    eventSource.onmessage = (e) => {
        const data = JSON.parse(e.data);
        if (data.event === 'progress') console.log('进度:', data.data);
        if (data.event === 'done') console.log('完成:', data.data.answer);
    };
    """
    # 转换 history 格式
    history = [{"role": msg.role, "content": msg.content} for msg in request.history]

    return StreamingResponse(
        generate_stream(request.query, history),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"  # 禁用 Nginx 缓冲
        }
    )


@app.get("/")
async def root():
    """API 根路径"""
    return {
        "name": "Nebullar AI Assistant API",
        "version": "1.0.0",
        "endpoints": {
            "chat": "/chat (POST) - 非流式对话",
            "chat_stream": "/chat/stream (POST) - SSE 流式对话",
            "config": "/config (GET) - 配置信息",
            "health": "/health (GET) - 健康检查"
        },
        "docs": "/docs (Swagger UI)"
    }


# ========== 启动入口 ==========

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8501)
