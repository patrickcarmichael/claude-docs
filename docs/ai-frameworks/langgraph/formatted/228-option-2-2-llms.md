---
title: "Langgraph: Option 2: 2 LLMs"
description: "Option 2: 2 LLMs section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Option 2: 2 LLMs


Let's now dive into how we would use a second LLM to force structured output.

### Define Graph

We can now define our graph:

```python
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_core.messages import HumanMessage

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← We now add a conditional edge](./227-we-now-add-a-conditional-edge.md)

**Next:** [Define the function that calls the model →](./229-define-the-function-that-calls-the-model.md)
