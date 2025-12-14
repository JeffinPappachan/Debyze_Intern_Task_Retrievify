from app.llm import llm
from app.vectorstore import get_vectorstore

vectorstore = get_vectorstore()

def hyde_retrieve_docs(query: str, k: int = 4):
    """
    HyDE retrieval:
    1. Generate hypothetical answer
    2. Embed & retrieve documents using that answer
    """

    # Step 1: Generate hypothetical document
    hyde_prompt = f"""
    Write a concise, factual paragraph that answers the following question:

    Question: {query}
    """

    hypothetical_answer = llm.invoke(hyde_prompt)

    # Step 2: Use hypothetical answer for retrieval
    docs = vectorstore.similarity_search(
        hypothetical_answer,
        k=k
    )

    return docs
