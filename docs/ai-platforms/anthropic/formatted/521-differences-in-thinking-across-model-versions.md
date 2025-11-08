---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Differences in thinking across model versions

The Messages API handles thinking differently across Claude Sonnet 3.7 and Claude 4 models, primarily in redaction and summarization behavior.

See the table below for a condensed comparison:

| Feature                  | Claude Sonnet 3.7            | Claude 4 Models                                              |
| ------------------------ | ---------------------------- | ------------------------------------------------------------ |
| **Thinking Output**      | Returns full thinking output | Returns summarized thinking                                  |
| **Interleaved Thinking** | Not supported                | Supported with `interleaved-thinking-2025-05-14` beta header |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
