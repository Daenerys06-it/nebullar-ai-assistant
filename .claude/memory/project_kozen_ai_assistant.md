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
