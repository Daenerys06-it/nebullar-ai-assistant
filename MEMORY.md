# Long-term Memory

## User Collaboration Pattern

**Rhythm**: Explain concept first → Provide skeleton with blanks → User fills core → I review and fix

**Key Validation**: On 2026-06-11 teaching `lookup_error`, the blocker wasn't logic but not seeing the data structure. Changed to "draw structure → leave skeleton → user fills" and they independently wrote nodes and routing.

**Application Method**:
- Before writing data processing: give structure diagram + retrieval examples + self-check command
- Leave `____` or `raise NotImplementedError` in skeleton
- Java analogies are effective (`.items()` ≈ `entrySet()`)

## Project Direction

**Stage**: Upgrading to align with mainstream LLM engineering positions (referencing CAS master's CV: vulnerability analysis, AIOps projects)

**Currently Working On**: Reranker (BGE Cross-Encoder reranking)

**Key Constraint**: Pure CPU no GPU, fine-tuning starts with intent classification (frozen embedding + small classification head)

**Advancement Method**: One upgrade at a time = learn one knowledge point + implement one code segment

## Environment Essentials

- Company machines use intranet gateway to call Kimi/GPT-5
- HuggingFace must be offline (company network resets huggingface.co)
- Download new models via hf-mirror.com
- pip direct connection to public network, no proxy needed
