import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_embedding_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

def read_all_files_from_dirs(data_dirs):
    corpus = []
    metadata = []
    for category, dir_path in data_dirs.items():
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    text = f.read()
                if len(text.strip()) == 0:
                    continue
                corpus.append(text)
                metadata.append({"category": category, "source": file})
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
    return corpus, metadata

def save_faiss_index(index, metadata, vector_store_dir=os.path.join(ROOT_DIR, "vector_store")):
    os.makedirs(vector_store_dir, exist_ok=True)
    faiss.write_index(index, os.path.join(vector_store_dir, "index.faiss"))
    with open(os.path.join(vector_store_dir, "metadata.pkl"), "wb") as f:
        pickle.dump(metadata, f)
