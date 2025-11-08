---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Rerank models

Our [Rerank API](/docs/rerank-overview) has built-in support for the following models, that we host via our serverless endpoints.

| Organization | Model Name   | Model Size | Model String for API                | Max Doc Size (tokens) | Max Docs |
| ------------ | ------------ | :--------- | ----------------------------------- | --------------------- | -------- |
| Salesforce   | LlamaRank    | 8B         | Salesforce/Llama-Rank-v1            | 8192                  | 1024     |
| MixedBread   | Rerank Large | 1.6B       | mixedbread-ai/Mxbai-Rerank-Large-V2 | 32768                 | -        |

**Rerank Model Examples**

* [Search and Reranking](https://github.com/togethercomputer/together-cookbook/blob/main/Search_with_Reranking.ipynb) - Simple semantic search pipeline improved using a reranker
* [Implementing Hybrid Search Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Open_Contextual_RAG.ipynb) - Implementing semantic + lexical search along with reranking

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
