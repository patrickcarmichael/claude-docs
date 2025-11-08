---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool name: search_code_examples | Parameters: {"endpoints":["embed","rerank"],"query":"..."}

```
```mdx
QUESTION:
Code examples of using embed and rerank endpoints.
==================================================
TOOL PLAN:
I will search for code examples of using embed and rerank endpoints. 

TOOL CALLS:
Tool name: search_code_examples_detailed | Parameters: {"query":"code examples","endpoints":["embed","rerank"]}
==================================================
RESPONSE:
Here are some code examples of using the embed and rerank endpoints:
- Wikipedia Semantic Search with Cohere Embedding Archives
- RAG With Chat Embed and Rerank via Pinecone
- Build Chatbots That Know Your Business with MongoDB and Cohere
==================================================
CITATIONS:

Start: 71| End:127| Text:'Wikipedia Semantic Search with Cohere Embedding Archives' 
Sources:
1. search_code_examples_detailed_qjtk4xbt5g4n:0


Start: 130| End:173| Text:'RAG With Chat Embed and Rerank via Pinecone' 
Sources:
1. search_code_examples_detailed_qjtk4xbt5g4n:1


Start: 176| End:238| Text:'Build Chatbots That Know Your Business with MongoDB and Cohere' 
Sources:
1. search_code_examples_detailed_qjtk4xbt5g4n:2
```
Finally, let's try a query that involves filtering based on both the programming language and the endpoints. Here, the user asks for "Python examples of using the chat endpoint".

And the agent correctly uses both parameters to query the code examples.
```python PYTHON
messages = run_agent("Python examples of using the chat endpoint.")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
