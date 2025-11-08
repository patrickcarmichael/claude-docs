---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Setting up a tool to interact with the database

Next, we'll create a tool that will allow the agent to interact with the SQLite database containing our evaluation results.
```python PYTHON
sql_table_query_tool = {
    "type": "function",
    "function": {
        "name": "sql_table_query",
        "description": "Execute an SQL query on the evaluation_results table in the SQLite database. The table has columns 'usecase', 'run', 'score', 'temperature', 'tokens', and 'latency'.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "SQL query to execute on the evaluation_results table",
                }
            },
            "required": ["query"],
        },
    },
}

tools = [sql_table_query_tool]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
