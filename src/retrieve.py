"""混合检索层：向量检索 + 关键词检索 + RRF 融合排序"""

# 向量检索：chromaDB
# 关键词检索：BM25算法（best matching25)
# RRF融合排序：将向量检索和关键词检索的结果进行融合排序，综合两者的优势，提高检索效果。
import os
from functools import lru_cache

# 强制 HuggingFace 离线：嵌入模型已本地缓存，公司网络会重置 huggingface.co 连接（10054）
os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")

import re
import chromadb
from rank_bm25 import BM25Okapi  # BM25 关键词检索算法

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE, "chroma_db")


# ---------- 模型预加载 ----------
_models_preloaded = False
_reranker_instance = None

def preload_all_models():
    """预加载所有检索模型（在应用启动时调用）"""
    global _models_preloaded, _reranker_instance

    if _models_preloaded:
        return

    print("[Preload] 预加载检索模型...")

    # 1. 预加载 ChromaDB 集合（避免首次连接耗时）
    print("[Preload] 连接 ChromaDB...")
    client = chromadb.PersistentClient(path=DB_DIR)
    try:
        collection = client.get_collection("nebullar_docs")
        # 预热查询
        collection.query(query_texts=["test"], n_results=1)
        print(f"[Preload] ChromaDB 已连接，文档数: {collection.count()}")
    except Exception as e:
        print(f"[Preload] ChromaDB 连接失败: {e}")

    # 2. 预加载 Cross-Encoder 精排模型
    print("[Preload] 加载 Cross-Encoder (bge-reranker-base)...")
    from sentence_transformers import CrossEncoder
    _reranker_instance = CrossEncoder(RERANKER_MODEL)
    print("[Preload] Cross-Encoder 已加载")

    _models_preloaded = True
    print("[Preload] 检索模型预加载完成！")


def _get_reranker():
    """获取 Cross-Encoder（优先返回预加载实例）"""
    global _reranker_instance
    if _reranker_instance is not None:
        return _reranker_instance

    # fallback
    from sentence_transformers import CrossEncoder
    _reranker_instance = CrossEncoder(RERANKER_MODEL)
    return _reranker_instance
