---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Using with OpenAI SDK

To use the `models` array with the OpenAI SDK, include it in the `extra_body` parameter. In the example below, gpt-4o will be tried first, and the `models` array will be tried in order as fallbacks.

<Template
  data={{
  API_KEY_REF,
}}
>
```python
    from openai import OpenAI

    openai_client = OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key={{API_KEY_REF}},
    )

    completion = openai_client.chat.completions.create(
        model="openai/gpt-4o",
        extra_body={
            "models": ["anthropic/claude-3.5-sonnet", "gryphe/mythomax-l2-13b"],
        },
        messages=[
            {
                "role": "user",
                "content": "What is the meaning of life?"
            }
        ]
    )

    print(completion.choices[0].message.content)
```
```typescript
    import OpenAI from 'openai';

    const openrouterClient = new OpenAI({
      baseURL: 'https://openrouter.ai/api/v1',
      apiKey: '{{API_KEY_REF}}',
    });

    async function main() {
      // @ts-expect-error
      const completion = await openrouterClient.chat.completions.create({
        model: 'openai/gpt-4o',
        models: ['anthropic/claude-3.5-sonnet', 'gryphe/mythomax-l2-13b'],
        messages: [
          {
            role: 'user',
            content: 'What is the meaning of life?',
          },
        ],
      });
      console.log(completion.choices[0].message);
    }

    main();
```
</Template>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
