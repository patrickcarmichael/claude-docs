---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Using prompt caching

### Common use cases

Requests to LLMs often share a large portion of their prompt. For example:

* Long system prompts with detailed instructions
* Descriptions of available tools for function calling
* Growing previous conversation history for chat use cases
* Shared per-user context, like a current file for a coding assistant

Prompt caching avoids re-processing the cached prefix of the prompt and starts output generation much sooner.

### Structuring prompts for caching

Prompt caching works only for exact prefix matches within a prompt. To
realize caching benefits, place static content like instructions and examples at
the beginning of your prompt, and put variable content, such as user-specific
information, at the end.

For function calling models, tools are considered part of the prompt.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
