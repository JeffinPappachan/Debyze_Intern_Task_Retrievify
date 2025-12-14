from ragas import evaluate
from ragas.metrics import (
    context_precision,
    context_recall,
    faithfulness,
    answer_relevancy
)

# Example dataset structure
dataset = [
    {
        "question": "What is the document about?",
        "answer": "The document describes summer guidelines...",
        "contexts": ["...retrieved chunk text..."],
        "ground_truth": "Summer operational guidelines..."
    }
]

results = evaluate(
    dataset,
    metrics=[
        context_precision,
        context_recall,
        faithfulness,
        answer_relevancy
    ]
)

print(results)
