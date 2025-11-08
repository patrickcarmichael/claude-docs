---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool planning and calling

We can now run the tool use workflow. We can think of a tool use system as consisting of four components:

* The user
* The application
* The LLM
* The tools

At its most basic, these four components interact in a workflow through four steps:

* **Step 1: Get user message** – The LLM gets the user message (via the application)
* **Step 2: Tool planning and calling** – The LLM makes a decision on the tools to call (if any) and generates - the tool calls
* **Step 3: Tool execution** - The application executes the tools and the results are sent to the LLM
* **Step 4: Response and citation generation** – The LLM generates the response and citations to back to the user
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
