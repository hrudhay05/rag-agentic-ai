from pathlib import Path
from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
FAISS_PATH = BASE_DIR / "data" / "faiss_index"


# LangGraph state
class GraphState(TypedDict):
    question: str
    context: list[str]
    answer: str
    score: float


# Free local embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Load FAISS vector database
vector_store = FAISS.load_local(
    str(FAISS_PATH),
    embeddings,
    allow_dangerous_deserialization=True,
)


# Free local LLM through Ollama
llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0,
)


# Retrieve relevant document chunks
def retrieve(state: GraphState):
    question = state["question"]

    results = vector_store.similarity_search_with_score(
        question,
        k=3,
    )

    context = []
    scores = []

    for document, score in results:
        context.append(document.page_content)
        scores.append(score)

    if scores:
        average_distance = sum(scores) / len(scores)
        confidence = 1 / (1 + average_distance)
    else:
        confidence = 0.0

    return {
        "context": context,
        "score": confidence,
    }


# Generate answer only from retrieved context
def generate(state: GraphState):
    question = state["question"]
    context = state["context"]
    score = state["score"]

    # Reject questions with weak retrieval
    if not context or score < 0.50:
        return {
            "answer": "I cannot answer based on the provided document."
        }

    context_text = "\n\n".join(context)

    prompt = f"""
You are a document-based question answering assistant.

You must answer questions ONLY using the provided
context extracted from the Agentic AI eBook.

IMPORTANT RULES:

1. Use only the provided context.
2. Do not use your general knowledge.
3. Do not invent or assume information.
4. If the answer is not present in the context, respond exactly:

I cannot answer based on the provided document.

5. Keep the answer clear and concise.

Context:
----------------
{context_text}
----------------

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }


# Create LangGraph workflow
workflow = StateGraph(GraphState)

workflow.add_node("retrieve", retrieve)
workflow.add_node("generate", generate)

workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)


# Compile the graph
graph = workflow.compile()