"""Nebullar Agent —— 检索增强问答核心。第一版 MVP：一问一答。"""

import os
import json
import re                                   # 正则：从问题文字里抠出错误码

from llm import (
    load_client,
    complete,
)  # 提供方抽象：按 .env 选 Opus(公司) 或 DeepSeek(家里)
from retrieve import search  # 混合检索入口：一个问题 → 最相关的文档片段

# 【第1步：照抄】错误码精确查表数据：模块加载时读一次（别每次查都重读文件）
_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(_BASE, "data", "error_codes.json"), encoding="utf-8") as f:
    ERROR_CODES = json.load(f)  # 结构：{ sdk: { 分类: { "码": "含义" } } }


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
        ref_parts.append(f"[参考文档{i}] 来源: {doc['module']}\n{doc['content']}\n")
    refs = "\n---\n".join(ref_parts)  # 用分隔线隔开不同文档

    return f"""【参考资料】
{refs}

【用户问题】
{query}

请根据上述参考资料回答用户问题。"""


def build_history_context(history: list[dict] | None, max_messages: int = 6) -> str:
    """把最近几轮聊天历史整理成 prompt 文本。

    history 来自前端 st.session_state.messages，结构是：
    [
        {"role": "user", "content": "刷卡返回 -70004 怎么排查？"},
        {"role": "assistant", "content": "结论：-70004 是 APDU Error..."},
    ]

    为什么只取最近 max_messages 条：
    - 多轮对话要让模型知道“这个/它/上面那个 API”指什么
    - 但历史太长会挤占参考文档空间，所以先保守取最近 6 条
    """
    if not history:
        return ""

    role_names = {
        "user": "用户",
        "assistant": "助手",
    }
    lines = []
    for msg in history[-max_messages:]:
        role = role_names.get(msg.get("role"), msg.get("role", "unknown"))
        content = str(msg.get("content", "")).strip()
        if content:
            lines.append(f"{role}: {content}")

    if not lines:
        return ""

    return "【最近对话历史（用于理解用户追问里的“这个/它/刚才”等指代）】\n" + "\n".join(lines) + "\n\n"


# ──────────────────────────────────────────────────────────────────────
# ERROR_CODES 长什么样（三层嵌套字典）—— 写 lookup_error 前先看清结构：
#
#   ERROR_CODES = {
#       "financial_sdk": {                  # 第1层  键=SDK名   值=↓整块分类字典
#           "common":     {"-10000": "...version mismatch", ...},
#           "cardreader": {                 # 第2层  键=分类名  值=↓整块错误码字典
#               "-70001": "Card Type Error",
#               "-70004": "APDU Error",     # 第3层  键=错误码  值=英文含义
#               ...
#           },
#           ...
#       },
#       "terminal_manager_sdk": { ...同样的三层结构... },
#   }
#
# 怎么取值（一层层用 [键] 钻进去）：
#   ERROR_CODES["financial_sdk"]["cardreader"]["-70004"]  →  "APDU Error"
#
# 想自己在终端探查里面有什么：
#   python -c "import json; d=json.load(open('data/error_codes.json',encoding='utf-8')); \
#              print('SDK:', list(d)); \
#              print('分类:', list(d['financial_sdk'])); \
#              print('cardreader 部分码:', list(d['financial_sdk']['cardreader'])[:5])"
# ──────────────────────────────────────────────────────────────────────
def lookup_error(code: str) -> dict | None:
    """在 error_codes.json 里精确查一个错误码，查到返回信息，查不到返回 None。

    输入: code = "-70004"
    输出: {"code": "-70004", "meaning": "APDU Error",
           "sdk": "financial_sdk", "category": "cardreader"}
          查不到 → None
    """
    # ERROR_CODES 是三层字典：sdk → 分类 → {码: 含义}
    # 思路：两层 for 遍历到最里层的 {码: 含义}，看 code 在不在里面
    for sdk_name, categories in ERROR_CODES.items():  # 第1层：每个 SDK
        for (
            category_name,
            codes,
        ) in categories.items():  # 第2层：每个分类（codes 是 {码:含义}）
            if code in codes:  # code 在这层字典里吗？
                return {
                    "code": code,
                    "meaning": codes[code],  # 提示：codes[code]
                    "sdk": sdk_name,
                    "category": category_name,
                }
    return None  # 三层都走完没找到 → 返回啥？


