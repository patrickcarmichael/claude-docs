---
title: "Langgraph: Create the workflow"
description: "Create the workflow section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Create the workflow


We will now create a LangGraph chatbot graph that calls AutoGen agent.

```python
from langchain_core.messages import convert_to_openai_messages, BaseMessage
from langgraph.func import entrypoint, task
from langgraph.graph import add_messages
from langgraph.checkpoint.memory import InMemorySaver

@task
def call_autogen_agent(messages: list[BaseMessage]):
    # convert to openai-style messages
    messages = convert_to_openai_messages(messages)
    response = user_proxy.initiate_chat(
        autogen_agent,
        message=messages[-1],
        # pass previous message history as context
        carryover=messages[:-1],
    )
    # get the final response from the agent
    content = response.chat_history[-1]["content"]
    return {"role": "assistant", "content": content}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define AutoGen agent](./182-define-autogen-agent.md)

**Next:** [add short-term memory for storing conversation history →](./184-add-short-term-memory-for-storing-conversation-his.md)
