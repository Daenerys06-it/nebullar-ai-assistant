"""Nebullar AI Assistant —— Streamlit 前端（记忆集成版）。

运行：在项目根目录执行  streamlit run src/app.py

新功能（长期记忆）：
1. 用户画像：自动识别用户偏好设备、常见问题类型
2. 对话历史：自动保存到 SQLite，支持跨会话恢复
3. 自动沉淀：高质量问答自动提取为待审核案例
"""
import sys

# ========== 强制清除缓存（解决模块更新不生效问题）==========
# 删除所有已缓存的模块，强制重新加载
for mod_name in list(sys.modules.keys()):
    if any(x in mod_name for x in ['memory', 'retrieve', 'agent', 'llm']):
        del sys.modules[mod_name]
# =====================================================

import streamlit as st
import uuid

# ========== 启动时预加载模型（避免首次查询慢）==========
print("[App] 启动预加载...")

# 测试导入 - 检查 _get_embedder
try:
    from retrieve import _get_embedder
    print(f"[App] _get_embedder imported successfully: {_get_embedder}")
except ImportError as e:
    print(f"[App] _get_embedder import failed: {e}")
    # 创建备用定义
    def _get_embedder():
        from memory import get_embedder
        return get_embedder()
    print("[App] Created fallback _get_embedder")

from memory import preload_models as preload_case_models
from retrieve import preload_all_models as preload_retrieve_models

preload_case_models()      # 预加载案例嵌入模型
preload_retrieve_models()  # 预加载检索模型
print("[App] 预加载完成！")
# ====================================================

from agent import MODEL, ask_structured_stream  # RAG 问答主流程
from llm import PROVIDER
from memory_db import get_memory_db

# 初始化记忆数据库
memory_db = get_memory_db()


# ---------- 页面基础配置（必须是第一个 st.* 调用）----------
st.set_page_config(page_title="Nebullar AI 技术支持", page_icon="🤖", layout="centered")


# ---------- 会话状态：用户ID + 会话ID ----------
def ensure_user_session():
    """确保有 user_id 和 session_id（用于长期记忆）。"""
    if "user_id" not in st.session_state:
        # 生成随机用户ID（实际项目中可从登录态获取）
        st.session_state.user_id = f"user_{uuid.uuid4().hex[:8]}"
    if "session_id" not in st.session_state:
        # 每次刷新页面生成新会话
        st.session_state.session_id = f"sess_{uuid.uuid4().hex[:12]}"
    return st.session_state.user_id, st.session_state.session_id


user_id, session_id = ensure_user_session()


# ---------- 侧栏：信息 + 用户画像 + 清空按钮 ----------
with st.sidebar:
    st.title("🤖 Nebullar AI")
    st.caption("部门级 FAE 技术支持助手")
    st.markdown(f"**当前模型**：`{MODEL}`  \n**提供方**：`{PROVIDER}`")
    st.divider()

    # 显示当前用户和会话
    st.caption(f"用户：`{user_id}`")
    st.caption(f"会话：`{session_id[:20]}...`")

    # 显示用户画像（如果有）
    profile = memory_db.get_user_profile(user_id)
    if profile and (profile.preferred_devices or profile.common_issues):
        st.divider()
        st.markdown("**📊 用户画像**")
        if profile.preferred_devices:
            st.markdown(f"常用设备：`{', '.join(profile.preferred_devices)}`")
        if profile.common_issues:
            st.markdown(f"常见问题：`{', '.join(profile.common_issues[:3])}`")
        if profile.total_sessions:
            st.caption(f"历史会话：{profile.total_sessions} 次")

    st.divider()
    if st.button("🗑️ 清空对话", use_container_width=True):
        st.session_state.messages = []     # 清空历史
        st.rerun()                         # 立即重跑，刷新界面

    if st.button("🆕 新会话", use_container_width=True):
        # 生成新会话ID
        st.session_state.session_id = f"sess_{uuid.uuid4().hex[:12]}"
        st.session_state.messages = []
        st.rerun()

    st.divider()
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

    # 2. 调 Agent 生成答案（节点级流式进度；出错也不让页面崩）
    with st.chat_message("assistant"):
        result = None
        try:
            with st.status("处理中…", expanded=False) as status:
                # 传入 user_id 和 session_id 启用记忆功能
                for kind, payload in ask_structured_stream(
                    query, history=old_history,
                    user_id=user_id, session_id=session_id
                ):
                    if kind == "progress":
                        status.update(label=payload)  # 每过一个节点，更新进度文案
                    else:  # ("done", 结构化结果)
                        result = payload
                status.update(label="完成 ✅", state="complete")
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
