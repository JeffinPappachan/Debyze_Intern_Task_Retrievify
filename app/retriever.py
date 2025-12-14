from app.vectorstore import get_vectorstore

def retrieve_docs(query: str, k: int = 4):
    vectorstore = get_vectorstore()

    # IMPORTANT: use similarity_search_by_vector
    embedding = vectorstore._embedding.embed_query(query)

    return vectorstore.similarity_search_by_vector(
        embedding,
        k=k
    )
