---
title: "Langgraph: Create a sequence of steps"
description: "Create a sequence of steps section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Create a sequence of steps


!!! info "Prerequisites"

    This guide assumes familiarity with the above section on [state](#define-and-update-state).

Here we demonstrate how to construct a simple sequence of steps. We will show:

1. How to build a sequential graph
2. Built-in short-hand for constructing similar graphs.

To add a sequence of nodes, we use the `.add_node` and `.add_edge` methods of our [graph](../concepts/low_level.md#stategraph):

```python
from langgraph.graph import START, StateGraph

builder = StateGraph(State)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Add node caching](./56-add-node-caching.md)

**Next:** [Add nodes →](./58-add-nodes.md)
