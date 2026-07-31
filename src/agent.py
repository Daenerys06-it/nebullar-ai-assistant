"""Nebullar Agent —— 检索增强问答核心。"""

import os
import json
import re  # 正则：从问题文字里抠出错误码
from typing import TypedDict, Optional  # State 的类型声明

from langgraph.graph import StateGraph, END  # LangGraph：把问答流程声明成"图"

from llm import (
    load_client,
    complete,
)  # 提供方抽象：按 .env 选 Opus(公司) 或 DeepSeek(家里)
from memory import build_cases_context, search_cases
from retrieve import search  # 混合检索入口：一个问题 → 最相关的文档片段
from memory_db import get_memory_db  # 记忆数据库

# 初始化记忆数据库
memory_db = get_memory_db()

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
2. 【历史支持案例】是 FAE 经验沉淀，适合处理操作类/环境类问题；案例命中时先抓住案例里的关键原因和操作步骤
3. 资料不足时，诚实说"当前知识库未覆盖该问题"，不要编造
4. 回答用中文，结构清晰：先给结论，再给排查步骤，最后给相关 API
5. 涉及错误码时，给出错误码含义、常见原因、建议解决方案
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

    return (
        "【最近对话历史（用于理解用户追问里的“这个/它/刚才”等指代）】\n"
        + "\n".join(lines)
        + "\n\n"
    )




# ---------- 多轮对话查询重写 ----------

def rewrite_query_with_context(query: str, history: list[dict] | None) -> str:
    """基于历史对话重写查询，处理指代和省略。
    
    示例:
        历史: 用户: D0551怎么刷机？  助手: 步骤1...步骤2...
        当前: 那个bin文件在哪里？
        重写: D0551刷机的bin文件在哪里？
    """
    if not history or len(history) < 2:
        return query
    
    # 取最近2轮对话
    recent = history[-4:]  # 最近2轮（user+assistant各2条）
    history_text = " ".join([m.get("content", "") for m in recent]).lower()
    
    rewritten = query
    
    # 1. 处理指代词（那个/这个/它/刚才）
    pronouns = ["那个", "这个", "它", "刚才", "之前", "上面"]
    if any(p in query for p in pronouns):
        # 从历史中提取设备型号
        import re
        device_match = re.search(r'(d0551|d0552|p18|d5|双屏)', history_text)
        if device_match and device_match.group(1).upper() not in query.upper():
            rewritten = f"{device_match.group(1).upper()} {rewritten}"
        
        # 从历史中提取操作类型
        if any(k in history_text for k in ["刷机", "flash"]) and not any(k in query.lower() for k in ["刷机", "flash"]):
            rewritten = f"刷机 {rewritten}"
        elif any(k in history_text for k in ["写号", "sn", "imei", "barcode"]) and not any(k in query.lower() for k in ["写号", "sn"]):
            rewritten = f"写号 {rewritten}"
    
    # 2. 处理省略（单独的名词短语）
    if len(query) < 10 and not query.startswith(("怎么", "如何", "什么", "哪里", "为什么")):
        if "刷机" in history_text and "刷机" not in query:
            rewritten = f"刷机 {rewritten}"
        elif "写号" in history_text and "写号" not in query:
            rewritten = f"写号 {rewritten}"
    
    # 3. 处理"怎么办/什么意思"类追问
    if query in ["怎么办", "什么意思", "怎么解决", "然后呢"]:
        for m in reversed(history[:-1]):
            if m.get("role") == "user":
                prev_q = m.get("content", "")
                rewritten = f"{prev_q} {query}"
                break
    
    if rewritten != query:
        print(f"[QueryRewrite] '{query}' -> '{rewritten}'")
    
    return rewritten


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
    history_text = " ".join(
        str(m.get("content", "")) for m in (history or [])[-6:]
    ).lower()
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
    card_related = any(
        word in combined for word in ["刷卡", "读卡", "卡片", "card", "nfc", "apdu"]
    )
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
        questions.append(
            "是哪种卡/读卡方式：磁条卡、接触式 IC、非接 NFC，还是 Felica？"
        )
    if "api_name_or_flow" in missing:
        questions.append(
            "你现在调用到哪一步或哪个 API 了？例如 checkCard、powerOnCard、transmitApdu，还是只是业务上说“刷卡无反应”？"
        )

    if not questions:
        questions.append("能补充一下设备型号、SDK 版本、调用 API 和返回日志吗？")

    return (
        "这个问题现在信息还不够，我先确认几个关键点，避免直接给一堆泛泛 API：\n\n"
        + "\n".join(f"{i}. {question}" for i, question in enumerate(questions, 1))
        + "\n\n你补充后我再按对应卡类型和调用链给排查步骤。"
    )


