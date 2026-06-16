# Claude Code 入口

本项目的 agent 统一上下文维护在 `AGENTS.md`。

Claude Code 打开项目后，请先阅读：

```text
AGENTS.md
```

## Claude Code 专属约定

- 用 Claude Code / Opus 对话开发时，项目里的 Agent 也尽量调用 Opus。
- 公司电脑 `.env` 设置：

```env
LLM_PROVIDER=opus
ANTHROPIC_BASE_URL=http://10.10.85.155:3000/api
OPUS_MODEL=claude-opus-4-8
```

- 不要把 `.env`、token、日志文件、`chroma_db/` 提交到 Git。
- 具体项目目标、架构、进度、公司/家庭电脑环境说明，都以 `AGENTS.md` 为准。
