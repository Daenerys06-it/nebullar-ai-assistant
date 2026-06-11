"""Nebullar Agent —— 检索增强问答核心。第一版 MVP：一问一答。"""
from llm import load_client, complete   # 提供方抽象：按 .env 选 Opus(公司) 或 DeepSeek(家里)

from retrieve import search             # 混合检索入口：一个问题 → 最相关的文档片段


# 全局客户端 + 模型，模块加载时按 LLM_PROVIDER 初始化一次
# 公司电脑 → (Anthropic client, "claude-opus-4-8")；家里电脑 → (OpenAI client, "deepseek-chat")
client, MODEL = load_client()

# 系统角色提示词 —— 告诉 LLM 它是谁、怎么答
SYSTEM_PROMPT = """你是 Nebullar 智能助手，Nebullar 部门的 FAE 技术支持专家。
你的知识来源于 Financial SDK 和 Terminal Manager SDK 的官方文档。

回答规则：
1. 根据【参考资料】回答问题，资料里有的直接引用
2. 资料不足时，诚实说"当前知识库未覆盖该问题"，不要编造
3. 回答用中文，结构清晰：先给结论，再给排查步骤，最后给相关 API
4. 涉及错误码时，给出错误码含义、常见原因、建议解决方案
"""


def build_prompt(query: str, docs: list[dict]) -> str:
    """把检索到的文档片段拼接成 LLM 可读的参考资料文本。

    输入: query="刷卡-70004怎么办", docs=search()返回的5个片段
    输出: 一段拼接好的文本，包含"参考文档X：...\n---\n参考文档Y：..."
    """
    ref_parts = []
    for i, doc in enumerate(docs, 1):
        ref_parts.append(
            f"[参考文档{i}] 来源: {doc['module']}\n{doc['content']}\n"
        )
    refs = "\n---\n".join(ref_parts)  # 用分隔线隔开不同文档

    return f"""【参考资料】
{refs}

【用户问题】
{query}

请根据上述参考资料回答用户问题。"""


def ask(query: str) -> str:
    """RAG 问答主流程：检索 → 拼 prompt → 调 Claude → 返回答案。

    输入: "刷卡返回错误码-70004是什么意思"
    输出: 中文排查建议（基于真实文档内容）
    """
    # 1. 检索相关文档片段（传 client+model 启用查询重写，提升口语/模糊问题命中）
    docs = search(query, top_k=5, client=client, model=MODEL)

    # 2. 拼接 prompt
    prompt = build_prompt(query, docs)

    # 3. 调 LLM 生成答案（complete 屏蔽 Opus / DeepSeek 两家 SDK 差异，返回纯文本）
    return complete(client, MODEL, SYSTEM_PROMPT, prompt, max_tokens=4096)


if __name__ == "__main__":
    # 测试：真实 SDK 问题
    print("=" * 60)
    print("Nebullar Agent MVP 测试")
    print("=" * 60)

    q = "刷卡返回错误码-70004是什么意思，怎么排查？"
    print(f"\n问题: {q}\n")
    answer = ask(q)
    print(f"回答:\n{answer}")
