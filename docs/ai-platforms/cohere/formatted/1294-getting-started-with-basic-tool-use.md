---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting Started with Basic Tool Use

> This page describes how to work with Cohere's basic tool use functionality.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/agents/Vanilla_Tool_Use.ipynb" />

Tool use allows customers to **connect their large language models to external tools, such as search engines, APIs, functions, and databases**.

This allows the customer to unlock a richer set of model behaviors by, for instance, leveraging data stored in tools, taking actions through APIs, interacting with a vector database, or querying a search engine.

Below, we illustrate tool use in four steps:

* Step 1: the user configures the request to the model
* Step 2: the model uses context to **determine which tool(s) to use and how**
* Step 3: the tool calls are executed
* Step 4: the model **generates a final answer with precise citations** based on the tool results
```python PYTHON
import cohere, json
API_KEY = "..." # fill in your Cohere API key here

co = cohere.Client(API_KEY)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
