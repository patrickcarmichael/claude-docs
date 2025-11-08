---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Retrieval with Embed

Given the search query, we need a way to retrieve the most relevant documents from a large collection of documents.

This is where we can leverage text embeddings through the Embed endpoint. It enables semantic search, which lets us to compare the semantic meaning of the documents and the query. It solves the problem faced by the more traditional approach of lexical search, which is great at finding keyword matches, but struggles at capturing the context or meaning of a piece of text.

The Embed endpoint takes in texts as input and returns embeddings as output.

First, we need to embed the documents to search from. We call the Embed endpoint using `co.embed()` and pass the following arguments:

* `model`: Here we choose `embed-v4.0`
* `input_type`: We choose `search_document` to ensure the model treats these as the documents (instead of the query) for search
* `texts`: The list of texts (the FAQs)
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
