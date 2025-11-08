---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Messages

* Message structure:
  * v1: uses separate `preamble` and `message` parameters.
  * v2: uses a single `messages` parameter consisting of a list of roles (`system`, `user`, `assistant`, or `tool`). The `system` role in v2 replaces the `preamble` parameter in v1.

* Chat history:
  * v1: manages the chat history via the `chat_history` parameter.
  * v2: manages the chat history via the `messages` list.

**v1**
```python PYTHON
res = co_v1.chat(
    model="command-a-03-2025",
    preamble="You respond in concise sentences.",
    chat_history=[
        {"role": "user", "message": "Hello"},
        {
            "role": "chatbot",
            "message": "Hi, how can I help you today?",
        },
    ],
    message="I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates?",
)

print(res.text)
```
```
Excited to join the team at Co1t, where I look forward to contributing my skills and collaborating with everyone to drive innovation and success.
```
**v2**
```python PYTHON
res = co_v2.chat(
    model="command-a-03-2025",
    messages=[
        {
            "role": "system",
            "content": "You respond in concise sentences.",
        },
        {"role": "user", "content": "Hello"},
        {
            "role": "assistant",
            "content": "Hi, how can I help you today?",
        },
        {
            "role": "user",
            "content": "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates.",
        },
    ],
)

print(res.message.content[0].text)
```
```
Excited to join the team at Co1t, bringing my passion for innovation and a background in [your expertise] to contribute to the company's success!
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
