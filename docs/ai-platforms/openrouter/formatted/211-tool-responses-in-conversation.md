---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool Responses in Conversation

Include tool responses in follow-up requests:
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
              text: 'What is the weather in Boston?',
            },
          ],
        },
        {
          type: 'function_call',
          id: 'fc_1',
          call_id: 'call_123',
          name: 'get_weather',
          arguments: JSON.stringify({ location: 'Boston, MA' }),
        },
        {
          type: 'function_call_output',
          id: 'fc_output_1',
          call_id: 'call_123',
          output: JSON.stringify({ temperature: '72°F', condition: 'Sunny' }),
        },
        {
          type: 'message',
          role: 'assistant',
          id: 'msg_abc123',
          status: 'completed',
          content: [
            {
              type: 'output_text',
              text: 'The weather in Boston is currently 72°F and sunny. This looks like perfect weather for a picnic!',
              annotations: []
            }
          ]
        },
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'Is that good weather for a picnic?',
            },
          ],
        },
      ],
      max_output_tokens: 9000,
    }),
  });
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
                          'text': 'What is the weather in Boston?',
                      },
                  ],
              },
              {
                  'type': 'function_call',
                  'id': 'fc_1',
                  'call_id': 'call_123',
                  'name': 'get_weather',
                  'arguments': '{"location": "Boston, MA"}',
              },
              {
                  'type': 'function_call_output',
                  'id': 'fc_output_1',
                  'call_id': 'call_123',
                  'output': '{"temperature": "72°F", "condition": "Sunny"}',
              },
              {
                  'type': 'message',
                  'role': 'assistant',
                  'id': 'msg_abc123',
                  'status': 'completed',
                  'content': [
                      {
                          'type': 'output_text',
                          'text': 'The weather in Boston is currently 72°F and sunny. This looks like perfect weather for a picnic!',
                          'annotations': []
                      }
                  ]
              },
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'Is that good weather for a picnic?',
                      },
                  ],
              },
          ],
          'max_output_tokens': 9000,
      }
  )
```

<Info title="Required Field">
  The `id` field is required for `function_call_output` objects when including tool responses in conversation history.
</Info>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
