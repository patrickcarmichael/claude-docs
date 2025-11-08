---
title: "Langgraph: Advanced tool features"
description: "Advanced tool features section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Advanced tool features


### Immediate return

Use `return_direct=True` to immediately return a tool's result without executing additional logic.

This is useful for tools that should not trigger further processing or tool calls, allowing you to return results directly to the user.

```python hl_lines="1"
@tool(return_direct=True)
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```

??? example "Extended example: Using return_direct in a prebuilt agent"

    ```python hl_lines="4"
    from langchain_core.tools import tool
    from langgraph.prebuilt import create_react_agent

    @tool(return_direct=True)
    def add(a: int, b: int) -> int:
        """Add two numbers"""
        return a + b

    agent = create_react_agent(
        model="anthropic:claude-3-7-sonnet-latest",
        tools=[add]
    )

    agent.invoke(
        {"messages": [{"role": "user", "content": "what's 3 + 5?"}]}
    )
    ```

!!! important "Using without prebuilt components"

    If you are building a custom workflow and are not relying on `create_react_agent` or `ToolNode`, you will also
    need to implement the control flow to handle `return_direct=True`.

### Force tool use

If you need to force a specific tool to be used, you will need to configure this at the **model** level using the `tool_choice` parameter in the bind_tools method.

Force specific tool usage via tool_choice:

```python hl_lines="11"
@tool(return_direct=True)
def greet(user_name: str) -> int:
    """Greet user."""
    return f"Hello {user_name}!"

tools = [greet]

configured_model = model.bind_tools(
    tools,
    # Force the use of the 'greet' tool
    tool_choice={"type": "tool", "name": "greet"}
)
```

??? example "Extended example: Force tool usage in an agent"

    To force the agent to use specific tools, you can set the `tool_choice` option in `model.bind_tools()`:

    ```python hl_lines="3 11"
    from langchain_core.tools import tool

    @tool(return_direct=True)
    def greet(user_name: str) -> int:
        """Greet user."""
        return f"Hello {user_name}!"

    tools = [greet]

    agent = create_react_agent(
        model=model.bind_tools(tools, tool_choice={"type": "tool", "name": "greet"}),
        tools=tools
    )

    agent.invoke(
        {"messages": [{"role": "user", "content": "Hi, I am Bob"}]}
    )
    ```

!!! Warning "Avoid infinite loops"

    Forcing tool usage without stopping conditions can create infinite loops. Use one of the following safeguards:

    - Mark the tool with [`return_direct=True`](#immediate-return) to end the loop after execution.
    - Set [`recursion_limit`](../concepts/low_level.md#recursion-limit) to restrict the number of execution steps.

!!! tip "Tool choice configuration"

    The `tool_choice` parameter is used to configure which tool should be used by the model when it decides to call a tool. This is useful when you want to ensure that a specific tool is always called for a particular task or when you want to override the model's default behavior of choosing a tool based on its internal logic.

    Note that not all models support this feature, and the exact configuration may vary depending on the model you are using.

### Disable parallel calls

For supported providers, you can disable parallel tool calling by setting `parallel_tool_calls=False` via the `model.bind_tools()` method:

```python hl_lines="3"
model.bind_tools(
    tools,
    parallel_tool_calls=False
)
```

??? example "Extended example: disable parallel tool calls in a prebuilt agent"

    ```python hl_lines="15"
    from langchain.chat_models import init_chat_model

    def add(a: int, b: int) -> int:
        """Add two numbers"""
        return a + b

    def multiply(a: int, b: int) -> int:
        """Multiply two numbers."""
        return a * b

    model = init_chat_model("anthropic:claude-3-5-sonnet-latest", temperature=0)
    tools = [add, multiply]
    agent = create_react_agent(
        # disable parallel tool calls
        model=model.bind_tools(tools, parallel_tool_calls=False),
        tools=tools
    )

    agent.invoke(
        {"messages": [{"role": "user", "content": "what's 3 + 5 and 4 * 7?"}]}
    )
    ```

### Handle errors

LangGraph provides built-in error handling for tool execution through the prebuilt [ToolNode](https://langchain-ai.github.io/langgraph/reference/agents/#langgraph.prebuilt.tool_node.ToolNode) component, used both independently and in prebuilt agents.

By **default**, `ToolNode` catches exceptions raised during tool execution and returns them as `ToolMessage` objects with a status indicating an error.

```python
from langchain_core.messages import AIMessage
from langgraph.prebuilt import ToolNode

def multiply(a: int, b: int) -> int:
    if a == 42:
        raise ValueError("The ultimate error")
    return a * b

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Invocation: reads the name from state (initially empty)](./141-invocation-reads-the-name-from-state-initially-emp.md)

**Next:** [Default error handling (enabled by default) →](./143-default-error-handling-enabled-by-default.md)
