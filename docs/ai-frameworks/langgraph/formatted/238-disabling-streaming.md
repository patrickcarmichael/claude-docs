---
title: "Langgraph: Disabling streaming"
description: "Disabling streaming section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Disabling streaming


Now without making any changes to our graph, let's set the [disable_streaming](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel.disable_streaming) parameter on our model to be `True` which will solve the problem:

```python
llm = ChatOpenAI(model="o1-preview", temperature=1, disable_streaming=True)

graph_builder = StateGraph(MessagesState)

def chatbot(state: MessagesState):
    return {"messages": [llm.invoke(state["messages"])]}

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()
```

And now, rerunning with the same input, we should see no errors:

```python
input = {"messages": {"role": "user", "content": "how many r's are in strawberry?"}}
async for event in graph.astream_events(input, version="v2"):
    if event["event"] == "on_chat_model_end":
        print(event["data"]["output"].content, end="", flush=True)
```
```output
There are three "r"s in the word "strawberry".
```

---

how-tos/react-agent-from-scratch-functional.ipynb

---

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Without disabling streaming](./237-without-disabling-streaming.md)

**Next:** [How to create a ReAct agent from scratch (Functional API) →](./239-how-to-create-a-react-agent-from-scratch-functiona.md)
