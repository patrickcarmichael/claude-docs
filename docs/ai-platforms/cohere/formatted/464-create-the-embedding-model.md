---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create the embedding model

embed_model = CohereEmbedding(
    api_key="COHERE_API_KEY",
    model="embed-english-v3.0",
    input_type="search_document",
    max_tokens=8000,
    embedding_types=["float"],
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
