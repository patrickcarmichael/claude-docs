---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate the query embedding

query_embeddings = co.embed(
    model="embed-v4.0",
    input_type="search_query",
    embedding_types=["float"],
    texts=[query],
).embeddings.float[0]

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
