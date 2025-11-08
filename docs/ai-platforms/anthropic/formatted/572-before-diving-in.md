---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Before diving in

This guide presumes that you have already decided to use extended thinking mode and have reviewed our basic steps on [how to get started with extended thinking](/en/docs/about-claude/models/extended-thinking-models#getting-started-with-extended-thinking-models) as well as our [extended thinking implementation guide](/en/docs/build-with-claude/extended-thinking).

### Technical considerations for extended thinking

* Thinking tokens have a minimum budget of 1024 tokens. We recommend that you start with the minimum thinking budget and incrementally increase to adjust based on your needs and task complexity.
* For workloads where the optimal thinking budget is above 32K, we recommend that you use [batch processing](/en/docs/build-with-claude/batch-processing) to avoid networking issues. Requests pushing the model to think above 32K tokens causes long running requests that might run up against system timeouts and open connection limits.
* Extended thinking performs best in English, though final outputs can be in [any language Claude supports](/en/docs/build-with-claude/multilingual-support).
* If you need thinking below the minimum budget, we recommend using standard mode, with thinking turned off, with traditional chain-of-thought prompting with XML tags (like `<thinking>`). See [chain of thought prompting](/en/docs/build-with-claude/prompt-engineering/chain-of-thought).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
