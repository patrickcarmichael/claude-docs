---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Query the corpus and get top-k results

query = "What are 'skip-level' meetings?"
results, scores = retriever.retrieve(
    bm25s.tokenize(query),
    k=5,
)
```

Similar to the function above which produces vector results from the vector index we can write a function that produces keyword search results from the BM25 index:
```py
def bm25_retrieval(query: str, k: int, bm25_index) -> List[int]:
    """
    Retrieve the top-k document indices based on the BM25 algorithm for a given query.
    Args:
        query (str): The search query string.
        k (int): The number of top documents to retrieve.
        bm25_index: The BM25 index object used for retrieval.
    Returns:
        List[int]: A list of indices of the top-k documents that match the query.
    """

    results, scores = bm25_index.retrieve(bm25s.tokenize(query), k=k)

    return [contextual_chunks.index(doc) for doc in results[0]]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
