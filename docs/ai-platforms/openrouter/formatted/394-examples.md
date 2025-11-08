---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Examples

### Basic Usage with Token Tracking

<Template
  data={{
  API_KEY_REF,
  MODEL: "anthropic/claude-3-opus"
}}
>
```typescript title="TypeScript SDK"
    import { OpenRouter } from '@openrouter/sdk';

    const openRouter = new OpenRouter({
      apiKey: '{{API_KEY_REF}}',
    });

    const response = await openRouter.chat.send({
      model: '{{MODEL}}',
      messages: [
        {
          role: 'user',
          content: 'What is the capital of France?',
        },
      ],
      usage: {
        include: true,
      },
      stream: false,
    });

    console.log('Response:', response.choices[0].message.content);
    console.log('Usage Stats:', response.usage);
```
```python title="Python (OpenAI SDK)"
    from openai import OpenAI

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="{{API_KEY_REF}}",
    )

    response = client.chat.completions.create(
        model="{{MODEL}}",
        messages=[
            {"role": "user", "content": "What is the capital of France?"}
        ],
        extra_body={
            "usage": {
                "include": True
            }
        }
    )

    print("Response:", response.choices[0].message.content)
    print("Usage Stats:", getattr(response, "usage", None))
```
```typescript title="TypeScript (OpenAI SDK)"
    import OpenAI from 'openai';

    const openai = new OpenAI({
      baseURL: 'https://openrouter.ai/api/v1',
      apiKey: '{{API_KEY_REF}}',
    });

    async function getResponseWithUsage() {
      const response = await openai.chat.completions.create({
        model: '{{MODEL}}',
        messages: [
          {
            role: 'user',
            content: 'What is the capital of France?',
          },
        ],
        usage: {
          include: true,
        },
      });

      console.log('Response:', response.choices[0].message.content);
      console.log('Usage Stats:', response.usage);
    }

    getResponseWithUsage();
```
</Template>

### Streaming with Usage Information

This example shows how to handle usage information in streaming mode:

<Template
  data={{
  API_KEY_REF,
  MODEL: "anthropic/claude-3-opus"
}}
>
```python Python
    from openai import OpenAI

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="{{API_KEY_REF}}",
    )

    def chat_completion_with_usage(messages):
        response = client.chat.completions.create(
            model="{{MODEL}}",
            messages=messages,
            extra_body={
                "usage": {
                    "include": True
                }
            },
            stream=True
        )
        return response

    for chunk in chat_completion_with_usage([
        {"role": "user", "content": "Write a haiku about Paris."}
    ]):
        if hasattr(chunk, 'usage'):
            if hasattr(chunk.usage, 'total_tokens'):
                print(f"\nUsage Statistics:")
                print(f"Total Tokens: {chunk.usage.total_tokens}")
                print(f"Prompt Tokens: {chunk.usage.prompt_tokens}")
                print(f"Completion Tokens: {chunk.usage.completion_tokens}")
                print(f"Cost: {chunk.usage.cost} credits")
        elif chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")
```
```typescript TypeScript
    import OpenAI from 'openai';

    const openai = new OpenAI({
      baseURL: 'https://openrouter.ai/api/v1',
      apiKey: '{{API_KEY_REF}}',
    });

    async function chatCompletionWithUsage(messages) {
      const response = await openai.chat.completions.create({
        model: '{{MODEL}}',
        messages,
        usage: {
          include: true,
        },
        stream: true,
      });

      return response;
    }

    (async () => {
      for await (const chunk of chatCompletionWithUsage([
        { role: 'user', content: 'Write a haiku about Paris.' },
      ])) {
        if (chunk.usage) {
          console.log('\nUsage Statistics:');
          console.log(`Total Tokens: ${chunk.usage.total_tokens}`);
          console.log(`Prompt Tokens: ${chunk.usage.prompt_tokens}`);
          console.log(`Completion Tokens: ${chunk.usage.completion_tokens}`);
          console.log(`Cost: ${chunk.usage.cost} credits`);
        } else if (chunk.choices[0].delta.content) {
          process.stdout.write(chunk.choices[0].delta.content);
        }
      }
    })();
```
</Template>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
