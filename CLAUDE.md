# KOZEN AI Assistant - 项目上下文

## 项目目标
构建一个智能 FAE 技术支持 Agent —— 不止是文档问答，而是像一个有经验的同事，能多轮引导排查、记住历史对话、自动沉淀案例。

## 背景
- 用户是上海翔诚通信科技有限公司（KOZEN）的 FAE（技术支持工程师）
- 日常处理 KOZEN Financial SDK V1.8 和 Terminal Manager SDK V1.4 的客户支持问题
- 研究生方向是 AI 大模型，有 Java 技术栈基础
- 希望通过这个项目积累"AI + 金融科技"的实战经验，用于求职

## 架构设计（2026-05-14 更新）

### 四层架构
```
┌─────────────────────────────────────────┐
│           Streamlit UI                   │
│  聊天面板 / 会话列表 / 案例管理 / 知识面板 │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│       LangGraph Agent Runtime            │
│                                          │
│  理解问题 → 检索知识 → [路由判断]         │
│              ├─ 信息足够 → 生成答案       │
│              └─ 信息不足 → 反问用户       │
│                                          │
│  工具: search_docs / lookup_error /       │
│        search_cases                       │
│  State: Checkpointer (SQLite) 持久化      │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│           Memory Layer                   │
│  - 短期: LangGraph Checkpointer          │
│  - 长期: SQLite + LLM 自动摘要           │
│  - 用户画像 / 会话历史 / 知识片段         │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│         Retrieval Layer                  │
│  - 向量检索: ChromaDB (语义匹配)          │
│  - 关键词: BM25 (精确匹配)               │
│  - 混合排序: RRF 融合                     │
└─────────────────────────────────────────┘
```

### 技术栈
| 层 | 组件 | 用途 |
|---|---|---|
| Agent 编排 | LangGraph | 状态图驱动，复杂分支路由，checkpoint 自动持久化 |
| 混合检索 | ChromaDB + BM25 | 语义匹配 + 关键词精确匹配，RRF 融合排序 |
| 长期记忆 | SQLite + LLM 摘要 | 会话结束自动压缩归档，跨会话注入上下文 |
| LLM | DeepSeek Chat API | Function Calling 兼容 OpenAI 格式 |
| 嵌入模型 | paraphrase-multilingual-MiniLM-L12-v2 | 跨语言中英文检索 |
| 前端 | Streamlit | 聊天界面 + 会话管理侧边栏 |
| 开发方式 | Claude Code + DeepSeek Vibe Coding |
| 语言 | Python |

### 核心能力
- 多轮排查引导（不是一问一答，Agent 主动反问澄清）
- 跨会话记忆（"你上次那个刷卡问题解决了吗？"）
- 自动案例归档（解决后 LLM 自动提取知识点存入 cases.jsonl）
- 混合检索（新人用大白话也能搜到，老手用术语也能精确匹配）

## 公司知识库（AI 部门提供）
- 目录: `DevDocForAIAgent_260507@latest/`
- 三个产品线: kozen_component (5) / kozen_financial (19) / kozen_terminal (12) = 36 个 md
- 格式: YAML frontmatter + 结构化 API 表格 + 关联文档链接
- 来源: AI 部门用 LLM-Wiki + Obsidian + Hermes 技术栈处理原始 .docx 产出
- 质量远高于 parse_docs.py 正则产物，将替换为知识库数据源

### 公司技术栈（参考）
- **LLM-Wiki**: Hermes 技能，LLM 驱动原始文档 → 结构化 wiki md
- **Obsidian**: 知识管理/可视化，markdown 即数据库，支持图谱浏览
- **Hermes**: 开源 Agent 框架，三级记忆 + FTS5 检索 + 技能学习循环
- 核心理念: "编译时"处理（提前结构化），不同于我们的"运行时" RAG

## 项目结构
```
kozen-ai-assistant/
├── data/
│   ├── processed/
│   │   ├── financial_sdk/       # parse_docs.py 产出（将被公司知识库替换）
│   │   └── terminal_manager_sdk/
│   ├── error_codes.json         # 结构化错误码（100+条）
│   └── cases.jsonl              # FAE 支持案例（持续积累）
├── DevDocForAIAgent_260507@latest/  # 公司AI部门知识库（36个md，高质量）
│   ├── kozen_component/
│   ├── kozen_financial/
│   └── kozen_terminal/
├── src/
│   ├── parse_docs.py            # PDF → Markdown（已完成，将被替换）
│   ├── ingest.py                # 文档切片 + 向量化入库（已完成）
│   ├── retrieve.py              # 混合检索层 ChromaDB + BM25（待开发）
│   ├── memory.py                # 长期记忆 + 会话管理（待开发）
│   ├── agent.py                 # LangGraph Agent 核心逻辑（待开发）
│   └── app.py                   # Streamlit 前端（待开发）
├── chroma_db/                   # 向量数据库（本地持久化，gitignore）
└── requirements.txt
```

## Git 仓库
- GitHub: https://github.com/Daenerys06-it/kozen-ai-assistant
- 用户名: Daenerys06-it
- 仓库设为 Private

## 开发策略
- 阶梯式: retrieve.py → memory.py → agent.py → app.py
- 每次只写一个函数，跑通再下一个
- FAE 问题日志持续积累到 cases.jsonl

## 进度
- [x] parse_docs.py — PDF转Markdown（后续替换为公司知识库）
- [x] error_codes.json — Financial SDK错误码结构化（100+条）
- [x] ingest.py — 文档切片+向量化入库（581 chunks，已跑通）
- [ ] retrieve.py — 混合检索（ChromaDB + BM25 + RRF）
- [ ] memory.py — 长期记忆 + 会话管理
- [ ] agent.py — LangGraph Agent 核心逻辑
- [ ] app.py — Streamlit 前端

## 笔记
- Python 3.11.9 已安装（C:\Program Files\Python311）
- 用户环境有代理 127.0.0.1:7897，pip install 需加 --proxy
- 运行时需设置环境变量 http_proxy 和 https_proxy（小写）
- Python Scripts 路径已加入用户 PATH（含 setx 永久配置）
- 公司电脑 pdftotext 可用（MinGW 环境）
- 文档来源：两份官方 PDF，已用 pdftotext 提取文本并按模块拆分
- 03_cardreader.md 含坏字节 0xAD，已通过编码 fallback 解决
