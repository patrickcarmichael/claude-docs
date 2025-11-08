---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cohere Embed on LangChain (Integration Guide)

> This page describes how to work with Cohere's embeddings models and LangChain.

Cohere supports various integrations with LangChain, a large language model (LLM) framework which allows you to quickly create applications based on Cohere's models. This doc will guide you through how to leverage different Cohere embeddings with LangChain.

### Prerequisites

Running Cohere embeddings with LangChain doesn't require many prerequisites, consult the [top-level document](/docs/cohere-and-langchain) for more information.

### Cohere Embeddings with LangChain

To use [Cohere's Embeddings](/docs/embeddings) with LangChain, create a [CohereEmbedding](https://github.com/langchain-ai/langchain-community/blob/main/libs/community/langchain_community/embeddings/cohere.py) object as follows (the available cohere embedding models [are listed here](/reference/embed)):
```python PYTHON
from langchain_cohere import CohereEmbeddings

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
