---
title: "Langgraph: define the multi-agent network workflow"
description: "define the multi-agent network workflow section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# define the multi-agent network workflow

@entrypoint(checkpointer)
def workflow(messages):
    call_active_agent = call_travel_advisor
    while True:
        agent_messages = call_active_agent(messages).result()
        ai_msg = get_last_ai_msg(agent_messages)
        if not ai_msg.tool_calls:
            user_input = interrupt(value="Ready for user input.")
            messages = messages + [{"role": "user", "content": user_input}]
            continue

        messages = messages + agent_messages
        call_active_agent = get_next_agent(messages)
    return entrypoint.final(value=agent_messages[-1], save=messages)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← define a task that calls an agent](./163-define-a-task-that-calls-an-agent.md)

**Next:** [Setup →](./165-setup.md)
