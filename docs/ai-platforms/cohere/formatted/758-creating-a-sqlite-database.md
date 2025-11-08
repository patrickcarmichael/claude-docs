---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Creating a SQLite database

Next, we'll create a SQLite database to store our evaluation results. SQLite is a lightweight, serverless database engine that's perfect for small to medium-sized applications. Here's what we're going to do:

1. Create a new SQLite database file named `evaluation_results.db`.
2. Create a table called `evaluation_results` with columns for `usecase`, `run`, `score`, `temperature`, `tokens`, and `latency`.
3. Insert sample data into the table to simulate our evaluation results.

>   **📝 Note**
>
> Important: the data can be 

  [found here](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/agentic-rag/evaluation_results.db)

  . Make sure to have the file in the same directory as this notebook for the imports to work correctly.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
