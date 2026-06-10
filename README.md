# KOZEN AI Assistant

基于 RAG + Agent 的 KOZEN SDK 智能技术支持助手——帮 FAE 从"翻文档"到"问 AI"。

## 项目结构

```
├── data/
│   ├── error_codes.json    # 结构化错误码（精确查表）
│   └── cases.jsonl         # FAE 支持案例（持续积累）
├── DevDocForAIAgent_260507@latest/   # 公司知识库（36个结构化md）
├── src/
│   ├── parse_docs.py       # PDF → Markdown（已弃用）
│   ├── ingest.py           # 文档切片 + 向量化入库
│   ├── retrieve.py         # 混合检索（向量+关键词+RRF）
│   ├── memory.py           # 长期记忆（开发中）
│   ├── agent.py            # Agent 核心逻辑（开发中）
│   └── app.py              # Streamlit 前端（开发中）
└── chroma_db/              # 向量数据库（gitignore）
```

## 快速开始

```bash
pip install -r requirements.txt   # 安装依赖
python src/ingest.py              # 文档向量化入库（首次下载约420MB嵌入模型）
streamlit run src/app.py          # 启动前端（开发中）
```

## 技术栈

- **LLM**: Claude (Anthropic API)
- **检索**: ChromaDB（向量）+ rank_bm25（关键词）+ RRF 融合
- **嵌入模型**: paraphrase-multilingual-MiniLM-L12-v2（跨语言中英文）
- **前端**: Streamlit

## 进度

- [x] ingest.py — 文档向量化入库（545 chunks）
- [x] retrieve.py — 混合检索层
- [ ] memory.py / agent.py / app.py
