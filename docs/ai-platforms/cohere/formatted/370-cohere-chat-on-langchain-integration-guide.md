---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cohere Chat on LangChain (Integration Guide)

> Integrate Cohere with LangChain to build applications using Cohere's models and LangChain tools.

Cohere supports various integrations with LangChain, a large language model (LLM) framework which allows you to quickly create applications based on Cohere's models. This doc will guide you through how to leverage Cohere Chat with LangChain.

### Prerequisites

Running Cohere Chat with LangChain doesn't require many prerequisites, consult the [top-level document](/docs/cohere-and-langchain) for more information.

### Cohere Chat with LangChain

To use [Cohere chat](/docs/chat-api) with LangChain, simply create a [ChatCohere](https://python.langchain.com/docs/integrations/chat/cohere/) object and pass in the message or message history. In the example below, you will need to add your Cohere API key.
```python PYTHON
from langchain_cohere import ChatCohere
from langchain_core.messages import AIMessage, HumanMessage

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
