---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Embed and index documents

Let's embed our documents and store the embeddings. These embeddings are high-dimensional vectors (1,024 dimensions) that capture the semantic meaning of each document. We'll use Cohere's Embed 4 model that we have defined in the client setup.

The Embed 4 model require us to specify an `input_type` parameter that indicates what we're embedding. For semantic search, we use `search_document` for the documents we want to search through, and `search_query` for the search queries we'll make later.

We'll also keep track information about each document's language and translation to provide richer search results.

Finally, we'll build a search index with the `hnsw` vector library to store these embeddings efficiently, enabling faster document searches.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
