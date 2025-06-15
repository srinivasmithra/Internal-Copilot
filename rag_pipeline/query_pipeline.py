""" Main logic of the copilot goes here as it takes input query and encode
    it using pre-loaded model and later the chunks are used to
    find the chunks in pre loaded vectors stored using faiss.
    Later we use Groke API inference to make use of LLM model (llama3).

 """

import os
import faiss
import pickle
import numpy as np
from rag_pipeline.embedding_loader import EmbeddingModel
from rag_pipeline.llm_inference import call_llm

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
vector_store_dir = os.path.join(ROOT_DIR, "vector_store")

index = faiss.read_index(os.path.join(vector_store_dir, "index.faiss"))
with open(os.path.join(vector_store_dir, "metadata.pkl"), "rb") as f:
    metadata = pickle.load(f)

model = EmbeddingModel.get_model()

def retrieve_context(query, top_k=5):
    query_vector = model.encode([query])
    distances, indices = index.search(query_vector, top_k)
    chunks = []
    for idx in indices[0]:
        if idx == -1:
            continue
        chunks.append(metadata[idx])
    return chunks

def build_prompt(query, retrieved_chunks):
    context = ""
    for chunk in retrieved_chunks:
        context += f"File: {chunk['source']} (Category: {chunk['category']})\n"
    prompt = f"""
You are a technical assistant specialized in Mithra Solutions hardware and software systems. Use the following retrieved documents to answer the user's question.

Retrieved Documents:
{context}

User Question: {query}

Answer:"""
    return prompt

def query_pipeline(user_query):
    retrieved_chunks = retrieve_context(user_query)
    prompt = build_prompt(user_query, retrieved_chunks)
    answer = call_llm(prompt)
    return answer
