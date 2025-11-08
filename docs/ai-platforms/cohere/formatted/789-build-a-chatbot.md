---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Build a Chatbot

While our previous examples were single-turn interactions, the Chat endpoint enables us to create chatbots that maintain memory of past conversation turns. This capability allows developers to build conversational applications that preserve context throughout the dialogue.

Below, we implement a basic customer support chatbot that acts as a helpful service agent. We'll create a function called run\_chatbot that handles the conversation flow and displays messages and events. The function can take an optional chat history parameter to maintain conversational context across multiple turns.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
