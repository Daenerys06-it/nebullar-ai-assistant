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
- 项目当前在 D:\kozen-ai-assistant，有完整 CLAUDE.md
- GitHub 仓库: https://github.com/Daenerys06-it/kozen-ai-assistant（Private）
- 用户在公司电脑（D:\kozen-ai-assistant）和家里电脑之间通过 GitHub 同步
- 记忆文件已随项目提交到 .claude/memory/，回家 clone 即可带记忆
- 开发策略：阶梯式（RAG → Agent），Vibe Coding + DeepSeek
- 当前状态：parse_docs.py 和 ingest.py 已完成，rag.py / agent.py / app.py 待开发

## 2026-05-12 进展

- Python 3.11.9 已通过 winget + curl 安装到公司电脑
- 7 个核心依赖 + 90+ 传递依赖全部安装成功
- ingest.py 已完成：使用 RecursiveCharacterTextSplitter (chunk_size=800, overlap=80) + paraphrase-multilingual-MiniLM-L12-v2 跨语言嵌入模型 + ChromaDB
- cases.jsonl 格式完善：增加 product 字段（financial_sdk / terminal_manager_sdk）
- 用户确认：两份 SDK 文档对应公司 K 产品（Financial SDK，管收银）和 D 产品（Terminal Manager SDK，管设备），均为 Android POS 终端
- ingest.py 待首次运行（需下载约 420MB 嵌入模型）

## 三个月学习路线

**定位**: 不只想 vibe coding，也想懂原理和实操。

**核心理念**: 视频看 40% + 代码写 60%，交替进行。

**项目直接涉及的 5 个核心概念**（只需要深入理解这些）:
1. Embedding（文字→向量）
2. 向量相似度检索（问题→最相关文档片段）
3. LLM 推理（token、context window、system prompt）
4. RAG 数据流（检索→拼 prompt→生成→返回）
5. Agent 工具调用（LLM 决定调哪个函数、传什么参数）

**不需要学的内容**: RNN、LSTM、GRU、BERT 预训练、反向传播、梯度下降、CNN

**Git 日常流程**:
```
git status          → 看看改了什么
git add -A          → 标记要保存的文件  
git commit -m "xxx" → 保存一个版本
git push            → 上传到 GitHub
```
