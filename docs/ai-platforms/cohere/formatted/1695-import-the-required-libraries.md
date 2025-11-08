---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Import the required libraries

First, let's import the necessary libraries for creating a SQL agent using Cohere and LangChain. These libraries enable natural language interaction with databases and provide tools for building AI-powered agents.
```python PYTHON
import os

os.environ["COHERE_API_KEY"] = "<cohere-api-key>"
```
```python PYTHON
! pip install langchain-core langchain-cohere langchain-community faiss-cpu -qq
```
```python PYTHON
from langchain_cohere import create_sql_agent
from langchain_cohere.chat_models import ChatCohere
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.vectorstores import FAISS
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_cohere import CohereEmbeddings
from datetime import datetime
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
