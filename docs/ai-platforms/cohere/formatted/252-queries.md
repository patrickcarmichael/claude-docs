---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Queries

Our `rerank-v3.5` and `rerank-v3.0` models are trained with a context length of 4096 tokens. The model takes both the *query* and the *document* into account when calculating against this limit, and the query can account for up to half of the full context length. If your query is larger than 2048 tokens, in other words, it will be truncated to the first 2048 tokens (leaving the other 2048 for the document(s)).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
