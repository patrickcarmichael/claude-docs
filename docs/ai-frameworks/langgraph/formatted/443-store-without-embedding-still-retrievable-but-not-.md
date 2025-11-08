---
title: "Langgraph: Store without embedding (still retrievable, but not searchable)"
description: "Store without embedding (still retrievable, but not searchable) section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Store without embedding (still retrievable, but not searchable)

store.put(
    namespace_for_memory,
    str(uuid.uuid4()),
    {"system_info": "Last updated: 2024-01-01"},
    index=False
)
```

### Using in LangGraph

With this all in place, we use the `in_memory_store` in LangGraph. The `in_memory_store` works hand-in-hand with the checkpointer: the checkpointer saves state to threads, as discussed above, and the `in_memory_store` allows us to store arbitrary information for access _across_ threads. We compile the graph with both the checkpointer and the `in_memory_store` as follows.

```python
from langgraph.checkpoint.memory import InMemorySaver

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Store with specific fields to embed](./442-store-with-specific-fields-to-embed.md)

**Next:** [We need this because we want to enable threads (conversations) →](./444-we-need-this-because-we-want-to-enable-threads-con.md)
