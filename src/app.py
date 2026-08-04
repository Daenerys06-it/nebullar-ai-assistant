"""Nebullar AI Assistant —— Streamlit 前端（记忆集成版）。

运行：在项目根目录执行  streamlit run src/app.py

新功能（长期记忆）：
1. 用户画像：自动识别用户偏好设备、常见问题类型
2. 对话历史：自动保存到 SQLite，支持跨会话恢复
3. 自动沉淀：高质量问答自动提取为待审核案例
4. 翻译模式：中英互译
5. 历史会话列表：可恢复、删除过往会话
"""
import sys

import streamlit as st
import uuid
import time  # 添加时间模块用于计时

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

# 确保当前会话在数据库中存在
memory_db.create_session(session_id, user_id, title="新对话")


# ---------- 侧栏：信息 + 翻译模式 + 用户画像 + 历史会话 + 清空按钮 ----------
with st.sidebar:
    st.title("🤖 Nebullar AI")
    st.caption("部门级 FAE 技术支持助手")
    st.markdown(f"**当前模型**：`{MODEL}`  \n**提供方**：`{PROVIDER}`")
    st.divider()

    # ===== 翻译模式开关 =====
    if "translate_mode" not in st.session_state:
        st.session_state.translate_mode = False

    translate_mode = st.toggle("🌐 翻译模式", value=st.session_state.translate_mode,
                               help="开启后，输入内容将直接翻译，不走技术支持流程")
    st.session_state.translate_mode = translate_mode

    if translate_mode:
        st.info("翻译模式已开启", icon="✅")
        # 语言选择
        lang_options = ["中文 <-> 英文", "中文 -> 英文", "英文 -> 中文"]
        selected_lang = st.selectbox("翻译方向", lang_options, index=0)
        st.session_state.translate_direction = selected_lang
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

    # ===== 历史会话列表 =====
    st.divider()
    st.markdown("**📜 历史会话**")

    sessions = memory_db.get_user_sessions(user_id, limit=10)
    if sessions:
        for sess in sessions:
            col1, col2 = st.columns([4, 1])
            with col1:
                # 显示会话标题和时间
                title = sess['title'] or f"会话 {sess['session_id'][:8]}"
                # 截断标题
                display_title = title[:12] + "..." if len(title) > 15 else title
                btn_label = f"{display_title} ({sess['msg_count']}条)"

                # 如果是当前会话，高亮显示
                is_current = sess['session_id'] == session_id
                btn_type = "primary" if is_current else "secondary"

                if st.button(btn_label, key=f"sess_{sess['session_id']}",
                           use_container_width=True, type=btn_type):
                    # 切换到该会话
                    st.session_state.session_id = sess['session_id']
                    # 加载该会话的消息历史
                    history_msgs = memory_db.get_session_history(sess['session_id'], limit=100)
                    st.session_state.messages = [
                        {"role": msg.role, "content": msg.content}
                        for msg in history_msgs
                    ]
                    st.rerun()
            with col2:
                if st.button("🗑️", key=f"del_{sess['session_id']}"):
                    # 删除会话
                    memory_db.delete_session(sess['session_id'])
                    # 如果删除的是当前会话，清空消息
                    if sess['session_id'] == session_id:
                        st.session_state.messages = []
                    st.rerun()
    else:
        st.caption("暂无历史会话")

    st.divider()
    if st.button("🗑️ 清空当前对话", use_container_width=True):
        st.session_state.messages = []     # 清空历史
        st.rerun()                         # 立即重跑，刷新界面

    if st.button("🆕 新建会话", use_container_width=True):
        # 生成新会话ID
        st.session_state.session_id = f"sess_{uuid.uuid4().hex[:12]}"
        st.session_state.messages = []
        # 在数据库中创建新会话
        memory_db.create_session(st.session_state.session_id, user_id)
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


# ---------- 小N 欢迎语（首次打开时显示） ----------
if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown("""
**嗨！我是小N** 🤖

你的智能 FAE 同事，24小时在线帮你搞定技术支持：

**🌐 翻译模式**（左侧开关开启）
- 中英技术文档互译
- 给客户写英文邮件不用愁

**💡 SDK 技术支持**
- Financial SDK V1.8（K 产品收银业务）
- Terminal Manager SDK V1.4（D 产品设备管理）
- 错误码查询、API 用法、集成排错

**🔧 FAE 经典问题**
- D5/P18/K1 刷机、写号
- 设备初始化、adb 连接
- 从 23+ 历史案例里找经验

不知道怎么描述问题？没关系，我会追问到你我都明白为止。
        """.strip())


