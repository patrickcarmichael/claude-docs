---
title: "Langgraph: define the multi-agent network workflow"
description: "define the multi-agent network workflow section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# define the multi-agent network workflow

@entrypoint()
def workflow(messages):
    call_active_agent = call_travel_advisor
    while True:
        agent_messages = call_active_agent(messages).result()
        messages = messages + agent_messages
        call_active_agent = get_next_agent(messages)
    return messages
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← define a task that calls an agent](./153-define-a-task-that-calls-an-agent.md)

**Next:** [Setup →](./155-setup.md)
