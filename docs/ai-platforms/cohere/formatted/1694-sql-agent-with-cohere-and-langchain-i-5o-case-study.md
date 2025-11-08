---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## SQL Agent with Cohere and LangChain (i-5O Case Study)

> This page contains a tutorial on how to build a SQL agent with Cohere and LangChain in the manufacturing industry.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/agents/i-5O-sql-agent/sql_agent_demo.ipynb" />

This tutorial demonstrates how to create a SQL agent using Cohere and LangChain. The agent can translate natural language queries coming from users into SQL, and execute them against a database. This powerful combination allows for intuitive interaction with databases without requiring direct SQL knowledge.

Key topics covered:

1. Setting up the necessary libraries and environment
2. Connecting to a SQLite database
3. Configuring the LangChain SQL Toolkit
4. Creating a custom prompt template with few-shot examples
5. Building and running the SQL agent
6. Adding memory to the agent to keep track of historical messages

By the end of this tutorial, you'll have a functional SQL agent that can answer questions about your data using natural language.

This tutorial uses a mocked up data of a manufacturing environment where a product item's production is tracked across multiple stations, allowing for analysis of production efficiency, station performance, and individual item progress through the manufacturing process. This is modelled after a real customer use case.

The database contains two tables:

* The `product_tracking` table records the movement of items through different zones in manufacturing stations, including start and end times, station names, and product IDs.
* The `status` table logs the operational status of stations, including timestamps, station names, and whether they are productive or in downtime.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
