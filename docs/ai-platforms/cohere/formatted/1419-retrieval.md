---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Retrieval

In this step, we use k-nearest neighbors to fetch the most relevant documents for our query. Once the nearest neighbors are retrieved, we use Cohere's reranker to reorder the documents in the most relevant order with regards to our input search query.
```python PYTHON
"""
Embed search query
Fetch k nearest neighbors
"""

query_emb = co.embed(texts=[prompt], model='embed-v4.0', input_type="search_query").embeddings
default_knn = 10
knn = default_knn if default_knn <= index.element_count else index.element_count
result = index.knn_query(query_emb, k=knn)
neighbors = [(result[0][0][i], result[1][0][i]) for i in range(len(result[0][0]))]
relevant_docs = [documents[x[0]] for x in sorted(neighbors, key=lambda x: x[1])]
```
```python PYTHON
"""
Rerank retrieved documents
"""

rerank_results = co.rerank(query=prompt, documents=relevant_docs, top_n=3, model='rerank-english-v2.0').results
reranked_relevant_docs = format_docs_for_chat([x.document["text"] for x in rerank_results])
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
