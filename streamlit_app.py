import streamlit as st

from src.graph import graph


# Page configuration
st.set_page_config(
    page_title="Agentic AI RAG Chatbot",
    page_icon="🤖",
    layout="centered",
)


# Title
st.title("🤖 Agentic AI RAG Chatbot")

st.write(
    "Ask questions based on the Agentic AI eBook."
)


# Question input
question = st.text_input(
    "Enter your question:",
    placeholder="Example: What is Agentic AI?",
)


# Ask button
if st.button("Ask Question"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:
        with st.spinner("Searching the eBook and generating answer..."):

            result = graph.invoke(
                {
                    "question": question,
                    "context": [],
                    "answer": "",
                    "score": 0.0,
                }
            )

        # Answer
        st.subheader("Answer")
        st.write(result["answer"])

        # Confidence
        st.subheader("Confidence Score")
        st.write(round(result["score"], 3))

        # Retrieved context
        # with st.expander("View Retrieved Context"):
        #     for i, chunk in enumerate(
        #         result["context"],
        #         start=1,
        #     ):
        #         st.markdown(f"**Chunk {i}**")
        #         st.write(chunk)