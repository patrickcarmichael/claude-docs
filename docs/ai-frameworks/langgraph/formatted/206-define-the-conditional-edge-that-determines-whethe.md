---
title: "Langgraph: Define the conditional edge that determines whether to continue or not"
description: "Define the conditional edge that determines whether to continue or not section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Define the conditional edge that determines whether to continue or not

def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]
    # If there is no function call, then we finish
    if not last_message.tool_calls:
        return "end"
    # Otherwise if there is, we continue
    else:
        return "continue"
```

### Define the graph

Now that we have defined all of our nodes and edges, we can define and compile our graph. Depending on if you have added more nodes or different edges, you will need to edit this to fit your specific use case.

```python
from langgraph.graph import StateGraph, END

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define the node that calls the model](./205-define-the-node-that-calls-the-model.md)

**Next:** [Define a new graph →](./207-define-a-new-graph.md)
