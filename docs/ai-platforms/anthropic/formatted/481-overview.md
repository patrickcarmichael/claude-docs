---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Overview

Context editing allows you to automatically manage conversation context as it grows, helping you optimize costs and stay within context window limits. The API provides different strategies for managing context:

* **Tool result clearing** (`clear_tool_uses_20250919`): Automatically clears tool use/result pairs when conversation context exceeds your configured threshold
* **Thinking block clearing** (`clear_thinking_20251015`): Manages [thinking blocks](/en/docs/build-with-claude/extended-thinking) by clearing older thinking blocks from previous turns

Each strategy can be configured independently and applied together to optimize your specific use case.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
