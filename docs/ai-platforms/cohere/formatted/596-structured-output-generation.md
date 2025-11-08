---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Structured output generation

By adding the `response_format` parameter, you can get the model to generate the output as a JSON object. By generating JSON objects, you can structure and organize the model's responses in a way that can be used in downstream applications.

The `response_format` parameter allows you to specify the schema the JSON object must follow. It takes the following parameters:

* `message`: The user message
* `response_format`: The schema of the JSON object
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
