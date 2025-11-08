---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example Implementation

Here's a complete example using the Fetch API:

<Template
  data={{
  API_KEY_REF,
  MODEL: 'openai/gpt-4'
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
        { role: 'user', content: 'What is the weather like in London?' },
      ],
      responseFormat: {
        type: 'json_schema',
        jsonSchema: {
          name: 'weather',
          strict: true,
          schema: {
            type: 'object',
            properties: {
              location: {
                type: 'string',
                description: 'City or location name',
              },
              temperature: {
                type: 'number',
                description: 'Temperature in Celsius',
              },
              conditions: {
                type: 'string',
                description: 'Weather conditions description',
              },
            },
            required: ['location', 'temperature', 'conditions'],
            additionalProperties: false,
          },
        },
      },
      stream: false,
    });

    const weatherInfo = response.choices[0].message.content;
```
```python title="Python"
    import requests
    import json

    response = requests.post(
      "https://openrouter.ai/api/v1/chat/completions",
      headers={
        "Authorization": f"Bearer {{API_KEY_REF}}",
        "Content-Type": "application/json",
      },

      json={
        "model": "{{MODEL}}",
        "messages": [
          {"role": "user", "content": "What is the weather like in London?"},
        ],
        "response_format": {
          "type": "json_schema",
          "json_schema": {
            "name": "weather",
            "strict": True,
            "schema": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "City or location name",
                },
                "temperature": {
                  "type": "number",
                  "description": "Temperature in Celsius",
                },
                "conditions": {
                  "type": "string",
                  "description": "Weather conditions description",
                },
              },
              "required": ["location", "temperature", "conditions"],
              "additionalProperties": False,
            },
          },
        },
      },
    )

    data = response.json()
    weather_info = data["choices"][0]["message"]["content"]
```
```typescript title="TypeScript (fetch)"
    const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: {
        Authorization: 'Bearer {{API_KEY_REF}}',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: '{{MODEL}}',
        messages: [
          { role: 'user', content: 'What is the weather like in London?' },
        ],
        response_format: {
          type: 'json_schema',
          json_schema: {
            name: 'weather',
            strict: true,
            schema: {
              type: 'object',
              properties: {
                location: {
                  type: 'string',
                  description: 'City or location name',
                },
                temperature: {
                  type: 'number',
                  description: 'Temperature in Celsius',
                },
                conditions: {
                  type: 'string',
                  description: 'Weather conditions description',
                },
              },
              required: ['location', 'temperature', 'conditions'],
              additionalProperties: false,
            },
          },
        },
      }),
    });

    const data = await response.json();
    const weatherInfo = data.choices[0].message.content;
```
</Template>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
