---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Overview

The Responses API is designed for building conversational applications and complex workflows. It allows you to:

* **Continue conversations**: Maintain context across multiple turns without resending the entire history.
* **Use external tools**: Integrate with external services and data sources through the Model Context Protocol (MCP).
* **Stream responses**: Receive results as they are generated, enabling real-time applications.
* **Control tool usage**: Set limits on tool calls with `max_tool_calls` parameter.
* **Manage data retention**: Choose whether to store conversations (default) or opt-out with `store=false`.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
