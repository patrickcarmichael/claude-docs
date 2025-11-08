---
title: "Langgraph: Subgraph"
description: "Subgraph section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Subgraph


def subgraph_node_1(state: State):
    return {"foo": "hi! " + state["foo"]}

subgraph_builder = StateGraph(State)
subgraph_builder.add_node(subgraph_node_1)
subgraph_builder.add_edge(START, "subgraph_node_1")
subgraph = subgraph_builder.compile()

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Shared state schemas](./102-shared-state-schemas.md)

**Next:** [Parent graph →](./104-parent-graph.md)
