---
title: "Langgraph: Python sync vs. async"
description: "Python sync vs. async section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Python sync vs. async


The Python SDK provides both synchronous (`get_sync_client`) and asynchronous (`get_client`) clients for interacting with LangGraph Server:

=== "Sync"

    ```python
    from langgraph_sdk import get_sync_client

    client = get_sync_client(url=..., api_key=...)
    client.assistants.search()
    ```

=== "Async"

    ```python
    from langgraph_sdk import get_client

    client = get_client(url=..., api_key=...)
    await client.assistants.search()
    ```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Installation](./328-installation.md)

**Next:** [Learn more →](./330-learn-more.md)
