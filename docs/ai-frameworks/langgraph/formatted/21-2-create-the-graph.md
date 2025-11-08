---
title: "Langgraph: 2. Create the graph"
description: "2. Create the graph section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## 2. Create the graph


We will now create a LangGraph chatbot graph that calls AutoGen agent.

```python
from langchain_core.messages import convert_to_openai_messages
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.checkpoint.memory import InMemorySaver

def call_autogen_agent(state: MessagesState):
    # Convert LangGraph messages to OpenAI format for AutoGen
    messages = convert_to_openai_messages(state["messages"])
    
    # Get the last user message
    last_message = messages[-1]
    
    # Pass previous message history as context (excluding the last message)
    carryover = messages[:-1] if len(messages) > 1 else []
    
    # Initiate chat with AutoGen
    response = user_proxy.initiate_chat(
        autogen_agent,
        message=last_message,
        carryover=carryover
    )
    
    # Extract the final response from the agent
    final_content = response.chat_history[-1]["content"]
    
    # Return the response in LangGraph format
    return {"messages": {"role": "assistant", "content": final_content}}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← 1. Define AutoGen agent](./20-1-define-autogen-agent.md)

**Next:** [Create the graph with memory for persistence →](./22-create-the-graph-with-memory-for-persistence.md)
