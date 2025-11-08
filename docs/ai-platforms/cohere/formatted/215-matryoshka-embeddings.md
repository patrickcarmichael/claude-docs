---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Matryoshka Embeddings

Matryoshka learning creates embeddings with coarse-to-fine representation within a single vector; `embed-v4.0` supports multiple output dimensions in the following values: `[256,512,1024,1536]`. To access this, you specify the parameter `output_dimension` when creating the embeddings.
```python PYTHON
texts = ["hello"]

response = co.embed(
    model="embed-v4.0",
    texts=texts,
    output_dimension=1024,
    input_type="classification",
    embedding_types=["float"],
).embeddings

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
