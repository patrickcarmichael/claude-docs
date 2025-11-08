---
title: "Langgraph: Using as a subgraph"
description: "Using as a subgraph section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Using as a subgraph


!!! Note

    If you need to use a `checkpointer` with a graph that has a `RemoteGraph` subgraph node, make sure to use UUIDs as thread IDs.

Since the `RemoteGraph` behaves the same way as a regular `CompiledGraph`, it can be also used as a subgraph in another graph. For example:

```python
from langgraph_sdk import get_sync_client
from langgraph.graph import StateGraph, MessagesState, START
from typing import TypedDict

url = <DEPLOYMENT_URL>
graph_name = "agent"
remote_graph = RemoteGraph(graph_name, url=url)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← verify that the state was persisted to the thread](./11-verify-that-the-state-was-persisted-to-the-thread.md)

**Next:** [define parent graph →](./13-define-parent-graph.md)
