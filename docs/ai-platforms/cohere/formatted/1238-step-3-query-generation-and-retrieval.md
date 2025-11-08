---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## **Step 3: Query generation and retrieval**

In order to do RAG, we need a query or a set of queries to actually *do* the retrieval step. As is standard in RAG settings, we'll use Command to generate those queries for us. Then, we'll use those queries along with the LlamaIndex retriever we built earlier to retrieve the most relevant pieces of the 10-K.

To learn more about document mode and query generation, check out [our documentation](https://docs.cohere.com/docs/retrieval-augmented-generation-rag).
```python PYTHON
PROMPT = "List the overall revenue numbers for 2021, 2022, and 2023 in the 10-K as bullet points, then explain the revenue growth trends."

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