# 同义词映射：覆盖所有案例场景
QUERY_EXPANSION_RULES = {
    # ========== 刷机/固件相关 (7个案例) ==========
    "flashtool": ["flash_tool", "SP Flash Tool", "刷机工具", "V5刷机", "固件升级"],
    "flash_tool": ["flashtool", "刷机工具", "固件升级", "firmware", "SP Flash Tool"],
    "刷机": ["flash", "固件升级", "firmware", "刷写", "烧录", "下载固件"],
    "怎么刷机": ["刷机步骤", "flash_tool怎么用", "固件升级方法", "怎么烧录"],
    "firmware": ["固件", "刷机", "flash", "升级", "软件版本"],
    "upgrade": ["升级", "刷机", "固件", "更新版本"],
    "固件升级": ["刷机", "firmware upgrade", "软件升级"],
    "刷不进去": ["刷机失败", "无法刷机", "刷不了", "下载失败", "Download失败"],
    "刷一半": ["刷机中断", "刷机断开", "断电", "USB断开"],
    "Download": ["下载", "刷机", "点Download没反应", "下载按钮"],
    "格式化": ["Format", "自动刷新", "整机刷新", "擦除数据", "清除数据"],
    "scatter": ["配置文件", "scatter file", "txt文件"],
    "ota": ["OTA", "版本包", "升级包", "固件包"],
    "bin": ["bin文件", "固件文件", "镜像文件"],
    "command line": ["命令行", "cli", "console", "批处理"],
    "auto format": ["自动刷新", "自动格式化", "auto refresh"],

    # ========== 写号/设备配置相关 (2个案例) ==========
    "写号": ["写SN", "写序列号", "Barcode", "IMEI Writer", "写key", "刷key"],
    "SN": ["序列号", "Barcode", "写号", "IMEI", "设备号"],
    "IMEI": ["写号", "SN", "序列号", "Barcode", "设备标识"],
    "序列号": ["SN", "Barcode", "写号", "IMEI"],
    "barcode": ["SN", "序列号", "写号"],
    "Google Key": ["Attestation Key", "写key", "key文件", "attestation"],
    "key": ["Google Key", "Attestation Key", "写号", "密钥"],
    "meta mode": ["写号", "刷机模式", "meta", "META模式"],
    "AP_DB": ["数据库", "DB文件"],

    # ========== 设备型号相关 ==========
    "D0551": ["D5", "D系列", "D0551设备"],
    "D0552": ["D5", "D系列", "双屏", "双屏机", "D0552设备"],
    "P18": ["P系列", "P18设备"],
    "D5": ["D0551", "D0552", "D系列"],
    "双屏": ["D0552", "双屏机", "dual screen"],

    # ========== USB/连接相关 (2个案例) ==========
    "USB": ["usb", "数据线", "连接线"],
    "adb": ["ADB", "adb devices", "调试"],
    "连不上": ["连接失败", "无法连接", "没反应", "识别不到"],
    "没反应": ["无响应", "失败", "timeout", "连不上"],
    "充电模式": ["充电", "power conflict", "电源冲突"],
    "debugging": ["调试", "debug", "开发者模式"],

    # ========== 错误/故障相关 ==========
    "报错": ["错误", "error", "失败", "exception", "提示错误"],
    "失败": ["报错", "错误", "失败", "error"],
    "错误码": ["error code", "status", "错误代码"],
    "timeout": ["超时", "没反应", "无响应"],
    "canceled": ["取消", "中断", "断开"],
    "无法识别": ["识别不到", "不认", "unknown device"],

    # ========== 日志相关 (1个案例) ==========
    "日志": ["log", "抓日志", "导出日志", "记录"],
    "抓日志": ["日志", "log", "debug log"],
    "*#98#": ["98", "日志暗码", "开日志"],

    # ========== 工程模式/测试相关 (1个案例) ==========
    "工程模式": ["工模", "测试模式", "*#87#", "硬件测试"],
    "*#87#": ["87", "工程模式", "MM1测试"],
    "测试": ["检测", "诊断", "test", "check"],
    "WiFi": ["wifi", "无线", "wlan", "网络"],
    "NFC": ["nfc", "近场通信", "非接"],

    # ========== 版本/信息查询 (1个案例) ==========
    "版本号": ["版本", "固件版本", "软件版本", "system version"],
    "查版本": ["版本号", "查看版本", "系统版本"],

    # ========== 恢复出厂/重置 (1个案例) ==========
    "恢复出厂": ["factory reset", "重置", "恢复设置", "*#422754#"],
    "*#422754#": ["422754", "恢复出厂", "清除标志位"],

    # ========== Play Integrity (1个案例) ==========
    "Play Integrity": ["integrity", "API check", "strong integrity", "Google Play"],
    "integrity": ["Play Integrity", "API检查", "Google认证"],

    # ========== MDM/资源管理 (1个案例) ==========
    "MDM": ["mdm", "资源包", "推送", "设备管理"],
    "资源包": ["resource", "MDM", "推送失败"],

    # ========== 电量/硬件问题 ==========
    "电量": ["电池", "没电", "低电量", "充电"],
    "充电": ["电量", "电源", "power"],
    "data_mux": ["data mux", "通信超时", "刷机超时"],
}


def expand_query_rules(query: str) -> list[str]:
    """规则查询扩展：用同义词映射替代LLM生成。

    示例:
        "flashtool怎么用" -> ["flashtool怎么用", "flash_tool怎么用", "刷机工具怎么用"]
        "D0551刷不进去" -> ["D0551刷不进去", "D0551刷机失败", "D0551无法刷机"]
    """
    expansions = [query]  # 保留原查询
    query_lower = query.lower()

    # 查找同义词并扩展
    for keyword, synonyms in QUERY_EXPANSION_RULES.items():
        if keyword.lower() in query_lower:
            # 为每个同义词生成新查询
            for syn in synonyms:
                new_query = query_lower.replace(keyword.lower(), syn.lower())
                if new_query not in expansions and len(expansions) < 5:
                    expansions.append(new_query)

    return expansions


