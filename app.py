
from fastapi import FastAPI
from pydantic import BaseModel
from rag import load_knowledge_base
from chatbot import generate_answer

app = FastAPI()

# Load vector store on startup
load_knowledge_base()

class Query(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "RAG Chatbot is running!"}

@app.post("/ask")
def ask(query: Query):
    answer = generate_answer(query.question)
    return {"answer": answer}
