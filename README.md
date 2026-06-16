# Nebullar AI Assistant

基于 RAG + Agent 的 智能技术支持助手——帮 FAE 从"翻文档"到"问 AI"。

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
│   ├── llm.py              # LLM 提供方抽象 GPT-5/Opus(公司)/DeepSeek(家里)
│   ├── memory.py           # FAE 历史案例检索第一版
│   ├── agent.py            # Agent 核心逻辑（查表+RAG+短期上下文+澄清反问）
│   └── app.py              # Streamlit 聊天前端第一版
└── chroma_db/              # 向量数据库（gitignore）
```

## 环境配置：公司电脑 / 家庭电脑（换电脑必看）

凭据放 `.env`（被 gitignore，**不随仓库同步**），所以每台电脑都用自己的 `.env`。
为了避免混乱，项目把配置拆成两个模板文件：

- 公司电脑：`env.company.example`
- 家庭电脑：`env.home.example`

### 公司电脑（GPT-5 / Opus 二选一）

公司电脑有两个可选 LLM provider：

- **用 Codex / GPT-5 对话开发时**：让项目里的 Agent 也调用 GPT-5。
- **用 Claude Code / Opus 对话开发时**：让项目里的 Agent 也调用 Opus，避免两个模型口径混用。

首次在公司电脑配置：

```powershell
Copy-Item env.company.example .env
```

然后编辑 `.env`：

- 用 Codex / GPT-5 开发：`LLM_PROVIDER=gpt5`
- 用 Claude Code / Opus 开发：`LLM_PROVIDER=opus`

公司电脑的两个网关路径不要混：

- GPT-5：`GPT5_BASE_URL=http://10.10.85.155:3000/openapi`
- Opus：`ANTHROPIC_BASE_URL=http://10.10.85.155:3000/api`

- pip / 模型下载**直连公网，不用代理**
- HuggingFace 走本地缓存（代码已强制 `HF_HUB_OFFLINE`，因公司网络会重置 huggingface.co）

### 🏠 家庭电脑（连不上网关，用 DeepSeek）—— 首次照这做

```powershell
# 1. 装依赖（嵌入库必须 <5，否则加载嵌入模型会崩）
pip install -r requirements.txt

# 2. 复制家庭电脑模板建自己的 .env
Copy-Item env.home.example .env

# 3. 编辑 .env，只填 DeepSeek：
#      DEEPSEEK_API_KEY=sk-你的key

# 4. 首次本地没有嵌入模型缓存 → 临时允许联网下载（约 420MB）
$env:HF_HUB_OFFLINE=0
python src/ingest.py        # 建向量库（chroma_db 不入库，换电脑必须本地重跑）

# 5. 验证整条链路（检索 → DeepSeek）
python src/agent.py
```
> 缓存好之后，下次跑不用再设 `HF_HUB_OFFLINE`（代码默认离线走缓存）。
> 中文乱码是 Windows 控制台显示问题，`$env:PYTHONUTF8=1` 可消除，不影响逻辑。

## 快速开始（环境已配好后）

```powershell
python src/ingest.py        # 文档向量化入库（首次约 420MB 嵌入模型）
python src/agent.py         # 一问一答验证
.\start_app.ps1             # 启动前端（保持 PowerShell 窗口打开）
```

## 技术栈

- **LLM**: GPT-5（公司可选）/ Claude Opus 4.8（公司内网网关）/ DeepSeek（家里）—— 靠 `.env` 的 `LLM_PROVIDER` 切换
- **检索**: ChromaDB（向量）+ rank_bm25（关键词）+ RRF 融合
- **嵌入模型**: paraphrase-multilingual-MiniLM-L12-v2（跨语言中英文，库锁 <5）
- **前端**: Streamlit

## 进度

- [x] ingest.py — 文档向量化入库（545 chunks）
- [x] retrieve.py — 混合检索层
- [x] llm.py — 三路 provider：公司 GPT-5(/openapi) / 公司 Opus(/api) / 家里 DeepSeek
- [x] agent.py — MVP 跑通：lookup_error 精确查表、RAG 问答、短期多轮上下文、信息不足先反问
- [x] app.py — Streamlit 聊天前端第一版，支持把历史消息传给 Agent
- [x] 环境模板 — `env.company.example` / `env.home.example` 分开，避免公司电脑和家庭电脑配置混乱
- [x] memory.py / search_cases 第一版 — 从 `data/cases.jsonl` 检索 FAE 历史案例并放入 Agent prompt
- [x] 结构化回答 / 来源展示第一版 — 前端展示 tools_used、错误码查表、历史案例、参考文档
- [x] 小型 eval 第一版 — 固定错误码、澄清反问、历史案例、结构化来源四类回归测试

## 当前效果

- 问 `刷卡返回 -70004 怎么排查？`：Agent 会先查 `data/error_codes.json`，识别 `-70004 = APDU Error`，再结合检索到的真实 SDK 文档生成排查建议。
- 问 `刷卡无反应怎么办` 这种信息不足的问题：Agent 不直接堆 API，会先反问卡类型、读卡方式、当前调用到的 API 等关键上下文。
- 问 `adb 查不到设备怎么办` 这类现场问题：Agent 会命中历史案例，优先提示检查开发者模式和 USB debugging。
- 前端回答下方可展开查看：命中的工具、错误码释义、历史案例和参考文档来源。
- 前端当前是会话内短期上下文，刷新或重启后不保存；长期记忆和案例沉淀放到后续 `memory.py`。

## 下一步

- 继续扩充 `data/cases.jsonl`，把常见现场排查沉淀成可检索案例。
- 继续增强 eval：加入真实检索链路、API 问答、资料不足等用例。
