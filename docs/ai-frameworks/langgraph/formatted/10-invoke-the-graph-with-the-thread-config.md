---
title: "Langgraph: invoke the graph with the thread config"
description: "invoke the graph with the thread config section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# invoke the graph with the thread config

config = {"configurable": {"thread_id": thread["thread_id"]}}
result = remote_graph.invoke({
    "messages": [{"role": "user", "content": "what's the weather in sf"}]
}, config=config)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← create a thread (or use an existing thread instead)](./09-create-a-thread-or-use-an-existing-thread-instead.md)

**Next:** [verify that the state was persisted to the thread →](./11-verify-that-the-state-was-persisted-to-the-thread.md)
