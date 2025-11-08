---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How To Implement Contextual RAG From Anthropic

Source: https://docs.together.ai/docs/how-to-implement-contextual-rag-from-anthropic

An open source line-by-line implementation and explanation of Contextual RAG from Anthropic!

[Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) is a chunk augmentation technique that uses an LLM to enhance each chunk.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/11.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c95e14ec01de84f03a0982ea44d565c4" alt="" data-og-width="3840" width="3840" data-og-height="2160" height="2160" data-path="images/guides/11.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/11.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d51f62f41d26706932895aa10cdb0fda 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/11.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a65bc40ec2d7e34403a2cbb20d0b9b30 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/11.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=12614a08d879bda5bb9bf6e7b681ecdc 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/11.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=46e51018c60daa77f9cab77c5f82e01b 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/11.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=89baff1add76974b4f68ed6eab4b2b6a 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/11.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=8f92575f98fa1614cfab7d5e336a5039 2500w" />
</Frame>

Here's an overview of how it works.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
