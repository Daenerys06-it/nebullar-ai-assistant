"""Nebullar Agent —— 检索增强问答核心。第一版 MVP：一问一答。"""
import os
from dotenv import load_dotenv          # 读取 .env 文件里的密钥
from openai import OpenAI               # DeepSeek 兼容 OpenAI 格式，用这个库调用

from retrieve import search             # 混合检索入口：一个问题 → 最相关的文档片段


def load_client():
    """从 .env 读 DeepSeek API key，建立客户端并返回。

    为什么这么写：
    - key 放 .env（被 gitignore），不写死在代码里，避免提交泄露
    - DeepSeek 兼容 OpenAI 接口，所以用 OpenAI 类，只需把 base_url 指向 DeepSeek
    """
    load_dotenv()                                  # 把 .env 内容加载进环境变量
    key = os.getenv("DEEPSEEK_API_KEY")            # 取出 key
    if not key:                                    # 防御：key 没读到就早报错，别等调用时才崩
        raise RuntimeError("未找到 DEEPSEEK_API_KEY，检查 .env 文件")
    client = OpenAI(api_key=key, base_url="https://api.deepseek.com")
    return client


# 全局客户端，模块加载时初始化一次（后续多轮对话改传参即可）
client = load_client()

# 系统角色提示词 —— 告诉 LLM 它是谁、怎么答
SYSTEM_PROMPT = """你是 Nebullar，KOZEN 部门的 FAE 技术支持专家。
你的知识来源于 KOZEN Financial SDK 和 Terminal Manager SDK 的官方文档。

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
    """RAG 问答主流程：检索 → 拼 prompt → 调 DeepSeek → 返回答案。

    输入: "刷卡返回错误码-70004是什么意思"
    输出: 中文排查建议（基于真实文档内容）
    """
    # 1. 检索相关文档片段（传 client 启用查询重写，提升口语/模糊问题命中）
    docs = search(query, top_k=5, client=client)

    # 2. 拼接 prompt
    prompt = build_prompt(query, docs)

    # 3. 调 DeepSeek 生成答案
    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,  # 低温度，减少随机性，让答案更稳定可复现
    )

    return resp.choices[0].message.content


if __name__ == "__main__":
    # 测试：真实 SDK 问题
    print("=" * 60)
    print("Nebullar Agent MVP 测试")
    print("=" * 60)

    q = "刷卡返回错误码-70004是什么意思，怎么排查？"
    print(f"\n问题: {q}\n")
    answer = ask(q)
    print(f"回答:\n{answer}")
