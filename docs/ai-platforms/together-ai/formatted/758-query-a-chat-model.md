---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Query a chat model

To query a chat model, use the `together chat.completions` method.

Use the `--model` option to choose your model, and the `--message` option to pass in a message's role and text:
```sh
together chat.completions \
  --model mistralai/Mixtral-8x7B-Instruct-v0.1 \
  --message "user" "What's 1 + 1?"
```
You can also pass in multiple messages:
```sh
together chat.completions \
  --model mistralai/Mixtral-8x7B-Instruct-v0.1 \
  --message "system" "You are a helpful assistant named Together" \
  --message "user" "What is your name?"
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
