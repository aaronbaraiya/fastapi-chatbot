
import chromadb
from chromadb.config import Settings
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize Chroma vector store
chroma_client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet",
                                         persist_directory="./chroma_db"))

collection = chromadb.Client().get_or_create_collection(
    name="knowledge_base",
    metadata={"hnsw:space": "cosine"}
)

def load_knowledge_base():
    """Loads text file into vector DB if empty."""
    if collection.count() > 0:
        return  # Don't reload every time

    with open("knowledge_base/carepool_info.txt", "r") as f:
        content = f.read()

    chunks = content.split("\n")
    for idx, chunk in enumerate(chunks):
        if chunk.strip():
            embedding = client.embeddings.create(
                model="text-embedding-3-small",
                input=chunk
            )
            collection.add(
                ids=[f"chunk-{idx}"],
                documents=[chunk],
                embeddings=[embedding.data[0].embedding]
            )
    print("Knowledge base loaded into ChromaDB.")

def retrieve_relevant_docs(query):
    embedding = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    )

    results = collection.query(
        query_embeddings=[embedding.data[0].embedding],
        n_results=3
    )

    return results["documents"][0] if results else []
