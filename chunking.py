def chunk_text(text):

    chunks = []

# Split based on questions
    parts = text.split("Q:")

    for part in parts:
        part = part.strip()

        if part:
            chunks.append("Q: " + part)

    return chunks