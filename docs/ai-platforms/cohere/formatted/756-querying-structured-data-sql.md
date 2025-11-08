---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Querying Structured Data (SQL)

> Build an agentic RAG system that can query structured data (SQL).

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/agentic-rag/agentic_rag_pt6_structured_data_SQL.ipynb">
  Open in Colab
</a>

In the previous tutorial, we explored how agentic RAG can handle complex queries on structured data in the form of tables using pandas. Now, we'll see how we can do the same for SQL databases.

Consider a scenario similar to the previous tutorial where we have evaluation results for an LLM application. However, instead of a CSV file, this data is now stored in a SQLite database. Users might still ask questions like "What's the average score for a specific use case?" or "Which configuration has the lowest latency?", but now we'll answer these using SQL queries instead of pandas operations.

In this tutorial, we'll cover:

* Setting up a SQLite database
* Creating a function to execute SQL queries
* Building an agent for querying SQL databases
* Running the agent with various types of queries

By implementing these techniques, we'll expand our agentic RAG system to handle structured data in SQL databases, complementing our previous work with tabular data in pandas.

Let's get started by setting up our environment and creating our SQLite database.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
