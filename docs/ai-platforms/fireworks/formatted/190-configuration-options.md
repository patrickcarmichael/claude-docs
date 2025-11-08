---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Configuration options

| Flag                         | Type   | Description                                                                                 |
| ---------------------------- | ------ | ------------------------------------------------------------------------------------------- |
| `--draft-model`              | string | Draft model name. Can be a Fireworks model or custom model. See recommendations below.      |
| `--draft-token-count`        | int32  | Tokens to generate per step. Required when using draft model or n-gram. Typically set to 4. |
| `--ngram-speculation-length` | int32  | Alternative to draft model: uses N-gram based speculation from previous input.              |

>   **📝 Note**
>
> `--draft-model` and `--ngram-speculation-length` cannot be used together.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
