---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Multilingual reranking

The Rerank models (`rerank-v3.5` and `rerank-multilingual-v3.0`) support 100+ languages. This means you can perform semantic search on texts in different languages.

In the example below, we repeat the steps of performing reranking with one difference – changing the model type to a multilingual one. Here, we use the `rerank-v3.5` model. Here, we are reranking the FAQ list using an Arabic query.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
