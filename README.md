# fastapi-chatbot
# FastAPI RAG Chatbot (LLM + Vector Search)

A lightweight **Retrieval-Augmented Generation (RAG)** chatbot built with:

- **FastAPI**
- **OpenAI LLMs**
- **ChromaDB** (vector embeddings)
- **Python**
- **Embeddings-based retrieval**

This project demonstrates how to build a production-style chatbot that can:

✔ answer questions using retrieved documents  
✔ integrate LLMs with a knowledge base  
✔ run as a lightweight API service  
✔ showcase end-to-end AI engineering  

---

## Project Structure

fastapi-rag-chatbot/
├── app.py # FastAPI server
├── chatbot.py # LLM logic
├── rag.py # embeddings + RAG pipeline
├── knowledge_base/ # simple text knowledge base
├── requirements.txt
└── README.md

## How It Works

1. Text from `knowledge_base/` is embedded and stored in ChromaDB.
2. When a user asks something, the system:
   - embeds the question  
   - retrieves similar documents  
   - sends context + question to an LLM  
3. The LLM generates a grounded, context-aware answer.

## Run Locally

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="your-key"
uvicorn app:app --reload



POST http://127.0.0.1:8000/ask
{
  "question": "What does Carepool do?"
}





