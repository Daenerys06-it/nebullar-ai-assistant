"""Load markdown docs, split into chunks, embed and store in ChromaDB."""

# 文档切片+向量化（545 chunks 入库 ChromaDB）
import os
import glob
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
)  # 智能文本切分器：按段落→句子→空格优先级拆分
import chromadb  # 轻量向量数据库，存文字向量做相似度检索
from chromadb.utils import embedding_functions  # 嵌入函数：调用模型把文字转成向量

# 从当前文件出发 向上跳两级 作为项目的BASE路径
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 公司AI部门知识库：LLM-Wiki产出的结构化md，三个产品线
DATA = os.path.join(BASE, "DevDocForAIAgent_260507@latest")
# 基于BASE路径，构建一个指向chroma_db的路径，作为数据库存储位置。
DB_DIR = os.path.join(BASE, "chroma_db")


# 遍历两个SDK的所有markdown文档，切片后向量化存入ChromaDB
def ingest():
    # 跨语言嵌入模型：中文提问也能匹配英文文档
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )
    # 本地持久化客户端，数据存硬盘
    # path=DB_DIR：指定数据库存储位置，方便后续查询时加载同一数据集
    client = chromadb.PersistentClient(path=DB_DIR)

    # 每次重建collection避免重复数据
    try:
        # 删除旧collection：如果存在同名collection，先删除它以避免重复数据和ID冲突
        client.delete_collection("kozen_docs")
    except Exception:
        pass
    # 创建新collection：指定名称、嵌入函数和元数据配置（使用余弦相似度计算向量距离）
    collection = client.create_collection(
        name="kozen_docs",
        embedding_function=embedding_fn,
        metadata={"hnsw:space": "cosine"},
        # 余弦相似度：向量方向越接近越相关
    )

    # chunk_size=800：每段最多800字符；
    # chunk_overlap=80：相邻段重叠80字符防止语义断裂
    # separators：优先按段落、句子、空格切分，最后按字符切分保证不丢内容
    # RecursiveCharacterTextSplitter：递归文本切分器，按优先级拆分文本成适合模型处理的小段，避免语义断裂和信息丢失
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        separators=["\n\n", "\n", ". ", "  ", " ", ""],
    )
    # 遍历数据目录：每个子目录代表一个产品，
    # 每个markdown文件代表一个模块，跳过00_full_document.md（完整文档不切分）
    # listdir：列出DATA目录下的所有文件和目录，sorted：按字母顺序排序，确保处理顺序一致
    for product_dir in sorted(os.listdir(DATA)):
        # 过滤非目录项：确保只处理目录（产品），跳过文件等其他类型
        # join：拼接路径，构建每个产品目录的完整路径
        product_path = os.path.join(DATA, product_dir)
        if not os.path.isdir(product_path):
            continue
        # 跳过嵌套的冗余目录（公司知识库自带一份副本）
        if product_dir.startswith("DevDocForAIAgent"):
            continue
        # glob.glob：获取目录下所有markdown文件的列表，按文件名排序处理
        for md_file in sorted(glob.glob(os.path.join(product_path, "*.md"))):
            if "00_full_document" in md_file:
                continue
            # os.path.basename：获取文件名，os.path.splitext：去掉扩展名，得到模块名称
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
            # 切分文本成小段：根据配置的chunk_size、chunk_overlap和separators优先级拆分文本，得到适合模型处理的段落列表
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
            # 打印当前处理的模块和切分后的段落数量，方便监控进度和检查数据质量
            print(f"  [{product_dir}/{module}] {len(chunks)} chunks")
    # 最后打印总共索引的段落数量和collection名称，确认数据成功存入数据库
    print(f"\nDone: {collection.count()} chunks indexed in '{collection.name}'")


if __name__ == "__main__":
    ingest()
