---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Single-Step Tool Use

In order to utilize single-step mode, you have to set `force_single_step=True`. Here's an example of using it to answer a few questions:
```python PYTHON
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
