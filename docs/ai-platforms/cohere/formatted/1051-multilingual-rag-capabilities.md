---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Multilingual RAG Capabilities

Command R7B Arabic has been trained specifically for Arabic and English tasks, such as the *generation* step of Retrieval Augmented Generation (RAG).

Command R7B Arabic's RAG functionality is supported through chat templates in Transformers. Using our RAG chat template, the model takes a conversation (with an optional user-supplied system preamble) and a list of document snippets as input. The resulting output contains a response with in-line citations. Here's what that looks like:
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
