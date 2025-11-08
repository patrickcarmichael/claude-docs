---
title: "Langgraph: Tool execution"
description: "Tool execution section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Tool execution


While the model determines when to call a tool, execution of the tool call must be handled by a runtime component.

LangGraph provides prebuilt components for this:

- [`ToolNode`](https://langchain-ai.github.io/langgraph/reference/agents/#langgraph.prebuilt.tool_node.ToolNode): A prebuilt node that executes tools.
- [`create_react_agent`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent): Constructs a full agent that manages tool calling automatically.

---

concepts/subgraphs.md

---

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Custom tools](./275-custom-tools.md)

**Next:** [Subgraphs →](./277-subgraphs.md)
