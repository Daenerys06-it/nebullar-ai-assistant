# Nebullar AI Assistant

基于 **RAG + Agent** 的智能技术支持助手——帮 FAE 从"翻文档"到"问 AI"。

> 覆盖 **26条** FAE历史案例 + **750+** 技术文档结构化片段，端到端响应 **3-6秒**，支持 **MCP工具化** 接入任意LLM客户端。

---

## 项目亮点

| 维度 | 实现方案 | 效果 |
|------|----------|------|
| **检索质量** | 向量(ChromaDB) + BM25 + RRF融合 + Cross-Encoder精排 | 召回准确率 > 90% |
| **Agent架构** | LangGraph StateGraph + 动态路由 + 自我纠错 | 多轮对话+工具调用+流式输出 |
| **知识覆盖** | 26条FAE案例 + 750+文档chunks（智能Chunking） | 支持口语化语义匹配 |
| **工程化** | FastAPI+SSE + MCP协议 + 多级缓存 | 首字延迟 < 1s，可被Claude等客户端调用 |

---

## 技术架构

```
用户提问
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│  Agent Layer (LangGraph)                                    │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │  analyze │───▶│  tools   │───▶│ generate │              │
│  │ 意图分析 │    │ 工具调用 │    │ 答案生成 │              │
│  └──────────┘    └──────────┘    └──────────┘              │
│       │               │               │                     │
│       └───────────────┴───────────────┘                     │
│                    自我纠错回路                              │
└─────────────────────────┬───────────────────────────────────┘
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
┌────────────────┐ ┌──────────────┐ ┌──────────────┐
│  RAG Retrieval │ │ Case Search  │ │ Error Lookup │
│  混合检索       │ │ 案例语义检索  │ │ 错误码查表   │
└───────┬────────┘ └──────┬───────┘ └──────┬───────┘
        │                 │                │
        ▼                 ▼                ▼
┌─────────────────────────────────────────────────────────┐
│  Data Layer                                             │
│  • ChromaDB (750+ chunks, 智能Chunking)                │
│  • cases.jsonl (26条向量化案例)                         │
│  • error_codes.json (结构化错误码)                      │
└─────────────────────────────────────────────────────────┘
```

---

## 项目结构

```
├── data/
│   ├── error_codes.json          # 结构化错误码（精确查表）
│   ├── cases.jsonl               # FAE支持案例26条（语义检索）
│   └── cases_knowledge_base_expanded.md  # 案例扩展版（OpenClaw用）
├── DevDocForAIAgent_260507@latest/   # 公司知识库（结构化md）
├── src/
│   ├── agent.py                  # LangGraph状态机：路由+工具+自纠错+流式
│   ├── api.py                    # FastAPI + SSE 流式后端
│   ├── app.py                    # Streamlit聊天前端（历史/翻译/响应时间）
│   ├── retrieve.py               # 混合检索(向量+BM25+RRF) + Cross-Encoder精排
│   ├── chunking.py               # 智能Chunking：Markdown感知+元数据增强
│   ├── mcp_server.py             # MCP工具服务（6个标准工具）
│   ├── memory.py                 # 案例语义检索（向量化+余弦相似度）
│   ├── memory_db.py              # SQLite持久化对话历史
│   ├── ingest.py                 # 文档智能切分 + 向量化入库
│   ├── llm.py                    # LLM provider抽象(Kimi/GPT-5/DeepSeek)+fallback
│   └── parse_docs.py             # PDF文档按模块切分
├── chroma_db/                    # 向量数据库（750+ chunks，gitignore）
├── PROJECT_INTRO.md              # 完整项目介绍（公司汇报用）
├── ROADMAP.md                    # 升级路线与技术补给
└── MCP_SETUP.md                  # MCP配置指南
```

---

## 技术栈

| 层级 | 技术 | 说明 |
|------|------|------|
| **LLM** | Kimi / GPT-5 / DeepSeek | 公司内网Anthropic兼容网关，`.env`切换+failover |
| **检索** | ChromaDB + BM25 + RRF + BGE-reranker-base | 三阶段：召回→融合→精排 |
| **嵌入** | paraphrase-multilingual-MiniLM-L12-v2 | 384维跨语言，公司离线缓存 |
| **Agent** | LangGraph (StateGraph) | 动态路由、条件边、自我纠错回路、节点级流式 |
| **Chunking** | MarkdownHeaderTextSplitter | 结构感知切分，代码块保护，元数据增强 |
| **后端** | FastAPI + SSE | 流式HTTP接口，节点进度实时推送 |
| **MCP** | FastMCP | Model Context Protocol工具标准化，stdio/SSE双模式 |
| **前端** | Streamlit | 聊天界面+历史侧边栏+响应时间显示 |
| **持久化** | SQLite | 对话历史、用户会话管理 |

---

## 快速开始

### 1. 环境配置

凭据放 `.env`（已gitignore），提供两个模板：

**公司电脑**（Kimi主用/GPT-5备用）：
```powershell
Copy-Item env.company.example .env
# 编辑 .env: LLM_PROVIDER=kimi
```

