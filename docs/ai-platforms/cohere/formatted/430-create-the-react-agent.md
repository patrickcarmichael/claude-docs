---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create the ReAct agent

agent = create_cohere_react_agent(
    llm=llm,
    tools=[internet_search],
    prompt=prompt,
)

agent_executor = AgentExecutor(
    agent=agent, tools=[internet_search], verbose=True
)

response = agent_executor.invoke(
    {
        "input": "Who is the mayor of the capital of Ontario",
        "preamble": preamble,
    }
)

print(response["output"])
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
