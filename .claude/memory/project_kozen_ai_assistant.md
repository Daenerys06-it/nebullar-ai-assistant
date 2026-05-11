---
name: project_kozen_ai_assistant
description: KOZEN SDK AI assistant project — RAG + Agent for financial terminal support
type: project
originSessionId: 503bdc81-3792-4c10-af93-e03db3930c46
---
## KOZEN AI Assistant 项目

用户正在构建一个基于 RAG + Agent 的 KOZEN SDK 智能技术支持助手。

**Why**: 将 FAE 实习经历转化为 AI 工程实践的成果，用于 AI 方向求职。核心洞察：金融终端日志和错误码数据是 LLM 训练集中稀缺的数据类型，FAE 的客户案例积累是最有价值的知识资产。

**How to apply**:
- 项目当前在 D:\kozen-ai-assistant（已从桌面迁移），有完整 CLAUDE.md
- GitHub 仓库: https://github.com/Daenerys06-it/kozen-ai-assistant（Private）
- 用户在公司电脑（D:\kozen-ai-assistant）和家里电脑之间通过 GitHub 同步
- 记忆文件已随项目提交到 .claude/memory/，回家 clone 即可带记忆
- 开发策略：阶梯式（RAG → Agent），Vibe Coding + DeepSeek
- 当前状态：文档已处理完（PDF → Markdown 拆分 + 结构化错误码 JSON），核心代码（ingest/rag/agent/app.py）待开发
- 下一步：回家安装 Python，写 ingest.py（向量化入库）

## 三个月学习路线

**定位**: 不只想 vibe coding，也想懂原理和实操。

**核心理念**: 视频看 40% + 代码写 60%，交替进行。看 2-3 集视频 → 打开编辑器写代码 → 卡住了精准查那个概念 → 回来继续写。不要刷完全部视频再动手。

**项目直接涉及的 5 个核心概念**（只需要深入理解这些，不需要 NLP 全套基础）:
1. Embedding（文字→向量）
2. 向量相似度检索（问题→最相关文档片段）
3. LLM 推理（token、context window、system prompt）
4. RAG 数据流（检索→拼 prompt→生成→返回）
5. Agent 工具调用（LLM 决定调哪个函数、传什么参数）

**不需要学的内容**（跟项目无关）: RNN、LSTM、GRU、BERT 预训练、反向传播、梯度下降、CNN

**B站收藏夹使用策略**:
- AI Agent 智能体搭建教程 → 最优先看，3-5 集后立刻写代码
- 2 小时提示词工程 → 一个下午刷完
- LLM 大模型入门（52 集）→ 只看 LangChain/RAG/Agent 的特定几集
- NLP 零基础（尚硅谷 187 集）→ 只看 Transformer 章节，前面的跳过
- 李宏毅 ML 全集 → 保留作为理论词典，碰到不懂的概念精准查阅，不从头刷
- Java 项目/计算机网络/MIT 概率论 → 暂时不需要
- 非技术类视频（aespa/福原爱/石川佳纯/柯南/唐探等）→ 娱乐类，不在学习范围内

**Git 日常流程**:
```
git status          → 看看改了什么
git add -A          → 标记要保存的文件  
git commit -m "xxx" → 保存一个版本
git push            → 上传到 GitHub
```
