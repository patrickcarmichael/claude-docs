---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Embed the query

query_emb = co.embed(
    inputs=query_input,
    model="embed-v4.0",
    input_type="search_query",
    output_dimension=1024,
    embedding_types=["float"],
).embeddings.float

### STEP 3: Return the most similar documents

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
