---
title: "Langgraph: Build a multi-agent system"
description: "Build a multi-agent system section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Build a multi-agent system


You can use handoffs in any agents built with LangGraph. We recommend using the prebuilt [agent](../agents/overview.md) or [`ToolNode`](./tool-calling.md#toolnode), as they natively support handoffs tools returning `Command`. Below is an example of how you can implement a multi-agent system for booking travel using handoffs:

```python hl_lines="16 17 21 22 28 29"
from langgraph.prebuilt import create_react_agent
from langgraph.graph import StateGraph, START, MessagesState

def create_handoff_tool(*, agent_name: str, description: str | None = None):
    # same implementation as above
    ...
    return Command(...)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Handoffs](./114-handoffs.md)

**Next:** [Handoffs →](./116-handoffs.md)
