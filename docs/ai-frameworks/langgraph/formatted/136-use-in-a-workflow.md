---
title: "Langgraph: Use in a workflow"
description: "Use in a workflow section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Use in a workflow


If you are writing a custom workflow, you will need to:

1. register the tools with the chat model
2. call the tool if the model decides to use it

Use `model.bind_tools()` to register the tools with the model.

```python hl_lines="5"
from langchain.chat_models import init_chat_model

model = init_chat_model(model="claude-3-5-haiku-latest")

model_with_tools = model.bind_tools([multiply])
```

LLMs automatically determine if a tool invocation is necessary and handle calling the tool with the appropriate arguments.

??? example "Extended example: attach tools to a chat model"

    ```python hl_lines="10"
    from langchain_core.tools import tool
    from langchain.chat_models import init_chat_model

    @tool
    def multiply(a: int, b: int) -> int:
        """Multiply two numbers."""
        return a * b

    model = init_chat_model(model="claude-3-5-haiku-latest")
    model_with_tools = model.bind_tools([multiply])

    response_message = model_with_tools.invoke("what's 42 x 7?")
    tool_call = response_message.tool_calls[0]

    multiply.invoke(tool_call)
    ```

    ```pycon
    ToolMessage(
        content='294',
        name='multiply',
        tool_call_id='toolu_0176DV4YKSD8FndkeuuLj36c'
    )
    ```

#### ToolNode

