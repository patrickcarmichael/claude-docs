---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How Skills Are Loaded

When you specify Skills in a container:

1. **Metadata Discovery**: Claude sees metadata for each Skill (name, description) in the system prompt
2. **File Loading**: Skill files are copied into the container at `/skills/{directory}/`
3. **Automatic Use**: Claude automatically loads and uses Skills when relevant to your request
4. **Composition**: Multiple Skills compose together for complex workflows

The progressive disclosure architecture ensures efficient context usage—Claude only loads full Skill instructions when needed.

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
