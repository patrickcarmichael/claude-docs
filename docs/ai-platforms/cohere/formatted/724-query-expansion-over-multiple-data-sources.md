---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Query expansion over multiple data sources

The earlier example focused on a single data source, the Cohere developer documentation. However, the agentic RAG can also perform query expansion over multiple data sources.

Here, the agent is asked a question that contains two parts: first asking for an explanation of the Embed endpoint and then asking for code examples.

It correctly identifies that this requires both searching the developer documentation and the code examples. Thus, it generates two queries, one for each data source, and performs two separate searches in parallel.

Its response then contains information referenced from both data sources.
```python PYTHON
messages = run_agent(
    "What is the Embed endpoint? Give me some code tutorials"
)
```
```mdx

QUESTION:
What is the Embed endpoint? Give me some code tutorials
==================================================
TOOL PLAN:
I will search for 'what is the Embed endpoint' and 'Embed endpoint code tutorials' at the same time. 

TOOL CALLS:
Tool name: search_developer_docs | Parameters: {"query":"what is the Embed endpoint"}
Tool name: search_code_examples | Parameters: {"query":"Embed endpoint code tutorials"}
==================================================
RESPONSE:
The Embed endpoint returns text embeddings. An embedding is a list of floating point numbers that captures semantic information about the text that it represents.

I'm afraid I couldn't find any code tutorials for the Embed endpoint.
==================================================
CITATIONS:

Start: 19| End:43| Text:'returns text embeddings.' 
Sources:
1. search_developer_docs_pgzdgqd3k0sd:1


Start: 62| End:162| Text:'list of floating point numbers that captures semantic information about the text that it represents.' 
Sources:
1. search_developer_docs_pgzdgqd3k0sd:1
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
