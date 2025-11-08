---
title: "Langgraph: Context management"
description: "Context management section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Context management


Tools within LangGraph sometimes require context data, such as runtime-only arguments (e.g., user IDs or session details), that should not be controlled by the model. LangGraph provides three methods for managing such context:

| Type                                    | Usage Scenario                           | Mutable | Lifetime                 |
| --------------------------------------- | ---------------------------------------- | ------- | ------------------------ |
| [Configuration](#configuration)         | Static, immutable runtime data           | ❌      | Single invocation        |
| [Short-term memory](#short-term-memory) | Dynamic, changing data during invocation | ✅      | Single invocation        |
| [Long-term memory](#long-term-memory)   | Persistent, cross-session data           | ✅      | Across multiple sessions |

### Configuration

Use configuration when you have **immutable** runtime data that tools require, such as user identifiers. You pass these arguments via [`RunnableConfig`](https://python.langchain.com/docs/concepts/runnables/#runnableconfig) at invocation and access them in the tool:

```python hl_lines="5 13"
from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig

@tool
def get_user_info(config: RunnableConfig) -> str:
    """Retrieve user information based on user ID."""
    user_id = config["configurable"].get("user_id")
    return "User is John Smith" if user_id == "user_123" else "Unknown user"

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Tool customization](./137-tool-customization.md)

**Next:** [Invocation example with an agent →](./139-invocation-example-with-an-agent.md)
