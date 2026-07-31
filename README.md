# Nebullar AI Assistant

基于 RAG + Agent 的智能技术支持助手——帮 FAE 从"翻文档"到"问 AI"。

## 项目结构

```
├── data/
│   ├── error_codes.json    # 结构化错误码（精确查表）
│   └── cases.jsonl         # FAE 支持案例（持续积累）
├── DevDocForAIAgent_260507@latest/   # 公司知识库（结构化 md）
├── src/
│   ├── ingest.py           # 文档切片 + 向量化入库
│   ├── retrieve.py         # 召回(向量+BM25+RRF) + Cross-Encoder 精排
│   ├── llm.py              # LLM provider 抽象 Kimi/GPT-5(公司)/DeepSeek(家里) + fallback
│   ├── memory.py           # 案例语义检索 search_cases（向量化）
│   ├── agent.py            # LangGraph 图：路由+工具+自我纠错+流式
│   └── app.py              # Streamlit 聊天前端
├── tests/                  # 回归测试
└── chroma_db/              # 向量数据库（gitignore）
```

## 技术栈

- **LLM**: Kimi（公司内网网关）/ GPT-5（公司备用）/ DeepSeek（家里）—— `.env` 的 `LLM_PROVIDER` 切换 + fallback
- **检索**: ChromaDB（向量）+ rank_bm25（关键词）+ RRF 融合 + **BGE-reranker-base 精排**
- **编排**: **LangGraph**（动态路由 / 工具 / 自我纠错回路 / 节点级流式）
- **嵌入**: paraphrase-multilingual-MiniLM-L12-v2（跨语言中英文，库锁 <5）
- **前端**: Streamlit

## 环境配置：公司电脑 / 家庭电脑（换电脑必看）

凭据放 `.env`（gitignore，不随仓库同步），每台电脑用自己的。模板拆成两个：`env.company.example`（公司）/ `env.home.example`（家里）。

### 公司电脑（Kimi 主用 / GPT-5 备用）
```powershell
Copy-Item env.company.example .env
# 编辑 .env：主用 Kimi → LLM_PROVIDER=kimi；备用 GPT-5 → LLM_PROVIDER=gpt5
```
- 两个网关：Kimi `http://10.10.5.136:8080`，GPT-5 `http://10.10.85.155:3000/openapi`
- pip / 模型下载直连公网，不用代理；HuggingFace 走本地缓存（代码已强制 `HF_HUB_OFFLINE`）
- 下新模型（如 reranker）走镜像：`HF_ENDPOINT=https://hf-mirror.com`

### 🏠 家庭电脑（连不上网关，用 DeepSeek）—— 首次照做
```powershell
pip install -r requirements.txt          # 嵌入库必须 <5
Copy-Item env.home.example .env          # 编辑 .env：填 DEEPSEEK_API_KEY
$env:HF_HUB_OFFLINE=0                     # 首次允许联网下嵌入模型（约 420MB）
python src/ingest.py                      # 建向量库（chroma_db 不入库，换机必须重跑）
python src/agent.py                       # 验证整条链路
```
> 缓存好后下次不用再设 `HF_HUB_OFFLINE`。家里没 reranker 模型时检索会自动退回 RRF，不影响使用。

## 快速开始（环境已配好后）
```powershell
python src/ingest.py        # 文档向量化入库
python src/agent.py         # 一问一答验证
.\start_app.ps1             # 启动 Streamlit 前端
```

## 进度

- [x] RAG：混合检索（向量+BM25+RRF）+ 查询重写
- [x] llm.py：多 provider 抽象 + fallback；公司/家庭环境模板
- [x] Agent：错误码查表 / 多轮 / 反问澄清 / 结构化返回 / 回归测试
- [x] LangGraph 重构：动态路由 + 自我纠错回路 + 节点级流式
- [x] #1 Reranker：RRF 召回 → Cross-Encoder 精排
- [x] #2 案例向量化：search_cases 关键词 → 语义检索
- [x] #3 HyDE/Multi-Query：检索前查询扩展
- [x] #4 FastAPI+SSE：api.py 后端 + 前端测试页面
- [ ] 下一步见 [ROADMAP.md](ROADMAP.md)：#5 MCP 工具化 → #6 Docker+LangSmith → … → 持久化 Memory / 微调

## 当前效果

- `刷卡返回 -70004 怎么排查？` → 先 `lookup_error` 查表识别 `APDU Error`，再结合 SDK 文档给排查建议
- `刷卡无反应怎么办`（信息不足）→ 先反问卡类型、读卡方式、当前 API，而非堆一串 API
- `adb 查不到设备`、`P18 刷机刷不动` → 语义命中历史案例（哪怕没有共同关键词）
- 前端回答下方可展开：命中的工具、错误码释义、历史案例、参考文档来源
