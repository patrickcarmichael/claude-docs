---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Security

>   **⚠️ Warning**
>
> The bash tool provides direct system access. Implement these essential safety measures:

  * Running in isolated environments (Docker/VM)
  * Implementing command filtering and allowlists
  * Setting resource limits (CPU, memory, disk)
  * Logging all executed commands

### Key recommendations

* Use `ulimit` to set resource constraints
* Filter dangerous commands (`sudo`, `rm -rf`, etc.)
* Run with minimal user permissions
* Monitor and log all command execution

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
