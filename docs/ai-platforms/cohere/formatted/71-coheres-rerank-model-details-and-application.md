---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cohere's Rerank Model (Details and Application)

> This page describes how Cohere's Rerank models work and how to use them.

Rerank models sort text inputs by semantic relevance to a specified query. They are often used to sort search results  returned from an existing search solution. Learn more about using Rerank in the [best practices guide](/docs/reranking-best-practices).

| Latest Model               | Description                                                                                                                                                                                                                      | Modality | Endpoints                   |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------------------------- |
| `rerank-v3.5`              | A model for documents and semi-structured data (JSON). State-of-the-art performance in English and non-English languages; supports the same languages as embed-multilingual-v3.0. This model has a context length of 4096 tokens | Text     | [Rerank](/reference/rerank) |
| `rerank-english-v3.0`      | A model that allows for re-ranking English Language documents and semi-structured data (JSON). This model has a context length of 4096 tokens.                                                                                   | Text     | [Rerank](/reference/rerank) |
| `rerank-multilingual-v3.0` | A model for documents and semi-structure data (JSON) that are not in English. Supports the same languages as `embed-multilingual-v3.0`. This model has a context length of 4096 tokens.                                          | Text     | [Rerank](/reference/rerank) |

>   **📝 Note**
>
> For each document included in a request, Rerank combines the tokens from the query with the tokens from the document and the combined total counts toward the context limit for a single document. If the combined number of tokens from the query and a given document exceeds the model’s context length for a single document, the document will automatically get chunked and processed in multiple inferences. See our [best practice guide](/docs/reranking-best-practices) for more info about formatting documents for the Rerank endpoint.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
