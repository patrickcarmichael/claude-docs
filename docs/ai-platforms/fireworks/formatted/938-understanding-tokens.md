---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Understanding tokens

Language models process text in chunks called **tokens**. In English, a token can be as short as one character or as long as one word. Different model families use different **tokenizers**, so the same text may translate to different token counts depending on the model.

**Why tokens matter:**

* Models have maximum context lengths measured in tokens
* Pricing is based on token usage (prompt + completion)
* Token count affects response time

For Llama models, use [this tokenizer tool](https://belladoreai.github.io/llama-tokenizer-js/example-demo/build/) to estimate token counts. Actual usage is returned in the `usage` field of every API response.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
