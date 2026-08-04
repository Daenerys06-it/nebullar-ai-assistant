# Tools and API Usage

## LLM Provider Abstraction

Unified access to multiple backends through `llm.py`, with fallback support:

| Provider | Environment | Usage |
|----------|-------------|-------|
| Kimi | Company intranet | Primary, `kimi-k2.5` |
| GPT-5 | Company intranet | Backup |
| DeepSeek | Home/Public network | Home only |

Switch method: Set `LLM_PROVIDER=kimi/gpt5/deepseek` in `.env`

## Retrieval Tools

**Hybrid Retrieval (retrieve.py)**
- ChromaDB vector retrieval + BM25 keyword + RRF fusion
- Cross-Encoder (BGE-reranker-base) reranking
- Embedding model: `paraphrase-multilingual-MiniLM-L12-v2`

**Case Retrieval (memory.py)**
- Semantic retrieval of FAE historical cases
- Threshold MIN_SIM=0.15, supports query expansion

## Agent Tools

LangGraph StateGraph orchestration:

| Tool | Function |
|------|----------|
| `lookup_error` | Exact error code table lookup |
| `search_cases` | Retrieve historical FAE cases |
| `search_docs` | Retrieve SDK documentation |

## External Interfaces

**FastAPI + SSE** (`api.py`)
- Streaming output backend
- `/chat` endpoint supports Server-Sent Events

**Streamlit Frontend** (`app.py`)
- Chat interface
- Node-level progress display
- Historical session management

## Environment Constraints

- Company network: HF_HUB_OFFLINE=1 (must be offline)
- Download new models via `hf-mirror.com`
- pip direct connection to PyPI, no proxy needed
