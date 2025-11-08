---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Before you try to reduce prompt leak

We recommend using leak-resistant prompt engineering strategies only when **absolutely necessary**. Attempts to leak-proof your prompt can add complexity that may degrade performance in other parts of the task due to increasing the complexity of the LLM’s overall task.

If you decide to implement leak-resistant techniques, be sure to test your prompts thoroughly to ensure that the added complexity does not negatively impact the model’s performance or the quality of its outputs.

<Tip>Try monitoring techniques first, like output screening and post-processing, to try to catch instances of prompt leak.</Tip>

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
