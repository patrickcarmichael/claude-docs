---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## LangGraph

*LangGraph is an OSS library for building stateful, multi-actor applications with LLMs*

Install `langgraph`
```bash
pip install -U langgraph langchain-together
export TOGETHER_API_KEY=***
```

Build a tool-using agent:
```python
import os
from langchain_together import ChatTogether

llm = ChatTogether(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    api_key=os.getenv("TOGETHER_API_KEY"),
)


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
