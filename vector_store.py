import faiss
import numpy as np


def create_vector_store(embeddings):

    dimension = len(embeddings[0])  # size of embedding vector

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings).astype("float32"))

    return index
