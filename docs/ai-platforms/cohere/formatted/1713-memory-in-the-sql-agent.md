---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Memory in the sql agent

We may want the agent to hold memory of our previous messages so that we're able to coherently engage with the agent to answer our queries. In this section, let's take a look at how we can add memory to the agent so that we're able to achieve this outcome!
```python PYTHON
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage
from pydantic import BaseModel, Field
from typing import List
```
In the code snippets below, we create a class to store the chat history in memory. This can be customised to store the messages from a database or any other suitable data store.
```python PYTHON
class InMemoryHistory(BaseChatMessageHistory, BaseModel):
    """In memory implementation of chat message history."""

    messages: List[BaseMessage] = Field(default_factory=list)

    def add_messages(self, messages: List[BaseMessage]) -> None:
        """Add a list of messages to the store"""
        self.messages.extend(messages)

    def clear(self) -> None:
        self.messages = []
```
In the below code snippet, we make use of the [RunnableWithMessageHistory](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.history.RunnableWithMessageHistory.html) abstraction to wrap around the agent we've created above to provide the message history to the agent that we can now utilize by chatting with the `agent_with_chat_history` as shown below.
```python PYTHON
store = {}


def get_by_session_id(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryHistory()
    return store[session_id]


agent_with_chat_history = RunnableWithMessageHistory(
    agent, get_by_session_id, history_messages_key="chat_history"
)

output = agent_with_chat_history.invoke(
    {
        "input": "What station had the longest duration on 27th May 2024?",
        "date": datetime.now(),
    },
    config={"configurable": {"session_id": "foo"}},
)
print(output["output"])

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