# ---------- 缓存层 ----------
from functools import lru_cache
import time

# 内存缓存：query -> (result, timestamp)
_vector_search_cache: dict[str, tuple[list[dict], float]] = {}
_keyword_search_cache: dict[str, tuple[list[dict], float]] = {}
CACHE_TTL = 300  # 缓存有效期5分钟


def _get_from_cache(cache: dict, key: str, ttl: int = CACHE_TTL) -> list[dict] | None:
    """从缓存获取结果，过期返回None"""
    if key in cache:
        result, timestamp = cache[key]
        if time.time() - timestamp < ttl:
            return result
        # 过期删除
        del cache[key]
    return None


def _set_cache(cache: dict, key: str, result: list[dict]):
    """设置缓存"""
    cache[key] = (result, time.time())


def get_cache_stats() -> dict:
    """获取缓存统计信息"""
    return {
        "vector_cache_size": len(_vector_search_cache),
        "keyword_cache_size": len(_keyword_search_cache),
        "total_cached_queries": len(_vector_search_cache) + len(_keyword_search_cache),
        "cache_ttl_seconds": CACHE_TTL,
    }


def clear_search_cache():
    """清除检索缓存（案例更新后调用）"""
    _vector_search_cache.clear()
    _keyword_search_cache.clear()
    print("[Cache] 检索缓存已清除")


@lru_cache(maxsize=128)
def _get_cached_embeddings(query: str) -> list[float]:
    """缓存查询向量化结果（LRU自动管理）"""
    from memory import get_embedder
    embedder = get_embedder()
    return embedder.encode([query], normalize_embeddings=True)[0].tolist()


def vector_search(query: str, top_k: int = 10, use_cache: bool = True) -> list[dict]:
    """向量语义检索（带缓存）"""
    # 1. 检查缓存
    if use_cache:
        cached = _get_from_cache(_vector_search_cache, query)
        if cached is not None:
            print(f"[Cache Hit] 向量检索: {query[:20]}...")
            return cached

    # 2. 执行检索
    client = chromadb.PersistentClient(path=DB_DIR)
    collection = client.get_collection("nebullar_docs")
    result = collection.query(query_texts=[query], n_results=top_k)

    docs = result["documents"][0]
    scores = result["distances"][0]
    metas = result["metadatas"][0]

    results = []
    for content, dist, meta in zip(docs, scores, metas):
        results.append({
            "content": content,
            "score": round(1.0 - dist, 4),
            "product": meta.get("product", ""),
            "module": meta.get("module", ""),
        })

    # 3. 存入缓存
    if use_cache:
        _set_cache(_vector_search_cache, query, results)

    return results


def keyword_search(query: str, top_k: int = 10, use_cache: bool = True) -> list[dict]:
    """关键词检索（带缓存）"""
    # 1. 检查缓存
    if use_cache:
        cached = _get_from_cache(_keyword_search_cache, query)
        if cached is not None:
            print(f"[Cache Hit] 关键词检索: {query[:20]}...")
            return cached

    # 2. 执行检索
    client = chromadb.PersistentClient(path=DB_DIR)
    collection = client.get_collection("nebullar_docs")
    all_data = collection.get()
    all_docs = all_data["documents"]
    all_metas = all_data["metadatas"]

    tokenized_docs = [doc.split() for doc in all_docs]
    tokenized_query = query.split()
    bm25 = BM25Okapi(tokenized_docs)
    scores = bm25.get_scores(tokenized_query)

    top_indices = scores.argsort()[::-1][:top_k]

    results = []
    for idx in top_indices:
        results.append({
            "content": all_docs[idx],
            "score": round(float(scores[idx]), 4),
            "product": all_metas[idx].get("product", ""),
            "module": all_metas[idx].get("module", ""),
        })

    # 3. 存入缓存
    if use_cache:
        _set_cache(_keyword_search_cache, query, results)

    return results


