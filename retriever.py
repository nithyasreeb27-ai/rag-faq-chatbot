import numpy as np


def retrieve(query_embedding, index, chunks, top_k=2):

    query_vector = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_vector, top_k)

    results = []

    for i in indices[0]:
        results.append(chunks[i])

    return results
