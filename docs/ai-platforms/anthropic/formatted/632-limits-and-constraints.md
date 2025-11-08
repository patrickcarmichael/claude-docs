---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Limits and Constraints

### Request Limits

* **Maximum Skills per request**: 8
* **Maximum Skill upload size**: 8MB (all files combined)
* **YAML frontmatter requirements**:
  * `name`: Maximum 64 characters, lowercase letters/numbers/hyphens only, no XML tags, no reserved words
  * `description`: Maximum 1024 characters, non-empty, no XML tags

### Environment Constraints

Skills run in the code execution container with these limitations:

* **No network access** - Cannot make external API calls
* **No runtime package installation** - Only pre-installed packages available
* **Isolated environment** - Each request gets a fresh container

See the [code execution tool documentation](/en/docs/agents-and-tools/tool-use/code-execution-tool) for available packages.

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
