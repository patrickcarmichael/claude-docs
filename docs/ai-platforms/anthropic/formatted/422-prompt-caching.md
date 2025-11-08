---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Prompt caching

Web fetch works with [prompt caching](/en/docs/build-with-claude/prompt-caching). To enable prompt caching, add `cache_control` breakpoints in your request. Cached fetch results can be reused across conversation turns.
```python
import anthropic

client = anthropic.Anthropic()

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
