---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## What is a reranker?

A reranker is a specialized model that improves search relevancy by reassessing and reordering a set of retrieved documents based on their relevance to a given query. It takes a query and a set of text inputs (called 'documents'), and returns a relevancy score for each document relative to the given query. This process helps filter and prioritize the most pertinent information, enhancing the quality of search results.

In Retrieval Augmented Generation (RAG) pipelines, the reranking step sits between the initial retrieval step and the final generation phase. It acts as a quality filter, refining the selection of documents that will be used as context for language models. By ensuring that only the most relevant information is passed to the generation phase, rerankers play a crucial role in improving the accuracy of generated responses while potentially reducing processing costs.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
