---
title: "Langgraph: Subgraph"
description: "Subgraph section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Subgraph


def subgraph_node_1(state: State):
    return {"foo": state["foo"] + "bar"}

subgraph_builder = StateGraph(State)
subgraph_builder.add_node(subgraph_node_1)
subgraph_builder.add_edge(START, "subgraph_node_1")
subgraph = subgraph_builder.compile()

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Add persistence](./108-add-persistence.md)

**Next:** [Parent graph →](./110-parent-graph.md)
