# RAG-based FAQ Chatbot

## Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline to answer user queries from a FAQ dataset using embeddings and vector search. It improves upon traditional keyword-based systems by retrieving contextually relevant information.

---

## Problem Statement

Traditional FAQ systems rely on keyword matching, which often fails to capture the semantic meaning of user queries, leading to irrelevant or inaccurate responses—especially when dealing with large or unstructured documents.

---

## Solution

This project uses a RAG pipeline to:

~Convert text data into embeddings
~Store embeddings in a vector database
~Retrieve relevant context based on user queries
~Generate accurate and context-aware responses

---

## Workflow

 Load FAQ data from text file
 Split text into smaller chunks
 Convert chunks into embeddings
 Store embeddings in a vector store
 Retrieve relevant chunks based on query
 Generate final response

---

## Project Structure

```
data/
  faq.txt

chunking.py
embeddings.py
ingestion.py
retriever.py
vector_store.py
rag_pipeline.py
app.py
README.md
```

---

## Tech Stack

Python
Natural Language Processing (NLP)
Embeddings (Sentence Transformers / OpenAI)
Vector Search

---

## Key Features

Context-aware answer retrieval
Efficient semantic search using embeddings
Modular and extensible pipeline design

---

## How to Run

1.Clone the repository:

```
git clone https://github.com/nithyasreeb27-ai/rag-faq-chatbot.git
cd rag-faq-chatbot
```

2.Install dependencies:

```
pip install -r requirements.txt
```

3.Add your API key in a `.env` file:

```
OPENAI_API_KEY=your_api_key
```

4.Run the application:

```
python app.py
```

---

## Sample Run

**Query:** What is the refund policy?
**Retrieved Context:** Customers can return products within 7 days...
**Final Answer:** Customers can return products within 7 days.

---

## Future Improvements

Integrate advanced LLMs for better response generation
Deploy as a web-based application
Use scalable vector databases (FAISS, Pinecone)
Add user interface for better interaction

---

## Author

Nithyasree B
Biotechnology Student | AI Intern
Interested in AI + Healthcare | NLP & Computer Vision
