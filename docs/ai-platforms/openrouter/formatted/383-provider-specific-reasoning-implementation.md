---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Provider-Specific Reasoning Implementation

### Anthropic Models with Reasoning Tokens

The latest Claude models, such as [anthropic/claude-3.7-sonnet](https://openrouter.ai/anthropic/claude-3.7-sonnet), support working with and returning reasoning tokens.

You can enable reasoning on Anthropic models **only** using the unified `reasoning` parameter with either `effort` or `max_tokens`.

**Note:** The `:thinking` variant is no longer supported for Anthropic models. Use the `reasoning` parameter instead.

#### Reasoning Max Tokens for Anthropic Models

When using Anthropic models with reasoning:

* When using the `reasoning.max_tokens` parameter, that value is used directly with a minimum of 1024 tokens.
* When using the `reasoning.effort` parameter, the budget\_tokens are calculated based on the `max_tokens` value.

The reasoning token allocation is capped at 32,000 tokens maximum and 1024 tokens minimum. The formula for calculating the budget\_tokens is: `budget_tokens = max(min(max_tokens * {effort_ratio}, 32000), 1024)`

effort\_ratio is 0.8 for high effort, 0.5 for medium effort, and 0.2 for low effort.

**Important**: `max_tokens` must be strictly higher than the reasoning budget to ensure there are tokens available for the final response after thinking.

<Note title="Token Usage and Billing">
  Please note that reasoning tokens are counted as output tokens for billing
  purposes. Using reasoning tokens will increase your token usage but can
  significantly improve the quality of model responses.
</Note>

### Examples with Anthropic Models

#### Example 1: Streaming mode with reasoning tokens

<Template
  data={{
  API_KEY_REF,
  MODEL: "anthropic/claude-3.7-sonnet"
}}
>
```python Python
    from openai import OpenAI

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="{{API_KEY_REF}}",
    )

    def chat_completion_with_reasoning(messages):
        response = client.chat.completions.create(
            model="{{MODEL}}",
            messages=messages,
            max_tokens=10000,
            extra_body={
                "reasoning": {
                    "max_tokens": 8000
                }
            },
            stream=True
        )
        return response

    for chunk in chat_completion_with_reasoning([
        {"role": "user", "content": "What's bigger, 9.9 or 9.11?"}
    ]):
        if hasattr(chunk.choices[0].delta, 'reasoning_details') and chunk.choices[0].delta.reasoning_details:
            print(f"REASONING_DETAILS: {chunk.choices[0].delta.reasoning_details}")
        elif getattr(chunk.choices[0].delta, 'content', None):
            print(f"CONTENT: {chunk.choices[0].delta.content}")
```
```typescript TypeScript
    import OpenAI from 'openai';

    const openai = new OpenAI({
      baseURL: 'https://openrouter.ai/api/v1',
      apiKey: '{{API_KEY_REF}}',
    });

    async function chatCompletionWithReasoning(messages) {
      const response = await openai.chat.completions.create({
        model: '{{MODEL}}',
        messages,
        max_tokens: 10000,
        reasoning: {
          max_tokens: 8000,
        },
        stream: true,
      });

      return response;
    }

    (async () => {
      for await (const chunk of chatCompletionWithReasoning([
        { role: 'user', content: "What's bigger, 9.9 or 9.11?" },
      ])) {
        if (chunk.choices[0].delta?.reasoning_details) {
          console.log(`REASONING_DETAILS:`, chunk.choices[0].delta.reasoning_details);
        } else if (chunk.choices[0].delta?.content) {
          console.log(`CONTENT: ${chunk.choices[0].delta.content}`);
        }
      }
    })();
```
</Template>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
