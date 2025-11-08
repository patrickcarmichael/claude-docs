---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Basic text generation

To get started with Chat, we need to pass two parameters, `model` for the LLM model ID and `messages`, which we add a single user message. We then call the Chat endpoint through the client we created earlier.

The response contains several objects. For simplicity, what we want right now is the `message.content[0].text` object.

Here's an example of the assistant responding to a new hire's query asking for help to make introductions.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
