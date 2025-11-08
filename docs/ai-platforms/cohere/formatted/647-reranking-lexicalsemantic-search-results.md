---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Reranking lexical/semantic search results

Rerank requires just a single line of code to implement.

Suppose we have a list of search results of an FAQ list, which can come from semantic, lexical, or any other types of search systems. But this list may not be optimally ranked for relevance to the user query.

This is where Rerank can help. We call the endpoint using `co.rerank()` and pass the following arguments:

* `query`: The user query
* `documents`: The list of documents
* `top_n`: The top reranked documents to select
* `model`: We choose Rerank English 3
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
