---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Running the agent

Let's start with a broad query about "RAG code examples".

Since it's broad, this query shouldn't require any metadata filtering.

And this is shown by the agent's response, which provides only one parameter, `query`, in its tool call.
```python PYTHON
messages = run_agent("Do you have any RAG code examples")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
