---
title: "Langgraph: Example: simple chatbot with short-term memory"
description: "Example: simple chatbot with short-term memory section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Example: simple chatbot with short-term memory


We will be using a workflow with a single task that calls a [chat model](https://python.langchain.com/docs/concepts/chat_models/).

Let's first define the model we'll be using:

```python
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model="claude-3-5-sonnet-latest")
```

Now we can define our task and workflow. To add in persistence, we need to pass in a [Checkpointer](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver) to the [entrypoint()][langgraph.func.entrypoint] decorator.

```python
from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages
from langgraph.func import entrypoint, task
from langgraph.checkpoint.memory import InMemorySaver

@task
def call_model(messages: list[BaseMessage]):
    response = model.invoke(messages)
    return response

checkpointer = InMemorySaver()

@entrypoint(checkpointer=checkpointer)
def workflow(inputs: list[BaseMessage], *, previous: list[BaseMessage]):
    if previous:
        inputs = add_messages(previous, inputs)

    response = call_model(inputs).result()
    return entrypoint.final(value=response, save=add_messages(inputs, response))
```

If we try to use this workflow, the context of the conversation will be persisted across interactions:

!!! note Note

    If you're using LangGraph Platform or LangGraph Studio, you __don't need__ to pass checkpointer to the entrypoint decorator, since it's done automatically.

We can now interact with the agent and see that it remembers previous messages!

```python
config = {"configurable": {"thread_id": "1"}}
input_message = {"role": "user", "content": "hi! I'm bob"}
for chunk in workflow.stream([input_message], config, stream_mode="values"):
    chunk.pretty_print()
```
```output
================================== Ai Message ==================================

Hi Bob! I'm Claude. Nice to meet you! How are you today?
```
You can always resume previous threads:

```python
input_message = {"role": "user", "content": "what's my name?"}
for chunk in workflow.stream([input_message], config, stream_mode="values"):
    chunk.pretty_print()
```
```output
================================== Ai Message ==================================

Your name is Bob.
```
If we want to start a new conversation, we can pass in a different `thread_id`. Poof! All the memories are gone!

```python
input_message = {"role": "user", "content": "what's my name?"}
for chunk in workflow.stream(
    [input_message],
    {"configurable": {"thread_id": "2"}},
    stream_mode="values",
):
    chunk.pretty_print()
```
```output
================================== Ai Message ==================================

I don't know your name unless you tell me. Each conversation I have starts fresh, so I don't have access to any previous interactions or personal information unless you share it with me.
```
!!! tip "Streaming tokens"

    If you would like to stream LLM tokens from your chatbot, you can use `stream_mode="messages"`. Check out this <a href="../streaming-tokens">how-to guide</a> to learn more.

---

how-tos/create-react-agent-manage-message-history.ipynb

---

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setup](./171-setup.md)

**Next:** [How to manage conversation history in a ReAct Agent →](./173-how-to-manage-conversation-history-in-a-react-agen.md)
