---
title: "Langgraph: Initializing the graph"
description: "Initializing the graph section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Initializing the graph


When initializing a `RemoteGraph`, you must always specify:

- `name`: the name of the graph you want to interact with. This is the same graph name you use in `langgraph.json` configuration file for your deployment.
- `api_key`: a valid LangSmith API key. Can be set as an environment variable (`LANGSMITH_API_KEY`) or passed directly via the `api_key` argument. The API key could also be provided via the `client` / `sync_client` arguments, if `LangGraphClient` / `SyncLangGraphClient` were initialized with `api_key` argument.

Additionally, you have to provide one of the following:

- `url`: URL of the deployment you want to interact with. If you pass `url` argument, both sync and async clients will be created using the provided URL, headers (if provided) and default configuration values (e.g. timeout, etc).
- `client`: a `LangGraphClient` instance for interacting with the deployment asynchronously (e.g. using `.astream()`, `.ainvoke()`, `.aget_state()`, `.aupdate_state()`, etc.)
- `sync_client`: a `SyncLangGraphClient` instance for interacting with the deployment synchronously (e.g. using `.stream()`, `.invoke()`, `.get_state()`, `.update_state()`, etc.)

!!! Note

    If you pass both `client` or `sync_client` as well as `url` argument, they will take precedence over the `url` argument. If none of the `client` / `sync_client` / `url` arguments are provided, `RemoteGraph` will raise a `ValueError` at runtime.

### Using URL

```python
from langgraph.pregel.remote import RemoteGraph

url = <DEPLOYMENT_URL>
graph_name = "agent"
remote_graph = RemoteGraph(graph_name, url=url)
```

### Using clients

```python
from langgraph_sdk import get_client, get_sync_client
from langgraph.pregel.remote import RemoteGraph

url = <DEPLOYMENT_URL>
graph_name = "agent"
client = get_client(url=url)
sync_client = get_sync_client(url=url)
remote_graph = RemoteGraph(graph_name, client=client, sync_client=sync_client)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← How to interact with the deployment using RemoteGraph](./01-how-to-interact-with-the-deployment-using-remotegr.md)

**Next:** [Invoking the graph →](./03-invoking-the-graph.md)
