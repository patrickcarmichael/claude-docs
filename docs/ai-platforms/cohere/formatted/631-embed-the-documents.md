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
    texts=[doc["text"] for doc in documents],
).embeddings

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
