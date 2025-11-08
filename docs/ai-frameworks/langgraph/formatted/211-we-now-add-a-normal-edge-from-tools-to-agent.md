---
title: "Langgraph: We now add a normal edge from `tools` to `agent`."
description: "We now add a normal edge from `tools` to `agent`. section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# We now add a normal edge from `tools` to `agent`.

# This means that after `tools` is called, `agent` node is called next.
workflow.add_edge("tools", "agent")

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← We now add a conditional edge](./210-we-now-add-a-conditional-edge.md)

**Next:** [Now we can compile and visualize our graph →](./212-now-we-can-compile-and-visualize-our-graph.md)
