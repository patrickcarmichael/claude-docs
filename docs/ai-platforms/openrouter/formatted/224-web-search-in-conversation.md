---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Web Search in Conversation

Include web search in multi-turn conversations:
```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: [
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'What is the latest version of React?',
            },
          ],
        },
        {
          type: 'message',
          id: 'msg_1',
          status: 'in_progress',
          role: 'assistant',
          content: [
            {
              type: 'output_text',
              text: 'Let me search for the latest React version.',
              annotations: [],
            },
          ],
        },
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'Yes, please find the most recent information',
            },
          ],
        },
      ],
      plugins: [{ id: 'web', max_results: 2 }],
      max_output_tokens: 9000,
    }),
  });

  const result = await response.json();
  console.log(result);
```
```python title="Python"
  import requests

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': [
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'What is the latest version of React?',
                      },
                  ],
              },
              {
                  'type': 'message',
                  'id': 'msg_1',
                  'status': 'in_progress',
                  'role': 'assistant',
                  'content': [
                      {
                          'type': 'output_text',
                          'text': 'Let me search for the latest React version.',
                          'annotations': [],
                      },
                  ],
              },
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'Yes, please find the most recent information',
                      },
                  ],
              },
          ],
          'plugins': [{'id': 'web', 'max_results': 2}],
          'max_output_tokens': 9000,
      }
  )

  result = response.json()
  print(result)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
