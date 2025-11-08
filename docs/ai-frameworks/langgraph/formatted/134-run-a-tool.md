---
title: "Langgraph: Run a tool"
description: "Run a tool section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Run a tool


Tools conform to the [Runnable interface](https://python.langchain.com/docs/concepts/runnables/), which means you can run a tool using the `invoke` method:

```python
multiply.invoke({"a": 6, "b": 7})  # returns 42
```

If the tool is invoked with `type="tool_call"`, it will return a [ToolMessage](https://python.langchain.com/docs/concepts/messages/#toolmessage):

```python
tool_call = {
    "type": "tool_call",
    "id": "1",
    "args": {"a": 42, "b": 7}
}
multiply.invoke(tool_call) # returns a ToolMessage object
```

Output:

```pycon
ToolMessage(content='294', name='multiply', tool_call_id='1')
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define a tool](./133-define-a-tool.md)

**Next:** [Use in an agent →](./135-use-in-an-agent.md)
