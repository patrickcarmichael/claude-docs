---
title: "Langgraph: Stream from an agent"
description: "Stream from an agent section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Stream from an agent


### Agent progress

To stream agent progress, use the [`stream()`](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.CompiledStateGraph.stream) or [`astream()`](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.state.CompiledStateGraph.astream) methods with `stream_mode="updates"`. This emits an event after every agent step.

For example, if you have an agent that calls a tool once, you should see the following updates:

- **LLM node**: AI message with tool call requests
- **Tool node**: Tool message with execution result
- **LLM node**: Final AI response

=== "Sync"

    ```python hl_lines="5 7"
    agent = create_react_agent(
        model="anthropic:claude-3-7-sonnet-latest",
        tools=[get_weather],
    )
    for chunk in agent.stream(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
        stream_mode="updates"
    ):
        print(chunk)
        print("\n")
    ```

=== "Async"

    ```python hl_lines="5 7"
    agent = create_react_agent(
        model="anthropic:claude-3-7-sonnet-latest",
        tools=[get_weather],
    )
    async for chunk in agent.astream(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
        stream_mode="updates"
    ):
        print(chunk)
        print("\n")
    ```

### LLM tokens

To stream tokens as they are produced by the LLM, use `stream_mode="messages"`:

=== "Sync"

    ```python hl_lines="5 7"
    agent = create_react_agent(
        model="anthropic:claude-3-7-sonnet-latest",
        tools=[get_weather],
    )
    for token, metadata in agent.stream(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
        stream_mode="messages"
    ):
        print("Token", token)
        print("Metadata", metadata)
        print("\n")
    ```

=== "Async"

    ```python hl_lines="5 7"
    agent = create_react_agent(
        model="anthropic:claude-3-7-sonnet-latest",
        tools=[get_weather],
    )
    async for token, metadata in agent.astream(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
        stream_mode="messages"
    ):
        print("Token", token)
        print("Metadata", metadata)
        print("\n")
    ```

### Tool updates

To stream updates from tools as they are executed, you can use [get_stream_writer](https://langchain-ai.github.io/langgraph/reference/config/#langgraph.config.get_stream_writer).

=== "Sync"

    ```python hl_lines="1 5 7 17"
    from langgraph.config import get_stream_writer

    def get_weather(city: str) -> str:
        """Get weather for a given city."""
        writer = get_stream_writer()
        # stream any arbitrary data
        writer(f"Looking up data for city: {city}")
        return f"It's always sunny in {city}!"

    agent = create_react_agent(
        model="anthropic:claude-3-7-sonnet-latest",
        tools=[get_weather],
    )

    for chunk in agent.stream(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
        stream_mode="custom"
    ):
        print(chunk)
        print("\n")
    ```

=== "Async"

    ```python hl_lines="1 5 7 17"
    from langgraph.config import get_stream_writer

    def get_weather(city: str) -> str:
        """Get weather for a given city."""
        writer = get_stream_writer()
        # stream any arbitrary data
        writer(f"Looking up data for city: {city}")
        return f"It's always sunny in {city}!"

    agent = create_react_agent(
        model="anthropic:claude-3-7-sonnet-latest",
        tools=[get_weather],
    )

    async for chunk in agent.astream(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
        stream_mode="custom"
    ):
        print(chunk)
        print("\n")
    ```

!!! Note

      If you add `get_stream_writer` inside your tool, you won't be able to invoke the tool outside of a LangGraph execution context.

### Stream multiple modes

You can specify multiple streaming modes by passing stream mode as a list: `stream_mode=["updates", "messages", "custom"]`:

=== "Sync"

    ```python hl_lines="8"
    agent = create_react_agent(
        model="anthropic:claude-3-7-sonnet-latest",
        tools=[get_weather],
    )

    for stream_mode, chunk in agent.stream(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
        stream_mode=["updates", "messages", "custom"]
    ):
        print(chunk)
        print("\n")
    ```

=== "Async"

    ```python hl_lines="8"
    agent = create_react_agent(
        model="anthropic:claude-3-7-sonnet-latest",
        tools=[get_weather],
    )

    async for stream_mode, chunk in agent.astream(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
        stream_mode=["updates", "messages", "custom"]
    ):
        print(chunk)
        print("\n")
    ```

### Disable streaming

In some applications you might need to disable streaming of individual tokens for a given model. This is useful in [multi-agent](../agents/multi-agent.md) systems to control which agents stream their output.

See the [Models](../agents/models.md#disable-streaming) guide to learn how to disable streaming.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Supported stream modes](./75-supported-stream-modes.md)

**Next:** [Stream from a workflow →](./77-stream-from-a-workflow.md)
