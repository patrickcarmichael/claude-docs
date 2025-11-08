---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Hosting Requirements

### Container-Based Sandboxing

For security and isolation, the SDK should run inside a **sandboxed container environment**. This provides:

* **Process isolation** - Separate execution environment per session
* **Resource limits** - CPU, memory, and storage constraints
* **Network control** - Restrict outbound connections
* **Ephemeral filesystems** - Clean state for each session

### System Requirements

Each SDK instance requires:

* **Runtime dependencies**
  * Python 3.10+ (for Python SDK) or Node.js 18+ (for TypeScript SDK)
  * Node.js (required by Claude Code CLI)
  * Claude Code CLI: `npm install -g @anthropic-ai/claude-code`

* **Resource allocation**
  * Recommended: 1GiB RAM, 5GiB of disk, and 1 CPU (vary this based on your task as needed)

* **Network access**
  * Outbound HTTPS to `api.anthropic.com`
  * Optional: Access to MCP servers or external tools

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
