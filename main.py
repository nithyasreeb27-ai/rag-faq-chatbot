from rag_pipeline import build_rag, ask_question
from llm import generate_answer

index, chunks = build_rag()

while True:

    question = input("Ask a question: ")

    context = ask_question(question, index, chunks)

    combined_context = "\n".join(context)

    answer = generate_answer(question, combined_context)

    print("\nAnswer:\n")
    print(answer)


