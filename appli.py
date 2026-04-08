import streamlit as st
from rag_pipeline import build_rag, ask_question
from llm import generate_answer
from embeddings import model

st.set_page_config(page_title="FAQ Assistant", page_icon="🤖")
st.title("🤖 FAQ Assistant")
st.markdown("Ask any question from the FAQ documents.")

@st.cache_resource
def load_model():
    return model

@st.cache_resource
def load_rag():
    index, chunks = build_rag()
    return index, chunks

embedding_model = load_model()
index, chunks = load_rag()

st.markdown("### 💡 Suggested Questions")
sample_questions = [
    "How do I reset my password?",
    "My computer is running slowly. How do I fix it?",
    "What should I do if I receive a suspicious email?",
    "How do I connect to the company VPN?",
    "What is the password policy for company accounts?",
    "How do I recover deleted files?",
]

cols = st.columns(2)
selected_question = None

for i, question in enumerate(sample_questions):
    if cols[i % 2].button(question):
        selected_question = question

st.markdown("---")

typed_question = st.text_input("Or type your own question:", placeholder="e.g. How do I set up a printer?")

final_question = selected_question or typed_question

if final_question:
    with st.spinner("Searching for answer..."):
        context = ask_question(final_question, index, chunks)
        combined_context = "\n".join(context)
        answer = generate_answer(final_question, combined_context)

    st.markdown(f"### ❓ Question\n{final_question}")
    st.markdown("### 💬 Answer")
    st.success(answer)