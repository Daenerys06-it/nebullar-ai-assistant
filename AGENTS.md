# Nebullar AI Assistant - 项目上下文

## 项目目标
部门级智能 FAE 技术支持 Agent（覆盖 Nebullar SDK 及部门文档）——不止文档问答，而像有经验的同事：多轮引导排查、命中历史案例、信息不足先反问。

## 背景
- 用户是上海翔诚通信科技（Nebullar）的 FAE，处理 Financial SDK / Terminal Manager SDK 客户支持
- 研究生方向 AI 大模型，有 Java 基础，借项目积累 RAG/Agent 工程经验用于求职
- 边学边写：先讲概念 → 给骨架留空 → 用户填核心 → 我补修

## 架构（当前）
- **检索 RAG**：ChromaDB 向量 + BM25 关键词 + RRF 召回 → BGE Cross-Encoder 精排
- **Agent 编排**：LangGraph StateGraph —— analyze 路由 → 工具(lookup_error / search_cases / search_docs) → generate → 自我纠错回路；节点级流式
- **记忆**：短期对话上下文（history）；案例库 cases.jsonl（已向量化语义检索）。⚠️ 持久化/跨会话 Memory 未做（ROADMAP 后续，用 LangGraph checkpointer）
- **前端**：Streamlit 聊天 + 节点进度 + 来源展示

## 技术栈
| 用途 | 选型 |
|---|---|
| LLM | Kimi/GPT-5（公司内网网关）/ DeepSeek（家里），`LLM_PROVIDER` 切换 + fallback |
| 检索 | ChromaDB + rank_bm25 + RRF + BGE-reranker-base（Cross-Encoder 精排） |
| 嵌入 | paraphrase-multilingual-MiniLM-L12-v2（跨语言中英文，库锁 <5） |
| 编排 | LangGraph StateGraph（路由 / 工具 / 自我纠错回路 / 节点级流式） |
| 前端 | Streamlit |
| 语言 | Python 3.11 |

## 数据源
- `DevDocForAIAgent_260507@latest/`：公司知识库（结构化 md，三产品线 component/financial/terminal），入库 545 chunks
- `data/error_codes.json`：结构化错误码（精确查表，与向量检索互补）
- `data/cases.jsonl`：FAE 支持案例（持续沉淀，核心差异化资产）

## 项目结构
```
src/
├── ingest.py     # 文档切片 + 向量化入库（545 chunks）
├── retrieve.py   # 召回(向量+BM25+RRF) + Cross-Encoder 精排
├── llm.py        # LLM provider 抽象 Kimi/GPT-5/DeepSeek + fallback
├── memory.py     # 案例语义检索 search_cases（向量化）
├── agent.py      # LangGraph 图：路由+工具+自我纠错+流式（ask_structured / ask_structured_stream）
├── app.py        # Streamlit 前端
└── parse_docs.py # 已弃用
tests/test_agent_eval.py   # 4 条回归测试
```
> 流程权威图见 `src/agent.py` 顶部图注；升级路线 + 知识补给清单见根目录 `ROADMAP.md`。

## 进度（里程碑）
- [x] RAG：ingest / 混合检索（向量+BM25+RRF）/ 查询重写
- [x] llm.py：provider 抽象 + fallback；公司/家庭环境模板
- [x] Agent：lookup_error 查表 / 多轮 / 反问澄清 / 结构化返回 / 4 条回归测试
- [x] LangGraph 重构：动态路由 + 自我纠错回路 + 节点级流式
- [x] **#1 Reranker**：RRF 召回 top20 → Cross-Encoder 精排 top5（懒加载 + 家里优雅降级）
- [x] **#2 案例向量化**：search_cases 关键词 → 语义检索（Bi-Encoder + 余弦 + 阈值）
- [x] 案例 5 条：adb / OTA send DA fail(0xC0060003) / D0552 strong integrity / P18 data_mux
- [x] **#3 HyDE/Multi-Query**：检索前查询扩展（Multi-Query 生成 3 个变体 + HyDE 假设文档）
- [x] **#4 FastAPI+SSE**：api.py 后端 + static/index.html 前端测试页面，完整流式输出
- [ ] 下一步：见 ROADMAP.md（#5 MCP 工具化 → #6 Docker+LangSmith → … → 持久化 Memory / 微调）

