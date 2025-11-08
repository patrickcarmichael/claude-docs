---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Common Parameters

| Parameter           | Type            | Description                                         |
| ------------------- | --------------- | --------------------------------------------------- |
| `model`             | string          | **Required.** Model to use (e.g., `openai/o4-mini`) |
| `input`             | string or array | **Required.** Text or message array                 |
| `stream`            | boolean         | Enable streaming responses (default: false)         |
| `max_output_tokens` | integer         | Maximum tokens to generate                          |
| `temperature`       | number          | Sampling temperature (0-2)                          |
| `top_p`             | number          | Nucleus sampling parameter (0-1)                    |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
