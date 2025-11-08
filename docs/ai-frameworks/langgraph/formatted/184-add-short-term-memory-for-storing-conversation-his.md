---
title: "Langgraph: add short-term memory for storing conversation history"
description: "add short-term memory for storing conversation history section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# add short-term memory for storing conversation history

checkpointer = InMemorySaver()

@entrypoint(checkpointer=checkpointer)
def workflow(messages: list[BaseMessage], previous: list[BaseMessage]):
    messages = add_messages(previous or [], messages)
    response = call_autogen_agent(messages).result()
    return entrypoint.final(value=response, save=add_messages(messages, response))
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create the workflow](./183-create-the-workflow.md)

**Next:** [Run the graph →](./185-run-the-graph.md)
