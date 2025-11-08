---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Moderation models

Use our [Completions](/reference/completions-1) endpoint to run a moderation model as a standalone classifier, or use it alongside any of the other models above as a filter to safeguard responses from 100+ models, by specifying the parameter `"safety_model": "MODEL_API_STRING"`

| Organization | Model Name          | Model String for API             | Context length |
| :----------- | :------------------ | :------------------------------- | :------------- |
| Meta         | Llama Guard (8B)    | meta-llama/Meta-Llama-Guard-3-8B | 8192           |
| Meta         | Llama Guard 4 (12B) | meta-llama/Llama-Guard-4-12B     | 1048576        |
| Virtue AI    | Virtue Guard        | VirtueAI/VirtueGuard-Text-Lite   | 32768          |


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
