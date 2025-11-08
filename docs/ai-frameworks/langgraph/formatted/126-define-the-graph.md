---
title: "Langgraph: Define the graph"
description: "Define the graph section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Define the graph


For this example we will use the [prebuilt ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/).

```python
from langchain_openai import ChatOpenAI
from typing import Literal
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setup](./125-setup.md)

**Next:** [First we initialize the model we want to use. →](./127-first-we-initialize-the-model-we-want-to-use.md)
