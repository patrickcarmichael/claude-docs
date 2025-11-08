---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Controlling Reasoning Tokens

You can control reasoning tokens in your requests using the `reasoning` parameter:
```json
{
  "model": "your-model",
  "messages": [],
  "reasoning": {
    // One of the following (not both):
    "effort": "high", // Can be "high", "medium", or "low" (OpenAI-style)
    "max_tokens": 2000, // Specific token limit (Anthropic-style)

    // Optional: Default is false. All models support this.
    "exclude": false, // Set to true to exclude reasoning tokens from response

    // Or enable reasoning with the default parameters:
    "enabled": true // Default: inferred from `effort` or `max_tokens`
  }
}
```
The `reasoning` config object consolidates settings for controlling reasoning strength across different models. See the Note for each option below to see which models are supported and how other models will behave.

### Max Tokens for Reasoning

<Note title="Supported models">
  Currently supported by:

  <ul>
    <li>
      Gemini thinking models
    </li>

    <li>
      Anthropic reasoning models (by using the <code>reasoning.max\_tokens</code>{' '}
      parameter)
    </li>

    <li>
      Some Alibaba Qwen thinking models (mapped to 

      <code>thinking_budget</code>

      )
    </li>
  </ul>

  For Alibaba, support varies by model — please check the individual model descriptions to confirm
  whether <code>reasoning.max\_tokens</code> (via <code>thinking\_budget</code>) is available.
</Note>

For models that support reasoning token allocation, you can control it like this:

* `"max_tokens": 2000` - Directly specifies the maximum number of tokens to use for reasoning

For models that only support `reasoning.effort` (see below), the `max_tokens` value will be used to determine the effort level.

### Reasoning Effort Level

<Note title="Supported models">
  Currently supported by OpenAI reasoning models (o1 series, o3 series, GPT-5 series) and Grok models
</Note>

* `"effort": "high"` - Allocates a large portion of tokens for reasoning (approximately 80% of max\_tokens)
* `"effort": "medium"` - Allocates a moderate portion of tokens (approximately 50% of max\_tokens)
* `"effort": "low"` - Allocates a smaller portion of tokens (approximately 20% of max\_tokens)

For models that only support `reasoning.max_tokens`, the effort level will be set based on the percentages above.

### Excluding Reasoning Tokens

If you want the model to use reasoning internally but not include it in the response:

* `"exclude": true` - The model will still use reasoning, but it won't be returned in the response

Reasoning tokens will appear in the `reasoning` field of each message.

### Enable Reasoning with Default Config

To enable reasoning with the default parameters:

* `"enabled": true` - Enables reasoning at the "medium" effort level with no exclusions.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
