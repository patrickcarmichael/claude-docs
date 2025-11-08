---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool name: search_code_examples | Parameters: {"query":"RAG code examples"}

```
```mdx
QUESTION:
Do you have any RAG code examples
==================================================
TOOL PLAN:
I will search for RAG code examples. 

TOOL CALLS:
Tool name: search_code_examples_detailed | Parameters: {"query":"RAG"}
==================================================
RESPONSE:
I found one code example for RAG with Chat, Embed and Rerank via Pinecone.
==================================================
CITATIONS:

Start: 38| End:74| Text:'Chat, Embed and Rerank via Pinecone.' 
Sources:
1. search_code_examples_detailed_kqa6j5x92e3k:2
```
Let's try a more specific query about "javascript tutorials on text summarization".

This time, the agent uses the `programming_language` parameter and passed the value `js` to it.
```python PYTHON
messages = run_agent("Javascript tutorials on summarization")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
