# app/llm.py
from langchain_community.llms import Ollama

llm = Ollama(
    model="llama3.2:1b",
    temperature=0.0
)
