---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Crafting a system message

When building a chatbot, it may be useful to constrain its behavior. For example, you may want to prevent the assistant from responding to certain prompts, or force it to respond in a desired tone. To achieve this, you can include a message with the role "system" in the `messages` array. Instructions in system messages always take precedence over instructions in user messages, so as a developer you have control over the chatbot behavior.

For example, if we want the chatbot to adopt a formal style, the system instruction can be used to encourage the generation of more business-like and professional responses. We can also instruct the chatbot to refuse requests that are unrelated to onboarding. When writing a system message, the recommended approach is to use two H2 Markdown headers: "Task and Context" and "Style Guide" in the exact order.

In the example below, the system instruction provides context for the assistant's task (task and context) and encourages the generation of rhymes as much as possible (style guide).
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
