---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Setting up the tools

In an agentic RAG system, each data source is represented as a tool. A tool is broadly any function or service that can receive and send objects to the LLM. But in the case of RAG, this becomes a more specific case of a tool that takes a query as input and returns a set of documents.

Here, we are defining a Python function for each tool, but more broadly, the tool can be any function or service that can receive and send objects.

* `search_developer_docs`: Searches Cohere developer documentation. Here we are creating a small list of sample documents for simplicity and will return the same list for every query. In practice, you will want to implement a search function such as those that use semantic search.
* `search_internet`: Performs an internet search using Tavily search, which we take from LangChain's ready implementation.
* `search_code_examples`: Searches for Cohere code examples and tutorials. Here we are also creating a small list of sample documents for simplicity.

These functions are mapped to a dictionary called `functions_map` for easy access.

Here, we are defining a Python function for each tool.

Further reading:

* [Documentation on parameter types in tool use](https://docs.cohere.com/v2/docs/parameter-types-in-tool-use)
```python PYTHON
functions_map = {
    "search_developer_docs": search_developer_docs,
    "search_internet": search_internet,
    "search_code_examples": search_code_examples,
}
```
The second and final setup step is to define the tool schemas in a format that can be passed to the Chat endpoint. A tool schema must contain the following fields: `name`, `description`, and `parameters` in the format shown below.

This schema informs the LLM about what the tool does, which enables an LLM to decide whether to use a particular tool. Therefore, the more descriptive and specific the schema, the more likely the LLM will make the right tool call decisions.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
