---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Changing embedding compression types

Semantic search over large datasets can require a lot of memory, which is expensive to host in a vector database. Changing the embeddings compression type can help reduce the memory footprint.

A typical embedding model generates embeddings as float32 format (consuming 4 bytes). By compressing the embeddings to int8 format (1 byte), we can reduce the memory 4x while keeping 99.99% of the original search quality.

We can go even further and use the binary format (1 bit), which reduces the needed memory 32x while keeping 90-98% of the original search quality.

The Embed endpoint supports the following formats: `float`, `int8`, `unint8`, `binary`, and `ubinary`. You can get these different compression levels by passing the `embedding_types` parameter.

In the example below, we embed the documents in two formats: `float` and `int8`.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
