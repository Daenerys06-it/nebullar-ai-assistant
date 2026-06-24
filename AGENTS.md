# Nebullar AI Assistant - 项目上下文

## 项目目标
部门级智能 FAE 技术支持 Agent（覆盖 Nebullar SDK 及部门通用文档）——不止文档问答，而像有经验的同事：多轮引导排查、记住历史对话、自动沉淀案例。

## 背景
- 用户是上海翔诚通信科技（Nebullar）的 FAE，处理 Financial SDK V1.8 和 Terminal Manager SDK V1.4 客户支持
- 研究生方向 AI 大模型，有 Java 基础，借项目积累"AI+金融科技"经验用于求职
- 个人主导开发本部门的 AI Assistant（Nebullar）
- 边学边写：先讲概念 → 给函数签名 → 用户试写 → 我补修

## 四层架构
- **UI** (Streamlit): 聊天面板 / 会话列表 / 案例管理
- **Agent**: 理解问题 → 检索 → 路由判断（信息够→答案 / 不够→反问）；工具 search_docs / lookup_error / search_cases
- **Memory**: 短期对话上下文 + 长期 cases.jsonl 沉淀
- **Retrieval**: ChromaDB 向量 + BM25 关键词 + RRF 融合

> 注：Agent 已用 **LangGraph 重构**（StateGraph：analyze→动态路由→工具→generate→**自我纠错回路**），含**节点级流式**。Memory 层仍是 cases.jsonl 关键词检索，向量化待 ROADMAP #2。

