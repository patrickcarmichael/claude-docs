---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Embed the passages and store them in an index

```python PYTHON
embeddings = CohereEmbeddings(model = "multilingual-22-12")
db = Qdrant.from_documents(texts, embeddings, location=":memory:", collection_name="my_documents", distance_func="Dot")
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
