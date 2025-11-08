---
title: "Langgraph: Add thread-level persistence"
description: "Add thread-level persistence section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Add thread-level persistence


Adding <a href="../../concepts/persistence#threads">thread-level persistence</a> lets us support conversational experiences with our agent: subsequent invocations will append to the prior messages list, retaining the full conversational context.

To add thread-level persistence to our agent:

1. Select a <a href="../../concepts/persistence#checkpointer-libraries">checkpointer</a>: here we will use <a href="../../reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver">InMemorySaver</a>, a simple in-memory checkpointer.
2. Update our entrypoint to accept the previous messages state as a second argument. Here, we simply append the message updates to the previous sequence of messages.
3. Choose which values will be returned from the workflow and which will be saved by the checkpointer as `previous` using `entrypoint.final` (optional)

```python hl_lines="3 6 7 8 9 30"
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()

@entrypoint(checkpointer=checkpointer)
def agent(messages, previous):
    if previous is not None:
        messages = add_messages(previous, messages)

    llm_response = call_model(messages).result()
    while True:
        if not llm_response.tool_calls:
            break

        # Execute tools
        tool_result_futures = [
            call_tool(tool_call) for tool_call in llm_response.tool_calls
        ]
        tool_results = [fut.result() for fut in tool_result_futures]

        # Append to message list
        messages = add_messages(messages, [llm_response, *tool_results])

        # Call model again
        llm_response = call_model(messages).result()

    # Generate final response
    messages = add_messages(messages, llm_response)
    return entrypoint.final(value=llm_response, save=messages)
```

We will now need to pass in a config when running our application. The config will specify an identifier for the conversational thread.

!!! tip

    Read more about thread-level persistence in our <a href="../../concepts/persistence/">concepts page</a> and <a href="../../how-tos/#persistence">how-to guides</a>.

```python
config = {"configurable": {"thread_id": "1"}}
```

We start a thread the same way as before, this time passing in the config:

```python hl_lines="4"
user_message = {"role": "user", "content": "What's the weather in san francisco?"}
print(user_message)

for step in agent.stream([user_message], config):
    for task_name, message in step.items():
        if task_name == "agent":
            continue  # Just print task updates
        print(f"\n{task_name}:")
        message.pretty_print()
```
```output
{'role': 'user', 'content': "What's the weather in san francisco?"}

call_model:
================================== Ai Message ==================================
Tool Calls:
  get_weather (call_lubbUSdDofmOhFunPEZLBz3g)
 Call ID: call_lubbUSdDofmOhFunPEZLBz3g
  Args:
    location: San Francisco

call_tool:
================================= Tool Message =================================

It's sunny!

call_model:
================================== Ai Message ==================================

The weather in San Francisco is sunny!
```
When we ask a follow-up conversation, the model uses the prior context to infer that we are asking about the weather:

```python
user_message = {"role": "user", "content": "How does it compare to Boston, MA?"}
print(user_message)

for step in agent.stream([user_message], config):
    for task_name, message in step.items():
        if task_name == "agent":
            continue  # Just print task updates
        print(f"\n{task_name}:")
        message.pretty_print()
```
```output
{'role': 'user', 'content': 'How does it compare to Boston, MA?'}

call_model:
================================== Ai Message ==================================
Tool Calls:
  get_weather (call_8sTKYAhSIHOdjLD5d6gaswuV)
 Call ID: call_8sTKYAhSIHOdjLD5d6gaswuV
  Args:
    location: Boston, MA

call_tool:
================================= Tool Message =================================

It's rainy!

call_model:
================================== Ai Message ==================================

Compared to San Francisco, which is sunny, Boston, MA is experiencing rainy weather.
```
In the [LangSmith trace](https://smith.langchain.com/public/20a1116b-bb3b-44c1-8765-7a28663439d9/r), we can see that the full conversational context is retained in each model call.

---

concepts/assistants.md

---

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage](./242-usage.md)

**Next:** [Assistants →](./244-assistants.md)
