"""Load markdown docs, split into chunks, embed and store in ChromaDB."""
import os
import glob
from langchain_text_splitters import RecursiveCharacterTextSplitter  # 智能文本切分器：按段落→句子→空格优先级拆分
import chromadb  # 轻量向量数据库，存文字向量做相似度检索
from chromadb.utils import embedding_functions  # 嵌入函数：调用模型把文字转成向量

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data", "processed")
DB_DIR = os.path.join(BASE, "chroma_db")


# 遍历两个SDK的所有markdown文档，切片后向量化存入ChromaDB
def ingest():
    # 跨语言嵌入模型：中文提问也能匹配英文文档
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )

    client = chromadb.PersistentClient(path=DB_DIR)  # 本地持久化客户端，数据存硬盘

    # 每次重建collection避免重复数据
    try:
        client.delete_collection("kozen_docs")
    except Exception:
        pass

    collection = client.create_collection(
        name="kozen_docs",
        embedding_function=embedding_fn,
        metadata={"hnsw:space": "cosine"},  # 余弦相似度：向量方向越接近越相关
    )

    # chunk_size=800：每段最多800字符；chunk_overlap=80：相邻段重叠80字符防止语义断裂
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        separators=["\n\n", "\n", ". ", "  ", " ", ""],
    )

    for product_dir in sorted(os.listdir(DATA)):
        product_path = os.path.join(DATA, product_dir)
        if not os.path.isdir(product_path):
            continue

        for md_file in sorted(glob.glob(os.path.join(product_path, "*.md"))):
            if "00_full_document" in md_file:
                continue

            module = os.path.splitext(os.path.basename(md_file))[0]

            # 编码兼容：UTF-8 → GBK → UTF-8容错（跳过坏字节）
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

            chunks = splitter.split_text(text)

            if not chunks:
                continue

            # 存入ChromaDB：文档内容 + 唯一ID + 元数据（产品、模块、来源文件）
            collection.add(
                documents=chunks,
                ids=[f"{product_dir}_{module}_{i}" for i in range(len(chunks))],
                metadatas=[
                    {
                        "product": product_dir,
                        "module": module,
                        "chunk_index": i,
                        "source": md_file,
                    }
                    for i in range(len(chunks))
                ],
            )

            print(f"  [{product_dir}/{module}] {len(chunks)} chunks")

    print(f"\nDone: {collection.count()} chunks indexed in '{collection.name}'")


if __name__ == "__main__":
    ingest()
