# app/main.py
from fastapi import FastAPI
from app.agent import agent


app = FastAPI(title="Agentic Document QA")

@app.post("/query")
def query_doc(question: str):
    result = agent.invoke({"query": question})
    return {
        "question": question,
        "answer": result["answer"]
    }
