---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 5. Rerank To Improve Quality

We will use a reranker model to improve retrieved chunk relevance quality:
```py
def rerank(query: str, chunks: List[str], top_k=3) -> List[int]:

    response = client.rerank.create(
        model="Salesforce/Llama-Rank-V1",
        query=query,
        documents=chunks,
        top_n=top_k,
    )

    return [result.index for result in response.results]


rerank_indices = rerank(
    "What are 'skip-level' meetings?",
    chunks=top_k_chunks,
    top_k=3,
)

reranked_chunks = ""

for index in rerank_indices:
    reranked_chunks += top_k_chunks[index] + "\n\n"

print(reranked_chunks)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
