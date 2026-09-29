# 🤖 Agentic AI RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions strictly based on a provided Agentic AI eBook.

This project uses local and free AI tools, so it does not require paid OpenAI API credits or Pinecone.

## 🚀 Features

- PDF document ingestion
- Text chunking using RecursiveCharacterTextSplitter
- Free local embeddings using Sentence Transformers
- FAISS vector database for similarity search
- LangGraph-based RAG workflow
- Local LLM using Ollama
- Document-grounded question answering
- Refuses questions that are not supported by the document
- Confidence score for retrieved information
- Streamlit web interface

## 🏗️ Architecture

```text
Agentic AI eBook PDF
        ↓
   PyPDFLoader
        ↓
Text Chunking
(chunk size = 1000,
 overlap = 200)
        ↓
Sentence Transformers
(all-MiniLM-L6-v2)
        ↓
      FAISS
   Vector Database
        ↓
    LangGraph
        ↓
   Retrieve Top 3
        ↓
 Confidence Check
        ↓
    Ollama LLM
 (qwen2.5:1.5b)
        ↓
   Final Answer
        ↓
    Streamlit UI
Project Structure
rag-agentic-ai/
│
├── data/
│   └── Ebook-Agentic-AI.pdf
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── free_ingestion.py
│   └── graph.py
│
├── streamlit_app.py
├── requirements.txt
├── .gitignore
└── README.md
🛠️ Technologies Used
Python
LangChain
LangGraph
Sentence Transformers
FAISS
Ollama
Streamlit
PyPDF
Hugging Face
⚙️ Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL
cd rag-agentic-ai

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt
📄 Add the PDF

Place the Agentic AI eBook inside:

data/Ebook-Agentic-AI.pdf

The application expects the PDF at this location.

🧠 Build the Vector Database

Run:

python -m src.free_ingestion

This performs:

PDF loading
Text extraction
Text chunking
Embedding generation
FAISS vector database creation

The generated FAISS database is stored in:

data/faiss_index/
🤖 Install and Run Ollama

Install Ollama and download the model:

ollama pull qwen2.5:1.5b

Test the model:

ollama run qwen2.5:1.5b
🌐 Run the Chatbot

Start Streamlit:

streamlit run streamlit_app.py --server.fileWatcherType none

Open:

http://localhost:8501
💬 Example Questions
Question 1
What is Agentic AI?

The chatbot retrieves relevant sections from the eBook and generates an answer using the retrieved context.

Question 2
How do AI agents differ from traditional automation systems?

The chatbot retrieves the relevant document chunks before generating the answer.

Question 3
What are the core components of an Agentic Architecture?

The answer is generated using the retrieved eBook content.

Question 4
What role does memory play in Agentic AI workflows?

The chatbot searches the vector database for relevant sections.

Question 5
Who won the 2022 FIFA World Cup?

Expected behavior:

I cannot answer based on the provided document.

The chatbot is designed not to answer questions that are outside the provided document.

🔄 LangGraph Workflow

The application uses the following workflow:

START
  ↓
retrieve
  ↓
generate
  ↓
END
Retrieve Node

The retrieve node:

Converts the question into an embedding
Searches the FAISS vector database
Retrieves the top 3 relevant chunks
Calculates a retrieval confidence score
Generate Node

The generate node:

Receives the question
Receives retrieved document context
Checks the confidence threshold
Sends the context to the local Ollama model
Generates an answer only from the provided context

If the retrieval confidence is too low, the chatbot responds:

I cannot answer based on the provided document.
🔐 Free / Local Architecture

The original assignment specifies OpenAI embeddings, Pinecone and OpenAI GPT models.

This implementation uses free local alternatives:

Assignment Component	This Project
OpenAI Embeddings	Sentence Transformers
Pinecone	FAISS
OpenAI GPT	Ollama
LangGraph	LangGraph
FastAPI / Streamlit	Streamlit

This allows the complete RAG pipeline to run locally without paid API credits.

🎯 Project Objective

The objective is to demonstrate a document-grounded RAG chatbot that retrieves relevant information from an Agentic AI eBook and generates answers using only the retrieved document context.