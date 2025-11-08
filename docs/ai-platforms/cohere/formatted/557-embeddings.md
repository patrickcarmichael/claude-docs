---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Embeddings

We expose two routes for Embed v4 and Embed v3 inference:

* `v1/embeddings` adheres to the Azure AI Generative Messages API schema;
* ` v1/embed` supports Cohere's native API schema.

You can find more information about Azure's API [here](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-embed#embed-api-reference-for-cohere-embed-models-deployed-as-a-service).
```python PYTHON
import urllib.request
import json

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
