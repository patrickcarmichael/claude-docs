---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Text Generation

We expose two routes for Command R and Command R+ inference:

* `v1/chat/completions` adheres to the Azure AI Generative Messages API schema;
* ` v1/chat` supports Cohere's native API schema.

You can find more information about Azure's API [here](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-command#chat-api-reference-for-cohere-models-deployed-as-a-service).

Here's a code snippet demonstrating how to programmatically interact with a Cohere model on Azure:
```python PYTHON
import urllib.request
import json

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
