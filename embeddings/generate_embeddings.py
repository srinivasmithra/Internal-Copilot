import os
from embed_utils import load_embedding_model, read_all_files_from_dirs, save_faiss_index
import faiss

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# My local parsed data folders
DATA_DIRS = {
    "code": os.path.join(ROOT_DIR, "processed_data/parsed_code"),
    "sdk": os.path.join(ROOT_DIR, "processed_data/parsed_sdk_docs"),
    "design": os.path.join(ROOT_DIR, "processed_data/parsed_design_docs"),
    "jira": os.path.join(ROOT_DIR, "processed_data/parsed_jira_issues"),
    "logs": os.path.join(ROOT_DIR, "processed_data/parsed_logs")
}

# Load model
model = load_embedding_model()

# Load data
corpus, metadata = read_all_files_from_dirs(DATA_DIRS)

# Create embeddings
embeddings = model.encode(corpus, show_progress_bar=True)

dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(embeddings)

save_faiss_index(index, metadata)

print("Embedding completed and saved into vector_store/")
