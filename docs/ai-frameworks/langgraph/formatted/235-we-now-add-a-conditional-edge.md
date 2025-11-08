---
title: "Langgraph: We now add a conditional edge"
description: "We now add a conditional edge section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# We now add a conditional edge

workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "tools",
        "respond": "respond",
    },
)

workflow.add_edge("tools", "agent")
workflow.add_edge("respond", END)
graph = workflow.compile()
```

### Usage

We can now invoke our graph to verify that the output is being structured as desired:

```python
answer = graph.invoke(input={"messages": [("human", "what's the weather in SF?")]})[
    "final_response"
]
```

```python
answer
```

```output
WeatherResponse(temperature=75.0, wind_directon='SE', wind_speed=4.83)
```

As we can see, the agent returned a `WeatherResponse` object as we expected. If would now be easy to use this agent in a more complex software stack without having to worry about the output of the agent not matching the format expected from the next step in the stack.

---

how-tos/disable-streaming.ipynb

---

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Set the entrypoint as `agent`](./234-set-the-entrypoint-as-agent.md)

**Next:** [How to disable streaming for models that don't support it →](./236-how-to-disable-streaming-for-models-that-dont-supp.md)
