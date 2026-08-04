# Project Goals and Architecture

## Purpose

Department-level intelligent FAE technical support Agent (covering Nebullar SDK and department documents) — beyond document Q&A, like an experienced colleague: multi-round guided troubleshooting, hit historical cases, ask back when information is insufficient.

## Architecture Design

**Retrieval Layer (RAG)**
- ChromaDB vector + BM25 keyword + RRF recall
- BGE Cross-Encoder reranking (top20→top5)
- HyDE / Multi-Query query expansion

**Agent Orchestration (LangGraph)**
- StateGraph state machine: analyze → tools → generate → self-correction
- Node-level streaming output
- Dynamic routing + tool calling

**Memory Layer**
- Short-term: dialog context
- Long-term: case library cases.jsonl (semantic retrieval)

## Data Sources

- `DevDocForAIAgent_260507@latest/`: Company knowledge base (545 chunks)
- `data/error_codes.json`: Structured error code table
- `data/cases.jsonl`: FAE support cases (core differentiated asset)

## Workflow

```
User asks
  → analyze_query (intent analysis)
  → routing decision (need tools? lookup error? direct answer?)
  → tool execution (lookup_error / search_cases / search_docs)
  → generate (generate answer)
  → self-correction check
  → streaming return + source display
```

## Agents Rules

1. **Ask back first when information is insufficient**, don't guess
2. **Prioritize hitting historical cases**, cases are the most valuable experience
3. **Exact error code table lookup**, don't mix with vector retrieval
4. **Real-time node progress feedback**, let users know the processing stage
5. **Transparent sources**, explain references for each conclusion

## Tech Stack

| Purpose | Selection |
|---------|-----------|
| LLM | Kimi/GPT-5/DeepSeek |
| Retrieval | ChromaDB + BM25 + RRF + Cross-Encoder |
| Embedding | paraphrase-multilingual-MiniLM-L12-v2 |
| Orchestration | LangGraph StateGraph |
| Frontend | Streamlit / FastAPI+SSE |
| Language | Python 3.11 |

## Progress Milestones

- [x] RAG hybrid retrieval + Reranker
- [x] Case vectorized semantic retrieval
- [x] HyDE/Multi-Query query expansion
- [x] LangGraph dynamic routing + self-correction
- [x] FastAPI+SSE streaming backend
- [ ] MCP tooling
- [ ] Docker + LangSmith
- [ ] Persistent Memory
- [ ] Fine-tuning (starting with intent classification)
