# Claude Code 入口

本项目的 agent 统一上下文维护在 `AGENTS.md`。

Claude Code 打开项目后，请先阅读：

```text
AGENTS.md
ROADMAP.md   # 升级路线（对标主流 RAG/Agent 岗）+ 知识补给清单
PROJECT_INTRO.md #项目大观介绍
```

## Claude Code 专属约定

- 项目里的 Agent 调用 Kimi（公司内网 Anthropic-compatible 网关）。
- GPT-5 网关备用（当 Kimi 不可用时切换）。
- 公司电脑 `.env` 设置：

```env
# 主用 Kimi
LLM_PROVIDER=kimi
KIMI_BASE_URL=http://10.10.5.136:8080
KIMI_API_KEY=sk-...
KIMI_MODEL=kimi-k2.5

# 备用 GPT-5
GPT5_BASE_URL=http://10.10.85.155:3000/openapi
GPT5_AUTH_TOKEN=cr-...
GPT5_MODEL=gpt-5
```

- 不要把 `.env`、token、日志文件、`chroma_db/` 提交到 Git。
- 具体项目目标、架构、进度、公司/家庭电脑环境说明，都以 `AGENTS.md` 为准。
