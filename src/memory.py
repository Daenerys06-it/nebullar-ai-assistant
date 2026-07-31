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


# ---------- 模型预加载机制 ----------
_model_preloaded = False
_embedder_instance = None
_case_vectors_cache = None


def preload_models():
    """预加载所有模型到内存，避免首次查询时加载耗时。

    应在应用启动时调用一次（如 app.py 初始化时）。
    """
    global _model_preloaded, _embedder_instance, _case_vectors_cache

    if _model_preloaded:
        return

    print("[Preload] 开始预加载模型...")

    # 1. 预加载嵌入模型
    print("[Preload] 加载嵌入模型 (paraphrase-multilingual-MiniLM-L12-v2)...")
    from sentence_transformers import SentenceTransformer
    _embedder_instance = SentenceTransformer(EMBED_MODEL)

    # 2. 预计算案例向量
    print("[Preload] 预计算案例向量...")
    cases = load_cases()
    if cases:
        texts = [_case_text(c) for c in cases]
        _case_vectors_cache = _embedder_instance.encode(texts, normalize_embeddings=True)

    _model_preloaded = True
    print(f"[Preload] 完成！已加载 {len(cases)} 个案例向量")


def get_embedder():
    """获取嵌入模型（优先返回预加载的实例）"""
    global _embedder_instance
    if _embedder_instance is not None:
        return _embedder_instance

    #  fallback：如果没有预加载，懒加载
    from sentence_transformers import SentenceTransformer
    _embedder_instance = SentenceTransformer(EMBED_MODEL)
    return _embedder_instance


def clear_search_cache():
    """清除案例检索缓存（案例更新后调用）"""
    global _case_vectors_cache
    _case_vectors_cache = None
    # 同时清除 lru_cache
    load_cases.cache_clear()
    _case_vectors.cache_clear() if hasattr(_case_vectors, 'cache_clear') else None
    print("[Cache] 案例检索缓存已清除")


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
            #strip() 去掉首尾空白字符（包括换行符），空行直接跳过
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
MIN_SIM = 0.15  # 相似度阈值：降低以召回更多案例


def _case_vectors():
    """获取案例向量（支持预加载）"""
    global _case_vectors_cache

    cases = load_cases()

    # 如果已经预加载了向量，直接返回
    if _case_vectors_cache is not None:
        return cases, _case_vectors_cache

    # 否则实时计算
    if not cases:
        return [], None

    texts = [_case_text(c) for c in cases]
    vecs = get_embedder().encode(texts, normalize_embeddings=True)
    return cases, vecs


# ---------- 查询扩展：边缘问题也能召回相关案例 ----------
# 同义词映射：用户可能用的不同说法
QUERY_EXPANSION_MAP = {
    # 刷机相关
    "flashtool": ["flash_tool", "刷机工具", "V5刷机", "固件升级"],
    "flash_tool": ["flashtool", "刷机工具", "SP Flash Tool", "固件升级"],
    "刷机": ["flash", "固件升级", "firmware", "刷写", "烧录"],
    "怎么刷机": ["刷机步骤", "flash_tool怎么用", "固件升级方法"],
    # 写号相关
    "写号": ["写SN", "写序列号", "Barcode", "IMEI Writer", "写key"],
    "IMEI": ["写号", "SN", "序列号", "Barcode"],
    # 设备型号别名
    "D0551": ["D5", "D系列"],
    "D0552": ["D5", "D系列", "双屏"],
    "P18": ["P系列"],
    # 其他
    "Download": ["下载", "刷机", "点Download没反应"],
    "meta mode": ["写号", "刷机模式", "meta"],
}


def expand_query(query: str) -> list[str]:
    """扩展查询词，提高召回率。

    示例:
        "flashtool怎么用" -> ["flashtool怎么用", "flash_tool怎么用", "刷机工具怎么用"]
    """
    expansions = [query]  # 保留原查询
    query_lower = query.lower()

    # 查找同义词并扩展
    for keyword, synonyms in QUERY_EXPANSION_MAP.items():
        if keyword.lower() in query_lower:
            # 为每个同义词生成新查询
            for syn in synonyms:
                new_query = query_lower.replace(keyword.lower(), syn.lower())
                if new_query not in expansions:
                    expansions.append(new_query)

    return expansions[:5]  # 最多5个查询


def search_cases(query: str, top_k: int = 5, min_sim: float = 0.15) -> list[dict]:
    """【扩展检索】使用查询扩展召回更多相关案例。

    1. 扩展查询词（flashtool -> flash_tool/刷机工具）
    2. 多个查询分别检索
    3. 合并结果，按相似度排序
    4. 返回 top_k 个最相关的
    """
    cases, vecs = _case_vectors()
    if not cases:
        return []

    # 扩展查询
    queries = expand_query(query)
    all_results = []  # (case, similarity) 元组列表
    seen_ids = set()

    for q in queries:
        qv = get_embedder().encode([q], normalize_embeddings=True)[0]
        sims = vecs @ qv

        # 取前10个候选，过滤低相似度的
        order = sims.argsort()[::-1][:10]
        for i in order:
            if sims[i] >= min_sim:
                case = cases[i]
                case_id = case.get("id")
                if case_id not in seen_ids:
                    seen_ids.add(case_id)
                    all_results.append((case, float(sims[i])))

    # 按相似度排序，取 top_k
    all_results.sort(key=lambda x: x[1], reverse=True)
    return [case for case, sim in all_results[:top_k]]


def build_cases_context(cases: list[dict]) -> str:
    """Render matched cases into prompt context."""
    if not cases:
        return ""

    parts = ["【历史支持案例（来自 FAE cases.jsonl，可作为排查经验参考）】"]
    for i, case in enumerate(cases, 1):
        tags = ", ".join(case.get("tags", []))
        solution = case.get("solution", "")

        # 检测是否包含详细步骤
        step_keywords = ["1.", "2.", "3.", "步骤", "①", "②", "点击", "选择", "打开"]
        has_steps = any(kw in solution for kw in step_keywords)
        step_marker = " [含详细操作步骤]" if has_steps else ""

        parts.append(
            f"[案例{i}]{step_marker} {case.get('module', 'unknown')}\n"
            f"现象: {case.get('symptom', '')}\n"
            f"原因: {case.get('root_cause', '')}\n"
            f"处理: {solution}\n"
            f"标签: {tags}\n"
        )

    return "\n".join(parts) + "\n"
