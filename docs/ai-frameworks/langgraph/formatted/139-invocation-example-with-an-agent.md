---
title: "Langgraph: Invocation example with an agent"
description: "Invocation example with an agent section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Invocation example with an agent

agent.invoke(
    {"messages": [{"role": "user", "content": "look up user info"}]},
    config={"configurable": {"user_id": "user_123"}}
)
```

??? example "Extended example: Access config in tools"

    ```python hl_lines="6 9 19"
    from langchain_core.runnables import RunnableConfig
    from langchain_core.tools import tool
    from langgraph.prebuilt import create_react_agent

    def get_user_info(
        config: RunnableConfig,
    ) -> str:
        """Look up user info."""
        user_id = config["configurable"].get("user_id")
        return "User is John Smith" if user_id == "user_123" else "Unknown user"

    agent = create_react_agent(
        model="anthropic:claude-3-7-sonnet-latest",
        tools=[get_user_info],
    )

    agent.invoke(
        {"messages": [{"role": "user", "content": "look up user information"}]},
        config={"configurable": {"user_id": "user_123"}}
    )
    ```

### Short-term memory

Short-term memory maintains **dynamic** state that changes during a single execution.

To **access** (read) the graph state inside the tools, you can use a special parameter **annotation** — [`InjectedState`](https://langchain-ai.github.io/langgraph/reference/agents/#langgraph.prebuilt.tool_node.InjectedState):

```python hl_lines="12"
from typing import Annotated, NotRequired
from langchain_core.tools import tool
from langgraph.prebuilt import InjectedState, create_react_agent
from langgraph.prebuilt.chat_agent_executor import AgentState

class CustomState(AgentState):
    # The user_name field in short-term state
    user_name: NotRequired[str]

@tool
def get_user_name(
    state: Annotated[CustomState, InjectedState]
) -> str:
    """Retrieve the current user-name from state."""
    # Return stored name or a default if not set
    return state.get("user_name", "Unknown user")

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Context management](./138-context-management.md)

**Next:** [Example agent setup →](./140-example-agent-setup.md)