def reciprocal_rank_fusion(
    vector_results: list[dict],
    keyword_results: list[dict],
    k: int = 60,
) -> list[dict]:
    """RRF融合排序：综合向量检索和关键词检索的结果，提升相关性和多样性。"""
    # 用一个字典存所有文档：key=文档前100字（去重用），value=文档信息
    merged = {}

    # 处理向量检索结果（第0名=最高）
    for rank, doc in enumerate(vector_results):
        key = doc["content"][:100]  # 前100字作为去重key
        merged[key] = {
            "content": doc["content"],
            "product": doc["product"],
            "module": doc["module"],
            "rrf_score": 1.0 / (k + rank),  # RRF公式：排名越前分数越高
        }

    # 处理关键词检索结果——同一文档累加RRF分
    for rank, doc in enumerate(keyword_results):
        key = doc["content"][:100]
        if key in merged:
            merged[key]["rrf_score"] += 1.0 / (k + rank)  # 两路都上榜，加分
        else:
            merged[key] = {
                "content": doc["content"],
                "product": doc["product"],
                "module": doc["module"],
                "rrf_score": 1.0 / (k + rank),
            }

    # 按 RRF 分数降序排列
    sorted_docs = sorted(merged.values(), key=lambda d: d["rrf_score"], reverse=True)
    return sorted_docs


# ---------- Reranker（Cross-Encoder 精排）----------
# 召回（向量+BM25+RRF）负责"广"，精排（Cross-Encoder）负责"准"：
# 把 (query, 候选文档) 一起送进模型，直接输出相关性分数，比向量距离精准。
RERANKER_MODEL = "BAAI/bge-reranker-base"


def rerank(query: str, candidates: list[dict], top_k: int = 5) -> list[dict]:
    """【★你来填★】用 Cross-Encoder 给召回的候选精排，取真正最相关的 top_k。

    candidates：RRF 融合后的候选，每个是 dict：
        {"content": "文档内容...", "product": "...", "module": "...", "rrf_score": 0.03}
    你能用的：
        model = _get_reranker()
        model.predict([[query, 文本1], [query, 文本2], ...])  # 返回每个 pair 的分数（numpy 数组）
    要做的 4 步：
        ① 把每个候选拼成 [query, 候选["content"]] 的 pair 列表
        ② model.predict(pairs) 得到分数数组
        ③ 把分数写回每个候选：候选["rerank_score"] = float(对应分数)   # float() 把 numpy 数转成普通 float
        ④ 按 rerank_score 从大到小排序，返回前 top_k 个
    """
    if not candidates:          # 没候选直接返回，省得白加载模型
        return []
    model = _get_reranker()     # 拿到 Cross-Encoder 对象（填的时候这行被删了，加回来）

    # 1. 拼成 pair 列表
    pairs = [[query, c["content"]] for c in candidates]
    # 2. 得到分数数组
    # model 是 _get_reranker() new 出来的 CrossEncoder 对象
    # .predict 是这个对象自带的库方法,把 [问题,文档] 配对打成相关性分数。
    scores = model.predict(pairs)  # 返回numpy数组，和candidates对应
    # 3. 写回每个候选（zip把两个列表配对遍历）
    for c, s in zip(candidates, scores):
        c["rerank_score"] = float(s)
    # lambda c: c["rerank_score"] —— 一个匿名函数(没名字的小函数)
    # def 取分数(c):
    # return c["rerank_score"]

    # 4. 按 rerank_score 排序，取前 top_k 个.(sorted 返回新列表，不改变原列表+lambda,reverse=True 降序)
    return sorted(candidates, key=lambda c: c["rerank_score"], reverse=True)[:top_k]


