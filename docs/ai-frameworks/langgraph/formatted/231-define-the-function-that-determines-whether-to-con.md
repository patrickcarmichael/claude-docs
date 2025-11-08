---
title: "Langgraph: Define the function that determines whether to continue or not"
description: "Define the function that determines whether to continue or not section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Define the function that determines whether to continue or not

def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]
    # If there is no function call, then we respond to the user
    if not last_message.tool_calls:
        return "respond"
    # Otherwise if there is, we continue
    else:
        return "continue"

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define the function that responds to the user](./230-define-the-function-that-responds-to-the-user.md)

**Next:** [Define a new graph →](./232-define-a-new-graph.md)
