---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool name: search_code_examples | Parameters: {"programming_language":"js","query":"..."}

```
```mdx
QUESTION:
Javascript tutorials on summarization
==================================================
TOOL PLAN:
I will search for Javascript tutorials on summarization. 

TOOL CALLS:
Tool name: search_code_examples_detailed | Parameters: {"query":"summarization","programming_language":"js"}
==================================================
RESPONSE:
I found one JavaScript tutorial on summarization:
- Build a Chrome extension to summarize web pages
==================================================
CITATIONS:

Start: 52| End:99| Text:'Build a Chrome extension to summarize web pages' 
Sources:
1. search_code_examples_detailed_mz15bkavd7r1:0
```
Let's now try a query that involves filtering based on the endpoints. Here, the user asks for "code examples of using embed and rerank endpoints".

And since we have set up the `endpoints` parameter to be an array, the agent is able to call the tool with a list of endpoints as its argument.
```python PYTHON
messages = run_agent(
    "Code examples of using embed and rerank endpoints."
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
