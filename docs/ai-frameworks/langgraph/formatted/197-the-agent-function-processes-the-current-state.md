---
title: "Langgraph: The agent function processes the current state"
description: "The agent function processes the current state section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# The agent function processes the current state

# by binding selected tools to the LLM.
def agent(state: State):
    # Map tool IDs to actual tools
    # based on the state's selected_tools list.
    selected_tools = [tool_registry[id] for id in state["selected_tools"]]
    # Bind the selected tools to the LLM for the current interaction.
    llm_with_tools = llm.bind_tools(selected_tools)
    # Invoke the LLM with the current messages and return the updated message list.
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Retrieve all available tools from the tool registry.](./196-retrieve-all-available-tools-from-the-tool-registr.md)

**Next:** [The select_tools function selects tools based on the user's last message content. →](./198-the-select_tools-function-selects-tools-based-on-t.md)
