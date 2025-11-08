---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Uncomment if you need to install the following packages
##!pip install --quiet langchain langchain_cohere langchain_experimental --upgrade
```
Langchain already has a SQLDBToolkit that consists of 4 tools to handle SQL query generation, execution and validation. To use this, you simply need to define your LLM and DB and pass these into the Toolkit.

These are the following tools:

* 'sql\_db\_query': executes SQL code on the database
* 'sql\_db\_schema': returns the schema of tables given the list of tables
* 'sql\_db\_list\_tables': lists the tables in the database
* 'sql\_db\_query\_checker': validates the SQL query
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
