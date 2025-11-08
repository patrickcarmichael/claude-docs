---
title: "Langgraph: Define the function that calls the model"
description: "Define the function that calls the model section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Define the function that calls the model

def call_model(state: AgentState):
    response = model_with_tools.invoke(state["messages"])
    # We return a list, because this will get added to the existing list
    return {"messages": [response]}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Option 2: 2 LLMs](./228-option-2-2-llms.md)

**Next:** [Define the function that responds to the user →](./230-define-the-function-that-responds-to-the-user.md)
