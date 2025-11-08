---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool Choice Options

Control when and how tools are called:

| Tool Choice                             | Description                         |
| --------------------------------------- | ----------------------------------- |
| `auto`                                  | Model decides whether to call tools |
| `none`                                  | Model will not call any tools       |
| `{type: 'function', name: 'tool_name'}` | Force specific tool call            |

### Force Specific Tool

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
              text: 'Hello, how are you?',
            },
          ],
        },
      ],
      tools: [weatherTool],
      tool_choice: { type: 'function', name: 'get_weather' },
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
                          'text': 'Hello, how are you?',
                      },
                  ],
              },
          ],
          'tools': [weather_tool],
          'tool_choice': {'type': 'function', 'name': 'get_weather'},
          'max_output_tokens': 9000,
      }
  )
```

### Disable Tool Calling

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
              text: 'What is the weather in Paris?',
            },
          ],
        },
      ],
      tools: [weatherTool],
      tool_choice: 'none',
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
                          'text': 'What is the weather in Paris?',
                      },
                  ],
              },
          ],
          'tools': [weather_tool],
          'tool_choice': 'none',
          'max_output_tokens': 9000,
      }
  )
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
