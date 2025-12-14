# 📘 Agentic Document Question Answering System

## 🔍 Overview
This project implements an **Agentic Document Question Answering (QA) system** that enables users to query documents and receive accurate, context‑grounded answers.

The system follows a modern **Retrieval‑Augmented Generation (RAG)** architecture and is built using **agent‑based reasoning with LangGraph**, a **vector database for semantic search**, and **local LLM inference using Ollama**.

This project was developed as part of an **Internship Technical Task** and prioritizes:

- Local inference  
- Clean architecture  
- Containerized deployment  
- Reproducible evaluation  

---

## 🚀 Key Features
- 🔗 Agentic workflow using **LangGraph**  
- 📄 PDF document ingestion & chunking  
- 🧠 Semantic search with vector embeddings  
- 🗃️ **Weaviate** vector database  
- 🤖 Local LLM inference via **Ollama**  
- 🌐 **FastAPI**‑based REST API  
- 🐳 **Docker & Docker Compose** support  
- 📑 Swagger / OpenAPI documentation  

---

## 🧰 Tech Stack

| Component        | Technology        |
|------------------|------------------|
| Agent Framework  | LangGraph        |
| LLM Framework    | LangChain        |
| Vector Store     | Weaviate         |
| LLM Inference    | Ollama (Local)   |
| API Server       | FastAPI          |
| Containerization | Docker, Docker Compose |

---

## 🧠 System Architecture

### High‑Level Flow
User │ ▼ FastAPI (/query) │ ▼ LangGraph Agent │ ├──► Retriever ──► Weaviate (Vector Store) │ └──► Reasoning ──► Ollama (Local LLM) │ ▼ Final Answer

### Architecture Description
1. Documents are ingested and split into chunks  
2. Embeddings are generated and stored in Weaviate  
3. User submits a query through FastAPI  
4. LangGraph agent retrieves relevant document chunks  
5. Local LLM generates a grounded response using retrieved context  

---

## 📁 Project Structure
 ├── app/ │   ├── agent.py        # LangGraph agent logic │   ├── retriever.py    # Vector search logic │   ├── vectorstore.py  # Weaviate connection │   ├── ingest.py       # Document ingestion pipeline │   ├── llm.py          # Ollama LLM configuration │   └── main.py         # FastAPI application ├── data/ │   └── documents/      # Input PDFs ├── run_ingest.py       # Manual ingestion script ├── Dockerfile ├── docker-compose.yml ├── requirements.txt └── README.md

---

## ⚙️ Setup & Execution

### Prerequisites
- Docker & Docker Compose  
- Ollama installed locally  

---

## 🧠 Local LLM (Ollama)

The project uses **local inference** via Ollama.

### Start Ollama on Host Machine
```bash
ollama run llama3.2:1b

Ollama is not containerized intentionally.
Docker containers communicate with Ollama via:
http://host.docker.internal:11434

🐳 Docker Deployment
Build & Start Services
docker compose up --build

(Optional) Ingest Documents
docker compose exec api python run_ingest.py

🔗 Access Services
| Service  | URL  | 
|API Docs  | http://localhost:8000/docs | 
| Weaviate | http://localhost:8080 | 

🔌 API Usage
Endpoint
POST /query



Query Parameter
- question – string (required)
Example Request
curl -X POST \
  "http://localhost:8000/query?question=What is the document about?"


Example Response
{
  "question": "What is the document about?",
  "answer": "The document describes guidelines and operational rules related to..."
}

📊 Evaluation 

This project follows a Retrieval-Augmented Generation (RAG) evaluation methodology using the **RAGAS** framework.

### Metrics Used
The following metrics are defined for evaluation:

- **Context Precision** – Measures how much of the retrieved context is relevant
- **Context Recall** – Measures whether relevant context was retrieved
- **Faithfulness** – Ensures answers are grounded in retrieved documents
- **Answer Relevancy** – Measures how well the answer addresses the user query

### Evaluation Script
An evaluation script is provided at:

```bash
evaluation/evaluate_rag.py

### HyDE Retrieval 

The retrieval pipeline was enhanced using **HyDE (Hypothetical Document Embeddings)**.
Instead of directly embedding the user query, the system first generates a hypothetical answer using the local LLM and performs retrieval using that generated text.

This improves semantic recall and contextual relevance, especially for abstract questions.

In the folder their is hyde_retriever.py file which is the Implementation of the Hypothetical Document Embeddings and in the agent.py file i have commented migration to the hyde pipeline code currently it is basic document ingestion and retreival , if need to change to the hyDE pipeline just uncomment these lines and comment the need lines of codes and re-run , then it good to go and will be successfully functioning with the Hypothetical Document Embeddings System.







