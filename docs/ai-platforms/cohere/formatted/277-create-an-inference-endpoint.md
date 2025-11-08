---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create an inference endpoint

One of the biggest pain points of building a vector search index is computing embeddings for a large corpus of data. Fortunately Elastic offers inference endpoints that can be used in ingest pipelines to automatically compute embeddings when bulk indexing operations are performed.

To set up an inference pipeline for ingestion we first must create an inference endpoint that uses Cohere embeddings. You'll need a Cohere API key for this that you can find in your Cohere account under the [API keys section](https://dashboard.cohere.com/api-keys).

We will create an inference endpoint that uses `embed-v4.0` and `int8` or `byte` compression to save on storage.
```python PYTHON
COHERE_API_KEY = getpass("Enter Cohere API key:  ")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
