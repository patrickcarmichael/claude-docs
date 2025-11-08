---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Embedding the documents

The Embed endpoint takes in texts as input and returns embeddings as output.

For semantic search, there are two types of documents we need to turn into embeddings.

* The list of documents that we want to search from.
* The query that will be used to search the documents.

Right now, we are doing the former. We call the Embed endpoint using `co.embed()` and pass the following arguments:

* `model`: Here we choose `embed-v4.0`
* `input_type`: We choose `search_document` to ensure the model treats these as the documents for search
* `texts`: The list of texts (the FAQs)
* `embedding_types`: We choose `float` to get the float embeddings.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
