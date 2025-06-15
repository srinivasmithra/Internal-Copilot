
""" Testing file for retrieving chunks from using transformer and faiss"""


import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# load index.faiss
vector_store_dir = os.path.join(ROOT_DIR, "vector_store")
index = faiss.read_index(os.path.join(vector_store_dir, "index.faiss"))

with open(os.path.join(vector_store_dir, "metadata.pkl"), "rb") as f:
    metadata = pickle.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_relevant_chunks(query, top_k=5):
    query_vector = model.encode([query])
    distances, indices = index.search(query_vector, top_k)

    results = []
    for idx in indices[0]:
        if idx == -1:
            continue
        results.append(metadata[idx])
    return results
