---
title: "Langgraph: Thread-level persistence"
description: "Thread-level persistence section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Thread-level persistence


By default, the graph runs (i.e. `.invoke()` or `.stream()` invocations) are stateless - the checkpoints and the final state of the graph are not persisted. If you would like to persist the outputs of the graph run (for example, to enable human-in-the-loop features), you can create a thread and provide the thread ID via the `config` argument, same as you would with a regular compiled graph:

```python
from langgraph_sdk import get_sync_client
url = <DEPLOYMENT_URL>
graph_name = "agent"
sync_client = get_sync_client(url=url)
remote_graph = RemoteGraph(graph_name, url=url)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← stream outputs from the graph](./07-stream-outputs-from-the-graph.md)

**Next:** [create a thread (or use an existing thread instead) →](./09-create-a-thread-or-use-an-existing-thread-instead.md)
