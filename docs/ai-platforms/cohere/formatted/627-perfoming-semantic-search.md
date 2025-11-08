---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Perfoming semantic search

Now, we want to search for the most relevant documents to the query. We do this by computing the similarity between the embeddings of the query and each of the documents.

There are various approaches to compute similarity between embeddings, and we'll choose the dot product approach. For this, we use the `numpy` library which comes with the implementation.

Each query-document pair returns a score, which represents how similar the pair is. We then sort these scores in descending order and select the top-most `n` similar pairs, which we choose to return the top two (`n=2`, this is an arbitrary choice, you can choose any number).

Here, we show the most relevant documents with their similarity scores.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
