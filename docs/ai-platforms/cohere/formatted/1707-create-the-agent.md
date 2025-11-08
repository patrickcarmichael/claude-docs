---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create the agent

Next, we create an instance of the SQL agent using the LangChain framework, specifically using `create_sql_agent`.

This agent will be capable of interpreting natural language queries, converting them into SQL queries, and executing them against our database. The agent uses the LLM we defined earlier, along with the SQL toolkit and the custom prompt we created.
```python PYTHON
agent = create_sql_agent(
   llm=llm,
   toolkit=toolkit,
   prompt=full_prompt,
   verbose=True
)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
