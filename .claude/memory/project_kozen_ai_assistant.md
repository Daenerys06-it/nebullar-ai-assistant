---
name: project_kozen_ai_assistant
description: KOZEN SDK AI assistant project — LangGraph Agent + Hybrid RAG for FAE support
type: project
originSessionId: 503bdc81-3792-4c10-af93-e03db3930c46
---

## KOZEN AI Assistant 项目

用户正在构建一个智能 FAE 技术支持 Agent —— 不止是文档问答，而是像一个有经验的同事，能多轮引导排查、记住历史对话、自动沉淀案例。

**Why**: 将 FAE 实习经历转化为 AI 工程实践的成果，用于 AI 方向求职。

**How to apply**:
- 项目当前在 D:\kozen-ai-assistant，有完整 CLAUDE.md
- GitHub 仓库: https://github.com/Daenerys06-it/kozen-ai-assistant（Private）
- 用户在公司电脑和家里电脑之间通过 GitHub 同步
- 记忆文件随项目提交到 .claude/memory/，回家 clone 即可带记忆
- 开发策略：阶梯式（retrieve → memory → agent → app），Vibe Coding + DeepSeek

## 2026-05-14 进展

### 架构升级
目标从"文档问答 RAG"升级为"智能同事 Agent"：

四层架构:
- Retrieval: ChromaDB 向量检索 + BM25 关键词，RRF 混合排序
- Memory: LangGraph Checkpointer (短期) + SQLite + LLM 自动摘要 (长期)
- Agent: LangGraph 状态图驱动，多轮排查引导，自动案例归档
- UI: Streamlit 聊天界面 + 会话管理侧边栏

技术栈: LangGraph + ChromaDB + BM25 + DeepSeek + Streamlit + SQLite

### 公司知识库
- AI 部门给了 DevDocForAIAgent_260507@latest/，36 个结构化 md（YAML frontmatter + API 表格）
- 三个产品线: kozen_component / kozen_financial / kozen_terminal
- 公司技术栈: LLM-Wiki (Hermes 技能，文档结构化) + Obsidian (知识管理) + Hermes (Agent 框架)
- 核心理念对比: 公司 = "编译时"预处理结构化 → 查结构化知识；我们 = "运行时" RAG → 搜碎片拼答案。互补

### ingest.py
- [x] 已完成首次运行，581 chunks 入库 ChromaDB
- 模型已下载，代理需设 http_proxy/https_proxy（小写）
- 编码兼容: UTF-8 → GBK → UTF-8(errors=replace)

### 开发计划
- [x] retrieve.py — vector_search 已写（ChromaDB向量检索），待加BM25+RRF
- [ ] memory.py — 长期记忆 + 会话管理
- [ ] agent.py — LangGraph Agent 核心逻辑
- [ ] app.py — Streamlit 前端

### 2026-05-25
- 公司知识库（72 md）替换旧数据，545 chunks 入库 ChromaDB
- retrieve.py 开始开发，用户想边学边写
- 教法：先讲概念 → 给函数签名 → 用户试写 → 我补修

### 核心能力目标
- 多轮排查引导（Agent 主动反问澄清）
- 跨会话记忆（"你上次那个刷卡问题解决了吗？"）
- 自动案例归档（解决后 LLM 自动提取知识点）
- 混合检索（新人用大白话也能搜，老手用术语也能精搜）

### 2026-06-10 进展（当前真实状态，以此为准）
- ingest.py 改用 MarkdownHeaderTextSplitter 按标题切，chunk带[模块|章节]前缀，614 chunks（解决表格被截断）
- retrieve.py 完成：vector_search/keyword_search/RRF/search + rewrite_query 查询重写（LLM扩展口语→检索词，原问题保底）
- agent.py MVP 完成：load_client/build_prompt/ask，RAG问答跑通（实测-70004答得专业）
- 离线模式：ingest/retrieve 顶部加 HF_HUB_OFFLINE，embedding 用本地缓存，**DeepSeek 直连不再需要代理**
- 最新提交 2c94a15，已同步 GitHub
- 本次会话踩坑：用户自建 PostToolUse hook 注入测试（inject_test.py 自我恢复），干扰工具输出，已大致清理

### 2026-06-11 ✅ 已切换到公司 Claude 网关 + 项目改名 Nebullar
- LLM 切换完成：DeepSeek → Claude Opus 4.8（model=claude-opus-4-8），已实测网关连通（usage 正常返回）
  - .env：ANTHROPIC_BASE_URL=http://10.10.85.155:3000/api，ANTHROPIC_AUTH_TOKEN=cr_...
  - agent.py / retrieve.py：从 OpenAI 格式(chat.completions) 换成 anthropic SDK(messages.create，system 单独传)；**删掉 temperature**（Opus 4.8 不支持，传了 400）；响应取 `"".join(b.text for b in resp.content if b.type=="text")`
  - load_client() 改 anthropic.Anthropic()，base_url/auth_token 由 SDK 从环境变量自动注入
  - requirements.txt 删 openai；未上 adaptive thinking（MVP 保持简单，后续可加 `thinking={"type":"adaptive"}`）
- **内网网关坑：不要挂代理**。若 shell 里设了 http_proxy/https_proxy（DeepSeek 时代留的），到 10.10.85.155 的请求会绕去 127.0.0.1:7897 失败 → NO_PROXY 加内网 IP，或当前 shell 不设代理（实测裸跑直连 OK）
- **改名决策（用户拍板）**：项目/代码改 Nebullar，**文档库正文保留 KOZEN**。Why：DevDocForAIAgent 正文含真实 API 类名 KozenFinancialService 等，是客户真在用的符号，乱改会让助手引用不存在的类，破坏 RAG 准确性
  - 已改：collection 名 kozen_docs → **nebullar_docs**（ingest.py + retrieve.py）；README 标题；CLAUDE.md 技术栈/MVP 的 LLM 说明
  - 文档文件夹已是 Nebullar_{component,financial,terminal}/，但文件名仍 kozen-*.md、正文仍 KOZEN —— **故意保留**
  - 嵌套冗余目录 DevDocForAIAgent_260507@latest/DevDocForAIAgent_260507@latest/ 仍在（ingest 已跳过，无害）
- ⚠️ **collection 改名后必须重跑 `python src/ingest.py` 一次**，否则 retrieve 找不到 nebullar_docs（现有 chroma_db 还是旧的 kozen_docs）
