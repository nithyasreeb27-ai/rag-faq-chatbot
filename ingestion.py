import os

DATA_FOLDER = "data"

def load_documents(folder_path):

    documents = []

    for filename in os.listdir(folder_path):

        if filename.lower().endswith(".txt"):

            filepath = os.path.join(folder_path, filename)

            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read().strip()

            documents.append({
                "filename": filename,
                "content": text
            })

    return documents

if __name__ == "__main__":

    docs = load_documents(DATA_FOLDER)

    for doc in docs:
        print("Loaded:", doc["filename"])
        print(doc["content"])
        print("-" * 50)