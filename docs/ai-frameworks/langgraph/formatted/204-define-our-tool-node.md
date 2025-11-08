---
title: "Langgraph: Define our tool node"
description: "Define our tool node section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Define our tool node

def tool_node(state: AgentState):
    outputs = []
    for tool_call in state["messages"][-1].tool_calls:
        tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
        outputs.append(
            ToolMessage(
                content=json.dumps(tool_result),
                name=tool_call["name"],
                tool_call_id=tool_call["id"],
            )
        )
    return {"messages": outputs}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create ReAct agent](./203-create-react-agent.md)

**Next:** [Define the node that calls the model →](./205-define-the-node-that-calls-the-model.md)
