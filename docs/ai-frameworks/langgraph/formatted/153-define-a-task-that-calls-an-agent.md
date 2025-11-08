---
title: "Langgraph: define a task that calls an agent"
description: "define a task that calls an agent section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# define a task that calls an agent

@task
def call_travel_advisor(messages):
    response = travel_advisor.invoke({"messages": messages})
    return response["messages"]

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← define an agent](./152-define-an-agent.md)

**Next:** [define the multi-agent network workflow →](./154-define-the-multi-agent-network-workflow.md)
