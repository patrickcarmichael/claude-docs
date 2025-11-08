---
title: "Langgraph: Shared state schemas"
description: "Shared state schemas section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Shared state schemas


A common case is for the parent graph and subgraph to communicate over a shared state key (channel) in the [schema](../concepts/low_level.md#state). For example, in [multi-agent](../concepts/multi_agent.md) systems, the agents often communicate over a shared [messages](https://langchain-ai.github.io/langgraph/concepts/low_level.md#why-use-messages) key.

If your subgraph shares state keys with the parent graph, you can follow these steps to add it to your graph:

1. Define the subgraph workflow (`subgraph_builder` in the example below) and compile it
2. Pass compiled subgraph to the `.add_node` method when defining the parent graph workflow

```python
from typing_extensions import TypedDict
from langgraph.graph.state import StateGraph, START

class State(TypedDict):
    foo: str

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setup](./101-setup.md)

**Next:** [Subgraph →](./103-subgraph.md)
