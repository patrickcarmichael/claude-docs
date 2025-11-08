---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Parallel Tool Calls

The API supports parallel execution of multiple tools:
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
              text: 'Calculate 10*5 and also tell me the weather in Miami',
            },
          ],
        },
      ],
      tools: [weatherTool, calculatorTool],
      tool_choice: 'auto',
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
                          'text': 'Calculate 10*5 and also tell me the weather in Miami',
                      },
                  ],
              },
          ],
          'tools': [weather_tool, calculator_tool],
          'tool_choice': 'auto',
          'max_output_tokens': 9000,
      }
  )

  result = response.json()
  print(result)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