## 技术栈
| 用途 | 选型 |
|---|---|
| LLM | GPT-5（公司可选）/ Claude Opus 4.8（公司 Anthropic 兼容网关）/ DeepSeek（家里） |
| 检索 | ChromaDB + rank_bm25 + RRF（+ BGE-reranker 精排，规划中 ROADMAP #1） |
| 编排 | LangGraph StateGraph（动态路由 / 工具 / 自我纠错回路 / 节点级流式） |
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
├── llm.py          # LLM 提供方抽象 GPT-5/Opus(公司)/DeepSeek(家里)（已完成）
├── memory.py       # 案例检索 search_cases（已完成，cases.jsonl 关键词版）
├── agent.py        # Agent核心（LangGraph 图：动态路由+工具+自我纠错回路+流式）
└── app.py          # Streamlit前端（聊天+节点级进度+来源展示）
```
> 根目录 `ROADMAP.md`：升级路线（Reranker / 记忆向量化 / HyDE / FastAPI+SSE / MCP / Docker / 微调）+ 知识补给清单。

## 进度
- [x] ingest.py — 545 chunks 入库 ChromaDB
- [x] retrieve.py — vector_search / keyword_search / RRF / search 入口
- [x] llm.py — 三路 provider：公司 GPT-5(/openapi) / 公司 Opus(/api) / 家里 DeepSeek
- [x] agent.py — MVP 跑通：lookup_error 精确查表、RAG 问答、短期多轮上下文、信息不足先反问
- [x] app.py — Streamlit 聊天前端第一版；`start_app.ps1` 一键启动
- [x] 环境模板 — `env.company.example` / `env.home.example` 分开，`.env.example` 只做入口说明
- [x] memory.py / search_cases 第一版 — 从 `data/cases.jsonl` 检索 FAE 历史案例并放入 Agent prompt
- [x] 结构化回答 / 来源展示第一版 — 前端展示 tools_used、错误码查表、历史案例、参考文档
- [x] 小型 eval 第一版 — 固定错误码、澄清反问、历史案例、结构化来源四类回归测试
- [x] LangGraph 重构 — ask_structured 迁移成图（State/节点/条件边），等价迁移测试 4/4
- [x] 动态路由 — 按意图分流：有错误码才查表，口语模糊先反问，其它直接检索
- [x] 自我纠错回路 — generate 后答案弱（"未覆盖"）则 refine 加宽检索词回 retrieve 再答一轮（MAX_RETRIES 防死循环）
- [x] 节点级流式 — ask_structured_stream + app.py st.status 实时显示 分析→查表→检索→生成
- [x] 案例已 3 条 — adb 设备 / OTA send DA fail(0xC0060003) / D0552 strong integrity
- [x] **ROADMAP #1 Reranker 完成** — retrieve.py RRF 召回 top20 → BGE-reranker-base Cross-Encoder 精排 top5（`rerank()` + 懒加载 + 家里机器优雅降级），测试 4/4
- [ ] 进行中：ROADMAP #2 案例记忆向量化 — search_cases 从关键词升级成向量检索
- [ ] 规划：见 ROADMAP.md（记忆向量化 / HyDE / FastAPI+SSE / MCP / Docker / 微调，按优先级）

## 当前可用效果
- `刷卡返回 -70004 怎么排查？`：先走 `lookup_error` 精确查表，识别 `-70004 = APDU Error`，再结合真实 SDK 文档生成排查建议
- `刷卡无反应怎么办`：信息不足时先反问卡类型、读卡方式、当前 API 调用位置，而不是直接堆一串 API
- `adb 查不到设备怎么办`：命中历史支持案例，优先提示检查开发者模式和 USB debugging
- Streamlit 前端已能做基础聊天，并把当前会话历史传给 `ask(query, history=...)`
- 前端回答下方可展开查看：命中的工具、错误码释义、历史案例和参考文档来源
- provider 已按电脑环境拆开：公司电脑用 GPT-5/Opus，家庭电脑用 DeepSeek；代码层通过 `LLM_PROVIDER` 切换，不改源码

## Agent（当前版：LangGraph 图，已不是手写 loop）
> 权威流程图见 `src/agent.py` 顶部的图注。节点：analyze / clarify / lookup_error / retrieve / generate / refine。
目标：`ask_structured("刷卡-70004怎么办")` 返回基于真实文档的中文排查建议 + 结构化来源。

当前数据流：
用户问题 → analyze_query() 路由分析 → 信息不足则反问 / 有错误码则 lookup_error() 精确查表 → search() 检索top5碎片 → 拼 prompt（最近对话历史 + 错误码释义 + 参考资料）→ 当前 provider（GPT-5 / Opus / DeepSeek）生成 → 返回答案

关键函数：
- `load_client()` / `complete()` — 从 .env 读 `LLM_PROVIDER`，建立 GPT-5 / Opus / DeepSeek 对应客户端并屏蔽 SDK 差异
- `lookup_error(code)` — 从 `data/error_codes.json` 精确查错误码；`-70004` → `APDU Error`
- `analyze_query(query, history)` — 轻量规则路由：抽错误码、识别刷卡/读卡排查意图、判断是否需要澄清
- `build_history_context(history)` — 取最近 6 条对话，支持“这个 API / 刚才那个错误码”等追问
- `build_prompt(query, docs)` — 拼 [系统角色 + 检索文档 + 用户问题]
- `ask(query, history=None)` — 主流程：分析 → 反问或查表+检索 → 拼prompt → 调当前 provider → 返回

prompt 原则：开卷考试，把文档摆给 LLM，文档没有就说"未找到"，禁止编造（防幻觉）。

当前仍刻意不做（留后续）：持久化会话 / 记忆向量化 / 自动案例沉淀。
迭代路线：MVP → 多轮 → 工具调用 → 反问澄清 → 小型 eval → ✅LangGraph 重构（动态路由+自我纠错+流式）→ **升级阶段见 ROADMAP.md（#1 Reranker 起步）**

## 已知待优化
- keyword_search 每次重建 BM25 索引（性能，agent 阶段优化）
- BM25 `.split()` 对中文查询无效，靠向量检索互补
- `analyze_query` 目前是规则版，后续可升级成 LLM router 或 LangGraph 节点
- 前端当前只做会话内短期上下文，刷新/重启后不保存；长期记忆留给 memory.py
- 需要 structured answer：返回 answer / sources / tools_used，方便前端展示来源
- 需要小型 eval：错误码、API、口语排查、资料不足四类用例防回归

## Git
- GitHub: https://github.com/Daenerys06-it/kozen-ai-assistant（Private）
- 公司电脑与家里电脑通过 GitHub 同步；chroma_db 不入库，clone 后需重跑 ingest.py

## 环境笔记（公司电脑 / 家庭电脑 分开）

### 公司电脑（主力，GPT-5 / Opus 二选一）
- 公司电脑复制 `env.company.example` 为 `.env`：`Copy-Item env.company.example .env`
- **用 GPT-5 / Codex 对话开发时**：`.env` 设 `LLM_PROVIDER=gpt5`，走公司内网 Anthropic-compatible GPT 网关 `GPT5_BASE_URL=http://10.10.85.155:3000/openapi`，`GPT5_AUTH_TOKEN=cr_...`，Agent 运行时调用 `GPT5_MODEL=gpt-5`
- **用 Opus / Claude Code 对话开发时**：`.env` 设 `LLM_PROVIDER=opus`，Agent 运行时走公司内网 Anthropic-compatible 网关 `ANTHROPIC_BASE_URL=http://10.10.85.155:3000/api`，`OPUS_MODEL=claude-opus-4-8`
- 规则：**跟我对话用哪个模型，前端/agent 跑起来也尽量设成同一个 provider**。GPT-5 对话时用 `gpt5`，Opus 对话时用 `opus`；这样排查结果和开发口径更一致，也能在 Claude Code 限流时切到 GPT-5
- 网关 IP 已加入用户级 `NO_PROXY`（`10.10.85.155,localhost,127.0.0.1`）确保直连
- **pip 直连公网 PyPI，不需要代理**（连公司 wifi 即可上外网，实测 200/0.3s）。早期"pip 加 --proxy 127.0.0.1:7897"是旧/家里环境，公司电脑别用
- **HuggingFace 必须离线**：公司网络会重置 huggingface.co 连接（10054）。ingest.py / retrieve.py 顶部已 `os.environ.setdefault("HF_HUB_OFFLINE","1")` 走本地缓存
- **嵌入库锁 <5**：`sentence-transformers 4.1.0` / `transformers 4.57.6` / `huggingface_hub 0.36.2`。5.x 会把纯文本模型 paraphrase-multilingual-MiniLM-L12-v2 当多模态走 AutoProcessor 而崩溃，被环境升级到 5.x 时要重新降级
- **下载新 HF 模型走镜像**：`huggingface.co` 被重置（curl 000），但 `hf-mirror.com` 通（200）。下新模型（如 reranker）用 `HF_ENDPOINT=https://hf-mirror.com python -c "..."`，缓存后再回离线。已用此法下 `BAAI/bge-reranker-base`
- **算力：本机纯 CPU**（torch `+cpu`，无 GPU，12 核）。微调只能做 CPU 友好小任务（意图分类：冻结嵌入 + 小分类头）；查询重写 / LLM 微调需免费云 GPU（Colab/Kaggle/AutoDL）。详见 ROADMAP #8

