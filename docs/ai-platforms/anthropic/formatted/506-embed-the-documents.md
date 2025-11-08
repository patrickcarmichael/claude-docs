---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Embed the documents

doc_embds = vo.embed(
    documents, model="voyage-3.5", input_type="document"
).embeddings
```
The embeddings will allow us to do semantic search / retrieval in the vector space. Given an example query,
```python
query = "When is Apple's conference call scheduled?"
```
we convert it into an embedding, and conduct a nearest neighbor search to find the most relevant document based on the distance in the embedding space.
```python
import numpy as np

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
