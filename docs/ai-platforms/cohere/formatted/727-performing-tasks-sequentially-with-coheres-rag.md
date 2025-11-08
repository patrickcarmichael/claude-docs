---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Performing Tasks Sequentially with Cohere's RAG

> Build an agentic RAG system that can handle user queries that require tasks to be performed in a sequence.

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/agentic-rag/agentic_rag_pt3_sequential.ipynb">
  Open in Colab
</a>

Compare two user queries to a RAG chatbot, "What was Apple's revenue in 2023?" and "What was the revenue of the most valuable company in the US in 2023?".

While the first query is straightforward to handle, the second query requires breaking down into two steps:

1. Identify the most valuable company in the US in 2023
2. Get the revenue of the company in 2023

These steps need to happen in a sequence rather than all at once. This is because the information retrieved from the first step is required to inform the second step.

This is an example of sequential reasoning. In this tutorial, we'll learn how agentic RAG with Cohere handles sequential reasoning, and in particular:

* Multi-step tool calling
* Multi-step, parallel tool calling
* Self-correction

We'll learn these by building an agent that answers questions about using Cohere.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
