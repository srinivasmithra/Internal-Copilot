
# Mithra Solutions - Internal Code Copilot (RAG System)

This is a full Retrieval-Augmented Generation (RAG) powered internal AI Copilot prototype. It assists engineers working with large codebases, hardware SDKs, APIs, error logs, and design documentation — built for real-world enterprise engineering use cases.

---

## Project Overview

- Modular RAG pipeline for internal documentation, SDKs, source code, and logs.
- FAISS vector store + SentenceTransformer embeddings for fast similarity search.
- Groq-powered LLM inference (LLaMA3-70B model).
- Lightweight Streamlit frontend for interactive developer queries.
- Fully local embedding, retrieval, and data prep pipelines.

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.10 |
| Embeddings | Sentence Transformers (`all-MiniLM-L6-v2`) |
| Vector Store | FAISS |
| LLM Inference | Groq (LLaMA3-70B) |
| Frontend | Streamlit |
| Environment | python-dotenv |
| SDK Parsing | PyMuPDF (fitz) |

---

## Project Structure

```bash
project-root/
├── parsing/              # Parsing code for SDKs, code repos, logs
├── embeddings/           # Embedding generator code
├── rag_pipeline/         # Retrieval pipeline and LLM interaction
├── frontend/             # Streamlit frontend app
├── mock_data/            # (local mock data - excluded from Git)
├── processed_data/       # (intermediate chunks - excluded from Git)
├── vector_store/         # (FAISS index - excluded from Git)
├── .env                  # (API keys - excluded from Git)
└── requirements.txt
```

---

## .gitignore Exclusions

```bash
.venv/
__pycache__/
*.pyc
vector_store/
processed_data/
mock_data/
.env
.DS_Store
```
---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/srinivasmithra/Internal-Copilot.git
cd copilot
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

Create a `.env` file at the project root:

```bash
GROQ_API_KEY=your-groq-api-key
```

---

## Data Preparation

Since embeddings and vector store are not included in Git, you must first parse and embed your local data:

### 1. Prepare mock data folders

- Place your SDK PDF docs under:
  ```bash
  mock_data/sdk_docs/
  ```
- Place your source code repos under:
  ```bash
  mock_data/code_repos/
  ```

### 2. Run parsing scripts

```bash
python parsing/parsed_code.py
python parsing/parsed_sdk_docs.py
```

### 3. Generate embeddings

```bash
python embeddings/generate_embeddings.py
```

This will create `processed_data/` and `vector_store/` locally.

---

## Run Streamlit App

```bash
streamlit run frontend/app.py
```

Your AI Copilot will now launch on:  
`http://localhost:8501/`

---

## Sample Queries to Try

- How is HDMI handshake error handled?
- Show me API usage for DataBusInterface.
- What causes EDID read timeout?
- Where is UART initialization handled in STM32 HAL drivers?

---

## Why This Project?

This prototype demonstrates how Retrieval-Augmented Generation (RAG) copilots can:

- Boost developer productivity
- Simplify onboarding for large codebases
- Improve internal documentation access
- Assist hardware/software integration debugging
- Preserve organizational tribal knowledge

---

## Disclaimer

- No customer data used.
- All SDKs and sample data are for demo/educational use only.
- Fully independent personal prototype.

---

## Future Work

- Streamed token-level responses
- More flexible models for embedding code repos.
- Chat history with session memory
- Hybrid multi-modal embeddings (code+docs)
- Role-based user access

---

## Author

Built by Srinivas Mithra (MithraKing Solutions Prototype, 2024)
