---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Programmatically

You can use the
[`is_available_on_serverless`](/tools-sdks/python-client/sdk-reference#is-available-on-serverless)
method on the [LLM](/tools-sdks/python-client/sdk-reference#llm) object in our
[Build SDK](/tools-sdks/python-client/sdk-introduction) to check if a model is
available on serverless.
```python
llm = LLM(model="llama4-maverick-instruct-basic", deployment_type="auto")
print(llm.is_available_on_serverless()) # True

llm = LLM(model="qwen2p5-7b-instruct", deployment_type="auto")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
