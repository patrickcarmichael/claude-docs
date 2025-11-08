---
title: "Langgraph: Default error handling (enabled by default)"
description: "Default error handling (enabled by default) section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Default error handling (enabled by default)

tool_node = ToolNode([multiply])

message = AIMessage(
    content="",
    tool_calls=[{
        "name": "multiply",
        "args": {"a": 42, "b": 7},
        "id": "tool_call_id",
        "type": "tool_call"
    }]
)

result = tool_node.invoke({"messages": [message]})
```

Output:

```pycon
{'messages': [
    ToolMessage(
        content="Error: ValueError('The ultimate error')\n Please fix your mistakes.",
        name='multiply',
        tool_call_id='tool_call_id',
        status='error'
    )
]}
```

#### Disable error handling

To propagate exceptions directly, disable error handling:

```python
tool_node = ToolNode([multiply], handle_tool_errors=False)
```

With error handling disabled, exceptions raised by tools will propagate up, requiring explicit management.

#### Custom error messages

Provide a custom error message by setting the error handling parameter to a string:

```python
tool_node = ToolNode(
    [multiply],
    handle_tool_errors="Can't use 42 as the first operand, please switch operands!"
)
```

Example output:

```python
{'messages': [
    ToolMessage(
        content="Can't use 42 as the first operand, please switch operands!",
        name='multiply',
        tool_call_id='tool_call_id',
        status='error'
    )
]}
```

#### Error handling in agents

Error handling in prebuilt agents (`create_react_agent`) leverages `ToolNode`:

```python
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(
    model="anthropic:claude-3-7-sonnet-latest",
    tools=[multiply]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Advanced tool features](./142-advanced-tool-features.md)

**Next:** [Default error handling →](./144-default-error-handling.md)
