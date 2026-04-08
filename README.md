# FAQ RAG Pipeline

A Retrieval-Augmented Generation (RAG) pipeline for answering questions from FAQ documents using open-source embeddings and a cloud LLM.

## Tech Stack
- **Embeddings:** sentence-transformers (all-MiniLM-L6-v2)
- **Vector Store:** FAISS
- **LLM:** LLaMA 3.3 70B via Groq API (free)
- **UI:** Streamlit

## Project Structure
```
rag_faq_project/
├── data/              → FAQ text files
├── ingestion.py       → Loads documents
├── chunking.py        → Splits text into chunks
├── embeddings.py      → Generates embeddings
├── vector_store.py    → Creates FAISS index
├── retriever.py       → Retrieves relevant chunks
├── rag_pipeline.py    → Connects all steps
├── llm.py             → Groq LLM integration
├── app.py             → Streamlit web UI
└── .env               → API key (not shared)
```

## Setup Instructions

### 1. Install dependencies
```bash
pip install sentence-transformers faiss-cpu groq streamlit python-dotenv
```

### 2. Add your FAQ files
Place `.txt` files inside the `data/` folder.

### 3. Add Groq API key
Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get a free key at: https://console.groq.com

### 4. Run the app
```bash
streamlit run app.py
```

## Sample Queries & Answers

| Question | Answer |
|---|---|
| What is the refund policy? | Refunds are allowed within 30 days of purchase. |
| How do I contact support? | You can reach support at support@company.com |
| What payment methods are accepted? | Visa, Mastercard, PayPal and UPI are accepted. |

## How It Works
1. Documents are loaded from the `data/` folder
2. Text is split into chunks for better retrieval
3. Chunks are converted to embeddings using sentence-transformers
4. Embeddings are stored in a FAISS vector database
5. User question is embedded and matched against stored chunks
6. Top matching chunks are passed to Groq LLM to generate an answer