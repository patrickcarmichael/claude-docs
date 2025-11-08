---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate Parallel Queries for Better RAG Retrieval

> Build an agentic RAG system that can expand a user query into a more optimized set of queries for retrieval.

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/agentic-rag/agentic_rag_pt2_parallel_queries.ipynb">
  Open in Colab
</a>

Compare two user queries to a RAG chatbot, "What was Apple's revenue in 2023?" and "What were Apple's and Google's revenue in 2023?".

The first query is straightforward as we can perform retrieval using pretty much the same query we get.

But the second query is more complex. We need to break it down into two separate queries, one for Apple and one for Google.

This is an example that requires query expansion. Here, the agentic RAG will need to transform the query into a more optimized set of queries it should use to perform the retrieval.

In this part, we'll learn how to create an agentic RAG system that can perform query expansion and then run those queries in parallel:

* Query expansion
* Query expansion over multiple data sources
* Query expansion in multi-turn conversations

We'll learn these by building an agent that answers questions about using Cohere.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
