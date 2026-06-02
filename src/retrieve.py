"""混合检索层：向量检索 + 关键词检索 + RRF 融合排序"""

# 向量检索：chromaDB
# 关键词检索：BM25算法（best matching25)
# RRF融合排序：将向量检索和关键词检索的结果进行融合排序，综合两者的优势，提高检索效果。
import os
import chromadb
from rank_bm25 import BM25Okapi  # BM25 关键词检索算法

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE, "chroma_db")


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
    collection = client.get_collection("kozen_docs")

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
    collection = client.get_collection("kozen_docs")
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
