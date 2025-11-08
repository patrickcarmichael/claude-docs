---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Pricing

Extended thinking uses the standard token pricing scheme:

| Model             | Base Input Tokens | Cache Writes   | Cache Hits    | Output Tokens |
| ----------------- | ----------------- | -------------- | ------------- | ------------- |
| Claude Opus 4.1   | \$15 / MTok       | \$18.75 / MTok | \$1.50 / MTok | \$75 / MTok   |
| Claude Opus 4     | \$15 / MTok       | \$18.75 / MTok | \$1.50 / MTok | \$75 / MTok   |
| Claude Sonnet 4.5 | \$3 / MTok        | \$3.75 / MTok  | \$0.30 / MTok | \$15 / MTok   |
| Claude Sonnet 4   | \$3 / MTok        | \$3.75 / MTok  | \$0.30 / MTok | \$15 / MTok   |
| Claude Sonnet 3.7 | \$3 / MTok        | \$3.75 / MTok  | \$0.30 / MTok | \$15 / MTok   |

The thinking process incurs charges for:

* Tokens used during thinking (output tokens)
* Thinking blocks from the last assistant turn included in subsequent requests (input tokens)
* Standard text output tokens

>   **📝 Note**
>
> When extended thinking is enabled, a specialized system prompt is automatically included to support this feature.

When using summarized thinking:

* **Input tokens**: Tokens in your original request (excludes thinking tokens from previous turns)
* **Output tokens (billed)**: The original thinking tokens that Claude generated internally
* **Output tokens (visible)**: The summarized thinking tokens you see in the response
* **No charge**: Tokens used to generate the summary

>   **⚠️ Warning**
>
> The billed output token count will **not** match the visible token count in the response. You are billed for the full thinking process, not the summary you see.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
