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

Now we can run our graph to check that it worked as intended:

```python
answer = graph.invoke(input={"messages": [("human", "what's the weather in SF?")]})[
    "final_response"
]
```

```python
answer
```

```output
WeatherResponse(temperature=75.0, wind_directon='SE', wind_speed=3.0)
```

Again, the agent returned a `WeatherResponse` object as we expected.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Set the entrypoint as `agent`](./226-set-the-entrypoint-as-agent.md)

**Next:** [Option 2: 2 LLMs →](./228-option-2-2-llms.md)
