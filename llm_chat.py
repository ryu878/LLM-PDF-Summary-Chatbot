import requests

OLLAMA_API_URL = "http://localhost:11434/api/chat"

def query_llm_with_context(context: str, question: str, model="llama3") -> str:
    """
    Sends context + user question to local LLM and returns the answer.
    """
    prompt = f"""
You are a helpful assistant that answers questions based on the following document:

--- BEGIN DOCUMENT ---
{context[:4000]}
--- END DOCUMENT ---

Question: {question}
Answer:
"""
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    response.raise_for_status()
    return response.json()["message"]["content"]
