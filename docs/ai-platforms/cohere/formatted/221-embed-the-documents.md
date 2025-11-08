---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Embed the documents

doc_emb = co.embed(
    inputs=embed_input,
    model="embed-v4.0",
    output_dimension=1024,
    input_type="search_document",
    embedding_types=["float"],
).embeddings.float

### STEP 2: Embed the query

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
