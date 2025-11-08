---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Other migration scenarios

The primary migration paths covered above (Sonnet 3.7 → 4.5 and Haiku 3.5 → 4.5) represent the most common upgrades. However, you may be migrating from other Claude models to Claude 4.5. This section covers those scenarios.

### Migrating from Claude Sonnet 4 → Sonnet 4.5

**Breaking change**: Cannot specify both `temperature` and `top_p` in the same request.

All other API calls will work without modification. Update your model ID and adjust sampling parameters if needed:
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
