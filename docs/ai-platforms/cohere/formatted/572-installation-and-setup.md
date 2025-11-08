---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Installation and Setup

The Cohere platform lets developers access large language model (LLM) capabilities with a few lines of code. These LLMs can solve a broad spectrum of natural language use cases, including classification, semantic search, paraphrasing, summarization, and content generation.

Cohere's models can be accessed through the [playground](https://dashboard.cohere.ai/playground/generate?model=xlarge&__hstc=14363112.d9126f508a1413c0edba5d36861c19ac.1701897884505.1722364657840.1722366723691.56&__hssc=14363112.1.1722366723691&__hsfp=3560715434) and SDK. We support SDKs in four different languages: Python, Typescript, Java, and Go. For these tutorials, we'll use the Python SDK and access the models through the Cohere platform with an API key.

To get started, first install the Cohere Python SDK.
```python PYTHON
! pip install -U cohere
```typescript
Next, we'll import the `cohere` library and create a client to be used throughout the examples. We create a client by passing the Cohere API key as an argument. To get an API key, [sign up with Cohere](https://dashboard.cohere.com/welcome/register) and get the API key [from the dashboard](https://dashboard.cohere.com/api-keys).
```python PYTHON
import cohere

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
