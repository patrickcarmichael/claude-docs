---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Rate limits

Our rate limits for the Messages API are measured in requests per minute (RPM), input tokens per minute (ITPM), and output tokens per minute (OTPM) for each model class.
If you exceed any of the rate limits you will get a [429 error](/en/api/errors) describing which rate limit was exceeded, along with a `retry-after` header indicating how long to wait.

>   **📝 Note**
>
> You might also encounter 429 errors due to acceleration limits on the API if your organization has a sharp increase in usage. To avoid hitting acceleration limits, ramp up your traffic gradually and maintain consistent usage patterns.

### Cache-aware ITPM

Many API providers use a combined "tokens per minute" (TPM) limit that may include all tokens, both cached and uncached, input and output. **For most Claude models, only uncached input tokens count towards your ITPM rate limits.** This is a key advantage that makes our rate limits effectively higher than they might initially appear.

ITPM rate limits are estimated at the beginning of each request, and the estimate is adjusted during the request to reflect the actual number of input tokens used.

Here's what counts towards ITPM:

* `input_tokens` (tokens after the last cache breakpoint) ✓ **Count towards ITPM**
* `cache_creation_input_tokens` (tokens being written to cache) ✓ **Count towards ITPM**
* `cache_read_input_tokens` (tokens read from cache) ✗ **Do NOT count towards ITPM** for most models

>   **📝 Note**
>
> The `input_tokens` field only represents tokens that appear **after your last cache breakpoint**, not all input tokens in your request. To calculate total input tokens:
```
  total_input_tokens = cache_read_input_tokens + cache_creation_input_tokens + input_tokens
```
  This means when you have cached content, `input_tokens` will typically be much smaller than your total input. For example, with a 200K token cached document and a 50 token user question, you'd see `input_tokens: 50` even though the total input is 200,050 tokens.

  For rate limit purposes on most models, only `input_tokens` + `cache_creation_input_tokens` count toward your ITPM limit, making [prompt caching](/en/docs/build-with-claude/prompt-caching) an effective way to increase your effective throughput.

**Example**: With a 2,000,000 ITPM limit and an 80% cache hit rate, you could effectively process 10,000,000 total input tokens per minute (2M uncached + 8M cached), since cached tokens don't count towards your rate limit.

>   **📝 Note**
>
> Some older models (marked with † in the rate limit tables below) also count `cache_read_input_tokens` towards ITPM rate limits.

  For all models without the † marker, cached input tokens do not count towards rate limits and are billed at a reduced rate (10% of base input token price). This means you can achieve significantly higher effective throughput by using [prompt caching](/en/docs/build-with-claude/prompt-caching).