# ---------- 翻译功能 ----------
def translate_text(text: str, direction: str) -> str:
    """调用 LLM 进行翻译。"""
    from llm import load_client, complete

    client, model = load_client()

    # 根据方向构建 prompt
    if direction == "中文 -> 英文":
        system = "你是一个专业的技术翻译助手。将用户输入的中文翻译成地道、专业的英文。保持技术术语的准确性，适合 FAE 和客户沟通使用。只输出翻译结果，不要解释。"
        prompt = f"请将以下内容翻译成英文：\n\n{text}"
    elif direction == "英文 -> 中文":
        system = "你是一个专业的技术翻译助手。将用户输入的英文翻译成准确、流畅的中文。保持技术术语的准确性，适合 FAE 理解和技术文档使用。只输出翻译结果，不要解释。"
        prompt = f"请将以下内容翻译成中文：\n\n{text}"
    else:  # 中文 <-> 英文（自动检测）
        system = "你是一个专业的技术翻译助手。自动检测用户输入的语言，如果是中文则翻译成英文，如果是英文则翻译成中文。保持技术术语的准确性。只输出翻译结果，不要解释。"
        prompt = f"请翻译以下内容：\n\n{text}"

    try:
        result = complete(client, model, system, prompt, max_tokens=2048)
        return result.strip()
    except Exception as e:
        return f"❌ 翻译失败：{e}"


# ---------- 底部输入框 + 一轮问答 ----------
# 根据模式显示不同的 placeholder
if st.session_state.translate_mode:
    placeholder = "输入要翻译的内容..."
else:
    placeholder = "问小N技术相关问题，比如D5设备怎么刷机"

if query := st.chat_input(placeholder):
    # ========== 翻译模式 ==========
    if st.session_state.translate_mode:
        # 1. 显示用户输入
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        # 保存用户消息到数据库
        memory_db.save_message(session_id, user_id, "user", query)

        # 2. 执行翻译
        with st.chat_message("assistant"):
            with st.spinner("翻译中..."):
                direction = st.session_state.get("translate_direction", "中文 <-> 英文")
                translated = translate_text(query, direction)

            # 显示翻译结果（带原语言提示）
            st.markdown(f"**翻译结果：**")
            st.markdown(translated)

            # 添加复制按钮（用代码块形式方便复制）
            st.code(translated, language="text")

        # 3. 保存到历史和数据库
        st.session_state.messages.append({"role": "assistant", "content": translated})
        memory_db.save_message(session_id, user_id, "assistant", translated)

    # ========== 正常技术支持模式 ==========
    else:
        # ⏱️ 从点击发送开始计时（包含所有处理：路由、检索、生成）
        start_time = time.time()

        # 先复制一份"用户本轮输入前"的历史，传给 Agent 用来理解追问。
        # 例如上一轮答了 powerOnCard，这一轮用户问"那这个 API 调用前要注意什么？"，
        # Agent 就能从 old_history 里知道"这个 API"指上一轮提到的内容。
        old_history = st.session_state.messages.copy()

        # 1. 先把用户这条显示出来并存进历史
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        # 保存用户消息到数据库
        memory_db.save_message(session_id, user_id, "user", query)

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
                # 计算总耗时（从点击发送到答案生成完毕）
                elapsed = time.time() - start_time
                model_used = result.get("provider_model", "unknown") if result else "unknown"
                # 在答案后添加耗时和模型信息
                answer += f"\n\n---\n⏱️ 响应时间: {elapsed:.2f}秒 | 模型: {model_used}"
            except Exception as e:
                result = None
                elapsed = time.time() - start_time
                answer = (
                    f"⚠️ 出错了：{e}\n\n"
                    "（公司电脑检查内网网关连通；家里电脑确认 .env 里 "
                    "`LLM_PROVIDER` 和 key 有效）"
                    f"\n\n---\n⏱️ 响应时间: {elapsed:.2f}秒"
                )
            st.markdown(answer)
            render_result_details(result)

        # 3. 答案也存进历史，下次重跑能重现整段对话
        st.session_state.messages.append({"role": "assistant", "content": answer, "result": result})
        # 保存助手回复到数据库
        memory_db.save_message(session_id, user_id, "assistant", answer,
                               tools_used=result.get("tools_used") if result else None)
