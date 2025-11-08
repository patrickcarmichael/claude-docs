---
title: "Langgraph: Repeating tool selection"
description: "Repeating tool selection section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Repeating tool selection


To manage errors from incorrect tool selection, we could revisit the `select_tools` node. One option for implementing this is to modify `select_tools` to generate the vector store query using all messages in the state (e.g., with a chat model) and add an edge routing from `tools` to `select_tools`.

We implement this change below. For demonstration purposes, we simulate an error in the initial tool selection by adding a `hack_remove_tool_condition` to the `select_tools` node, which removes the correct tool on the first iteration of the node. Note that on the second iteration, the agent finishes the run as it has access to the correct tool.

<div class="admonition note">
    <p class="admonition-title">Using Pydantic with LangChain</p>
    <p>
        This notebook uses Pydantic v2 <code>BaseModel</code>, which requires <code>langchain-core >= 0.3</code>. Using <code>langchain-core < 0.3</code> will result in errors due to mixing of Pydantic v1 and v2 <code>BaseModels</code>.
    </p>
</div>  

```python
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langgraph.pregel.retry import RetryPolicy

from pydantic import BaseModel, Field

class QueryForTools(BaseModel):
    """Generate a query for additional tools."""

    query: str = Field(..., description="Query for additional tools.")

def select_tools(state: State):
    """Selects tools based on the last message in the conversation state.

    If the last message is from a human, directly uses the content of the message
    as the query. Otherwise, constructs a query using a system message and invokes
    the LLM to generate tool suggestions.
    """
    last_message = state["messages"][-1]
    hack_remove_tool_condition = False  # Simulate an error in the first tool selection

    if isinstance(last_message, HumanMessage):
        query = last_message.content
        hack_remove_tool_condition = True  # Simulate wrong tool selection
    else:
        assert isinstance(last_message, ToolMessage)
        system = SystemMessage(
            "Given this conversation, generate a query for additional tools. "
            "The query should be a short string containing what type of information "
            "is needed. If no further information is needed, "
            "set more_information_needed False and populate a blank string for the query."
        )
        input_messages = [system] + state["messages"]
        response = llm.bind_tools([QueryForTools], tool_choice=True).invoke(
            input_messages
        )
        query = response.tool_calls[0]["args"]["query"]

    # Search the tool vector store using the generated query
    tool_documents = vector_store.similarity_search(query)
    if hack_remove_tool_condition:
        # Simulate error by removing the correct tool from the selection
        selected_tools = [
            document.id
            for document in tool_documents
            if document.metadata["tool_name"] != "Advanced_Micro_Devices"
        ]
    else:
        selected_tools = [document.id for document in tool_documents]
    return {"selected_tools": selected_tools}

graph_builder = StateGraph(State)
graph_builder.add_node("agent", agent)
graph_builder.add_node(
    "select_tools", select_tools, retry_policy=RetryPolicy(max_attempts=3)
)

tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools", tool_node)

graph_builder.add_conditional_edges(
    "agent",
    tools_condition,
)
graph_builder.add_edge("tools", "select_tools")
graph_builder.add_edge("select_tools", "agent")
graph_builder.add_edge(START, "select_tools")
graph = graph_builder.compile()
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
for message in result["messages"]:
    message.pretty_print()
```
```output
================================ Human Message =================================

Can you give me some information about AMD in 2022?
================================== Ai Message ==================================
Tool Calls:
  Accenture (call_qGmwFnENwwzHOYJXiCAaY5Mx)
 Call ID: call_qGmwFnENwwzHOYJXiCAaY5Mx
  Args:
    year: 2022
================================= Tool Message =================================
Name: Accenture

Accenture had revenues of $100 in 2022.
================================== Ai Message ==================================
Tool Calls:
  Advanced_Micro_Devices (call_u9e5UIJtiieXVYi7Y9GgyDpn)
 Call ID: call_u9e5UIJtiieXVYi7Y9GgyDpn
  Args:
    year: 2022
================================= Tool Message =================================
Name: Advanced_Micro_Devices

Advanced Micro Devices had revenues of $100 in 2022.
================================== Ai Message ==================================

In 2022, AMD had revenues of $100.
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← The select_tools function selects tools based on the user's last message content.](./198-the-select_tools-function-selects-tools-based-on-t.md)

**Next:** [Next steps →](./200-next-steps.md)
