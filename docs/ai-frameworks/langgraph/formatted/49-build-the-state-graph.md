---
title: "Langgraph: Build the state graph"
description: "Build the state graph section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Build the state graph

builder = StateGraph(OverallState)
builder.add_node(node)  # node_1 is the first node
builder.add_edge(START, "node")  # Start the graph with node_1
builder.add_edge("node", END)  # End the graph after node_1
graph = builder.compile()

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← The overall state of the graph (this is the public state shared across nodes)](./48-the-overall-state-of-the-graph-this-is-the-public-.md)

**Next:** [Test the graph with a valid input →](./50-test-the-graph-with-a-valid-input.md)
