---
title: "Langgraph: Different state schemas"
description: "Different state schemas section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Different state schemas


For more complex systems you might want to define subgraphs that have a **completely different schema** from the parent graph (no shared keys). For example, you might want to keep a private message history for each of the agents in a [multi-agent](../concepts/multi_agent.md) system.

If that's the case for your application, you need to define a node **function that invokes the subgraph**. This function needs to transform the input (parent) state to the subgraph state before invoking the subgraph, and transform the results back to the parent state before returning the state update from the node.

```python
from typing_extensions import TypedDict
from langgraph.graph.state import StateGraph, START

class SubgraphState(TypedDict):
    bar: str

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Parent graph](./104-parent-graph.md)

**Next:** [Subgraph →](./106-subgraph.md)
