---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool definition

The code execution tool requires no additional parameters:
```json
{
  "type": "code_execution_20250825",
  "name": "code_execution"
}
```
When this tool is provided, Claude automatically gains access to two sub-tools:

* `bash_code_execution`: Run shell commands
* `text_editor_code_execution`: View, create, and edit files, including writing code

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
