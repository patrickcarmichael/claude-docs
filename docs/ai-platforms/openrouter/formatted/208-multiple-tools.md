---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Multiple Tools

Define multiple tools for complex workflows:
```typescript title="TypeScript"
  const calculatorTool = {
    type: 'function' as const,
    name: 'calculate',
    description: 'Perform mathematical calculations',
    strict: null,
    parameters: {
      type: 'object',
      properties: {
        expression: {
          type: 'string',
          description: 'The mathematical expression to evaluate',
        },
      },
      required: ['expression'],
    },
  };

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
              text: 'What is 25 * 4?',
            },
          ],
        },
      ],
      tools: [weatherTool, calculatorTool],
      tool_choice: 'auto',
      max_output_tokens: 9000,
    }),
  });
```
```python title="Python"
  calculator_tool = {
      'type': 'function',
      'name': 'calculate',
      'description': 'Perform mathematical calculations',
      'strict': None,
      'parameters': {
          'type': 'object',
          'properties': {
              'expression': {
                  'type': 'string',
                  'description': 'The mathematical expression to evaluate',
              },
          },
          'required': ['expression'],
      },
  }

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
                          'text': 'What is 25 * 4?',
                      },
                  ],
              },
          ],
          'tools': [weather_tool, calculator_tool],
          'tool_choice': 'auto',
          'max_output_tokens': 9000,
      }
  )
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
