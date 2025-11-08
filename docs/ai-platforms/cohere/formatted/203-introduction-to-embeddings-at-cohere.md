---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Introduction to Embeddings at Cohere

> Embeddings transform text into numerical data, enabling language-agnostic similarity searches and efficient storage with compression.

<img src="file:7e36b26c-4bca-4a04-b751-977fb8ccd384" alt="embeddings." />

Embeddings are a way to represent the meaning of texts, images, or information as a list of numbers. Using a simple comparison function, we can then calculate a similarity score for two embeddings to figure out whether two pieces of information are about similar things. Common use-cases for embeddings include semantic search, clustering, and classification.

In the example below we use the `embed-v4.0` model to generate embeddings for 3 phrases and compare them using a similarity function. The two similar phrases have a high similarity score, and the embeddings for two unrelated phrases have a low similarity score:
```python PYTHON
import cohere
import numpy as np

co = cohere.ClientV2(api_key="YOUR_API_KEY")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
