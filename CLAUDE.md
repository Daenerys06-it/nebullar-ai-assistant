# KOZEN AI Assistant - 项目上下文

## 项目目标
构建一个 KOZEN 金融终端 SDK 的 AI 智能技术支持助手（RAG + Agent）。

## 背景
- 用户是上海翔诚通信科技有限公司（KOZEN）的 FAE（技术支持工程师）
- 日常处理 KOZEN Financial SDK V1.8 和 Terminal Manager SDK V1.4 的客户支持问题
- 研究生方向是 AI 大模型，有 Java 技术栈基础
- 希望通过这个项目积累"AI + 金融科技"的实战经验，用于求职

## 技术栈
- LLM: DeepSeek API（便宜且中文友好）
- 向量数据库: ChromaDB（轻量，零配置）
- 前端: Streamlit
- 嵌入模型: text-embedding-3-small 或 BGE 中文
- 开发方式: Claude Code + DeepSeek Vibe Coding
- 语言: Python

## 项目结构
```
kozen-ai-assistant/
├── data/
│   ├── processed/
│   │   ├── financial_sdk/      # Financial SDK 按模块拆分（13个md）
│   │   └── terminal_manager_sdk/  # Terminal Manager SDK 按模块拆分（10个md）
│   ├── error_codes.json        # 结构化错误码（100+条）
│   └── cases.jsonl             # FAE 支持案例（手动积累）
├── src/
│   ├── parse_docs.py           # PDF → Markdown
│   ├── ingest.py               # 文档切片 + 向量化入库（待开发）
│   ├── rag.py                  # 检索层（待开发）
│   ├── agent.py                # Agent 核心逻辑（待开发）
│   └── app.py                  # Streamlit 前端（待开发）
├── chroma_db/                  # 向量数据库（本地持久化）
└── requirements.txt
```

## Git 仓库
- GitHub: https://github.com/Daenerys06-it/kozen-ai-assistant
- 用户名: Daenerys06-it
- 仓库设为 Private

## 开发策略
- 阶梯式实现：RAG → Agent → 迭代优化
- 使用 Vibe Coding，每次只写一个函数，跑通再下一个
- FAE 问题日志持续积累到 cases.jsonl

## 笔记
- 公司电脑没有 Python，需要安装后再开发
- 公司电脑 pdftotext 可用（MinGW 环境）
- 文档来源：两份官方 PDF，已用 pdftotext 提取文本并按模块拆分
