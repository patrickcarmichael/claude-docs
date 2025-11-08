---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Routing Queries to Data Sources

> Build an agentic RAG system that routes queries to the most relevant tools based on the query's nature.

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/agentic-rag/agentic_rag_pt1_routing.ipynb">
  Open in Colab
</a>

Imagine a RAG system that can search over diverse sources, such as a website, a database, and a set of documents.

In a standard RAG setting, the application would aggregate retrieved documents from all the different sources it is connected to. This may contribute to noise from less relevant documents.

Additionally, it doesn’t take into consideration that, given a data source's nature, it might be less or more relevant to a query than the other data sources.

An agentic RAG system can solve this problem by routing queries to the most relevant tools based on the query's nature. This is done by leveraging the tool use capabilities of the Chat endpoint.

In this tutorial, we'll cover:

* Setting up the tools
* Running an agentic RAG workflow
* Routing queries to tools

We'll build an agent that can answer questions about using Cohere, equipped with a number of different tools.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
