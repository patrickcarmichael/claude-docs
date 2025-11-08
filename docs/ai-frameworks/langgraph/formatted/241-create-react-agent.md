---
title: "Langgraph: Create ReAct agent"
description: "Create ReAct agent section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Create ReAct agent


Now that you have installed the required packages and set your environment variables, we can create our agent.

### Define model and tools

Let's first define the tools and model we will use for our example. Here we will use a single place-holder tool that gets a description of the weather for a location.

We will use an [OpenAI](https://python.langchain.com/docs/integrations/providers/openai/) chat model for this example, but any model [supporting tool-calling](https://python.langchain.com/docs/integrations/chat/) will suffice.

```python
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

model = ChatOpenAI(model="gpt-4o-mini")

@tool
def get_weather(location: str):
    """Call to get the weather from a specific location."""
    # This is a placeholder for the actual implementation
    if any([city in location.lower() for city in ["sf", "san francisco"]]):
        return "It's sunny!"
    elif "boston" in location.lower():
        return "It's rainy!"
    else:
        return f"I am not sure what the weather is in {location}"

tools = [get_weather]
```

### Define tasks

We next define the <a href="../../concepts/functional_api/#task">tasks</a> we will execute. Here there are two different tasks:

1. **Call model**: We want to query our chat model with a list of messages.
2. **Call tool**: If our model generates tool calls, we want to execute them.

```python
from langchain_core.messages import ToolMessage
from langgraph.func import entrypoint, task

tools_by_name = {tool.name: tool for tool in tools}

@task
def call_model(messages):
    """Call model with a sequence of messages."""
    response = model.bind_tools(tools).invoke(messages)
    return response

@task
def call_tool(tool_call):
    tool = tools_by_name[tool_call["name"]]
    observation = tool.invoke(tool_call["args"])
    return ToolMessage(content=observation, tool_call_id=tool_call["id"])
```

### Define entrypoint

Our <a href="../../concepts/functional_api/#entrypoint">entrypoint</a> will handle the orchestration of these two tasks. As described above, when our `call_model` task generates tool calls, the `call_tool` task will generate responses for each. We append all messages to a single messages list.

!!! tip
    Note that because tasks return future-like objects, the below implementation executes tools in parallel.

```python
from langgraph.graph.message import add_messages

@entrypoint()
def agent(messages):
    llm_response = call_model(messages).result()
    while True:
        if not llm_response.tool_calls:
            break

        # Execute tools
        tool_result_futures = [
            call_tool(tool_call) for tool_call in llm_response.tool_calls
        ]
        tool_results = [fut.result() for fut in tool_result_futures]

        # Append to message list
        messages = add_messages(messages, [llm_response, *tool_results])

        # Call model again
        llm_response = call_model(messages).result()

    return llm_response
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setup](./240-setup.md)

**Next:** [Usage →](./242-usage.md)
