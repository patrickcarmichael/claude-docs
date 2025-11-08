---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Ranking

In order to effectively combine the results from our vector and BM25 retrieval, we can use Cohere's Rerank 3 model through the inference API to provide a final, more precise, semantic reranking of our results.

First, create an inference endpoint with your Cohere API key. Make sure to specify a name for your endpoint, and the model\_id of one of the rerank models. In this example we will use Rerank 3.
```python PYTHON 

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
