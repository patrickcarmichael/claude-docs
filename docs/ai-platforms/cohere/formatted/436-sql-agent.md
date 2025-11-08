---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## SQL Agent

LangChain's SQL Agent abstraction provides a flexible way of interacting with SQL Databases. This can be accessed via the `create_sql_agent` constructor.
```python PYTHON
from langchain_cohere import ChatCohere, create_sql_agent
from langchain_community.utilities import SQLDatabase
import urllib.request
import pandas as pd
import sqlite3

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
