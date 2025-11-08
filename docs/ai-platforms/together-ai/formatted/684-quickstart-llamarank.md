---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## QuickStart: LlamaRank

Source: https://docs.together.ai/docs/together-and-llamarank

Try out Salesforce's LlamaRank exclusively on Together's Rerank API

The Together AI platform makes it easy to run state-of-the-art models using only a few lines of code. [LlamaRank](https://blog.salesforceairesearch.com/llamarank/) is a proprietary reranker model developed by Salesforce AI Research that has been shown to outperform competitive reranker models like Cohere Rerank v3 and Mistral-7B QLM on accuracy.

Reranker models **improve search relevancy** by reassessing and reordering a set of retrieved documents based on their relevance to a given query. It takes a `query` and a set of text inputs (called `documents`), and returns a relevancy score for each document relative to the given query. In RAG pipelines, the reranking step sits between the initial retrieval step and the final generation phase, enhancing the quality of information fed into language models.

Try out Salesforce's LlamaRank *exclusively* on Together's serverless Rerank API endpoint. Together's Rerank API is **Cohere compatible**, making it easy to integrate into your existing applications.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
