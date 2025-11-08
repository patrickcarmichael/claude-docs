---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Setup

To get started, first we need to install the `cohere` library and create a Cohere client.

We also need to import the tool definitions that we'll use in this tutorial.

>   **📝 Note**
>
> Important: the source code for tool definitions can be 

  [found here](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/agentic-rag/tool_def.py)

  . Make sure to have the 

  `tool_def.py`

   file in the same directory as this notebook for the imports to work correctly.
```python PYTHON
! pip install cohere langchain langchain-community pydantic -qq
```
```python PYTHON
import json
import os
import cohere

from tool_def import (
    search_developer_docs,
    search_developer_docs_tool,
    search_internet,
    search_internet_tool,
    search_code_examples,
    search_code_examples_tool,
)

co = cohere.ClientV2(
    "COHERE_API_KEY"
)  # Get your free API key: https://dashboard.cohere.com/api-keys

os.environ["TAVILY_API_KEY"] = (
    "TAVILY_API_KEY"  # We'll need the Tavily API key to perform internet search. Get your API key: https://app.tavily.com/home

)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
