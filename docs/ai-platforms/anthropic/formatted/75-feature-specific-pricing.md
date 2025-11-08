---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Feature-specific pricing

### Batch processing

The Batch API allows asynchronous processing of large volumes of requests with a 50% discount on both input and output tokens.

| Model                                                                      | Batch input    | Batch output   |
| -------------------------------------------------------------------------- | -------------- | -------------- |
| Claude Opus 4.1                                                            | \$7.50 / MTok  | \$37.50 / MTok |
| Claude Opus 4                                                              | \$7.50 / MTok  | \$37.50 / MTok |
| Claude Sonnet 4.5                                                          | \$1.50 / MTok  | \$7.50 / MTok  |
| Claude Sonnet 4                                                            | \$1.50 / MTok  | \$7.50 / MTok  |
| Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | \$1.50 / MTok  | \$7.50 / MTok  |
| Claude Haiku 4.5                                                           | \$0.50 / MTok  | \$2.50 / MTok  |
| Claude Haiku 3.5                                                           | \$0.40 / MTok  | \$2 / MTok     |
| Claude Opus 3 ([deprecated](/en/docs/about-claude/model-deprecations))     | \$7.50 / MTok  | \$37.50 / MTok |
| Claude Haiku 3                                                             | \$0.125 / MTok | \$0.625 / MTok |

For more information about batch processing, see our [batch processing documentation](/en/docs/build-with-claude/batch-processing).

### Long context pricing

When using Claude Sonnet 4 or Sonnet 4.5 with the [1M token context window enabled](/en/docs/build-with-claude/context-windows#1m-token-context-window), requests that exceed 200K input tokens are automatically charged at premium long context rates:

>   **📝 Note**
>
> The 1M token context window is currently in beta for organizations in [usage tier](/en/api/rate-limits) 4 and organizations with custom rate limits. The 1M token context window is only available for Claude Sonnet 4 and Sonnet 4.5.

| ≤ 200K input tokens | > 200K input tokens    |
| ------------------- | ---------------------- |
| Input: \$3 / MTok   | Input: \$6 / MTok      |
| Output: \$15 / MTok | Output: \$22.50 / MTok |

Long context pricing stacks with other pricing modifiers:

* The [Batch API 50% discount](#batch-processing) applies to long context pricing
* [Prompt caching multipliers](#model-pricing) apply on top of long context pricing

>   **📝 Note**
>
> Even with the beta flag enabled, requests with fewer than 200K input tokens are charged at standard rates. If your request exceeds 200K input tokens, all tokens incur premium pricing.

  The 200K threshold is based solely on input tokens (including cache reads/writes). Output token count does not affect pricing tier selection, though output tokens are charged at the higher rate when the input threshold is exceeded.

To check if your API request was charged at the 1M context window rates, examine the `usage` object in the API response:
```json
{
  "usage": {
    "input_tokens": 250000,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "output_tokens": 500
  }
}
```

Calculate the total input tokens by summing:

* `input_tokens`
* `cache_creation_input_tokens` (if using prompt caching)
* `cache_read_input_tokens` (if using prompt caching)

If the total exceeds 200,000 tokens, the entire request was billed at 1M context rates.

For more information about the `usage` object, see the [API response documentation](/en/api/messages#response-usage).

### Tool use pricing

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

For current per-model prices, refer to our [model pricing](#model-pricing) section above.

For more information about tool use implementation and best practices, see our [tool use documentation](/en/docs/agents-and-tools/tool-use/overview).

### Specific tool pricing

#### Bash tool

The bash tool adds **245 input tokens** to your API calls.

Additional tokens are consumed by:

* Command outputs (stdout/stderr)
* Error messages
* Large file contents

See [tool use pricing](#tool-use-pricing) for complete pricing details.

#### Code execution tool

Code execution tool usage is tracked separately from token usage. Execution time has a minimum of 5 minutes.
If files are included in the request, execution time is billed even if the tool is not used due to files being preloaded onto the container.

Each organization receives 50 free hours of usage with the code execution tool per day. Additional usage beyond the first 50 hours is billed at \$0.05 per hour, per container.

#### Text editor tool

The text editor tool uses the same pricing structure as other tools used with Claude. It follows the standard input and output token pricing based on the Claude model you're using.

In addition to the base tokens, the following additional input tokens are needed for the text editor tool:

| Tool                                                                                                | Additional input tokens |
| --------------------------------------------------------------------------------------------------- | ----------------------- |
| `text_editor_20250429` (Claude 4.x)                                                                 | 700 tokens              |
| `text_editor_20250124` (Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations))) | 700 tokens              |

See [tool use pricing](#tool-use-pricing) for complete pricing details.

#### Web search tool

Web search usage is charged in addition to token usage:
```json
"usage": {
  "input_tokens": 105,
  "output_tokens": 6039,
  "cache_read_input_tokens": 7123,
  "cache_creation_input_tokens": 7345,
  "server_tool_use": {
    "web_search_requests": 1
  }
}
```

Web search is available on the Claude API for **\$10 per 1,000 searches**, plus standard token costs for search-generated content. Web search results retrieved throughout a conversation are counted as input tokens, in search iterations executed during a single turn and in subsequent conversation turns.

Each web search counts as one use, regardless of the number of results returned. If an error occurs during web search, the web search will not be billed.

#### Web fetch tool

Web fetch usage has **no additional charges** beyond standard token costs:
```json
"usage": {
  "input_tokens": 25039,
  "output_tokens": 931,
  "cache_read_input_tokens": 0,
  "cache_creation_input_tokens": 0,
  "server_tool_use": {
    "web_fetch_requests": 1
  }
}
```

The web fetch tool is available on the Claude API at **no additional cost**. You only pay standard token costs for the fetched content that becomes part of your conversation context.

To protect against inadvertently fetching large content that would consume excessive tokens, use the `max_content_tokens` parameter to set appropriate limits based on your use case and budget considerations.

Example token usage for typical content:

* Average web page (10KB): \~2,500 tokens
* Large documentation page (100KB): \~25,000 tokens
* Research paper PDF (500KB): \~125,000 tokens

#### Computer use tool

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
