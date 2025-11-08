---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Rerank

The Rerank model can improve created models by re-organizing their results based on certain parameters. This can be used to improve search algorithms.

| Model Name                 | Description                                                                                                                                                                           | Modalities | Context Length | Endpoints                   |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | -------------- | --------------------------- |
| `rerank-v3.5`              | A model that allows for re-ranking English Language documents and semi-structured data (JSON). This model has a context length of 4096 tokens.                                        | Text       | 4k             | [Rerank](/reference/rerank) |
| `rerank-english-v3.0`      | A model that allows for re-ranking English Language documents and semi-structured data (JSON). This model has a context length of 4096 tokens.                                        | Text       | 4k             | [Rerank](/reference/rerank) |
| `rerank-multilingual-v3.0` | A model for documents and semi-structure data (JSON) that are not in English. Supports the same languages as embed-multilingual-v3.0. This model has a context length of 4096 tokens. | Text       | 4k             | [Rerank](/reference/rerank) |

### Using Rerank Models on Different Platforms

In this table, we provide some important context for using Cohere Rerank models on Amazon Bedrock, SageMaker, and more.

| Model Name                 | Amazon Bedrock Model ID | Amazon SageMaker      | Azure AI Foundry                | Oracle OCI Generative AI Service |
| :------------------------- | :---------------------- | :-------------------- | :------------------------------ | :------------------------------- |
| `rerank-v3.5`              | `cohere.rerank-v3-5:0`  | Unique per deployment | `Cohere-rerank-v3.5`            | `cohere.rerank.3-5`              |
| `rerank-english-v3.0`      | N/A                     | Unique per deployment | `Cohere-rerank-v3-english`      | N/A                              |
| `rerank-multilingual-v3.0` | N/A                     | Unique per deployment | `Cohere-rerank-v3-multilingual` | N/A                              |

<br />

>   **📝 Note**
>
> Rerank accepts full strings rather than tokens, so the token limit works a little differently. Rerank will automatically chunk documents longer than 510 tokens, and there is therefore no explicit limit to how long a document can be when using rerank. See our [best practice guide](/docs/reranking-best-practices) for more info about formatting documents for the Rerank endpoint.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