# ---------- Multi-Query 查询扩展（#3）----------
# 一个问题换多个角度去检索，召回更全。每个扩展 query 各自召回，汇成去重候选池，
# 最后用 reranker 对整池按"原始问题"精排。
MULTI_QUERY_SYSTEM = """你是检索查询扩展助手。用户给你一个技术支持问题，
请生成 3 个"换种说法 / 不同角度"的检索查询，覆盖同义表达、英文术语、可能的错误码或 API 名。
要求：每行一个查询，只输出查询本身，不要编号、不要解释、不要空行。"""

# HyDE：Hypothetical Document Embedding —— 用 LLM 生成"假设答案"去检索
# 原理：口语问题 → LLM 生成专业术语文档 → 用该文档向量去检索，比原问题更贴真实文档
HYDE_SYSTEM = """你是技术文档助手。用户问一个 Nebullar SDK 技术支持问题，请写一篇简短的技术文档片段作为"假设答案"。
要求：
1. 用专业术语、包含可能的错误码 / API 名 / 解决步骤
2. 50-100 字，像真实文档里的内容
3. 只输出文档内容，不要解释"""


def expand_queries(query: str, client, model, n: int = 2) -> list[str]:  # 3→2
    """用 LLM 扩展查询：Multi-Query + HyDE。

    返回：[原始query, 变体1, ..., 假设答案文档]（原始 query 一定放第一个）
    步骤：
      ① Multi-Query：调 LLM 生成多个角度的查询变体
      ② HyDE：调 LLM 生成假设答案文档（含专业术语，更接近真实文档）
      ③ 返回 [query] + variants[:n] + [hypo_doc]
    容错：任何出错就 return [query]，别让检索崩
    """
    try:
        from llm import complete
        # Multi-Query：生成多角度查询
        resp = complete(client, model, MULTI_QUERY_SYSTEM, query, max_tokens=256)
        variants = [line.strip() for line in resp.splitlines() if line.strip()]

        # HyDE：生成假设答案文档
        hypo_doc = complete(client, model, HYDE_SYSTEM, query, max_tokens=256)
        hypo_doc = hypo_doc.strip() if hypo_doc else ""

        # 组装：原始 + Multi-Query 变体 + HyDE 假设答案（假设答案非空才加）
        result = [query] + variants[:n]
        if hypo_doc:
            result.append(hypo_doc)
        return result
    except Exception:
        return [query]          # 出错就只用原始 query，别让检索崩


def search(query: str, top_k: int = 5, use_expansion: bool = True) -> list[dict]:
    """混合检索统一入口（规则扩展版）：
       规则查询扩展 → 每个 query 各自召回(向量+BM25+RRF) → 汇成去重候选池
       → Cross-Encoder 用「原始 query」精排 → 返回 top_k。

    Args:
        query: 用户查询
        top_k: 返回结果数量
        use_expansion: 是否使用规则扩展（默认True）

    优化：
    - 用规则扩展替代LLM Multi-Query，节省5-8秒
    - 保留Cross-Encoder精排，保证质量
    """
    # 规则扩展查询（替代LLM）
    queries = expand_query_rules(query) if use_expansion else [query]

    # 每个扩展 query 各自召回并 RRF，汇进一个按内容去重的候选池
    pool: dict[str, dict] = {}
    for q in queries:
        v_res = vector_search(q, top_k * 2)
        k_res = keyword_search(q, top_k * 2)
        for doc in reciprocal_rank_fusion(v_res, k_res):
            key = doc["content"][:100]
            # 同一文档被多个 query 召回时，保留 RRF 分更高的那次
            if key not in pool or doc["rrf_score"] > pool[key]["rrf_score"]:
                pool[key] = doc
    candidates = list(pool.values())

    # 精排：用「原始 query」对整个候选池打分，取真正最相关的 top_k
    try:
        return rerank(query, candidates, top_k)
    except Exception:
        # 没有 reranker 模型（如家里机器）就退回按 RRF 分排序
        return sorted(candidates, key=lambda d: d["rrf_score"], reverse=True)[:top_k]


# Backwards compatibility alias
def _get_embedder():
    """Alias for get_embedder from memory module"""
    from memory import get_embedder
    return get_embedder()
