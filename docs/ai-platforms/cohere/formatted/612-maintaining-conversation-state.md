---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Maintaining conversation state

Conversations with your chatbot will often span more than one turn. In order to not lose context of previous turns, the entire chat history will need to be passed in the `messages` array when making calls with the Chat API.
In the example below, we keep adding "assistant" and "user" messages to the `messages` array to build up the chat history over multiple turns:
```python PYTHON
messages = [
    {"role": "system", "content": system_instruction},
]

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
