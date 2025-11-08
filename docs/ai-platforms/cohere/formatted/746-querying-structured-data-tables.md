---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Querying Structured Data (Tables)

> Build an agentic RAG system that can query structured data (tables).

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/agentic-rag/agentic_rag_pt5_structured_data_tables.ipynb">
  Open in Colab
</a>

In the previous tutorials, we explored how to build agentic RAG applications over unstructured and semi-structured data. In this tutorial and the next, we'll turn our focus to structured data.

This tutorial focuses on querying tables, and the next tutorial will be about querying SQL databases.

Consider a scenario where you have a CSV file containing evaluation results for an LLM application.

A user might ask questions like "What's the average score for a specific use case?" or "Which configuration has the lowest latency?". These queries require not just retrieval, but also data analysis and interpretation.

In this tutorial, we'll cover:

* Creating a function to execute Python code
* Setting up a tool to interact with tabular data
* Building an agent for querying tabular data
* Running the agent

Let's get started by setting up our environment and defining the necessary tools for our agent.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
