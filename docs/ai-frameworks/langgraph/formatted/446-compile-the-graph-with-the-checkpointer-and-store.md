---
title: "Langgraph: Compile the graph with the checkpointer and store"
description: "Compile the graph with the checkpointer and store section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Compile the graph with the checkpointer and store

graph = graph.compile(checkpointer=checkpointer, store=in_memory_store)
```

We invoke the graph with a `thread_id`, as before, and also with a `user_id`, which we'll use to namespace our memories to this particular user as we showed above.

```python

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← ... Define the graph ...](./445-define-the-graph.md)

**Next:** [Invoke the graph →](./447-invoke-the-graph.md)
