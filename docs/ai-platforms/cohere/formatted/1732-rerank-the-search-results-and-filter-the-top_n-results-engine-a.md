---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Rerank the search results and filter the top\_n results ("Engine A")

In this section, we'll implement our first retrieval approach using Cohere's reranking model. Reranking is a technique that takes an initial set of search results and reorders them based on their relevance to the original query.

We'll use Cohere's `rerank` API to:

1. Take the Wikipedia search results we obtained earlier
2. Send them to Cohere's reranking model along with the original query
3. Filter to keep only the top-n most relevant results

This approach will be referred to as "Engine A" in our evaluation, and we'll compare its performance against the original Wikipedia search rankings.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
