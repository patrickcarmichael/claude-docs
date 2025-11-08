---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Parameters

The `e2b_code_execution_reward` function accepts the following parameters:

| Parameter           | Type                   | Description                                                          |
| ------------------- | ---------------------- | -------------------------------------------------------------------- |
| `messages`          | List\[Dict\[str, str]] | Generated conversation messages (required)                           |
| `original_messages` | List\[Dict\[str, str]] | Original conversation context (optional)                             |
| `expected_output`   | str                    | Expected output from code execution (optional)                       |
| `language`          | str                    | Programming language of the code (default: "python")                 |
| `timeout`           | int                    | Maximum execution time in seconds (default: 30)                      |
| `api_key`           | str                    | E2B API key (default: None, uses E2B\_API\_KEY environment variable) |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
