---
title: "Langgraph: Add persistence"
description: "Add persistence section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Add persistence


You only need to **provide the checkpointer when compiling the parent graph**. LangGraph will automatically propagate the checkpointer to the child subgraphs.

```python
from langgraph.graph import START, StateGraph
from langgraph.checkpoint.memory import MemorySaver
from typing_extensions import TypedDict

class State(TypedDict):
    foo: str

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Parent graph](./107-parent-graph.md)

**Next:** [Subgraph →](./109-subgraph.md)
