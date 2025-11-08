---
title: "Langgraph: The select_tools function selects tools based on the user's last message content."
description: "The select_tools function selects tools based on the user's last message content. section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# The select_tools function selects tools based on the user's last message content.

def select_tools(state: State):
    last_user_message = state["messages"][-1]
    query = last_user_message.content
    tool_documents = vector_store.similarity_search(query)
    return {"selected_tools": [document.id for document in tool_documents]}

builder.add_node("agent", agent)
builder.add_node("select_tools", select_tools)

tool_node = ToolNode(tools=tools)
builder.add_node("tools", tool_node)

builder.add_conditional_edges("agent", tools_condition, path_map=["tools", "__end__"])
builder.add_edge("tools", "agent")
builder.add_edge("select_tools", "agent")
builder.add_edge(START, "select_tools")
graph = builder.compile()
```

```python
from IPython.display import Image, display

try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    # This requires some extra dependencies and is optional
    pass
```

<p>

</p>

```python
user_input = "Can you give me some information about AMD in 2022?"

result = graph.invoke({"messages": [("user", user_input)]})
```

```python
print(result["selected_tools"])
```
```output
['ab9c0d59-3d16-448d-910c-73cf10a26020', 'f5eff8f6-7fb9-47b6-b54f-19872a52db84', '2962e168-9ef4-48dc-8b7c-9227e7956d39', '24a9fb82-19fe-4a88-944e-47bc4032e94a']
```

```python
for message in result["messages"]:
    message.pretty_print()
```
```output
================================ Human Message =================================

Can you give me some information about AMD in 2022?
================================== Ai Message ==================================
Tool Calls:
  Advanced_Micro_Devices (call_CRxQ0oT7NY7lqf35DaRNTJ35)
 Call ID: call_CRxQ0oT7NY7lqf35DaRNTJ35
  Args:
    year: 2022
================================= Tool Message =================================
Name: Advanced_Micro_Devices

Advanced Micro Devices had revenues of $100 in 2022.
================================== Ai Message ==================================

In 2022, Advanced Micro Devices (AMD) had revenues of $100.
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← The agent function processes the current state](./197-the-agent-function-processes-the-current-state.md)

**Next:** [Repeating tool selection →](./199-repeating-tool-selection.md)
