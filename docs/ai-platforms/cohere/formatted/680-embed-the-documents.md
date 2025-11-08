---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Embed the documents

doc_emb = co.embed(
    model="embed-v4.0",
    input_type="search_document",
    texts=[doc["data"]["text"] for doc in faqs_long],
    embedding_types=["float"],
).embeddings.float
```
Next, we add a query, which asks about how to get to know the team.

We choose `search_query` as the `input_type` to ensure the model treats this as the query (instead of the documents) for search.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
