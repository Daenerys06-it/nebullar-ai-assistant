"""Nebullar AI Assistant —— Streamlit 前端（第一版：单聊天面板）。

运行：在项目根目录执行  streamlit run src/app.py

Streamlit 心智模型（理解这三点就够写聊天页了）：
1. 「整页重跑」：用户每点一次按钮/输入一次，Streamlit 会从上到下把整个脚本重新执行一遍。
   → 所以普通局部变量每轮都会重置，留不住聊天记录。
2. 「session_state」：唯一能跨重跑保存的地方，像个会话级字典。聊天历史就存这里。
3. 「chat 组件」：st.chat_message(role) 画一个气泡，st.chat_input() 是底部输入框。
"""
import streamlit as st

from agent import ask, MODEL      # RAG 问答主流程（检索→LLM）+ 当前模型名
from llm import PROVIDER          # 当前提供方 opus / deepseek（侧栏展示用）


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
    st.caption("基于 Financial / Terminal SDK 官方文档开卷作答，未覆盖会如实说明。")


# ---------- 会话状态：跨「重跑」保存聊天记录 ----------
# 第一次进来还没有 messages，初始化成空列表。
# 每条消息形如 {"role": "user"/"assistant", "content": "文本"}
if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------- 渲染已有历史 ----------
st.title("Nebullar 技术支持")
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# ---------- 底部输入框 + 一轮问答 ----------
# 海象运算符 := ：用户回车则 query=输入文本并进 if；没输入则返回 None 跳过。
if query := st.chat_input("问我 SDK 问题，比如：刷卡返回 -70004 怎么排查？"):
    # 1. 先把用户这条显示出来并存进历史
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # 2. 调 Agent 生成答案（转圈等待；出错也不让页面崩）
    with st.chat_message("assistant"):
        with st.spinner("检索文档 + 思考中…"):
            try:
                answer = ask(query)
            except Exception as e:
                answer = (
                    f"⚠️ 出错了：{e}\n\n"
                    "（公司电脑检查内网网关连通；家里电脑确认 .env 里 "
                    "`LLM_PROVIDER=deepseek` 且 key 有效）"
                )
        st.markdown(answer)

    # 3. 答案也存进历史，下次重跑能重现整段对话
    st.session_state.messages.append({"role": "assistant", "content": answer})
