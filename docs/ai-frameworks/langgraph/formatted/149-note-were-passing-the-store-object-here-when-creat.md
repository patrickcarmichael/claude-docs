---
title: "Langgraph: NOTE: we're passing the store object here when creating a workflow via entrypoint()"
description: "NOTE: we're passing the store object here when creating a workflow via entrypoint() section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# NOTE: we're passing the store object here when creating a workflow via entrypoint()

@entrypoint(checkpointer=InMemorySaver(), store=in_memory_store)
def workflow(
    inputs: list[BaseMessage],
    *,
    previous: list[BaseMessage],
    config: RunnableConfig,
    store: BaseStore,
):
    user_id = config["configurable"]["user_id"]
    previous = previous or []
    inputs = add_messages(previous, inputs)
    response = call_model(inputs, store, user_id).result()
    return entrypoint.final(value=response, save=add_messages(inputs, response))
```

!!! note Note

    If you're using LangGraph Cloud or LangGraph Studio, you __don't need__ to pass store to the entrypoint decorator, since it's done automatically.

### Run the workflow!

Now let's specify a user ID in the config and tell the model our name:

```python
config = {"configurable": {"thread_id": "1", "user_id": "1"}}
input_message = {"role": "user", "content": "Hi! Remember: my name is Bob"}
for chunk in workflow.stream([input_message], config, stream_mode="values"):
    chunk.pretty_print()
```
```output
================================== Ai Message ==================================

Hello Bob! Nice to meet you. I'll remember that your name is Bob. How can I help you today?
```

```python
config = {"configurable": {"thread_id": "2", "user_id": "1"}}
input_message = {"role": "user", "content": "what is my name?"}
for chunk in workflow.stream([input_message], config, stream_mode="values"):
    chunk.pretty_print()
```
```output
================================== Ai Message ==================================

Your name is Bob.
```
We can now inspect our in-memory store and verify that we have in fact saved the memories for the user:

```python
for memory in in_memory_store.search(("memories", "1")):
    print(memory.value)
```
```output
{'data': 'User name is Bob'}
```
Let's now run the workflow for another user to verify that the memories about the first user are self contained:

```python
config = {"configurable": {"thread_id": "3", "user_id": "2"}}
input_message = {"role": "user", "content": "what is my name?"}
for chunk in workflow.stream([input_message], config, stream_mode="values"):
    chunk.pretty_print()
```
```output
================================== Ai Message ==================================

I don't have any information about your name. I can only see our current conversation without any prior context or personal details about you. If you'd like me to know your name, feel free to tell me!
```

---

how-tos/multi-agent-network-functional.ipynb

---

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example: simple chatbot with long-term memory](./148-example-simple-chatbot-with-long-term-memory.md)

**Next:** [How to build a multi-agent network (functional API) →](./150-how-to-build-a-multi-agent-network-functional-api.md)
