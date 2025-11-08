---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Contextual RAG:

1. For every chunk - prepend an explanatory context snippet that situates the chunk within the rest of the document. -> Get a small cost effective LLM to do this.
2. Hybrid Search: Embed the chunk using both sparse (keyword) and dense(semantic) embeddings.
3. Perform rank fusion using an algorithm like Reciprocal Rank Fusion(RRF).
4. Retrieve top 150 chunks and pass those to a Reranker to obtain top 20 chunks.
5. Pass top 20 chunks to LLM to generate an answer.

Below we implement each step in this process using Open Source models.

To breakdown the concept further we break down the process into a one-time indexing step and a query time step.

**Data Ingestion Phase:**

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/12.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=3d2da83adbb003deca81154f23d11867" alt="" data-og-width="1675" width="1675" data-og-height="1281" height="1281" data-path="images/guides/12.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/12.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c93703cef1766f91b2b0f18d21801fc1 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/12.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=fa9055a5d5e2c501f1acb90f0d5e5a29 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/12.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5a95544a4bf3e27faf78e917aad90379 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/12.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ff0025c3cef507c5a91454390d32a912 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/12.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=cc5f81ec127b0c7d0134c998e47bd6da 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/12.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=2dbd7ecadba466e4f214f22712111715 2500w" />
</Frame>

1. Data processing and chunking
2. Context generation using a quantized Llama 3.2 3B Model
3. Vector Embedding and Index Generation
4. BM25 Keyword Index Generation

**At Query Time:**

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/13.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d7d2540ce149d7d9a6ea84b568d4512d" alt="" data-og-width="1804" width="1804" data-og-height="385" height="385" data-path="images/guides/13.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/13.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=9895e8a1bfd611578457bcba5bc80d05 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/13.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=88d16d6f5bd7a549b407678efdfb779f 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/13.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=623b991278e23b3750a66664c40b7f34 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/13.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=48f97337f20fca38533c26d04af71678 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/13.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=6eb0f97d48de8dbec8597d7ec5f12800 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/13.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=edb78219ad34e6dc86f5cddb68a2c77d 2500w" />
</Frame>

1. Perform retrieval using both indices and combine them using RRF
2. Reranker to improve retrieval quality
3. Generation with Llama3.1 405B

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
