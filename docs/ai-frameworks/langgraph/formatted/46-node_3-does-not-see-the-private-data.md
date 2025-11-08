---
title: "Langgraph: node_3 does not see the private data."
description: "node_3 does not see the private data. section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# node_3 does not see the private data.

builder = StateGraph(OverallState).add_sequence([node_1, node_2, node_3])
builder.add_edge(START, "node_1")
graph = builder.compile()

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Connect nodes in a sequence](./45-connect-nodes-in-a-sequence.md)

**Next:** [Invoke the graph with the initial state →](./47-invoke-the-graph-with-the-initial-state.md)
