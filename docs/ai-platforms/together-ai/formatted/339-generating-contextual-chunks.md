---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generating Contextual Chunks

This part contains the main intuition behind `Contextual Retrieval`. We will make an LLM call for each chunk to add much needed relevant context to the chunk. In order to do this we pass in the ENTIRE document per LLM call.

It may seem that passing in the entire document per chunk and making an LLM call per chunk is quite inefficient, this is true and there very well might be more efficient techniques to accomplish the same end goal. But in keeping with implementing the current technique at hand lets do it.

Additionally using quantized small 1-3B models (here we will use Llama 3.2 3B) along with prompt caching does make this more feasible.

Prompt caching allows key and value matrices corresponding to the document to be cached for future LLM calls.

We will use the following prompt to generate context for each chunk:
```py

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
