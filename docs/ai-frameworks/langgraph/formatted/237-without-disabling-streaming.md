---
title: "Langgraph: Without disabling streaming"
description: "Without disabling streaming section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Without disabling streaming


Now that we've defined our graph, let's try to call `astream_events` without disabling streaming. This should throw an error because the `o1` model does not support streaming natively:

```python
input = {"messages": {"role": "user", "content": "how many r's are in strawberry?"}}
try:
    async for event in graph.astream_events(input, version="v2"):
        if event["event"] == "on_chat_model_end":
            print(event["data"]["output"].content, end="", flush=True)
except:
    print("Streaming not supported!")
```
```output
Streaming not supported!
```
An error occurred as we expected, luckily there is an easy fix!

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← How to disable streaming for models that don't support it](./236-how-to-disable-streaming-for-models-that-dont-supp.md)

**Next:** [Disabling streaming →](./238-disabling-streaming.md)
