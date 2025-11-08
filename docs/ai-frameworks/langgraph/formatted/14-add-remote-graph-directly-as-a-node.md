---
title: "Langgraph: add remote graph directly as a node"
description: "add remote graph directly as a node section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# add remote graph directly as a node

builder.add_node("child", remote_graph)
builder.add_edge(START, "child")
graph = builder.compile()

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← define parent graph](./13-define-parent-graph.md)

**Next:** [invoke the parent graph →](./15-invoke-the-parent-graph.md)
