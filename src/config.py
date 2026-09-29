from pathlib import Path


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent


# Data directory
DATA_DIR = BASE_DIR / "data"


# PDF file
PDF_PATH = DATA_DIR / "Ebook-Agentic-AI.pdf"


# FAISS vector database
FAISS_PATH = DATA_DIR / "faiss_index"


# Free embedding model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


# Free local LLM
LLM_MODEL = "qwen2.5:1.5b"


# RAG settings
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K = 3
CONFIDENCE_THRESHOLD = 0.50