## 已知待优化
- keyword_search 每次重建 BM25 索引（性能）
- BM25 `.split()` 对中文查询无效，靠向量检索互补
- `analyze_query` 仍是规则版，可升级 LLM router / 原生 tool calling
- 持久化对话 Memory、自动案例沉淀未做（计划用 LangGraph checkpointer）

## Git
- GitHub: https://github.com/Daenerys06-it/kozen-ai-assistant（Private；仓库名仍是 kozen，待改 Nebullar）
- 公司电脑与家里电脑通过 GitHub 同步；chroma_db 不入库，clone 后需重跑 ingest.py

## 环境笔记（公司电脑 / 家庭电脑 分开）

### 公司电脑（主力，Kimi / GPT-5 可选）
- 公司电脑复制 `env.company.example` 为 `.env`：`Copy-Item env.company.example .env`
- **用 Kimi**：`.env` 设 `LLM_PROVIDER=kimi`，走公司内网 Anthropic-compatible 网关 `KIMI_BASE_URL=http://10.10.5.136:8080`
- **用 GPT-5**（当可用时）：`.env` 设 `LLM_PROVIDER=gpt5`，走 `GPT5_BASE_URL=http://10.10.85.155:3000/openapi`
- 网关 IP 已加入用户级 `NO_PROXY`（`10.10.5.136,10.10.85.155,localhost,127.0.0.1`）确保直连
- **pip 直连公网 PyPI，不需要代理**（连公司 wifi 即可上外网）
- **HuggingFace 必须离线**：公司网络会重置 huggingface.co（10054）。ingest/retrieve/memory 顶部已 `os.environ.setdefault("HF_HUB_OFFLINE","1")` 走本地缓存
- **嵌入库锁 <5**：`sentence-transformers 4.1.0` / `transformers 4.57.6` / `huggingface_hub 0.36.2`。5.x 会把纯文本模型走 AutoProcessor 而崩溃
- **下载新 HF 模型走镜像**：`huggingface.co` 被重置（curl 000），但 `hf-mirror.com` 通（200）。下新模型用 `HF_ENDPOINT=https://hf-mirror.com python -c "..."`，缓存后再回离线。已用此法下 `BAAI/bge-reranker-base`
- **算力：本机纯 CPU**（torch `+cpu`，无 GPU，12 核）。微调只能做 CPU 友好小任务（意图分类：冻结嵌入 + 小分类头）；LLM 微调需免费云 GPU。详见 ROADMAP #8

### 家庭电脑（下班继续，只能连 DeepSeek）
- 复制 `env.home.example` 为 `.env`；网关是公司内网家里访问不到 → 固定 `LLM_PROVIDER=deepseek`，只填 `DEEPSEEK_API_KEY`
- `.env` 被 gitignore、不随仓库同步：家里 clone 后照 `env.home.example` 新建
- 首次跑 ingest 若本地无嵌入模型缓存：临时 `set HF_HUB_OFFLINE=0` 让它下载一次（约 420MB），缓存后恢复离线。reranker 模型同理（走 hf-mirror）
- 家里没 reranker 模型缓存时，`search()` 会自动退回 RRF（已做优雅降级，不崩）

### 通用
- Python Scripts 路径已加入用户 PATH（setx 永久）
- 嵌入/reranker 模型缓存在 `~/.cache/huggingface`，不入库
- 控制台中文乱码是 Windows GBK 显示问题，`$env:PYTHONUTF8=1` 可消除，不影响逻辑
