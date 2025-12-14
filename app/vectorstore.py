# app/vectorstore.py
import os
import weaviate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Weaviate

WEAVIATE_URL = os.getenv("WEAVIATE_URL", "http://localhost:8080")

client = weaviate.Client(WEAVIATE_URL)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def get_vectorstore():
    return Weaviate(
        client=client,
        index_name="Documents",
        text_key="content",
        embedding=embeddings,
        by_text=False,  
    )
