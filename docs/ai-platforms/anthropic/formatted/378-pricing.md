---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Pricing

Computer use follows the standard [tool use pricing](/en/docs/agents-and-tools/tool-use/overview#pricing). When using the computer use tool:

**System prompt overhead**: The computer use beta adds 466-499 tokens to the system prompt

**Computer use tool token usage**:

| Model                                                                      | Input tokens per tool definition |
| -------------------------------------------------------------------------- | -------------------------------- |
| Claude 4.x models                                                          | 735 tokens                       |
| Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | 735 tokens                       |

**Additional token consumption**:

* Screenshot images (see [Vision pricing](/en/docs/build-with-claude/vision))
* Tool execution results returned to Claude

>   **📝 Note**
>
> If you're also using bash or text editor tools alongside computer use, those tools have their own token costs as documented in their respective pages.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
