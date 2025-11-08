---
title: "Langgraph: Parent graph"
description: "Parent graph section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Parent graph


builder = StateGraph(State)
builder.add_node("node_1", subgraph)
builder.add_edge(START, "node_1")

checkpointer = MemorySaver()
graph = builder.compile(checkpointer=checkpointer)
```    

If you want the subgraph to **have its own memory**, you can compile it with the appropriate checkpointer option. This is useful in [multi-agent](../concepts/multi_agent.md) systems, if you want agents to keep track of their internal message histories:

```python
subgraph_builder = StateGraph(...)
subgraph = subgraph_builder.compile(checkpointer=True)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Subgraph](./109-subgraph.md)

**Next:** [View subgraph state →](./111-view-subgraph-state.md)
