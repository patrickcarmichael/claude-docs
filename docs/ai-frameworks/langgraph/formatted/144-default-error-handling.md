---
title: "Langgraph: Default error handling"
description: "Default error handling section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Default error handling

agent.invoke({"messages": [{"role": "user", "content": "what's 42 x 7?"}]})
```

To disable or customize error handling in prebuilt agents, explicitly pass a configured `ToolNode`:

```python
custom_tool_node = ToolNode(
    [multiply],
    handle_tool_errors="Cannot use 42 as a first operand!"
)

agent_custom = create_react_agent(
    model="anthropic:claude-3-7-sonnet-latest",
    tools=custom_tool_node
)

agent_custom.invoke({"messages": [{"role": "user", "content": "what's 42 x 7?"}]})
```

### Handle large numbers of tools

As the number of available tools grows, you may want to limit the scope of the LLM's selection, to decrease token consumption and to help manage sources of error in LLM reasoning.

To address this, you can dynamically adjust the tools available to a model by retrieving relevant tools at runtime using semantic search.

See [`langgraph-bigtool`](https://github.com/langchain-ai/langgraph-bigtool) prebuilt library for a ready-to-use implementation.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Default error handling (enabled by default)](./143-default-error-handling-enabled-by-default.md)

**Next:** [Prebuilt tools →](./145-prebuilt-tools.md)
