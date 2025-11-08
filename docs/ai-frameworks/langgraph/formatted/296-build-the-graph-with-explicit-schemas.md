---
title: "Langgraph: Build the graph with explicit schemas"
description: "Build the graph with explicit schemas section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Build the graph with explicit schemas

builder = StateGraph(OverallState, input_schema=InputState, output_schema=OutputState)
builder.add_node(answer_node)
builder.add_edge(START, "answer_node")
builder.add_edge("answer_node", END)
graph = builder.compile()

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define the processing node](./295-define-the-processing-node.md)

**Next:** [Run the graph →](./297-run-the-graph.md)
