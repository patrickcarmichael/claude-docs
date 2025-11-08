---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Query expansion

Let's ask the agent a few questions, starting with this one about the Chat endpoint and the RAG feature.

Firstly, the agent rightly chooses the `search_developer_docs` tool to retrieve the information it needs.

Additionally, because the question asks about two different things, retrieving information using the same query as the user's may not be the optimal approach. Instead, the query needs to be expanded or split into multiple parts, each retrieving its own set of documents.

Thus, the agent expands the original query into two queries.

This is enabled by the parallel tool calling feature that comes with the Chat endpoint.

This results in a richer and more representative list of documents retrieved, and therefore a more accurate and comprehensive answer.
```python PYTHON
messages = run_agent("Explain the Chat endpoint and the RAG feature")
```
```mdx

QUESTION:
Explain the Chat endpoint and the RAG feature
==================================================
TOOL PLAN:
I will search the Cohere developer documentation for the Chat endpoint and the RAG feature. 

TOOL CALLS:
Tool name: search_developer_docs | Parameters: {"query":"Chat endpoint"}
Tool name: search_developer_docs | Parameters: {"query":"RAG feature"}
==================================================
RESPONSE:
The Chat endpoint facilitates a conversational interface, allowing users to send messages to the model and receive text responses.

Retrieval Augmented Generation (RAG) is a method for generating text using additional information fetched from an external data source, which can greatly increase the accuracy of the response.
==================================================
CITATIONS:

Start: 18| End:56| Text:'facilitates a conversational interface' 
Sources:
1. search_developer_docs_c059cbhr042g:3
2. search_developer_docs_beycjq0ejbvx:3


Start: 58| End:130| Text:'allowing users to send messages to the model and receive text responses.' 
Sources:
1. search_developer_docs_c059cbhr042g:3
2. search_developer_docs_beycjq0ejbvx:3


Start: 132| End:162| Text:'Retrieval Augmented Generation' 
Sources:
1. search_developer_docs_c059cbhr042g:4
2. search_developer_docs_beycjq0ejbvx:4


Start: 174| End:266| Text:'method for generating text using additional information fetched from an external data source' 
Sources:
1. search_developer_docs_c059cbhr042g:4
2. search_developer_docs_beycjq0ejbvx:4


Start: 278| End:324| Text:'greatly increase the accuracy of the response.' 
Sources:
1. search_developer_docs_c059cbhr042g:4
2. search_developer_docs_beycjq0ejbvx:4
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
