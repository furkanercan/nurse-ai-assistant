from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import json
import os
from pathlib import Path
import numpy as np
from typing import List, Dict

client = OpenAI()
app = FastAPI()

# Data directory
DATA_DIR = Path("data")

def load_patient_embeddings(patient_id: str) -> List[Dict]:
    """Load embedded chunks for a patient."""
    patient_dir = DATA_DIR / patient_id
    embeddings_file = patient_dir / f"{patient_id}_embedded_chunks.json"
    
    if not embeddings_file.exists():
        return []
    
    try:
        with open(embeddings_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading embeddings for {patient_id}: {e}")
        return []

def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    """Calculate cosine similarity between two vectors."""
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def get_relevant_chunks(question_embedding: List[float], patient_chunks: List[Dict], top_k: int = 5) -> List[str]:
    """Retrieve top-k most relevant chunks based on cosine similarity."""
    similarities = []
    
    for chunk in patient_chunks:
        # Handle different chunk formats
        chunk_embedding = chunk.get("embedding", [])
        chunk_text = chunk.get("text", "")
        
        if chunk_embedding and chunk_text:
            similarity = cosine_similarity(question_embedding, chunk_embedding)
            similarities.append((similarity, chunk_text))
    
    # Sort by similarity (descending) and get top-k
    similarities.sort(key=lambda x: x[0], reverse=True)
    return [text for _, text in similarities[:top_k]]

class Query(BaseModel):
    patient_id: str
    question: str

@app.post("/ask")
def ask(query: Query):
    # Load patient embeddings
    patient_chunks = load_patient_embeddings(query.patient_id)
    
    # Embed the user's question
    try:
        question_embedding = client.embeddings.create(
            input=[query.question],
            model="text-embedding-3-small"
        ).data[0].embedding
    except Exception as e:
        return {"answer": f"Error creating question embedding: {e}"}
    
    # Get relevant chunks if patient data exists
    context_text = ""
    if patient_chunks:
        relevant_chunks = get_relevant_chunks(question_embedding, patient_chunks, top_k=5)
        if relevant_chunks:
            context_text = "\n\n".join(relevant_chunks)
    
    # Build the prompt
    if context_text:
        system_message = """You are a helpful medical assistant. You have access to specific patient information. 
        When answering questions about the patient, use the patient information provided below.
        Answer directly and factually based on the patient data. Do not refuse to answer or say you cannot provide information - the patient data is provided for you to use.
        If the question is a general medical question not about this specific patient, answer based on your general medical knowledge."""
        
        user_message = f"""Here is the relevant patient information:

{context_text}

Question: {query.question}

Answer the question using the patient information provided above."""
    else:
        system_message = "You are a helpful medical assistant. Answer medical questions based on your general knowledge."
        user_message = query.question
    
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]

    try:
        res = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return {"answer": res.choices[0].message.content}
    except Exception as e:
        return {"answer": f"Error generating response: {e}"}
