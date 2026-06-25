"""Long-term support cases.

案例记忆层：
- cases.jsonl 保存 FAE 支持案例（手动沉淀）
- search_cases(query) 用嵌入向量做语义检索，命中最相关的案例放进 Agent prompt

#2：从关键词匹配升级成向量语义检索（和文档 RAG 同一套路）。
"""

from __future__ import annotations

import json
import os
from functools import lru_cache

# 强制 HuggingFace 离线（同 ingest/retrieve）：嵌入模型已本地缓存，公司网会重置 huggingface.co
os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")


_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASES_PATH = os.path.join(_BASE, "data", "cases.jsonl")


CASE_FIELDS = [
    "symptom",
    "root_cause",
    "solution",
    "module",
    "product",
    "tags",
]


@lru_cache(maxsize=1)
def load_cases() -> list[dict]:
    """Load cases from data/cases.jsonl.

    每行一个 JSON。空行跳过；坏行直接跳过，避免一个手写案例破坏整个 Agent。
    """
    if not os.path.exists(CASES_PATH):
        return []

    cases = []
    with open(CASES_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                case = json.loads(line)
            except json.JSONDecodeError:
                continue

            if case.get("symptom") or case.get("solution"):
                cases.append(case)

    return cases


def _case_text(case: dict) -> str:
    """把一条案例的关键字段拼成一段文本，用来编码成向量。"""
    parts = []
    for field in CASE_FIELDS:
        value = case.get(field, "")
        if isinstance(value, list):
            parts.extend(str(item) for item in value)
        else:
            parts.append(str(value))
    return " ".join(parts).lower()


# ---------- 案例向量化检索（#2：关键词 → 语义）----------
# 和文档 RAG 同理：每条案例编码成向量，问题也编码成向量，算余弦相似度找最像的。
# 复用文档用的同一个嵌入模型，不另外下载。
EMBED_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"
MIN_SIM = 0.3  # 相似度阈值：低于它视为不相关，不塞进 prompt（避免硬凑案例）

_EMBEDDER = None


def _get_embedder():
    """懒加载嵌入模型（和 ingest 用的同一个，已本地缓存）。"""
    global _EMBEDDER
    if _EMBEDDER is None:
        from sentence_transformers import SentenceTransformer

        _EMBEDDER = SentenceTransformer(EMBED_MODEL)
    return _EMBEDDER


# @是注释器  lru_cache = 记住函数的返回结果(缓存)。同样的调用第二次直接返回上次的结果,不再执行函数体。
# lru_cache=@Cacheable
# 第 1 次调用:真的跑一遍,把 N 条案例编码成向量(慢,几秒),结果存进缓存
# 之后每次调用:直接返回缓存的向量,不再重新编码
@lru_cache(maxsize=1)
def _case_vectors():
    """把所有案例编码成归一化向量并缓存（案例不变只算一次）。

    返回 (cases, vecs)：cases=案例列表；vecs shape=(N, 384) 归一化矩阵。
    归一化后，余弦相似度 = 向量点积（算起来简单）。
    """
    cases = load_cases()
    if not cases:
        return [], None
    texts = [_case_text(c) for c in cases]
    vecs = _get_embedder().encode(texts, normalize_embeddings=True)
    return cases, vecs


def search_cases(query: str, top_k: int = 3) -> list[dict]:
    """【★你来填★】语义检索：把 query 编码成向量，找最相似的 top_k 条案例。

    脚手架已给你：
        cases, vecs = _case_vectors()   # vecs:(N,384) 归一化矩阵，cases:案例列表
        vecs : (N, 384)   ← N 条案例，每条一个 384 维向量（一行一条）
        qv   : (384,)     ← query 的 384 维向量,归一化向量。

    要做的 4 步：
        ① 算相似度：sims =
             # 矩阵(N,384) × 向量(384,) → (N,)，每条案例一个余弦分（归一化后点积=余弦）
        ② 排下标：order = sims.argsort()[::-1][:top_k]
             # argsort 给升序下标 → [::-1] 反成降序 → 取前 top_k
        ③ 过滤+取案例：遍历 order 里的 i，只有 sims[i] >= MIN_SIM 才把 cases[i] 收进结果
        ④ 返回结果列表
    """
    cases, vecs = _case_vectors()
    if not cases:                 # 空案例：必须在用 vecs 之前挡，否则 None @ qv 会崩
        return []
    qv = _get_embedder().encode([query], normalize_embeddings=True)[0]
    # @ 是矩阵乘法：vecs(N,384) × qv(384,) → sims(N,)，每条案例一个余弦分
    sims = vecs @ qv
    order = sims.argsort()[::-1][:top_k]
    result = []
    for i in order:
        if sims[i] >= MIN_SIM:    # 低于阈值的视为不相关，丢掉
            result.append(cases[i])
    return result


def build_cases_context(cases: list[dict]) -> str:
    """Render matched cases into prompt context."""
    if not cases:
        return ""

    parts = ["【历史支持案例（来自 FAE cases.jsonl，可作为排查经验参考）】"]
    for i, case in enumerate(cases, 1):
        tags = ", ".join(case.get("tags", []))
        parts.append(
            f"[案例{i}] {case.get('module', 'unknown')}\n"
            f"现象: {case.get('symptom', '')}\n"
            f"原因: {case.get('root_cause', '')}\n"
            f"处理: {case.get('solution', '')}\n"
            f"标签: {tags}\n"
        )

    return "\n".join(parts) + "\n"
