---
title: "Langgraph: stream outputs from the graph"
description: "stream outputs from the graph section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# stream outputs from the graph

async for chunk in remote_graph.astream({
    "messages": [{"role": "user", "content": "what's the weather in la"}]
}):
    print(chunk)
```

### Synchronously

!!! Note

    To use the graph synchronously, you must provide either the `url` or `sync_client` when initializing the `RemoteGraph`.

```python

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← invoke the graph](./04-invoke-the-graph.md)

**Next:** [invoke the graph →](./06-invoke-the-graph.md)