def _format_doc_source(doc: dict, index: int) -> dict:
    """把 retrieve.search() 的文档片段整理成前端可展示的来源。"""
    content = str(doc.get("content", "")).strip()
    return {
        "index": index,
        "module": doc.get("module", ""),
        "product": doc.get("product", ""),
        "score": doc.get("rrf_score", doc.get("score", "")),
        "preview": content[:300] + ("..." if len(content) > 300 else ""),
    }


# ══════════════════════════════════════════════════════════════════════
# LangGraph 版问答流程（等价迁移：行为和原 ask_structured 完全一样）
#
#   · State：贯穿全程的字典 AgentState，每个节点往里写自己的产出。
#   · Node ：函数 (state) -> 只含"我改了哪些字段"的小字典，LangGraph 自动合并。
# ══════════════════════════════════════════════════════════════════════


class AgentState(TypedDict):
    """在节点间传递的"接力棒"。每个字段由某个节点负责填。"""

    query: str  # 用户问题（入口给）
    history: list  # 多轮历史（入口给）
    analysis: dict  # analyze 节点产出
    error_hint: str  # lookup_error 节点产出：拼进 prompt 的错误码释义
    error_hit: Optional[dict]  # lookup_error 节点产出：命中的错误码信息（给前端）
    cases: list  # retrieve 节点产出：命中的案例
    docs: list  # retrieve 节点产出：检索到的文档片段
    tools_used: list  # 各节点累加：用过哪些工具
    answer: str  # generate / clarify 节点产出：最终答案
    needs_clarification: bool  # analyze 节点产出：是否要先反问
    retrieval_query: str  # refine 节点产出：纠错回路时用的"加宽版"检索词
    retries: int  # 自我纠错已重试次数（防死循环）
    # 记忆相关
    user_id: Optional[str]  # 用户ID
    session_id: Optional[str]  # 会话ID
    user_profile: Optional[object]  # 用户画像


# ---------- 节点们（每个都是 state -> 要更新的字段dict）----------


def analyze_node(state: AgentState) -> dict:
    """【模板·已写】分析问题，决定是否要反问。"""
    analysis = analyze_query(state["query"], state["history"])
    return {
        "analysis": analysis,
        "tools_used": ["analyze_query"],  # 第一个节点，给 tools_used 起个头
        "needs_clarification": analysis["should_clarify"],
    }


def clarify_node(state: AgentState) -> dict:
    """【模板·已写】信息不足 → 生成一次性反问，流程到此结束。"""
    return {"answer": build_clarifying_question(state["analysis"])}


def lookup_error_node(state: AgentState) -> dict:
    """【★你来填★】有错误码就查表，命中则拼一段权威释义 error_hint。

    你能用的：
      - state["analysis"]["error_code"]  → "-70004" 或 None
      - state["tools_used"]              → 目前用过的工具列表（命中时要在末尾加 "lookup_error"）
      - lookup_error(code)               → 命中返回 {code,meaning,sdk,category}，否则 None
    要返回的 dict（三个字段）：
      {"error_hit": 命中信息或None, "error_hint": 释义文本或"", "tools_used": 更新后的列表}

    提示：逻辑跟原 ask_structured 第 1 步一模一样。没错误码时 error_hit=None、error_hint=""，
    tools_used 原样返回。注意别用 .append（那是原地改），改用 列表 + ["lookup_error"] 拼新列表。
    """
    code = state["analysis"]["error_code"]
    tools = state["tools_used"]

    if not code:                          # 路径①没错误码：三个字段原样返回
        return {"error_hit": None, "error_hint": "", "tools_used": tools}

    # 有错误码就算"用了查表工具"（无论命中与否，和原 ask_structured 一致）
    tools = tools + ["lookup_error"]
    hit = lookup_error(code)
    if not hit:                           # 路径②有码但表里查不到：没释义，但也要正常返回
        return {"error_hit": None, "error_hint": "", "tools_used": tools}

    # 路径③命中：拼一段权威释义，放进 prompt 最前面，引导 LLM 优先采信
    error_hint = (
        "【错误码官方释义（来自结构化错误码表，权威，请优先采信）】\n"
        f"{hit['code']} = {hit['meaning']}（出处：{hit['sdk']} / {hit['category']}）\n\n"
    )
    return {"error_hit": hit, "error_hint": error_hint, "tools_used": tools}


def retrieve_node(state: AgentState) -> dict:
    """【模板·已写】检索历史案例 + 文档片段。

    纠错回路里会被跑第二次：这时改用 refine 节点加宽后的 retrieval_query。
    """
    query = state.get("retrieval_query") or state["query"]  # 回路时用加宽版检索词
    tools = state["tools_used"]

    cases = search_cases(query, top_k=3)
    if cases and "search_cases" not in tools:  # 回路重跑时别重复记工具
        tools = tools + ["search_cases"]

    docs = search(query, top_k=5)  # 规则扩展，无需LLM
    if docs and "search_docs" not in tools:
        tools = tools + ["search_docs"]

    return {"cases": cases, "docs": docs, "tools_used": tools}


