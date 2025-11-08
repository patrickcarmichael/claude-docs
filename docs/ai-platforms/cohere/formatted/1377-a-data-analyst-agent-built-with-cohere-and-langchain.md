---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## A Data Analyst Agent Built with Cohere and Langchain

> This page describes how to build a data-analysis system out of Cohere's models.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/agents/Data_Analyst_Agent_Cohere_and_Langchain.ipynb" />

Tool use is a method which allows developers to connect Cohere's Command models to external tools like search engines, APIs, databases, and other software tools. Just like how [Retrieval-Augmented Generation (RAG)](https://docs.cohere.com/docs/retrieval-augmented-generation-rag) allows a model to use an external data source to improve factual generation, tool use is a capability that allows retrieving data from multiple sources. But it goes beyond simply retrieving information and is able to use software tools to execute code, or even create entries in a CRM system.

In this notebook, we'll see how we can use two tools to create a simple data analyst agent that is able to search the web and run code in a python interpreter. This agent uses Cohere's Command R+ mode and Langchain.

<img alt="" src="https://raw.githubusercontent.com/cohere-ai/cohere-developer-experience/main/notebooks/images/tool-use-notebook-header.png" />

Let's start by installing the required libraries
```python PYTHON
! pip install --quiet langchain langchain_cohere langchain_experimental
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
