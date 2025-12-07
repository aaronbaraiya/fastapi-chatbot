
from openai import OpenAI
import os
from rag import retrieve_relevant_docs

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(query: str):
    # Retrieve documents related to the query
    docs = retrieve_relevant_docs(query)
    context = "\n".join(docs)

    prompt = f"""
You are an helpful assistant for a company project.
Use ONLY the context below to answer user questions.
If context is not enough, say you don't know.

CONTEXT:
{context}

QUESTION:
{query}

ANSWER:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message["content"].strip()
