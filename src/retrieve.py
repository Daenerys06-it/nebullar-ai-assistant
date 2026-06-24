"""混合检索层：向量检索 + 关键词检索 + RRF 融合排序"""

# 向量检索：chromaDB
# 关键词检索：BM25算法（best matching25)
# RRF融合排序：将向量检索和关键词检索的结果进行融合排序，综合两者的优势，提高检索效果。
import os

# 强制 HuggingFace 离线：嵌入模型已本地缓存，公司网络会重置 huggingface.co 连接（10054）
os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")

import re
import chromadb
from rank_bm25 import BM25Okapi  # BM25 关键词检索算法

from llm import complete  # 统一补全入口，屏蔽 Opus / DeepSeek 差异

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE, "chroma_db")


# 查询重写系统提示词：把口语问题改写成检索友好的中英关键词
REWRITE_SYSTEM_PROMPT = """你是检索词优化助手。把用户的口语问题，改写成适合搜索 Nebullar SDK 英文技术文档的关键词。
规则：
1. 输出中文术语 + 对应英文术语 + 可能的API名/错误码
2. 只输出关键词，用空格分隔，不要解释、不要标点符号
3. 覆盖同义表达（如"刷卡"→card swipe, card reader, 读卡）"""


def rewrite_query(query: str, client, model) -> str:
    """用 LLM 把口语问题改写成检索友好的中英关键词。

    输入: "卡碰上去没反应刷不了"
    输出: 原始问题 + 扩展关键词，例如
          "卡碰上去没反应刷不了 非接触卡 无响应 contactless card no response checkCard"

    为什么把原始问题也拼上：万一改写跑偏，原问题还在，不丢原意。
    失败兜底：任何错误都回退到原始 query，不让检索崩。
    （client+model 由上层 agent 按 LLM_PROVIDER 传入，Opus / DeepSeek 都能用）
    """
    try:
        rewritten = complete(
            client, model, REWRITE_SYSTEM_PROMPT, query, max_tokens=512
        )  # 只输出关键词，几百 token 足够
        if rewritten and rewritten.strip():
            return query + " " + rewritten.strip()  # 原问题 + 扩展词
        return query
    except Exception:
        return query  # 网络/API 出错，回退原始 query


def vector_search(query: str, top_k: int = 10) -> list[dict]:
    """向量语义检索：把问题在 ChromaDB 里搜最相关的文档片段。
     底层原理
     1. 嵌入模型 (paraphrase-multilingual-MiniLM-L12-v2) 将 query 转成 384 个浮点数的向量
     2. 用这个向量跟库里 545 个 chunk 的向量逐个算余弦距离
     3. 距离越小 = 语义越近，返回 top_k 个
    NLP 知识点：Embedding（词嵌入）—— 语义相近的句子在向量空间里距离就近。
    """
    # PersistentClient：连接持久化客户端
    # get_collection：获取之前创建的 collection，里面存了文档向量和元数据
    client = chromadb.PersistentClient(path=DB_DIR)
    collection = client.get_collection("nebullar_docs")

    # collection.query 自动完成：query → 向量 → 余弦相似度计算 → 排序返回
    result = collection.query(query_texts=[query], n_results=top_k)

    # result 结构: {'documents': [[...]], 'distances': [[...]], 'metadatas': [[...]]}
    # 取 [0] 是因为 query_texts 是列表，每个 query 对应一组结果
    docs = result["documents"][0]  # 文档片段内容
    scores = result["distances"][0]  # 余弦距离（越小越相似）
    metas = result["metadatas"][0]  # 元数据（product, module 等）

    results = []
    for content, dist, meta in zip(docs, scores, metas):
        results.append(
            {
                "content": content,
                "score": round(1.0 - dist, 4),  # distance→similarity: 距离0→分数1
                "product": meta.get("product", ""),
                "module": meta.get("module", ""),
            }
        )
    return results


def keyword_search(query: str, top_k: int = 10) -> list[dict]:
    # 1.连接chromaDB
    client = chromadb.PersistentClient(path=DB_DIR)
    collection = client.get_collection("nebullar_docs")
    all_data = collection.get()  # 取全部
    # collection.get() 返回一个字典，
    # 包含 'documents'（文档内容列表）
    # 和 'metadatas'（对应的元数据列表）
    all_docs = all_data["documents"]  # 文档内容列表
    all_metas = all_data["metadatas"]  # 元数据列表
    # 2.分词
    # 545个chunk的文档内容，分词成列表；
    # query也分词成列表
    tokenized_docs = [doc.split() for doc in all_docs]
    tokenized_query = query.split()
    # 3.建立BM25索引并打分
    # BM25算法：基于词频和逆文档频率的关键词匹配算法，适合短文本检索
    bm25 = BM25Okapi(tokenized_docs)  # 建索引
    # get_scores：计算 query 与每个文档的相关性得分，返回一个分数列表（numpy array）
    scores = bm25.get_scores(tokenized_query)  # 每个文档一个分（numpy array）

    # 4.取 top_k 高分并组装结果
    # argsort：返回分数从小到大的索引，[::-1]倒序取分数最高的前top_k个索引
    top_indices = scores.argsort()[::-1][:top_k]  # argsort从小到大，[::-1]倒序取最大

    results = []
    for idx in top_indices:
        results.append(
            {
                "content": all_docs[idx],
                "score": round(float(scores[idx]), 4),
                "product": all_metas[idx].get("product", ""),
                "module": all_metas[idx].get("module", ""),
            }
        )
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
_RERANKER = None  # 懒加载：第一次用到才加载（已本地缓存，走 HF_HUB_OFFLINE 离线）


def _get_reranker():
    """懒加载 Cross-Encoder 重排模型（设施，已写）。"""
    global _RERANKER
    if _RERANKER is None:
        from sentence_transformers import CrossEncoder

        _RERANKER = CrossEncoder(RERANKER_MODEL)
    return _RERANKER


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


def search(query: str, top_k: int = 5, client=None, model=None) -> list[dict]:
    """混合检索统一入口：召回（向量+BM25+RRF）→ Cross-Encoder 精排 → 返回 top_k。

    client+model 可选：传入则先用 rewrite_query 扩展问题再检索，
    提升口语/模糊问题（如"黑屏怎么办"）的命中率；不传则用原始 query。
    """
    # 传了 client+model 就先扩展查询（把口语问题加上更多检索线索）
    search_query = rewrite_query(query, client, model) if client else query
    v_res = vector_search(search_query, top_k * 4)  # 召回多取一些，给精排更大候选池
    k_res = keyword_search(search_query, top_k * 4)
    rrf_res = reciprocal_rank_fusion(v_res, k_res)  # 默认 k=60

    # 精排：用 Cross-Encoder 对候选重新打分，取真正最相关的 top_k
    # 注意用「原始 query」而非改写后的 search_query —— 精排要判真实相关性
    try:
        return rerank(query, rrf_res, top_k)
    except Exception:
        return rrf_res[:top_k]  # 没有 reranker 模型（如家里机器未缓存）就退回 RRF 排序
