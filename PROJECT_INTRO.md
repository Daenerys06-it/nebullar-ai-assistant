# Nebullar AI Assistant - 智能FAE技术支持系统

## 一、项目概述

Nebullar AI Assistant 是面向FAE（现场应用工程师）技术支持的智能问答系统，基于RAG+Agent架构，覆盖Nebullar SDK技术文档和部门历史案例库。系统支持多轮对话、语义检索、工具调用，旨在将一线技术支持经验沉淀为可复用的智能助手。

---

## 二、核心功能

### 2.1 混合检索引擎（RAG）
- **向量检索**：基于ChromaDB的语义检索，支持中文提问匹配英文文档
- **关键词检索**：BM25算法处理精确术语匹配
- **RRF融合排序**：多路检索结果融合，平衡语义相关性和关键词匹配
- **Cross-Encoder精排**：BGE重排模型对召回结果二次精排，提升准确性

### 2.2 案例语义检索
- 26条真实FAE支持案例向量化入库
- 支持口语化描述匹配（如"P18刷不进去"匹配到"data_mux超时"案例）
- 余弦相似度阈值过滤，确保召回质量

### 2.3 智能Agent编排（LangGraph）
- **StateGraph状态机**：analyze → tools → generate → self-correction 工作流
- **动态路由**：根据问题类型自动选择工具（文档检索/错误码查表/案例匹配）
- **自我纠错**：生成结果自检，必要时重新检索或反问澄清
- **节点级流式**：实时显示处理进度（分析中→检索中→生成中）

### 2.4 工具生态
| 工具 | 功能描述 |
|------|----------|
| `search_docs` | SDK技术文档检索 |
| `search_cases` | 历史案例语义检索 |
| `lookup_error` | 错误码精确查表 |
| `get_device_flash_guide` | D5/P18/K1刷机指南 |
| `translate` | 中英技术文档互译 |

### 2.5 MCP工具化
- 基于Model Context Protocol标准，将工具暴露给任意LLM客户端
- 支持stdio模式（本地Claude Desktop）和SSE模式（内网服务）
- 工具即插即用，生态兼容

### 2.6 智能Chunking策略
- Markdown结构感知切分（按标题层级）
- 代码块/表格完整性保护
- 元数据增强（header_path、chunk_type、行号）
- 750+结构化chunks入库（较原有545条提升37%）

---

## 三、技术栈

| 层级 | 技术选型 | 说明 |
|------|----------|------|
| **LLM** | Kimi/GPT-5/DeepSeek | 公司内网Anthropic兼容网关 |
| **向量库** | ChromaDB | 轻量级本地向量存储 |
| **检索** | BM25 + RRF + Cross-Encoder | 召回→精排两阶段架构 |
| **嵌入** | paraphrase-multilingual-MiniLM-L12-v2 | 384维跨语言嵌入 |
| **Agent** | LangGraph (StateGraph) | 状态机编排+条件路由 |
| **后端** | FastAPI + SSE | HTTP流式接口 |
| **前端** | Streamlit | 快速原型界面 |
| **协议** | MCP (Model Context Protocol) | 工具标准化暴露 |
| **语言** | Python 3.11 | 类型注解+异步支持 |

---

## 四、当前效果

### 4.1 已验证场景
- ✅ SDK API使用问答（Scanner/EMV/CardReader模块）
- ✅ 26条FAE案例语义检索（刷机/写号/adb/OTA等）
- ✅ 错误码查表（结构化工单号映射）
- ✅ 多轮对话与反问澄清（信息不足时主动追问）
- ✅ 中英技术翻译（SDK术语保留）
- ✅ 流式输出+节点进度显示（提升等待体验）

### 4.2 数据规模
- 技术文档：3个产品线，750+结构化chunks
- 历史案例：26条FAE支持记录（含解决方案、耗时、标签）
- 错误码表：结构化错误码定义

### 4.3 性能指标
- **平均回答时长**：3-6秒（端到端：提问→检索→生成完整回复）
  - 简单问答（无需检索）：~3秒
  - 标准检索问答：~4-5秒
  - 多工具串联（案例+文档）：~6秒
- 平均检索耗时：< 300ms（向量+BM25+RRF）
- 精排耗时：~500ms（Cross-Encoder top20→top5）
- 流式首字延迟：< 1s（用户感知到第一个字出现）

---

## 五、未来优化方向

### 5.1 工程化（近期）
- **Docker容器化**：标准化部署，脱离源码依赖
- **LangSmith可观测性**：链路追踪、性能监控、调试分析
- **PostgreSQL持久化**：对话历史、用户反馈、长期记忆落库
- **生产级向量库**：Milvus/pgvector替换ChromaDB，支持高并发

### 5.2 架构升级（中期）
- **多智能体拆分**：
  - Router Agent：意图识别+任务分发
  - Retrieval Agent：专注检索策略优化
  - Generation Agent：答案生成与格式化
- **ReAct范式**：Reason→Act→Observe循环，支持更复杂工具链
- **Subgraph子图**：模块化Agent组件，支持热插拔

### 5.3 模型层（远期）
- **LoRA微调**：
  - 意图分类器（冻结Embedding+小分类头）
  - 查询重写模型（领域特定同义词学习）
- **DPO对齐**：基于FAE专家反馈的偏好对齐
- **评测体系**：构造评测集+命中率/正确率量化指标

### 5.4 功能扩展
- **多模态支持**：截图诊断（设备屏幕报错图→文字识别→案例匹配）
- **知识库运营**：案例入库UI、标签管理、相似案例去重
- **A/B测试**：检索策略对比、Prompt版本管理

---

## 六、项目资产

| 文件 | 说明 |
|------|------|
| `src/agent.py` | LangGraph状态机定义 |
| `src/retrieve.py` | 混合检索+RRF+Reranker |
| `src/memory.py` | 案例语义检索 |
| `src/mcp_server.py` | MCP工具服务 |
| `src/chunking.py` | 智能文档切分 |
| `data/cases.jsonl` | 26条FAE案例库 |
| `chroma_db/` | 向量索引（750 chunks） |

---

## 七、快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 启动MCP Server（stdio模式）
python src/mcp_server.py

# 或启动FastAPI服务
python src/api.py

# 或启动Streamlit界面
streamlit run src/app.py
```

---

**项目状态**：核心功能已完成，进入工程化优化阶段  
**维护者**：FAE部门  
**最后更新**：2026-08
