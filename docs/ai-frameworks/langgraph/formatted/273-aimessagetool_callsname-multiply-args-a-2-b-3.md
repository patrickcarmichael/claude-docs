---
title: "Langgraph: -> AIMessage(tool_calls=[{'name': 'multiply', 'args': {'a': 2, 'b': 3}, ...}])"
description: "-> AIMessage(tool_calls=[{'name': 'multiply', 'args': {'a': 2, 'b': 3}, ...}]) section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# -> AIMessage(tool_calls=[{'name': 'multiply', 'args': {'a': 2, 'b': 3}, ...}])

```

```
AIMessage(
  tool_calls=[
    ToolCall(name="multiply", args={"a": 2, "b": 3}),
    ...
  ]
)
```

If the input is unrelated to any tool, the model returns only a natural language message:

```python
llm_with_tools.invoke("Hello world!")  # -> AIMessage(content="Hello!")
```

Importantly, the model does not execute the tool—it only generates a request. A separate executor (such as a runtime or agent) is responsible for handling the tool call and returning the result.

See the [tool calling guide](../how-tos/tool-calling.md) for more details.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Tool calling](./272-tool-calling.md)

**Next:** [Prebuilt tools →](./274-prebuilt-tools.md)
