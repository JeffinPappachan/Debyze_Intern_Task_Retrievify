from langgraph.graph import StateGraph
from app.retriever import retrieve_docs
from app.llm import llm


def retrieval_node(state: dict) -> dict:
    """
    Retrieves relevant documents from the vector store
    based on the user query.
    """
    docs = retrieve_docs(state["query"])
    return {
        "query": state["query"],
        "context": docs
    }


def reasoning_node(state: dict) -> dict:
    prompt = f"""
You are a precise document question-answering assistant.

Answer the question using ONLY the context provided.
If the answer is not in the context, say "Not found in the document."

Context:
{state['context']}

Question:
{state['query']}
"""
    answer = llm.invoke(prompt)
    return {"answer": answer}


# -----------------------------
# LangGraph Agent Construction
# -----------------------------
graph = StateGraph(dict)

graph.add_node("retrieve", retrieval_node)
graph.add_node("reason", reasoning_node)

graph.set_entry_point("retrieve")
graph.add_edge("retrieve", "reason")

agent = graph.compile()
