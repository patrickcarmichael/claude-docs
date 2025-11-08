---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Implementation Examples

```typescript title="TypeScript SDK"
  import { OpenRouter } from '@openrouter/sdk';

  const openRouter = new OpenRouter({
    apiKey: '<OPENROUTER_API_KEY>',
    defaultHeaders: {
      'HTTP-Referer': 'https://myapp.com', // Your app's URL
      'X-Title': 'My AI Assistant', // Your app's display name
    },
  });

  const completion = await openRouter.chat.send({
    model: 'openai/gpt-4o',
    messages: [
      {
        role: 'user',
        content: 'Hello, world!',
      },
    ],
    stream: false,
  });

  console.log(completion.choices[0].message);
```
```python title="Python (OpenAI SDK)"
  from openai import OpenAI

  client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="<OPENROUTER_API_KEY>",
  )

  completion = client.chat.completions.create(
    extra_headers={
      "HTTP-Referer": "https://myapp.com", # Your app's URL

      "X-Title": "My AI Assistant", # Your app's display name

    },
    model="openai/gpt-4o",
    messages=[
      {
        "role": "user",
        "content": "Hello, world!"
      }
    ]
  )
```
```typescript title="TypeScript (OpenAI SDK)"
  import OpenAI from 'openai';

  const openai = new OpenAI({
    baseURL: 'https://openrouter.ai/api/v1',
    apiKey: '<OPENROUTER_API_KEY>',
    defaultHeaders: {
      'HTTP-Referer': 'https://myapp.com', // Your app's URL
      'X-Title': 'My AI Assistant', // Your app's display name
    },
  });

  async function main() {
    const completion = await openai.chat.completions.create({
      model: 'openai/gpt-4o',
      messages: [
        {
          role: 'user',
          content: 'Hello, world!',
        },
      ],
    });

    console.log(completion.choices[0].message);
  }

  main();
```
```python title="Python (Direct API)"
  import requests
  import json

  response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
      "Authorization": "Bearer <OPENROUTER_API_KEY>",
      "HTTP-Referer": "https://myapp.com", # Your app's URL

      "X-Title": "My AI Assistant", # Your app's display name

      "Content-Type": "application/json",
    },
    data=json.dumps({
      "model": "openai/gpt-4o",
      "messages": [
        {
          "role": "user",
          "content": "Hello, world!"
        }
      ]
    })
  )
```
```typescript title="TypeScript (fetch)"
  fetch('https://openrouter.ai/api/v1/chat/completions', {
    method: 'POST',
    headers: {
      Authorization: 'Bearer <OPENROUTER_API_KEY>',
      'HTTP-Referer': 'https://myapp.com', // Your app's URL
      'X-Title': 'My AI Assistant', // Your app's display name
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/gpt-4o',
      messages: [
        {
          role: 'user',
          content: 'Hello, world!',
        },
      ],
    }),
  });
```
```shell title="cURL"
  curl https://openrouter.ai/api/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENROUTER_API_KEY" \
    -H "HTTP-Referer: https://myapp.com" \
    -H "X-Title: My AI Assistant" \
    -d '{
    "model": "openai/gpt-4o",
    "messages": [
      {
        "role": "user",
        "content": "Hello, world!"
      }
    ]
  }'
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
