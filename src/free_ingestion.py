# from pathlib import Path

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS


# # --------------------------------
# # 1. Find the PDF
# # --------------------------------

# BASE_DIR = Path(__file__).resolve().parent.parent

# PDF_PATH = BASE_DIR / "data" / "Ebook-Agentic-AI.pdf"

# FAISS_PATH = BASE_DIR / "data" / "faiss_index"


# # --------------------------------
# # 2. Load the PDF
# # --------------------------------

# def load_pdf():

#     print("Loading PDF...")

#     if not PDF_PATH.exists():
#         raise FileNotFoundError(
#             f"PDF not found at: {PDF_PATH}"
#         )

#     loader = PyPDFLoader(str(PDF_PATH))

#     documents = loader.load()

#     print(f"PDF loaded successfully.")
#     print(f"Number of pages: {len(documents)}")

#     return documents


# # --------------------------------
# # 3. Split PDF into chunks
# # --------------------------------

# def split_documents(documents):

#     print("\nSplitting document...")

#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=1000,
#         chunk_overlap=200,
#     )

#     chunks = text_splitter.split_documents(
#         documents
#     )

#     print(f"Document split into {len(chunks)} chunks.")

#     return chunks


# # --------------------------------
# # 4. Create free embeddings
# # --------------------------------

# def create_embeddings():

#     print("\nLoading free embedding model...")

#     embeddings = HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-MiniLM-L6-v2"
#     )

#     print("Embedding model loaded successfully.")

#     return embeddings


# # --------------------------------
# # 5. Store embeddings in FAISS
# # --------------------------------

# def store_in_faiss(chunks, embeddings):

#     print("\nCreating FAISS vector database...")

#     vector_store = FAISS.from_documents(
#         documents=chunks,
#         embedding=embeddings,
#     )

#     vector_store.save_local(
#         str(FAISS_PATH)
#     )

#     print("FAISS vector database created successfully.")

#     print(f"Saved at: {FAISS_PATH}")

#     return vector_store


# # --------------------------------
# # 6. Main function
# # --------------------------------

# def main():

#     print("================================")
#     print("FREE RAG INGESTION")
#     print("================================")

#     documents = load_pdf()

#     chunks = split_documents(documents)

#     embeddings = create_embeddings()

#     store_in_faiss(
#         chunks,
#         embeddings,
#     )

#     print("\n================================")
#     print("INGESTION COMPLETED SUCCESSFULLY")
#     print("================================")


# if __name__ == "__main__":
#     main()
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

PDF_PATH = BASE_DIR / "data" / "Ebook-Agentic-AI.pdf"
FAISS_PATH = BASE_DIR / "data" / "faiss_index"


# Load PDF
def load_pdf():
    print("Loading PDF...")

    if not PDF_PATH.exists():
        raise FileNotFoundError(
            f"PDF not found at: {PDF_PATH}"
        )

    loader = PyPDFLoader(str(PDF_PATH))
    documents = loader.load()

    print("PDF loaded successfully.")
    print(f"Number of pages: {len(documents)}")

    return documents


# Split PDF into chunks
def split_documents(documents):
    print("\nSplitting document...")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    chunks = text_splitter.split_documents(documents)

    print(
        f"Document split into {len(chunks)} chunks."
    )

    return chunks


# Create free local embeddings
def create_embeddings():
    print("\nLoading free embedding model...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Embedding model loaded successfully.")

    return embeddings


# Store embeddings in FAISS
def store_in_faiss(chunks, embeddings):
    print("\nCreating FAISS vector database...")

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings,
    )

    vector_store.save_local(str(FAISS_PATH))

    print(
        "FAISS vector database created successfully."
    )

    print(f"Saved at: {FAISS_PATH}")


# Main ingestion pipeline
def main():
    print("================================")
    print("FREE RAG INGESTION")
    print("================================")

    documents = load_pdf()

    chunks = split_documents(documents)

    embeddings = create_embeddings()

    store_in_faiss(
        chunks,
        embeddings,
    )

    print("\n================================")
    print("INGESTION COMPLETED SUCCESSFULLY")
    print("================================")


if __name__ == "__main__":
    main()