def generate_node(state: AgentState) -> dict:
    """【模板·已写】拼 prompt（历史 + 错误码释义 + 案例 + 文档）→ 调 LLM。"""
    history_context = build_history_context(state["history"])
    cases_context = build_cases_context(state["cases"])
    prompt = (
        history_context
        + state["error_hint"]
        + cases_context
        + build_prompt(state["query"], state["docs"])
    )
    answer = complete(client, MODEL, SYSTEM_PROMPT, prompt, max_tokens=4096)
    return {"answer": answer}


# 自我纠错回路：答案明显不足时，换更宽的检索词回 retrieve 再答一轮（最多 MAX_RETRIES 次）
MAX_RETRIES = 1


def route_after_generate(state: AgentState) -> str:
    """条件边：答案够好就结束；说"未覆盖/无法回答"且还没重试过 → 去 refine 再来一轮。"""
    answer = state["answer"]
    looks_weak = ("未覆盖" in answer) or ("无法回答" in answer)
    if looks_weak and state["retries"] < MAX_RETRIES:
        return "refine"
    return "end"


def refine_node(state: AgentState) -> dict:
    """加宽检索词后回到 retrieve：把错误码官方释义 + 通用排查词拼进去，给检索更多线索。"""
    extra = []
    if state["error_hit"]:
        extra.append(state["error_hit"]["meaning"])  # 用官方释义当补充检索词
    extra += ["排查", "原因", "步骤", "troubleshoot", "cause"]
    refined = state["query"] + " " + " ".join(extra)
    return {"retries": state["retries"] + 1, "retrieval_query": refined}


def route_after_analyze(state: AgentState) -> str:
    """【★你来填★】条件边：analyze 之后该去哪个节点？

    规则：
      - state["needs_clarification"] 为真 → 返回 "clarify"
      - 否则                              → 返回 "lookup_error"
    返回的字符串必须是下面 add_conditional_edges 映射表里的某个 key。

    动态路由（agentic 雏形）：
      - 信息不足            → "clarify"（先反问）
      - 问题里真有错误码    → "lookup_error"（查表，再检索）
      - 否则                → "retrieve"（没码就别白跑查表，直接检索）
    """
    if state["needs_clarification"]:
        return "clarify"
    if state["analysis"]["error_code"]:
        return "lookup_error"
    return "retrieve"


# ---------- 把节点和边连成图，编译成可运行对象（模块加载时一次）----------
_graph = StateGraph(AgentState)
_graph.add_node("analyze", analyze_node)
_graph.add_node("clarify", clarify_node)
_graph.add_node("lookup_error", lookup_error_node)
_graph.add_node("retrieve", retrieve_node)
_graph.add_node("generate", generate_node)
_graph.add_node("refine", refine_node)

_graph.set_entry_point("analyze")
_graph.add_conditional_edges(  # analyze 后，按 route_after_analyze 的返回值分叉
    "analyze",
    route_after_analyze,
    {"clarify": "clarify", "lookup_error": "lookup_error", "retrieve": "retrieve"},
)
_graph.add_edge("clarify", END)  # 反问完直接结束
_graph.add_edge("lookup_error", "retrieve")
_graph.add_edge("retrieve", "generate")
_graph.add_conditional_edges(  # generate 后：够好就 END，不够就回 refine 再来一轮（形成环）
    "generate",
    route_after_generate,
    {"refine": "refine", "end": END},
)
_graph.add_edge("refine", "retrieve")  # refine 完回到检索 → 这条"回边"就是 LangGraph 的环

APP_GRAPH = _graph.compile()


def _init_state(query: str, history: list[dict] | None, user_id: Optional[str] = None, session_id: Optional[str] = None) -> AgentState:
    """组装跑图用的初始 state（所有字段都给默认值）。"""
    return {
        "query": query,
        "history": history or [],
        "analysis": {},
        "error_hint": "",
        "error_hit": None,
        "cases": [],
        "docs": [],
        "tools_used": [],
        "answer": "",
        "needs_clarification": False,
        "retrieval_query": "",
        "retries": 0,
        "user_id": user_id,
        "session_id": session_id,
        "user_profile": None,
    }