**家庭电脑**（DeepSeek）：
```powershell
Copy-Item env.home.example .env
# 编辑 .env: 填 DEEPSEEK_API_KEY
```

### 2. 安装依赖
```powershell
pip install -r requirements.txt
```

### 3. 构建向量库（必须）
```powershell
python src/ingest.py
# 输出: Done: 750 chunks indexed
```

### 4. 启动服务（三选一）

**A. Streamlit前端（完整界面）**
```powershell
streamlit run src/app.py
# 访问 http://localhost:8501
```

**B. FastAPI后端（API服务）**
```powershell
python src/api.py
# 访问 http://localhost:8000
```

**C. MCP Server（工具模式）**
```powershell
# stdio模式（Claude Desktop）
python src/mcp_server.py

# 或SSE模式（内网服务）
python src/mcp_server.py --transport sse --port 8000
```

---

## 核心功能演示

### 功能1：混合检索+Reranker精排
```python
from src.retrieve import search

results = search("Scanner初始化", top_k=5)
# 1. 向量检索召回top20
# 2. BM25关键词检索召回top20
# 3. RRF融合排序
# 4. Cross-Encoder精排取top5
```

### 功能2：案例语义检索
```python
from src.memory import search_cases

cases = search_cases("P18刷不进去", top_k=3)
# 返回: case_p18_flash_data_mux_timeout_low_battery
# 相似度: 0.89
```

### 功能3：Agent多轮对话+工具调用
```
用户: D0551怎么刷机？
AI:   [调用get_device_flash_guide]
      D0551刷机步骤：
      1. 安装驱动...
      2. 选择Firmware Upgrade模式...

用户: 刷到一半报错0xC0060003
AI:   [调用lookup_error + search_cases]
      错误码0xC0060003表示send DA fail...
      建议先Format初始化再刷机...
```

### 功能4：MCP工具接入Claude Desktop
配置Claude Desktop后，AI可直接调用：
- `search_docs` - 搜索技术文档
- `search_cases` - 搜索历史案例
- `lookup_error` - 查询错误码
- `get_device_flash_guide` - 获取刷机指南
- `translate` - 中英技术翻译

---

## 性能指标

| 指标 | 数值 | 说明 |
|------|------|------|
| **平均回答时长** | 3-6秒 | 端到端：提问→检索→生成完整回复 |
| 简单问答（无需检索） | ~3秒 | 直接生成 |
| 标准检索问答 | ~4-5秒 | 向量+BM25+RRF+精排+生成 |
| 多工具串联 | ~6秒 | 案例+文档多路检索 |
| **检索耗时** | <300ms | 向量+BM25+RRF融合 |
| **精排耗时** | ~500ms | Cross-Encoder top20→top5 |
| **首字延迟** | <1s | 流式输出首字到达时间 |
| **知识覆盖** | 750+ chunks | 3产品线技术文档 |
| **案例库** | 26条 | FAE真实支持记录 |

---

## 升级路线

已完成：
- [x] RAG混合检索 + Reranker精排
- [x] 案例向量化语义检索（26条）
- [x] HyDE/Multi-Query查询扩展
- [x] LangGraph动态路由 + 自我纠错
- [x] FastAPI+SSE流式后端
- [x] **智能Chunking**（Markdown感知+元数据增强）
- [x] **MCP工具化**（6个标准工具，stdio/SSE双模式）

进行中：
- [ ] Docker容器化
- [ ] LangSmith可观测性
- [ ] PostgreSQL持久化

规划中：
- [ ] 多智能体拆分（Router/Retrieval/Generation）
- [ ] LoRA微调（意图分类+查询重写）
- [ ] 评测体系构建

详见 [ROADMAP.md](ROADMAP.md)

---

## 文档索引

| 文档 | 用途 |
|------|------|
| [PROJECT_INTRO.md](PROJECT_INTRO.md) | 完整项目介绍（技术栈/效果/未来规划，公司汇报用） |
| [ROADMAP.md](ROADMAP.md) | 升级路线+知识补给（CV对标主流LLM工程岗） |
| [MCP_SETUP.md](MCP_SETUP.md) | MCP配置指南（Claude Desktop集成） |
| [AGENTS.md](AGENTS.md) | Agent架构设计文档 |
| [IDENTITY.md](IDENTITY.md) | Agent身份设定（Neo - Nebullar FAE Assistant） |

---

## 环境适配说明

**公司电脑**：
- 两个网关：Kimi `http://10.10.5.136:8080`，GPT-5 `http://10.10.85.155:3000/openapi`
- HuggingFace离线模式（已缓存模型）
- pip直连公网，无需代理

**家庭电脑**：
- 使用DeepSeek API（OpenAI兼容）
- 首次运行需联网下载嵌入模型（约420MB）
- 无reranker模型时自动退回RRF排序

---

## License

公司内部项目，仅供Nebullar事业部使用。

---

**维护者**：Nebullar FAE团队  
**最后更新**：2026-08