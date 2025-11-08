---
title: "Langgraph: Invocation: reads the name from state (initially empty)"
description: "Invocation: reads the name from state (initially empty) section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Invocation: reads the name from state (initially empty)

agent.invoke({"messages": "what's my name?"})
```

Use a tool that returns a `Command` to **update** `user_name` and append a confirmation message:

```python hl_lines="12 13 14 15 16 17"
from typing import Annotated
from langgraph.types import Command
from langchain_core.messages import ToolMessage
from langchain_core.tools import tool, InjectedToolCallId

@tool
def update_user_name(
    new_name: str,
    tool_call_id: Annotated[str, InjectedToolCallId]
) -> Command:
    """Update user-name in short-term memory."""
    return Command(update={
        "user_name": new_name,
        "messages": [
            ToolMessage(f"Updated user name to {new_name}", tool_call_id=tool_call_id)
        ]
    })
```

!!! important

    If you want to use tools that return `Command` and update graph state, you can either use prebuilt [`create_react_agent`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) / [`ToolNode`](https://langchain-ai.github.io/langgraph/reference/agents/#langgraph.prebuilt.tool_node.ToolNode) components, or implement your own tool-executing node that collects `Command` objects returned by the tools and returns a list of them, e.g.:

    ```python
    def call_tools(state):
        ...
        commands = [tools_by_name[tool_call["name"]].invoke(tool_call) for tool_call in tool_calls]
        return commands
    ```

### Long-term memory

Use [long-term memory](../concepts/memory.md#long-term-memory) to store user-specific or application-specific data across conversations. This is useful for applications like chatbots, where you want to remember user preferences or other information.

To use long-term memory, you need to:

1. [Configure a store](memory/add-memory.md#add-long-term-memory) to persist data across invocations.
2. Access the store from within tools.

To **access** information in the store:

```python hl_lines="4 11 13"
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from langgraph.graph import StateGraph
from langgraph.config import get_store

@tool
def get_user_info(config: RunnableConfig) -> str:
    """Look up user info."""
    # Same as that provided to `builder.compile(store=store)`
    # or `create_react_agent`
    store = get_store()
    user_id = config["configurable"].get("user_id")
    user_info = store.get(("users",), user_id)
    return str(user_info.value) if user_info else "Unknown user"

builder = StateGraph(...)
...
graph = builder.compile(store=store)
```

??? example "Access long-term memory"

    ```python hl_lines="7 9 22 24 30 36"
    from langchain_core.runnables import RunnableConfig
    from langchain_core.tools import tool
    from langgraph.config import get_store
    from langgraph.prebuilt import create_react_agent
    from langgraph.store.memory import InMemoryStore

    store = InMemoryStore() # (1)!

    store.put(  # (2)!
        ("users",),  # (3)!
        "user_123",  # (4)!
        {
            "name": "John Smith",
            "language": "English",
        } # (5)!
    )

    @tool
    def get_user_info(config: RunnableConfig) -> str:
        """Look up user info."""
        # Same as that provided to `create_react_agent`
        store = get_store() # (6)!
        user_id = config["configurable"].get("user_id")
        user_info = store.get(("users",), user_id) # (7)!
        return str(user_info.value) if user_info else "Unknown user"

    agent = create_react_agent(
        model="anthropic:claude-3-7-sonnet-latest",
        tools=[get_user_info],
        store=store # (8)!
    )

    # Run the agent
    agent.invoke(
        {"messages": [{"role": "user", "content": "look up user information"}]},
        config={"configurable": {"user_id": "user_123"}}
    )
    ```

    1. The `InMemoryStore` is a store that stores data in memory. In a production setting, you would typically use a database or other persistent storage. Please review the [store documentation][../reference/store.md) for more options. If you're deploying with **LangGraph Platform**, the platform will provide a production-ready store for you.
    2. For this example, we write some sample data to the store using the `put` method. Please see the [BaseStore.put](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.put) API reference for more details.
    3. The first argument is the namespace. This is used to group related data together. In this case, we are using the `users` namespace to group user data.
    4. A key within the namespace. This example uses a user ID for the key.
    5. The data that we want to store for the given user.
    6. The `get_store` function is used to access the store. You can call it from anywhere in your code, including tools and prompts. This function returns the store that was passed to the agent when it was created.
    7. The `get` method is used to retrieve data from the store. The first argument is the namespace, and the second argument is the key. This will return a `StoreValue` object, which contains the value and metadata about the value.
    8. The `store` is passed to the agent. This enables the agent to access the store when running tools. You can also use the `get_store` function to access the store from anywhere in your code.

To **update** information in the store:

```python hl_lines="4 11 13"
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from langgraph.graph import StateGraph
from langgraph.config import get_store

@tool
def save_user_info(user_info: str, config: RunnableConfig) -> str:
    """Save user info."""
    # Same as that provided to `builder.compile(store=store)`
    # or `create_react_agent`
    store = get_store()
    user_id = config["configurable"].get("user_id")
    store.put(("users",), user_id, user_info)
    return "Successfully saved user info."

builder = StateGraph(...)
...
graph = builder.compile(store=store)
```

??? example "Update long-term memory"

    ```python hl_lines="18 20 26 32"
    from typing_extensions import TypedDict

    from langchain_core.tools import tool
    from langgraph.config import get_store
    from langchain_core.runnables import RunnableConfig
    from langgraph.prebuilt import create_react_agent
    from langgraph.store.memory import InMemoryStore

    store = InMemoryStore() # (1)!

    class UserInfo(TypedDict): # (2)!
        name: str

    @tool
    def save_user_info(user_info: UserInfo, config: RunnableConfig) -> str: # (3)!
        """Save user info."""
        # Same as that provided to `create_react_agent`
        store = get_store() # (4)!
        user_id = config["configurable"].get("user_id")
        store.put(("users",), user_id, user_info) # (5)!
        return "Successfully saved user info."

    agent = create_react_agent(
        model="anthropic:claude-3-7-sonnet-latest",
        tools=[save_user_info],
        store=store
    )

    # Run the agent
    agent.invoke(
        {"messages": [{"role": "user", "content": "My name is John Smith"}]},
        config={"configurable": {"user_id": "user_123"}} # (6)!
    )

    # You can access the store directly to get the value
    store.get(("users",), "user_123").value
    ```

    1. The `InMemoryStore` is a store that stores data in memory. In a production setting, you would typically use a database or other persistent storage. Please review the [store documentation](../reference/store.md) for more options. If you're deploying with **LangGraph Platform**, the platform will provide a production-ready store for you.
    2. The `UserInfo` class is a `TypedDict` that defines the structure of the user information. The LLM will use this to format the response according to the schema.
    3. The `save_user_info` function is a tool that allows an agent to update user information. This could be useful for a chat application where the user wants to update their profile information.
    4. The `get_store` function is used to access the store. You can call it from anywhere in your code, including tools and prompts. This function returns the store that was passed to the agent when it was created.
    5. The `put` method is used to store data in the store. The first argument is the namespace, and the second argument is the key. This will store the user information in the store.
    6. The `user_id` is passed in the config. This is used to identify the user whose information is being updated.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example agent setup](./140-example-agent-setup.md)

**Next:** [Advanced tool features →](./142-advanced-tool-features.md)
