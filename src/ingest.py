"""Load markdown docs, split into chunks, embed and store in ChromaDB."""
import os
import glob
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
from chromadb.utils import embedding_functions

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data", "processed")
DB_DIR = os.path.join(BASE, "chroma_db")


def ingest():
    # multilingual model: supports Chinese queries → English docs cross-lingual search
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )

    client = chromadb.PersistentClient(path=DB_DIR)

    # Delete and recreate to avoid duplicates on re-ingest
    try:
        client.delete_collection("kozen_docs")
    except Exception:
        pass

    collection = client.create_collection(
        name="kozen_docs",
        embedding_function=embedding_fn,
        metadata={"hnsw:space": "cosine"},
    )

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

            with open(md_file, "r", encoding="utf-8") as f:
                text = f.read()

            chunks = splitter.split_text(text)

            if not chunks:
                continue

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
