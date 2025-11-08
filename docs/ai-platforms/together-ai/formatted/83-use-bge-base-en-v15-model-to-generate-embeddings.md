---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Use bge-base-en-v1.5 model to generate embeddings

embeddings = generate_embeddings(to_embed, "BAAI/bge-base-en-v1.5")
```
This will generate embeddings of the movies which we can use later to retrieve similar movies.

When a use makes a query we can embed the query using the same model and perform a vector similarity search as shown below:
```py
from sklearn.metrics.pairwise import cosine_similarity

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
