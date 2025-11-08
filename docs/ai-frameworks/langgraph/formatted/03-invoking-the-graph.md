---
title: "Langgraph: Invoking the graph"
description: "Invoking the graph section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Invoking the graph


Since `RemoteGraph` is a `Runnable` that implements the same methods as `CompiledGraph`, you can interact with it the same way you normally would with a compiled graph, i.e. by calling `.invoke()`, `.stream()`, `.get_state()`, `.update_state()`, etc (as well as their async counterparts).

### Asynchronously

!!! Note

    To use the graph asynchronously, you must provide either the `url` or `client` when initializing the `RemoteGraph`.

```python

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initializing the graph](./02-initializing-the-graph.md)

**Next:** [invoke the graph →](./04-invoke-the-graph.md)