def _finalize(final: dict) -> dict:
    """把图跑完的最终 state 整理成对外的结构化结果（契约不变）。"""
    return {
        "answer": final["answer"],
        "tools_used": final["tools_used"],
        "error": final["error_hit"],
        "cases": final["cases"],
        "sources": [
            _format_doc_source(doc, i) for i, doc in enumerate(final["docs"], 1)
        ],
        "analysis": final["analysis"],
        "provider_model": MODEL,
        "needs_clarification": final["needs_clarification"],
    }


def ask_structured(query: str, history: list[dict] | None = None,
                   user_id: Optional[str] = None, session_id: Optional[str] = None) -> dict:
    """RAG 问答主流程（记忆集成版）.

    新增参数:
        user_id: 用户ID（用于加载用户画像和保存历史）
        session_id: 会话ID（用于保存对话历史）
    """
    import time

    # 1. 确保用户和会话存在
    profile = None
    if user_id:
        profile = memory_db.create_or_update_user(user_id)
        if session_id:
            memory_db.create_session(session_id, user_id, title=query[:30])

    # 2. 加载数据库中的对话历史
    db_history = []
    if session_id:
        db_messages = memory_db.get_session_history(session_id, limit=10)
        db_history = [{"role": m.role, "content": m.content} for m in db_messages]

    combined_history = db_history + (history or [])

    # 3. 初始化 state
    state = _init_state(query, combined_history, user_id, session_id)
    if profile:
        state["user_profile"] = profile

    # 4. 保存用户消息
    if session_id and user_id:
        memory_db.save_message(session_id, user_id, "user", query)

    # 5. 运行 LangGraph
    start_time = time.time()
    final = APP_GRAPH.invoke(state)
    latency_ms = int((time.time() - start_time) * 1000)

    # 6. 保存助手消息
    if session_id and user_id:
        memory_db.save_message(
            session_id, user_id, "assistant",
            final["answer"],
            tools_used=final["tools_used"],
            cases_referenced=[c["id"] for c in final["cases"]] if final.get("cases") else None,
            latency_ms=latency_ms
        )

    return _finalize(final)


# 节点 → 给用户看的友好进度文案（流式时显示）
NODE_LABELS = {
    "analyze": "分析问题…",
    "clarify": "信息不足，整理反问…",
    "lookup_error": "查错误码表…",
    "retrieve": "检索历史案例 + 文档…",
    "refine": "答案不足，换个检索词再来一轮…",
    "generate": "生成答案…",
}


def ask_structured_stream(query: str, history: list[dict] | None = None,
                          user_id: str = None, session_id: str = None):
    """流式版：每跑完一个节点 yield ("progress", 友好文案)；最后 yield ("done", 结构化结果)。

    用 APP_GRAPH.stream() 一步步拿到"哪个节点刚跑完 + 它改了哪些字段"，
    一边累积状态，一边把进度推给前端。
    """
    import time

    # 1. 确保用户和会话存在
    profile = None
    if user_id:
        profile = memory_db.create_or_update_user(user_id)
        if session_id:
            memory_db.create_session(session_id, user_id, title=query[:30])

    # 2. 加载数据库中的对话历史
    db_history = []
    if session_id:
        db_messages = memory_db.get_session_history(session_id, limit=10)
        db_history = [{"role": m.role, "content": m.content} for m in db_messages]

    combined_history = db_history + (history or [])

    # 3. 初始化 state，传入记忆信息
    state = _init_state(query, combined_history, user_id, session_id)
    if profile:
        state["user_profile"] = profile

    # 4. 保存用户消息
    if session_id and user_id:
        memory_db.save_message(session_id, user_id, "user", query)

    # 5. 流式运行
    start_time = time.time()
    for step in APP_GRAPH.stream(state):
        for node_name, partial in step.items():
            if partial:
                state = {**state, **partial}
            yield ("progress", NODE_LABELS.get(node_name, node_name))

    # 6. 计算耗时并保存助手消息
    latency_ms = int((time.time() - start_time) * 1000)
    if session_id and user_id:
        memory_db.save_message(
            session_id, user_id, "assistant",
            state["answer"],
            tools_used=state["tools_used"],
            cases_referenced=[c["id"] for c in state["cases"]] if state.get("cases") else None,
            latency_ms=latency_ms
        )

    yield ("done", _finalize(state))


def ask(query: str, history: list[dict] | None = None) -> str:
    """兼容旧调用：只返回答案文本。"""
    return ask_structured(query, history=history)["answer"]


if __name__ == "__main__":
    # 测试：真实 SDK 问题
    print("=" * 60)
    print("Nebullar Agent MVP 测试")
    print("=" * 60)

    q = "刷卡返回错误码-70004是什么意思，怎么排查？"
    print(f"\n问题: {q}\n")
    result = ask_structured(q)
    print(f"回答:\n{result['answer']}")
    print(f"\n工具: {', '.join(result['tools_used'])}")
