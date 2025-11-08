---
title: "Langgraph: How to integrate LangGraph (functional API) with AutoGen, CrewAI, and other frameworks"
description: "How to integrate LangGraph (functional API) with AutoGen, CrewAI, and other frameworks section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# How to integrate LangGraph (functional API) with AutoGen, CrewAI, and other frameworks


LangGraph is a framework for building agentic and multi-agent applications. LangGraph can be easily integrated with other agent frameworks. 

The primary reasons you might want to integrate LangGraph with other agent frameworks:

- create <a href="../../concepts/multi_agent">multi-agent systems</a> where individual agents are built with different frameworks
- leverage LangGraph to add features like <a href="../../concepts/persistence">persistence</a>, <a href="../../concepts/streaming">streaming</a>, <a href="../../concepts/memory">short and long-term memory</a> and more

The simplest way to integrate agents from other frameworks is by calling those agents inside a LangGraph <a href="../../concepts/low_level/#nodes">node</a>:

```python
import autogen
from langgraph.func import entrypoint, task

autogen_agent = autogen.AssistantAgent(name="assistant", ...)
user_proxy = autogen.UserProxyAgent(name="user_proxy", ...)

@task
def call_autogen_agent(messages):
    response = user_proxy.initiate_chat(
        autogen_agent,
        message=messages[-1],
        ...
    )
    ...

@entrypoint()
def workflow(messages):
    response = call_autogen_agent(messages).result()
    return response

workflow.invoke(
    [
        {
            "role": "user",
            "content": "Find numbers between 10 and 30 in fibonacci sequence",
        }
    ]
)
```

In this guide we show how to build a LangGraph chatbot that integrates with AutoGen, but you can follow the same approach with other frameworks.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Summarizing message history](./179-summarizing-message-history.md)

**Next:** [Setup →](./181-setup.md)
