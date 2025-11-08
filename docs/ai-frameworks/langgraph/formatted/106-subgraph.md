---
title: "Langgraph: Subgraph"
description: "Subgraph section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Subgraph


def subgraph_node_1(state: SubgraphState):
    return {"bar": "hi! " + state["bar"]}

subgraph_builder = StateGraph(SubgraphState)
subgraph_builder.add_node(subgraph_node_1)
subgraph_builder.add_edge(START, "subgraph_node_1")
subgraph = subgraph_builder.compile()

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Different state schemas](./105-different-state-schemas.md)

**Next:** [Parent graph →](./107-parent-graph.md)