### 家庭电脑（下班继续开发，只能连 DeepSeek）
- 家庭电脑复制 `env.home.example` 为 `.env`：`Copy-Item env.home.example .env`
- 网关 `10.10.85.155` 是公司内网，**家里访问不到** → 家里 `.env` 固定 `LLM_PROVIDER=deepseek`，只填 `DEEPSEEK_API_KEY`
- ✅ **provider 切换已做好**（src/llm.py）：公司 `.env` 用 `gpt5` 或 `opus`；家里 `.env` 用 `deepseek`。代码不用改
- 注意 `.env` 被 gitignore、不随仓库同步：家里 clone 后要照 `env.home.example` 新建自己的 `.env`
- 首次跑 ingest 若本地无嵌入模型缓存：临时 `set HF_HUB_OFFLINE=0` 让它下载一次（约 420MB），缓存后再恢复离线
- pip / 模型下载是否需要代理按家里实际网络决定

### 通用
- Python Scripts 路径已加入用户 PATH（setx 永久配置）
- 嵌入模型缓存在 `~/.cache/huggingface`，不入库；换机器首次需联网下载约 420MB
- 文档编码兼容：UTF-8 → GBK → UTF-8(errors=replace)，解决坏字节 0xAD
- 控制台中文乱码是 Windows GBK 显示问题，`$env:PYTHONUTF8=1` 可消除，不影响逻辑