To execute tools in custom workflows, use the prebuilt [`ToolNode`](https://langchain-ai.github.io/langgraph/reference/agents/#langgraph.prebuilt.tool_node.ToolNode) or implement your own custom node.

`ToolNode` is a specialized node for executing tools in a workflow. It provides the following features:

- Supports both synchronous and asynchronous tools.
- Executes multiple tools concurrently.
- Handles errors during tool execution (`handle_tool_errors=True`, enabled by default). See [handling tool errors](#handle-errors) for more details.

`ToolNode` operates on [`MessagesState`](../concepts/low_level.md#messagesstate):

- **Input**: `MessagesState`, where the last message is an `AIMessage` containing the `tool_calls` parameter.
- **Output**: `MessagesState` updated with the resulting [`ToolMessage`](https://python.langchain.com/docs/concepts/messages/#toolmessage) from executed tools.

```python hl_lines="1 14"
from langgraph.prebuilt import ToolNode

def get_weather(location: str):
    """Call to get the current weather."""
    if location.lower() in ["sf", "san francisco"]:
        return "It's 60 degrees and foggy."
    else:
        return "It's 90 degrees and sunny."

def get_coolest_cities():
    """Get a list of coolest cities"""
    return "nyc, sf"

tool_node = ToolNode([get_weather, get_coolest_cities])
tool_node.invoke({"messages": [...]})
```

??? example "Single tool call"

    ```python hl_lines="13"
    from langchain_core.messages import AIMessage
    from langgraph.prebuilt import ToolNode

    # Define tools
    @tool
    def get_weather(location: str):
        """Call to get the current weather."""
        if location.lower() in ["sf", "san francisco"]:
            return "It's 60 degrees and foggy."
        else:
            return "It's 90 degrees and sunny."

    tool_node = ToolNode([get_weather])

    message_with_single_tool_call = AIMessage(
        content="",
        tool_calls=[
            {
                "name": "get_weather",
                "args": {"location": "sf"},
                "id": "tool_call_id",
                "type": "tool_call",
            }
        ],
    )

    tool_node.invoke({"messages": [message_with_single_tool_call]})
    ```

```json
    {'messages': [ToolMessage(content="It's 60 degrees and foggy.", name='get_weather', tool_call_id='tool_call_id')]}
    ```

??? example "Multiple tool calls"

    ```python hl_lines="17 37"
    from langchain_core.messages import AIMessage
    from langgraph.prebuilt import ToolNode

    # Define tools

    def get_weather(location: str):
        """Call to get the current weather."""
        if location.lower() in ["sf", "san francisco"]:
            return "It's 60 degrees and foggy."
        else:
            return "It's 90 degrees and sunny."

    def get_coolest_cities():
        """Get a list of coolest cities"""
        return "nyc, sf"

    tool_node = ToolNode([get_weather, get_coolest_cities])

    message_with_multiple_tool_calls = AIMessage(
        content="",
        tool_calls=[
            {
                "name": "get_coolest_cities",
                "args": {},
                "id": "tool_call_id_1",
                "type": "tool_call",
            },
            {
                "name": "get_weather",
                "args": {"location": "sf"},
                "id": "tool_call_id_2",
                "type": "tool_call",
            },
        ],
    )

    tool_node.invoke({"messages": [message_with_multiple_tool_calls]})  # (1)!
    ```

    1. `ToolNode` will execute both tools in parallel

    ```
    {
        'messages': [
            ToolMessage(content='nyc, sf', name='get_coolest_cities', tool_call_id='tool_call_id_1'),
            ToolMessage(content="It's 60 degrees and foggy.", name='get_weather', tool_call_id='tool_call_id_2')
        ]
    }
    ```

??? example "Use with a chat model"

    ```python hl_lines="11 14 17"
    from langchain.chat_models import init_chat_model
    from langgraph.prebuilt import ToolNode

    def get_weather(location: str):
        """Call to get the current weather."""
        if location.lower() in ["sf", "san francisco"]:
            return "It's 60 degrees and foggy."
        else:
            return "It's 90 degrees and sunny."

    tool_node = ToolNode([get_weather])

    model = init_chat_model(model="claude-3-5-haiku-latest")
    model_with_tools = model.bind_tools([get_weather])  # (1)!

    response_message = model_with_tools.invoke("what's the weather in sf?")
    tool_node.invoke({"messages": [response_message]})
    ```

    1. Use `.bind_tools()` to attach the tool schema to the chat model

```json
    {'messages': [ToolMessage(content="It's 60 degrees and foggy.", name='get_weather', tool_call_id='toolu_01Pnkgw5JeTRxXAU7tyHT4UW')]}
    ```

??? example "Use in a tool-calling agent"

    This is an example of creating a tool-calling agent from scratch using `ToolNode`. You can also use LangGraph's prebuilt [agent](../agents/agents.md).

    ```python hl_lines="12 15 33"
    from langchain.chat_models import init_chat_model
    from langgraph.prebuilt import ToolNode
    from langgraph.graph import StateGraph, MessagesState, START, END

    def get_weather(location: str):
        """Call to get the current weather."""
        if location.lower() in ["sf", "san francisco"]:
            return "It's 60 degrees and foggy."
        else:
            return "It's 90 degrees and sunny."

    tool_node = ToolNode([get_weather])

    model = init_chat_model(model="claude-3-5-haiku-latest")
    model_with_tools = model.bind_tools([get_weather])

    def should_continue(state: MessagesState):
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools"
        return END

    def call_model(state: MessagesState):
        messages = state["messages"]
        response = model_with_tools.invoke(messages)
        return {"messages": [response]}

    builder = StateGraph(MessagesState)

    # Define the two nodes we will cycle between
    builder.add_node("call_model", call_model)
    builder.add_node("tools", tool_node)

    builder.add_edge(START, "call_model")
    builder.add_conditional_edges("call_model", should_continue, ["tools", END])
    builder.add_edge("tools", "call_model")

    graph = builder.compile()

    graph.invoke({"messages": [{"role": "user", "content": "what's the weather in sf?"}]})
    ```

    ```
    {
        'messages': [
            HumanMessage(content="what's the weather in sf?"),
            AIMessage(
                content=[{'text': "I'll help you check the weather in San Francisco right now.", 'type': 'text'}, {'id': 'toolu_01A4vwUEgBKxfFVc5H3v1CNs', 'input': {'location': 'San Francisco'}, 'name': 'get_weather', 'type': 'tool_use'}],
                tool_calls=[{'name': 'get_weather', 'args': {'location': 'San Francisco'}, 'id': 'toolu_01A4vwUEgBKxfFVc5H3v1CNs', 'type': 'tool_call'}]
            ),
            ToolMessage(content="It's 60 degrees and foggy."),
            AIMessage(content="The current weather in San Francisco is 60 degrees and foggy. Typical San Francisco weather with its famous marine layer!")
        ]
    }
    ```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Use in an agent](./135-use-in-an-agent.md)

**Next:** [Tool customization →](./137-tool-customization.md)
