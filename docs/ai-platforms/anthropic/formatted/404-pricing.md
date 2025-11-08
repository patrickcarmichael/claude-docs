---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Pricing

Tool use requests are priced based on:

1. The total number of input tokens sent to the model (including in the `tools` parameter)
2. The number of output tokens generated
3. For server-side tools, additional usage-based pricing (e.g., web search charges per search performed)

Client-side tools are priced the same as any other Claude API request, while server-side tools may incur additional charges based on their specific usage.

The additional tokens from tool use come from:

* The `tools` parameter in API requests (tool names, descriptions, and schemas)
* `tool_use` content blocks in API requests and responses
* `tool_result` content blocks in API requests

When you use `tools`, we also automatically include a special system prompt for the model which enables tool use. The number of tool use tokens required for each model are listed below (excluding the additional tokens listed above). Note that the table assumes at least 1 tool is provided. If no `tools` are provided, then a tool choice of `none` uses 0 additional system prompt tokens.

| Model                                                                      | Tool choice                                        | Tool use system prompt token count          |
| -------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------- |
| Claude Opus 4.1                                                            | `auto`, `none`<hr className="my-2" />`any`, `tool` | 346 tokens<hr className="my-2" />313 tokens |
| Claude Opus 4                                                              | `auto`, `none`<hr className="my-2" />`any`, `tool` | 346 tokens<hr className="my-2" />313 tokens |
| Claude Sonnet 4.5                                                          | `auto`, `none`<hr className="my-2" />`any`, `tool` | 346 tokens<hr className="my-2" />313 tokens |
| Claude Sonnet 4                                                            | `auto`, `none`<hr className="my-2" />`any`, `tool` | 346 tokens<hr className="my-2" />313 tokens |
| Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | `auto`, `none`<hr className="my-2" />`any`, `tool` | 346 tokens<hr className="my-2" />313 tokens |
| Claude Haiku 4.5                                                           | `auto`, `none`<hr className="my-2" />`any`, `tool` | 346 tokens<hr className="my-2" />313 tokens |
| Claude Haiku 3.5                                                           | `auto`, `none`<hr className="my-2" />`any`, `tool` | 264 tokens<hr className="my-2" />340 tokens |
| Claude Opus 3 ([deprecated](/en/docs/about-claude/model-deprecations))     | `auto`, `none`<hr className="my-2" />`any`, `tool` | 530 tokens<hr className="my-2" />281 tokens |
| Claude Sonnet 3                                                            | `auto`, `none`<hr className="my-2" />`any`, `tool` | 159 tokens<hr className="my-2" />235 tokens |
| Claude Haiku 3                                                             | `auto`, `none`<hr className="my-2" />`any`, `tool` | 264 tokens<hr className="my-2" />340 tokens |

These token counts are added to your normal input and output tokens to calculate the total cost of a request.

Refer to our [models overview table](/en/docs/about-claude/models/overview#model-comparison-table) for current per-model prices.

When you send a tool use prompt, just like any other API request, the response will output both input and output token counts as part of the reported `usage` metrics.

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
