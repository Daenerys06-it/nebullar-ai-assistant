# Nebullar 升级路线 + 知识补给

> 目标：把项目从"能跑的 RAG Agent"升级到"生产级、技术点对标主流 LLM 工程岗"。
> 原则：**全部在现有项目上增量加，不推翻重来**；每个升级都顺带学会对应概念（边做边学）。

---

## 0. 先认清：你已经会的（别低估自己）

这些你**亲手写过、能讲清**，已经覆盖了不少核心点：

- ✅ Embedding 向量检索（ChromaDB，384 维）
- ✅ BM25 关键词检索
- ✅ RRF 融合排序
- ✅ 查询重写（query rewrite）
- ✅ LangGraph：State / Node / 条件边 / 自我纠错回路（环）/ 节点级流式
- ✅ 工具调用（错误码查表、案例检索）
- ✅ 多轮上下文、反问澄清、结构化返回
- ✅ provider 抽象 + fallback、回归测试

"懂得很少"是错觉——这领域名词密集，但你已经握住了 RAG + Agent 的主干。下面是把主干加粗、加宽。

---

## 1. 升级清单（按性价比排序）

| # | 升级 | 改哪里 | 学到的概念 | 难度 |
|---|---|---|---|---|
| 1 | **加 Reranker 精排** | retrieve.py（RRF 后再排一层） | Cross-Encoder 重排、召回 vs 精排 | ⭐ |
| 2 | **案例/记忆落库 + 向量化** | memory.py（jsonl → SQLite/pgvector + 向量检索） | 长期记忆、向量库 CRUD | ⭐⭐ |
| 3 | **HyDE / Multi-Query** | retrieve.py（检索前先扩写） | 查询扩展、假设文档 | ⭐⭐ |
| 4 | **FastAPI + SSE 后端** | 新增 api.py（Streamlit 仍留作演示） | 前后端分离、流式协议 | ⭐⭐ |
| 5 | **工具 MCP 化** | 新增 mcp_server.py（FastMCP 暴露 3 个工具） | MCP 协议、工具标准化 | ⭐⭐ |
| 6 | **Docker + LangSmith 追踪** | Dockerfile + 环境变量 | 容器化、可观测/链路追踪 | ⭐⭐ |
| 7 | **多智能体拆分** | agent.py（拆 Router + 子图/Subagent） | Supervisor/Handoff/子图 | ⭐⭐⭐ |
| 8 | ⭐**微调小实验** | 新目录 finetune/（LoRA 微调查询重写/意图分类） | SFT、LoRA/QLoRA、数据集构造、评测 | ⭐⭐⭐⭐ |

> 做完 1–3，RAG 质量就对标 CV 的"Advanced RAG"；做完 4–6，就有了"生产级"骨架；7–8 是进阶加分，尤其 8 是补"会训模型"这个唯一硬缺口。

---

## 2. 知识补给地图（每个一句话 + 是否已上手）

### A. RAG 进阶
- ✅ **Embedding**：把文字转成向量，语义近 = 距离近
- ✅ **BM25**：基于词频的关键词匹配
- ✅ **RRF**：把多路检索的排名融合
- ⬜ **Reranker（Cross-Encoder）**：把"问题+候选文档"一起送进模型打分，比向量精准；用于"召回一批 → 精排前几"
- ⬜ **HyDE**：先让 LLM "假设"一个答案文档，用它的向量去检索（比原始问题更贴）
- ⬜ **Multi-Query**：把一个问题改写成多个角度再分别检索，合并结果
- ⬜ **Chunking 策略**：按标题/语义切块，影响召回质量

### B. Agent / LangGraph 进阶
- ✅ **StateGraph / 条件边 / 环**：你已掌握
- ⬜ **ReAct**：Reason（想）→ Act（调工具）→ Observe（看结果）循环，Agent 的经典范式
- ⬜ **原生 Tool Calling**：让 LLM 自己输出"要调哪个工具+参数"，而非规则路由
- ⬜ **多智能体**：Supervisor/Router 分发、Subagent 子任务、Handoff 交接、Subgraph 子图
- ⬜ **Memory**：短期（对话窗口）vs 长期（落库可检索）；LangGraph 的 checkpointer 做持久化
- ⬜ **MCP**：Model Context Protocol，把工具/数据源标准化暴露给任意 LLM 客户端

### C. 工程化 / 部署
- ⬜ **FastAPI**：Python 主流后端框架，把 Agent 包成 HTTP 接口
- ⬜ **SSE 流式**：Server-Sent Events，服务器逐字推送（打字机效果的协议）
- ⬜ **向量库生产化**：Milvus / pgvector（vs 轻量 Chroma）
- ⬜ **PostgreSQL**：存对话、案例、长期记忆
- ⬜ **Docker**：容器化，一键部署
- ⬜ **可观测**：LangSmith（链路追踪）、Prometheus + Grafana（指标监控）

### D. 模型层（最硬，进阶）
- ⬜ **基础**：token、context window、temperature、prompt engineering
- ⬜ **SFT（监督微调）**：用"问题→标准答案"数据继续训练模型
- ⬜ **LoRA / QLoRA**：低成本微调（只训一小部分参数，单卡可跑）
- ⬜ **DPO**：用"好答案 vs 坏答案"偏好对让模型对齐
- ⬜ **vLLM**：高吞吐推理服务
- ⬜ **评测**：构造评测集 + 指标（命中率/正确率），量化效果

---

## 3. 建议节奏

1. **先 #1 Reranker**（最小投入、立竿见影），顺带学透"召回 vs 精排 + Cross-Encoder"
2. 再 **#2 记忆落库**，学"长期记忆 + 向量库 CRUD"
3. 然后 **#4 FastAPI+SSE**，补工程化短板
4. 中间穿插补 **B 区概念**（ReAct / Tool Calling / 多智能体）
5. 最后挑战 **#8 微调小实验**——这是和 CV 拉平的关键一招

> 学习方式沿用老规矩：**每个升级先讲概念 → 给骨架留空 → 你填核心 → 我补修**。一个升级 = 学一个知识点 + 落一段代码。
