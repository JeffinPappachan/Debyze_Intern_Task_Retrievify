# app/ingest.py

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.vectorstore import get_vectorstore


def ingest_document(path: str):
    # Load PDF document
    loader = PyPDFLoader(path)
    documents = loader.load()

    # Split document into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(documents)

    # ✅ Create vectorstore instance
    vectorstore = get_vectorstore()

    # Store chunks in Weaviate
    vectorstore.add_documents(chunks)

    print(f"Ingested {len(chunks)} chunks from {path}")
