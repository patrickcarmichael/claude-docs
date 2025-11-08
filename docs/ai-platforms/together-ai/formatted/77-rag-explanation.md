---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## RAG Explanation

RAG operates by preprocessing a large knowledge base and dynamically retrieving relevant information at runtime.

Here's a breakdown of the process:

1. Indexing the Knowledge Base: The corpus (collection of documents) is divided into smaller, manageable chunks of text. Each chunk is converted into a vector embedding using an embedding model. These embeddings are stored in a vector database optimized for similarity searches.
2. Query Processing and Retrieval: When a user submits a prompt that would initially go directly to a LLM we process that and extract a query, the system searches the vector database for chunks semantically similar to the query. The most relevant chunks are retrieved and injected into the prompt sent to the generative AI model.
3. Response Generation: The AI model then uses the retrieved information along with its pre-trained knowledge to generate a response. Not only does this reduce the likelihood of hallucination since relevant context is provided directly in the prompt but it also allows us to cite to source material as well.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/10.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=eecff2928f79a8d1755393a5cd4abbc6" alt="" data-og-width="2588" width="2588" data-og-height="750" height="750" data-path="images/guides/10.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/10.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=8752a2afc44dd36a3ef1c70c82ed15e3 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/10.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e085396196bbb128e594cab1074af25c 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/10.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=1409177f8230d0fa49955c2fd2ade227 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/10.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=2c280a938e44a874ccebb79932bdb730 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/10.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ffdb075d3bb62725ab5632dfa9d851e9 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/10.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=59a6b6c2aa7d191fc7ccee1c968afb29 2500w" />
</Frame>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
