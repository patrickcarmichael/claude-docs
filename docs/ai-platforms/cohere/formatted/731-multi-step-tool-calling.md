---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Multi-step tool calling

Let's ask the agent a few questions, starting with this one about a specific feature. The user is asking about two things: a feature to reorder search results and code examples for that feature.

In this case, the agent first needs to identify what that feature is before it can answer the second part of the question.

This is reflected in the agent's tool plan, which describes the steps it will take to answer the question.

So, it first calls the `search_developer_docs` tool to find the feature.

It then discovers that the feature is Rerank. Using this information, it calls the `search_code_examples` tool to find code examples for that feature.

Finally, it uses the retrieved information to answer both parts of the user's question.
```python PYTHON
messages = run_agent(
    "What's the Cohere feature to reorder search results? Do you have any code examples on that?"
)
```
```mdx
QUESTION:
What's the Cohere feature to reorder search results? Do you have any code examples on that?
==================================================
TOOL PLAN:
I will search for the Cohere feature to reorder search results. Then I will search for code examples on that. 

TOOL CALLS:
Tool name: search_developer_docs | Parameters: {"query":"reorder search results"}
==================================================
TOOL PLAN:
I found that the Rerank endpoint is the feature that reorders search results. I will now search for code examples on that. 

TOOL CALLS:
Tool name: search_code_examples | Parameters: {"query":"rerank endpoint"}
==================================================
RESPONSE:
The Rerank endpoint is the feature that reorders search results. Unfortunately, I could not find any code examples on that.
==================================================
CITATIONS:

Start: 4| End:19| Text:'Rerank endpoint' 
Sources:
1. search_developer_docs_53tfk9zgwgzt:0
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
