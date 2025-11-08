---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Embed the search query

query_emb = co.embed(
    model="embed-v4.0",
    input_type="search_query",
    texts=[queries_for_search],
    embedding_types=["float"],
).embeddings.float
```
```
Search query:  how to get to know teammates
```
Now, we want to search for the most relevant documents to the query. For this, we make use of the `numpy` library to compute the similarity between each query-document pair using the dot product approach.

Each query-document pair returns a score, which represents how similar the pair are. We then sort these scores in descending order and select the top most similar pairs, which we choose 5 (this is an arbitrary choice, you can choose any number).

Here, we show the most relevant documents with their similarity scores.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
