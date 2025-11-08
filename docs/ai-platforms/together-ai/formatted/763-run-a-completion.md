---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Run a completion

To run a completion for a language or code model, use the `together completions` method.

Pass the prompt in as the first argument, and use the `--model` option to choose your model:
```sh
together completions "Large language models are " \
  --model mistralai/Mixtral-8x7B-Instruct-v0.1
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