def analyze_query(query: str, history: list[dict] | None = None) -> dict:
    """轻量问题分析：判断 intent、抽错误码，并决定是否先反问。

    这一步先不用 LLM，也不上 LangGraph；用规则把最常见的 FAE 排查入口兜住。
    后续如果规则变复杂，再考虑升级成 LLM router 或 LangGraph 节点。
    """
    text = query.lower()
    history_text = " ".join(str(m.get("content", "")) for m in (history or [])[-6:]).lower()
    combined = text + " " + history_text

    code_match = re.search(r"-?\d{4,6}", query)
    error_code = None
    if code_match:
        error_code = "-" + code_match.group().lstrip("-")

    card_type_keywords = {
        "magstripe": ["磁条", "mag", "swipe"],
        "contact": ["接触", "插卡", "ic card", "contact card"],
        "contactless": ["非接", "挥卡", "nfc", "contactless", "tap"],
        "felica": ["felica"],
    }
    mentioned_card_types = [
        card_type
        for card_type, keywords in card_type_keywords.items()
        if any(keyword in combined for keyword in keywords)
    ]

    has_api = bool(re.search(r"\b[a-zA-Z_][a-zA-Z0-9_]{2,}\s*\(", query)) or any(
        name in combined
        for name in [
            "poweroncard",
            "checkcard",
            "getcardexiststatus",
            "transmitapdu",
            "cardreader",
        ]
    )

    troubleshooting_words = [
        "无反应",
        "没反应",
        "失败",
        "失败了",
        "刷不了",
        "读不到",
        "报错",
        "怎么办",
        "怎么排查",
        "why",
        "fail",
        "error",
        "no response",
    ]
    is_troubleshooting = any(word in combined for word in troubleshooting_words)

    intent = "unknown"
    if error_code:
        intent = "error_lookup"
    elif is_troubleshooting:
        intent = "troubleshooting"
    elif has_api:
        intent = "api_usage"

    missing_info = []
    # 没错误码、没卡类型的“刷卡/读卡无反应”问题，直接回答容易太泛，先追问。
    card_related = any(word in combined for word in ["刷卡", "读卡", "卡片", "card", "nfc", "apdu"])
    if intent == "troubleshooting" and card_related and not error_code:
        if not mentioned_card_types:
            missing_info.append("card_type")
        if not has_api:
            missing_info.append("api_name_or_flow")

    return {
        "intent": intent,
        "error_code": error_code,
        "card_types": mentioned_card_types,
        "has_api": has_api,
        "missing_info": missing_info,
        "should_clarify": bool(missing_info),
    }


def build_clarifying_question(analysis: dict) -> str:
    """根据缺失信息生成一次性反问，避免信息不足时直接泛泛回答。"""
    questions = []
    missing = analysis.get("missing_info", [])

    if "card_type" in missing:
        questions.append("是哪种卡/读卡方式：磁条卡、接触式 IC、非接 NFC，还是 Felica？")
    if "api_name_or_flow" in missing:
        questions.append("你现在调用到哪一步或哪个 API 了？例如 checkCard、powerOnCard、transmitApdu，还是只是业务上说“刷卡无反应”？")

    if not questions:
        questions.append("能补充一下设备型号、SDK 版本、调用 API 和返回日志吗？")

    return (
        "这个问题现在信息还不够，我先确认几个关键点，避免直接给一堆泛泛 API：\n\n"
        + "\n".join(f"{i}. {question}" for i, question in enumerate(questions, 1))
        + "\n\n你补充后我再按对应卡类型和调用链给排查步骤。"
    )


def ask(query: str, history: list[dict] | None = None) -> str:
    """RAG 问答主流程：检索 → 拼 prompt → 调 Claude → 返回答案。

    输入: "刷卡返回错误码-70004是什么意思"
    输出: 中文排查建议（基于真实文档内容）
    """
    # 0. 先分析问题：信息明显不足时先反问，而不是直接泛泛回答。
    analysis = analyze_query(query, history)
    if analysis["should_clarify"]:
        return build_clarifying_question(analysis)

    # 1. 看问题里有没有错误码：有就查官方释义表（精确查表，补向量检索的短板）
    error_hint = ""
    if analysis["error_code"]:
        code = analysis["error_code"]
        hit = lookup_error(code)
        if hit:                              # 查表命中 → 拼一段权威释义，放 prompt 最前面
            error_hint = (
                "【错误码官方释义（来自结构化错误码表，权威，请优先采信）】\n"
                f"{hit['code']} = {hit['meaning']}"
                f"（出处：{hit['sdk']} / {hit['category']}）\n\n"
            )

    # 2. 检索相关文档片段（传 client+model 启用查询重写，提升口语/模糊问题命中）
    docs = search(query, top_k=5, client=client, model=MODEL)

    # 3. 拼接 prompt
    #    - 历史：帮助理解“这个/它/刚才那个 API”等追问
    #    - 错误码释义：放最前面当高优先线索
    #    - 参考资料：RAG 检索结果，回答仍以官方文档为准
    history_context = build_history_context(history)
    prompt = history_context + error_hint + build_prompt(query, docs)

    # 4. 调 LLM 生成答案（complete 屏蔽 GPT-5 / Opus / DeepSeek SDK 差异，返回纯文本）
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
