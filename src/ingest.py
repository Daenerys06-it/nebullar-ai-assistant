"""Load markdown docs, split into chunks with smart chunking, embed and store in ChromaDB."""

# 文档切片+向量化（使用智能Chunking策略）
import os

# 强制 HuggingFace 离线：嵌入模型已本地缓存，公司网络会重置 huggingface.co 连接（10054）
os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")

import glob
import chromadb
from chromadb.utils import embedding_functions

# 导入智能Chunking模块
from chunking import create_chunker

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "DevDocForAIAgent_260507@latest")
DB_DIR = os.path.join(BASE, "chroma_db")


# 遍历两个SDK的所有markdown文档，切片后向量化存入ChromaDB
def ingest():
    """使用智能Chunking策略重建ChromaDB索引"""
    # 跨语言嵌入模型：中文提问也能匹配英文文档
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )
    # 本地持久化客户端，数据存硬盘
    client = chromadb.PersistentClient(path=DB_DIR)

    # 每次重建collection避免重复数据
    try:
        client.delete_collection("nebullar_docs")
    except Exception:
        pass

    # 创建新collection，使用余弦相似度
    collection = client.create_collection(
        name="nebullar_docs",
        embedding_function=embedding_fn,
        metadata={"hnsw:space": "cosine"},
    )

    # 创建智能Chunker（Markdown结构感知）
    chunker = create_chunker(
        strategy="markdown",
        chunk_size=512,
        chunk_overlap=50,
        max_code_lines=100,
    )

    total_chunks = 0

    # 遍历数据目录
    for product_dir in sorted(os.listdir(DATA)):
        product_path = os.path.join(DATA, product_dir)
        if not os.path.isdir(product_path):
            continue
        if product_dir.startswith("DevDocForAIAgent"):
            continue

        for md_file in sorted(glob.glob(os.path.join(product_path, "*.md"))):
            if "00_full_document" in md_file:
                continue

            module = os.path.splitext(os.path.basename(md_file))[0]

            # 读取文件
            try:
                with open(md_file, "r", encoding="utf-8") as f:
                    text = f.read()
            except UnicodeDecodeError:
                try:
                    with open(md_file, "r", encoding="gbk") as f:
                        text = f.read()
                except UnicodeDecodeError:
                    with open(md_file, "r", encoding="utf-8", errors="replace") as f:
                        text = f.read()

            # 使用智能Chunking切分文档
            chunks = chunker.chunk_document(
                text=text,
                source=md_file,
                product=product_dir,
                module=module,
            )

            if not chunks:
                continue

            # 转换为增强格式并入库
            documents = []
            ids = []
            metadatas = []

            for i, chunk in enumerate(chunks):
                enhanced = chunker.chunk_with_enhanced_metadata(chunk)
                documents.append(enhanced["content"])
                ids.append(f"{product_dir}_{module}_{i}")
                metadatas.append(enhanced["metadata"])

            collection.add(
                documents=documents,
                ids=ids,
                metadatas=metadatas,
            )

            total_chunks += len(chunks)
            print(f"  [{product_dir}/{module}] {len(chunks)} chunks (types: {set(c.chunk_type for c in chunks)})")

    print(f"\nDone: {total_chunks} chunks indexed in '{collection.name}'")
    print(f"   Collection count: {collection.count()}")
    return total_chunks


if __name__ == "__main__":
    ingest()
