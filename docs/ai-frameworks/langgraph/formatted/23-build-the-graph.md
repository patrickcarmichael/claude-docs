---
title: "Langgraph: Build the graph"
description: "Build the graph section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Build the graph

builder = StateGraph(MessagesState)
builder.add_node("autogen", call_autogen_agent)
builder.add_edge(START, "autogen")

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create the graph with memory for persistence](./22-create-the-graph-with-memory-for-persistence.md)

**Next:** [Compile with checkpointer for persistence →](./24-compile-with-checkpointer-for-persistence.md)
