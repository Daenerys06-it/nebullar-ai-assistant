# KOZEN AI Assistant

基于 RAG + Agent 的 KOZEN SDK 智能技术支持助手。

## 项目结构

```
├── data/
│   ├── processed/
│   │   ├── financial_sdk/      # KOZEN Financial SDK 按模块拆分的文档
│   │   └── terminal_manager_sdk/  # KOZEN Terminal Manager SDK 文档
│   ├── error_codes.json        # 结构化错误码
│   └── cases.jsonl             # 真实客户支持案例（持续积累）
├── src/
│   ├── parse_docs.py           # PDF → Markdown 结构化处理
│   ├── ingest.py               # 文档切片 + 向量化入库
│   ├── rag.py                  # 检索层
│   ├── agent.py                # Agent 核心逻辑
│   └── app.py                  # Streamlit 前端
├── chroma_db/                  # 向量数据库（gitignore）
└── requirements.txt
```

## 快速开始

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 文档向量化入库
python src/ingest.py

# 3. 启动前端
streamlit run src/app.py
```

## 技术栈

- **LLM**: Claude API / DeepSeek API
- **向量数据库**: ChromaDB
- **嵌入模型**: text-embedding-3-small
- **前端**: Streamlit

## 数据说明

- `data/processed/`: SDK 文档按模块拆分的 markdown，来源为官方 PDF
- `data/error_codes.json`: 从文档提取的结构化错误码
- `data/cases.jsonl`: 日常 FAE 工作中记录的真实支持案例（手动维护）
