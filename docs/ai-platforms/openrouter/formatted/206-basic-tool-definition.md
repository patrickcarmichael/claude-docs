---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Basic Tool Definition

Define tools using the OpenAI function calling format:
```typescript title="TypeScript"
  const weatherTool = {
    type: 'function' as const,
    name: 'get_weather',
    description: 'Get the current weather in a location',
    strict: null,
    parameters: {
      type: 'object',
      properties: {
        location: {
          type: 'string',
          description: 'The city and state, e.g. San Francisco, CA',
        },
        unit: {
          type: 'string',
          enum: ['celsius', 'fahrenheit'],
        },
      },
      required: ['location'],
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
              text: 'What is the weather in San Francisco?',
            },
          ],
        },
      ],
      tools: [weatherTool],
      tool_choice: 'auto',
      max_output_tokens: 9000,
    }),
  });

  const result = await response.json();
  console.log(result);
```
```python title="Python"
  import requests

  weather_tool = {
      'type': 'function',
      'name': 'get_weather',
      'description': 'Get the current weather in a location',
      'strict': None,
      'parameters': {
          'type': 'object',
          'properties': {
              'location': {
                  'type': 'string',
                  'description': 'The city and state, e.g. San Francisco, CA',
              },
              'unit': {
                  'type': 'string',
                  'enum': ['celsius', 'fahrenheit'],
              },
          },
          'required': ['location'],
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
                          'text': 'What is the weather in San Francisco?',
                      },
                  ],
              },
          ],
          'tools': [weather_tool],
          'tool_choice': 'auto',
          'max_output_tokens': 9000,
      }
  )

  result = response.json()
  print(result)
```
```bash title="cURL"
  curl -X POST https://openrouter.ai/api/v1/responses \
    -H "Authorization: Bearer YOUR_OPENROUTER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/o4-mini",
      "input": [
        {
          "type": "message",
          "role": "user",
          "content": [
            {
              "type": "input_text",
              "text": "What is the weather in San Francisco?"
            }
          ]
        }
      ],
      "tools": [
        {
          "type": "function",
          "name": "get_weather",
          "description": "Get the current weather in a location",
          "strict": null,
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA"
              },
              "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"]
              }
            },
            "required": ["location"]
          }
        }
      ],
      "tool_choice": "auto",
      "max_output_tokens": 9000
    }'
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
