---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Responses API Shape

When reasoning models generate responses, the reasoning information is structured in a standardized format through the `reasoning_details` array. This section documents the API response structure for reasoning details in both streaming and non-streaming responses.

### reasoning\_details Array Structure

The `reasoning_details` field contains an array of reasoning detail objects. Each object in the array represents a specific piece of reasoning information and follows one of three possible types. The location of this array differs between streaming and non-streaming responses:

* **Non-streaming responses**: `reasoning_details` appears in `choices[].message.reasoning_details`
* **Streaming responses**: `reasoning_details` appears in `choices[].delta.reasoning_details` for each chunk

#### Common Fields

All reasoning detail objects share these common fields:

* `id` (string | null): Unique identifier for the reasoning detail
* `format` (string): The format of the reasoning detail, with possible values:
  * `"unknown"` - Format is not specified
  * `"openai-responses-v1"` - OpenAI responses format version 1
  * `"xai-responses-v1"` - xAI responses format version 1
  * `"anthropic-claude-v1"` - Anthropic Claude format version 1 (default)
* `index` (number, optional): Sequential index of the reasoning detail

#### Reasoning Detail Types

**1. Summary Type (`reasoning.summary`)**

Contains a high-level summary of the reasoning process:
```json
{
  "type": "reasoning.summary",
  "summary": "The model analyzed the problem by first identifying key constraints, then evaluating possible solutions...",
  "id": "reasoning-summary-1",
  "format": "anthropic-claude-v1",
  "index": 0
}
```
**2. Encrypted Type (`reasoning.encrypted`)**

Contains encrypted reasoning data that may be redacted or protected:
```json
{
  "type": "reasoning.encrypted",
  "data": "eyJlbmNyeXB0ZWQiOiJ0cnVlIiwiY29udGVudCI6IltSRURBQ1RFRF0ifQ==",
  "id": "reasoning-encrypted-1",
  "format": "anthropic-claude-v1",
  "index": 1
}
```
**3. Text Type (`reasoning.text`)**

Contains raw text reasoning with optional signature verification:
```json
{
  "type": "reasoning.text",
  "text": "Let me think through this step by step:\n1. First, I need to understand the user's question...",
  "signature": "sha256:abc123def456...",
  "id": "reasoning-text-1",
  "format": "anthropic-claude-v1",
  "index": 2
}
```

### Response Examples

#### Non-Streaming Response

In non-streaming responses, `reasoning_details` appears in the message:
```json
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Based on my analysis, I recommend the following approach...",
        "reasoning_details": [
          {
            "type": "reasoning.summary",
            "summary": "Analyzed the problem by breaking it into components",
            "id": "reasoning-summary-1",
            "format": "anthropic-claude-v1",
            "index": 0
          },
          {
            "type": "reasoning.text",
            "text": "Let me work through this systematically:\n1. First consideration...\n2. Second consideration...",
            "signature": null,
            "id": "reasoning-text-1",
            "format": "anthropic-claude-v1",
            "index": 1
          }
        ]
      }
    }
  ]
}
```

#### Streaming Response

In streaming responses, `reasoning_details` appears in delta chunks as the reasoning is generated:
```json
{
  "choices": [
    {
      "delta": {
        "reasoning_details": [
          {
            "type": "reasoning.text",
            "text": "Let me think about this step by step...",
            "signature": null,
            "id": "reasoning-text-1",
            "format": "anthropic-claude-v1",
            "index": 0
          }
        ]
      }
    }
  ]
}
```
**Streaming Behavior Notes:**

* Each reasoning detail chunk is sent as it becomes available
* The `reasoning_details` array in each chunk may contain one or more reasoning objects
* For encrypted reasoning, the content may appear as `[REDACTED]` in streaming responses
* The complete reasoning sequence is built by concatenating all chunks in order

### Example: Preserving Reasoning Blocks with OpenRouter and Claude

<Template
  data={{
  API_KEY_REF,
  MODEL: 'anthropic/claude-sonnet-4'
}}
>
```python
    from openai import OpenAI

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="{{API_KEY_REF}}",
    )

    # Define tools once and reuse

    tools = [{
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                },
                "required": ["location"]
            }
        }
    }]

    # First API call with tools

    # Note: You can use 'openai/gpt-5-mini' instead of 'anthropic/claude-sonnet-4' - they're completely interchangeable

    response = client.chat.completions.create(
        model="{{MODEL}}",
        messages=[
            {"role": "user", "content": "What's the weather like in Boston? Then recommend what to wear."}
        ],
        tools=tools,
        extra_body={"reasoning": {"max_tokens": 2000}}
    )

    # Extract the assistant message with reasoning_details

    message = response.choices[0].message

    # Preserve the complete reasoning_details when passing back

    messages = [
        {"role": "user", "content": "What's the weather like in Boston? Then recommend what to wear."},
        {
            "role": "assistant",
            "content": message.content,
            "tool_calls": message.tool_calls,
            "reasoning_details": message.reasoning_details  # Pass back unmodified

        },
        {
            "role": "tool",
            "tool_call_id": message.tool_calls[0].id,
            "content": '{"temperature": 45, "condition": "rainy", "humidity": 85}'
        }
    ]

    # Second API call - Claude continues reasoning from where it left off

    response2 = client.chat.completions.create(
        model="{{MODEL}}",
        messages=messages,  # Includes preserved thinking blocks

        tools=tools
    )
```
```typescript
    import OpenAI from 'openai';

    const client = new OpenAI({
      baseURL: 'https://openrouter.ai/api/v1',
      apiKey: '{{API_KEY_REF}}',
    });

    // Define tools once and reuse
    const tools = [
      {
        type: 'function',
        function: {
          name: 'get_weather',
          description: 'Get current weather',
          parameters: {
            type: 'object',
            properties: {
              location: { type: 'string' },
            },
            required: ['location'],
          },
        },
      },
    ] as const;

    // First API call with tools
    // Note: You can use 'openai/gpt-5-mini' instead of 'anthropic/claude-sonnet-4' - they're completely interchangeable
    const response = await client.chat.completions.create({
      model: '{{MODEL}}',
      messages: [
        {
          role: 'user',
          content:
            "What's the weather like in Boston? Then recommend what to wear.",
        },
      ],
      tools,
      reasoning: { max_tokens: 2000 },
    });

    // Extract the assistant message with reasoning_details
    type ORChatMessage = (typeof response)['choices'][number]['message'] & {
      reasoning_details?: unknown;
    };
    const message = response.choices[0].message as ORChatMessage;

    // Preserve the complete reasoning_details when passing back
    const messages = [
      {
        role: 'user' as const,
        content: "What's the weather like in Boston? Then recommend what to wear.",
      },
      {
        role: 'assistant' as const,
        content: message.content,
        tool_calls: message.tool_calls,
        reasoning_details: message.reasoning_details, // Pass back unmodified
      },
      {
        role: 'tool' as const,
        tool_call_id: message.tool_calls?.[0]?.id,
        content: JSON.stringify({
          temperature: 45,
          condition: 'rainy',
          humidity: 85,
        }),
      },
    ];

    // Second API call - Claude continues reasoning from where it left off
    const response2 = await client.chat.completions.create({
      model: '{{MODEL}}',
      messages, // Includes preserved thinking blocks
      tools,
    });
```
</Template>

For more detailed information about thinking encryption, redacted blocks, and advanced use cases, see [Anthropic's documentation on extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/tool-use#extended-thinking).

For more information about OpenAI reasoning models, see [OpenAI's reasoning documentation](https://platform.openai.com/docs/guides/reasoning#keeping-reasoning-items-in-context).


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
