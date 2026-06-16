"""Nebullar AI Assistant —— Streamlit 前端（第一版：单聊天面板）。

运行：在项目根目录执行  streamlit run src/app.py

Streamlit 心智模型（理解这三点就够写聊天页了）：
1. 「整页重跑」：用户每点一次按钮/输入一次，Streamlit 会从上到下把整个脚本重新执行一遍。
   → 所以普通局部变量每轮都会重置，留不住聊天记录。
2. 「session_state」：唯一能跨重跑保存的地方，像个会话级字典。聊天历史就存这里。
3. 「chat 组件」：st.chat_message(role) 画一个气泡，st.chat_input() 是底部输入框。
"""
import streamlit as st

from agent import MODEL, ask_structured      # RAG 问答主流程（检索→LLM）+ 当前模型名
from llm import PROVIDER          # 当前提供方 gpt5 / opus / deepseek（侧栏展示用）


# ---------- 页面基础配置（必须是第一个 st.* 调用）----------
st.set_page_config(page_title="Nebullar AI 技术支持", page_icon="🤖", layout="centered")


# ---------- 侧栏：信息 + 清空按钮 ----------
with st.sidebar:
    st.title("🤖 Nebullar AI")
    st.caption("部门级 FAE 技术支持助手")
    st.markdown(f"**当前模型**：`{MODEL}`  \n**提供方**：`{PROVIDER}`")
    st.divider()
    if st.button("🗑️ 清空对话", use_container_width=True):
        st.session_state.messages = []     # 清空历史
        st.rerun()                         # 立即重跑，刷新界面
    st.caption("基于 Financial / Terminal SDK 官方文档开卷作答；信息不足时会先反问澄清。")


# ---------- 会话状态：跨「重跑」保存聊天记录 ----------
# 第一次进来还没有 messages，初始化成空列表。
# 每条消息形如 {"role": "user"/"assistant", "content": "文本"}
if "messages" not in st.session_state:
    st.session_state.messages = []


def render_result_details(result: dict | None) -> None:
    """展示 Agent 用过的工具、命中的案例和参考文档来源。"""
    if not result:
        return

    tools = result.get("tools_used") or []
    error = result.get("error")
    cases = result.get("cases") or []
    sources = result.get("sources") or []

    if not tools and not error and not cases and not sources:
        return

    with st.expander("参考依据 / 工具命中", expanded=False):
        if tools:
            st.markdown("**工具**：" + " / ".join(f"`{tool}`" for tool in tools))

        if error:
            st.markdown("**错误码查表**")
            st.markdown(
                f"- `{error.get('code')}` = `{error.get('meaning')}`\n"
                f"- 来源：`{error.get('sdk')}` / `{error.get('category')}`"
            )

        if cases:
            st.markdown("**历史案例**")
            for case in cases:
                st.markdown(
                    f"- `{case.get('module', 'case')}`：{case.get('symptom', '')}\n"
                    f"  - 原因：{case.get('root_cause', '')}\n"
                    f"  - 处理：{case.get('solution', '')}"
                )

        if sources:
            st.markdown("**参考文档**")
            for source in sources:
                title = source.get("module") or "unknown"
                product = source.get("product") or ""
                st.markdown(
                    f"- [{source.get('index')}] `{title}` {product}\n\n"
                    f"  {source.get('preview', '')}"
                )


# ---------- 渲染已有历史 ----------
st.title("Nebullar 技术支持")
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg["role"] == "assistant":
            render_result_details(msg.get("result"))


# ---------- 底部输入框 + 一轮问答 ----------
# 海象运算符 := ：用户回车则 query=输入文本并进 if；没输入则返回 None 跳过。
if query := st.chat_input("问我 SDK 问题，比如：刷卡返回 -70004 怎么排查？"):
    # 先复制一份“用户本轮输入前”的历史，传给 Agent 用来理解追问。
    # 例如上一轮答了 powerOnCard，这一轮用户问“那这个 API 调用前要注意什么？”，
    # Agent 就能从 old_history 里知道“这个 API”指上一轮提到的内容。
    old_history = st.session_state.messages.copy()

    # 1. 先把用户这条显示出来并存进历史
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # 2. 调 Agent 生成答案（转圈等待；出错也不让页面崩）
    with st.chat_message("assistant"):
        with st.spinner("检索文档 + 思考中…"):
            try:
                result = ask_structured(query, history=old_history)
                answer = result["answer"]
            except Exception as e:
                result = None
                answer = (
                    f"⚠️ 出错了：{e}\n\n"
                    "（公司电脑检查内网网关连通；家里电脑确认 .env 里 "
                    "`LLM_PROVIDER` 和 key 有效）"
                )
        st.markdown(answer)
        render_result_details(result)

    # 3. 答案也存进历史，下次重跑能重现整段对话
    st.session_state.messages.append({"role": "assistant", "content": answer, "result": result})