<Tip>
  **Maximize your rate limits with prompt caching**

  To get the most out of your rate limits, use [prompt caching](/en/docs/build-with-claude/prompt-caching) for repeated content like:

  * System instructions and prompts
  * Large context documents
  * Tool definitions
  * Conversation history

  With effective caching, you can dramatically increase your actual throughput without increasing your rate limits. Monitor your cache hit rate on the [Usage page](https://console.anthropic.com/settings/usage) to optimize your caching strategy.
</Tip>

OTPM rate limits are estimated based on `max_tokens` at the beginning of each request, and the estimate is adjusted at the end of the request to reflect the actual number of output tokens used.
If you're hitting OTPM limits earlier than expected, try reducing `max_tokens` to better approximate the size of your completions.

Rate limits are applied separately for each model; therefore you can use different models up to their respective limits simultaneously.
You can check your current rate limits and behavior in the [Claude Console](https://console.anthropic.com/settings/limits).

>   **📝 Note**
>
> For long context requests (>200K tokens) when using the `context-1m-2025-08-07` beta header with Claude Sonnet 4.x, separate rate limits apply. See [Long context rate limits](#long-context-rate-limits) below.

<Tabs>
  <Tab title="Tier 1">
    | Model                                                                      | Maximum requests per minute (RPM) | Maximum input tokens per minute (ITPM) | Maximum output tokens per minute (OTPM) |
    | -------------------------------------------------------------------------- | --------------------------------- | -------------------------------------- | --------------------------------------- |
    | Claude Sonnet 4.x<sup>\*\*</sup>                                           | 50                                | 30,000                                 | 8,000                                   |
    | Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | 50                                | 20,000                                 | 8,000                                   |
    | Claude Haiku 4.5                                                           | 50                                | 50,000                                 | 10,000                                  |
    | Claude Haiku 3.5                                                           | 50                                | 50,000<sup>†</sup>                     | 10,000                                  |
    | Claude Haiku 3                                                             | 50                                | 50,000<sup>†</sup>                     | 10,000                                  |
    | Claude Opus 4.x<sup>\*</sup>                                               | 50                                | 30,000                                 | 8,000                                   |
    | Claude Opus 3 ([deprecated](/en/docs/about-claude/model-deprecations))     | 50                                | 20,000<sup>†</sup>                     | 4,000                                   |
  </Tab>

  <Tab title="Tier 2">
    | Model                                                                      | Maximum requests per minute (RPM) | Maximum input tokens per minute (ITPM) | Maximum output tokens per minute (OTPM) |
    | -------------------------------------------------------------------------- | --------------------------------- | -------------------------------------- | --------------------------------------- |
    | Claude Sonnet 4.x<sup>\*\*</sup>                                           | 1,000                             | 450,000                                | 90,000                                  |
    | Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | 1,000                             | 40,000                                 | 16,000                                  |
    | Claude Haiku 4.5                                                           | 1,000                             | 450,000                                | 90,000                                  |
    | Claude Haiku 3.5                                                           | 1,000                             | 100,000<sup>†</sup>                    | 20,000                                  |
    | Claude Haiku 3                                                             | 1,000                             | 100,000<sup>†</sup>                    | 20,000                                  |
    | Claude Opus 4.x<sup>\*</sup>                                               | 1,000                             | 450,000                                | 90,000                                  |
    | Claude Opus 3 ([deprecated](/en/docs/about-claude/model-deprecations))     | 1,000                             | 40,000<sup>†</sup>                     | 8,000                                   |
  </Tab>

  <Tab title="Tier 3">
    | Model                                                                      | Maximum requests per minute (RPM) | Maximum input tokens per minute (ITPM) | Maximum output tokens per minute (OTPM) |
    | -------------------------------------------------------------------------- | --------------------------------- | -------------------------------------- | --------------------------------------- |
    | Claude Sonnet 4.x<sup>\*\*</sup>                                           | 2,000                             | 800,000                                | 160,000                                 |
    | Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | 2,000                             | 80,000                                 | 32,000                                  |
    | Claude Haiku 4.5                                                           | 2,000                             | 1,000,000                              | 200,000                                 |
    | Claude Haiku 3.5                                                           | 2,000                             | 200,000<sup>†</sup>                    | 40,000                                  |
    | Claude Haiku 3                                                             | 2,000                             | 200,000<sup>†</sup>                    | 40,000                                  |
    | Claude Opus 4.x<sup>\*</sup>                                               | 2,000                             | 800,000                                | 160,000                                 |
    | Claude Opus 3 ([deprecated](/en/docs/about-claude/model-deprecations))     | 2,000                             | 80,000<sup>†</sup>                     | 16,000                                  |
  </Tab>

  <Tab title="Tier 4">
    | Model                                                                      | Maximum requests per minute (RPM) | Maximum input tokens per minute (ITPM) | Maximum output tokens per minute (OTPM) |
    | -------------------------------------------------------------------------- | --------------------------------- | -------------------------------------- | --------------------------------------- |
    | Claude Sonnet 4.x<sup>\*\*</sup>                                           | 4,000                             | 2,000,000                              | 400,000                                 |
    | Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | 4,000                             | 200,000                                | 80,000                                  |
    | Claude Haiku 4.5                                                           | 4,000                             | 4,000,000                              | 800,000                                 |
    | Claude Haiku 3.5                                                           | 4,000                             | 400,000<sup>†</sup>                    | 80,000                                  |
    | Claude Haiku 3                                                             | 4,000                             | 400,000<sup>†</sup>                    | 80,000                                  |
    | Claude Opus 4.x<sup>\*</sup>                                               | 4,000                             | 2,000,000                              | 400,000                                 |
    | Claude Opus 3 ([deprecated](/en/docs/about-claude/model-deprecations))     | 4,000                             | 400,000<sup>†</sup>                    | 80,000                                  |
  </Tab>

  <Tab title="Custom">
    If you're seeking higher limits for an Enterprise use case, contact sales through the [Claude Console](https://console.anthropic.com/settings/limits).
  </Tab>
</Tabs>

*<sup>\* - Opus 4.x rate limit is a total limit that applies to combined traffic across both Opus 4 and Opus 4.1.</sup>*

*<sup>\*\* - Sonnet 4.x rate limit is a total limit that applies to combined traffic across both Sonnet 4 and Sonnet 4.5.</sup>*

*<sup>† - Limit counts `cache_read_input_tokens` towards ITPM usage.</sup>*

### Message Batches API

The Message Batches API has its own set of rate limits which are shared across all models. These include a requests per minute (RPM) limit to all API endpoints and a limit on the number of batch requests that can be in the processing queue at the same time. A "batch request" here refers to part of a Message Batch. You may create a Message Batch containing thousands of batch requests, each of which count towards this limit. A batch request is considered part of the processing queue when it has yet to be successfully processed by the model.

<Tabs>
  <Tab title="Tier 1">
    | Maximum requests per minute (RPM) | Maximum batch requests in processing queue | Maximum batch requests per batch |
    | --------------------------------- | ------------------------------------------ | -------------------------------- |
    | 50                                | 100,000                                    | 100,000                          |
  </Tab>

  <Tab title="Tier 2">
    | Maximum requests per minute (RPM) | Maximum batch requests in processing queue | Maximum batch requests per batch |
    | --------------------------------- | ------------------------------------------ | -------------------------------- |
    | 1,000                             | 200,000                                    | 100,000                          |
  </Tab>

  <Tab title="Tier 3">
    | Maximum requests per minute (RPM) | Maximum batch requests in processing queue | Maximum batch requests per batch |
    | --------------------------------- | ------------------------------------------ | -------------------------------- |
    | 2,000                             | 300,000                                    | 100,000                          |
  </Tab>

  <Tab title="Tier 4">
    | Maximum requests per minute (RPM) | Maximum batch requests in processing queue | Maximum batch requests per batch |
    | --------------------------------- | ------------------------------------------ | -------------------------------- |
    | 4,000                             | 500,000                                    | 100,000                          |
  </Tab>

  <Tab title="Custom">
    If you're seeking higher limits for an Enterprise use case, contact sales through the [Claude Console](https://console.anthropic.com/settings/limits).
  </Tab>
</Tabs>

### Long context rate limits

When using Claude Sonnet 4 and Sonnet 4.5 with the [1M token context window enabled](/en/docs/build-with-claude/context-windows#1m-token-context-window), the following dedicated rate limits apply to requests exceeding 200K tokens.

>   **📝 Note**
>
> The 1M token context window is currently in beta for organizations in usage tier 4 and organizations with custom rate limits. The 1M token context window is only available for Claude Sonnet 4 and Sonnet 4.5.

<Tabs>
  <Tab title="Tier 4">
    | Maximum input tokens per minute (ITPM) | Maximum output tokens per minute (OTPM) |
    | -------------------------------------- | --------------------------------------- |
    | 1,000,000                              | 200,000                                 |
  </Tab>

  <Tab title="Custom">
    For custom long context rate limits for enterprise use cases, contact sales through the [Claude Console](https://console.anthropic.com/settings/limits).
  </Tab>
</Tabs>

<Tip>
  To get the most out of the 1M token context window with rate limits, use [prompt caching](/en/docs/build-with-claude/prompt-caching).
</Tip>

### Monitoring your rate limits in the Console

You can monitor your rate limit usage on the [Usage](https://console.anthropic.com/settings/usage) page of the [Claude Console](https://console.anthropic.com/).

In addition to providing token and request charts, the Usage page provides two separate rate limit charts. Use these charts to see what headroom you have to grow, when you may be hitting peak use, better undersand what rate limits to request, or how you can improve your caching rates. The charts visualize a number of metrics for a given rate limit (e.g. per model):

* The **Rate Limit - Input Tokens** chart includes:
  * Hourly maximum uncached input tokens per minute
  * Your current input tokens per minute rate limit
  * The cache rate for your input tokens (i.e. the percentage of input tokens read from the cache)
* The **Rate Limit - Output Tokens** chart includes:
  * Hourly maximum output tokens per minute
  * Your current output tokens per minute rate limit

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
