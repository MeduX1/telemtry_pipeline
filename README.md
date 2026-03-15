# 🏥 Medical Telemetry RAG Pipeline: Explainable AI (XAI) Agent

An end-to-end Data Engineering and Retrieval-Augmented Generation (RAG) pipeline designed to simulate a hospital digital twin network. This backend architecture ingests real-time patient telemetry, securely stores it across dual databases, and utilizes a LangGraph AI agent to generate transparent, explainable medical recommendations.

## ⚙️ Architecture & Data Flow

This project bridges structured numerical data and unstructured clinical text to prevent LLM hallucinations and enforce Explainable AI (XAI) principles.

1. **The Web Layer (FastAPI):** Acts as the ingestion point for simulated IoT hospital sensors and the REST interface for medical staff.
2. **The Structured Vault (SQLite & SQLAlchemy):** Permanently stores exact numerical telemetry (Heart Rate, Systolic BP) with precise timestamps.
3. **The Unstructured Brain (ChromaDB):** Converts messy clinical notes into vector embeddings using `all-MiniLM-L6-v2` for semantic similarity search.
4. **The XAI Orchestrator (LangGraph & Llama 3.2):** A localized AI agent that queries both databases simultaneously, grounding its medical recommendations entirely in retrieved patient facts.

## 🛠️ Tech Stack
* **API Framework:** FastAPI, Uvicorn, Pydantic
* **Relational Database (ORM):** SQLite, SQLAlchemy
* **Vector Database:** ChromaDB, Hugging Face Sentence-Transformers
* **AI Orchestration:** LangGraph
* **Local LLM Inferencing:** Ollama (Llama 3.2:1b)

## 🚀 Getting Started

### 1. Installation
Clone the repository and install the required dependencies:
```bash
git clone [https://github.com/YOUR_USERNAME/medical-telemetry-rag-pipeline.git](https://github.com/YOUR_USERNAME/medical-telemetry-rag-pipeline.git)
cd medical-telemetry-rag-pipeline
pip install -r requirements.txt
