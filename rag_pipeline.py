from ingestion import load_documents
from chunking import chunk_text
from embeddings import generate_embeddings, model
from vector_store import create_vector_store
from retriever import retrieve


def build_rag():
    # Step 1 — Load documents from data folder
    docs = load_documents("data")

    # Step 2 — Chunk each document
    all_chunks = []
    for doc in docs:
        text = doc["content"]
        chunks = chunk_text(text)
        all_chunks.extend(chunks)

    # Step 3 — Check chunks exist
    if len(all_chunks) == 0:
        raise ValueError("No chunks created!")

    # Step 4 — Generate embeddings
    embeddings = generate_embeddings(all_chunks)

    # Step 5 — Store in FAISS
    index = create_vector_store(embeddings)

    return index, all_chunks


def ask_question(question, index, chunks):
    # Convert question to numbers
    query_embedding = model.encode(question)

    # Search FAISS for relevant chunks
    results = retrieve(query_embedding, index, chunks)

    return results
