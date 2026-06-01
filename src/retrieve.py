"""混合检索层：向量检索 + 关键词检索 + RRF 融合排序"""
import os
import chromadb

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE, "chroma_db")


def vector_search(query: str, top_k: int = 10) -> list[dict]:
    """向量语义检索：把问题在 ChromaDB 里搜最相关的文档片段。"""
    client = chromadb.PersistentClient(path=DB_DIR)
    collection = client.get_collection("kozen_docs")

    result = collection.query(query_texts=[query], n_results=top_k)

    # result 结构: {'documents': [[...]], 'distances': [[...]], 'metadatas': [[...]]}
    docs = result["documents"][0]
    scores = result["distances"][0]
    metas = result["metadatas"][0]

    results = []
    for content, dist, meta in zip(docs, scores, metas):
        results.append({
            "content": content,
            "score": round(1.0 - dist, 4),  # 余弦距离转相似度
            "product": meta.get("product", ""),
            "module": meta.get("module", ""),
        })
    return results
