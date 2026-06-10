# Nebullar AI Assistant - 项目上下文

## 项目目标
部门级智能 FAE 技术支持 Agent（覆盖 KOZEN SDK 及部门通用文档）——不止文档问答，而像有经验的同事：多轮引导排查、记住历史对话、自动沉淀案例。

## 背景
- 用户是上海翔诚通信科技（KOZEN）的 FAE，处理 Financial SDK V1.8 和 Terminal Manager SDK V1.4 客户支持
- 研究生方向 AI 大模型，有 Java 基础，借项目积累"AI+金融科技"经验用于求职
- 个人主导开发本部门的 AI Assistant（Nebullar）
- 边学边写：先讲概念 → 给函数签名 → 用户试写 → 我补修

## 四层架构
- **UI** (Streamlit): 聊天面板 / 会话列表 / 案例管理
- **Agent**: 理解问题 → 检索 → 路由判断（信息够→答案 / 不够→反问）；工具 search_docs / lookup_error / search_cases
- **Memory**: 短期对话上下文 + 长期 cases.jsonl 沉淀
- **Retrieval**: ChromaDB 向量 + BM25 关键词 + RRF 融合

> 注：Agent 框架 LangGraph vs 手写 loop 待定。第一版先手写 loop 跑通再考虑 LangGraph。Memory 层暂不做 LLM 自动摘要等重设计。

## 技术栈
| 用途 | 选型 |
|---|---|
| LLM | DeepSeek Chat API（Function Calling 兼容 OpenAI 格式） |
| 检索 | ChromaDB + rank_bm25 + RRF |
| 嵌入模型 | paraphrase-multilingual-MiniLM-L12-v2（跨语言中英文） |
| 前端 | Streamlit |
| 语言 | Python 3.11.9 |

## 数据源
- **公司知识库** `DevDocForAIAgent_260507@latest/`：36个结构化md，三产品线（component 5 / financial 19 / terminal 12），YAML frontmatter + API 表格。AI部门用 LLM-Wiki + Obsidian + Hermes 处理 .docx 产出
- `data/error_codes.json`：结构化错误码（精确查表用，与向量检索互补）
- `data/cases.jsonl`：FAE 支持案例（持续积累，核心差异化资产）

## 项目结构
```
src/
├── parse_docs.py   # PDF→md（已弃用）
├── ingest.py       # 切片+向量化入库（已完成，545 chunks）
├── retrieve.py     # 混合检索 向量+BM25+RRF（已完成）
├── memory.py       # 长期记忆（待开发）
├── agent.py        # Agent核心（进行中）
└── app.py          # Streamlit前端（待开发）
```

## 进度
- [x] ingest.py — 545 chunks 入库 ChromaDB
- [x] retrieve.py — vector_search / keyword_search / RRF / search 入口
- [ ] **agent.py（进行中，先做 MVP）**
- [ ] memory.py → app.py

## Agent MVP（第一版，手写 loop 不用 LangGraph）
目标：一问一答跑通——`ask("刷卡-70004怎么办")` 返回基于真实文档的中文排查建议。

数据流：用户问题 → search() 检索top5碎片 → 拼prompt → DeepSeek生成 → 返回答案

三个函数：
- `load_client()` — 从 .env 读 DEEPSEEK_API_KEY，建 OpenAI 兼容客户端
- `build_prompt(query, docs)` — 拼 [系统角色 + 检索文档 + 用户问题]
- `ask(query)` — 主流程：检索 → 拼prompt → 调DeepSeek → 返回

prompt 原则：开卷考试，把文档摆给 LLM，文档没有就说"未找到"，禁止编造（防幻觉）。

MVP 刻意不做（留后续）：多轮 / 记忆 / 工具自动选择 / 反问 / LangGraph。
迭代路线：MVP → 多轮 → 工具调用(search/lookup_error/search_cases) → 反问澄清 →（再考虑 LangGraph 重构）

## 已知待优化
- keyword_search 每次重建 BM25 索引（性能，agent 阶段优化）
- BM25 `.split()` 对中文查询无效，靠向量检索互补
- lookup_error 工具接 error_codes.json 做精确查表（待 agent 阶段）

## Git
- GitHub: https://github.com/Daenerys06-it/kozen-ai-assistant（Private）
- 公司电脑与家里电脑通过 GitHub 同步；chroma_db 不入库，clone 后需重跑 ingest.py

## 环境笔记
- 代理 127.0.0.1:7897；运行需设小写环境变量 http_proxy / https_proxy；pip install 加 --proxy
- Python Scripts 路径已加入用户 PATH（setx 永久配置）
- 嵌入模型首次运行下载约 420MB
- 文档编码兼容：UTF-8 → GBK → UTF-8(errors=replace)，解决坏字节 0xAD
