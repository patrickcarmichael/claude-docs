---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Function Calling

```python
  from openai import OpenAI
  import os, json

  client = OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_weather",
              "description": "Get current temperature for a given location.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "City and country e.g. Bogotá, Colombia",
                      }
                  },
                  "required": ["location"],
                  "additionalProperties": False,
              },
              "strict": True,
          },
      }
  ]

  completion = client.chat.completions.create(
      model="zai-org/GLM-4.5-Air-FP8",
      messages=[
          {"role": "user", "content": "What is the weather like in Paris today?"}
      ],
      tools=tools,
      tool_choice="auto",
  )

  print(
      json.dumps(
          completion.choices[0].message.model_dump()["tool_calls"], indent=2
      )
  )
```
```typescript
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: 'https://api.together.xyz/v1',
  });

  const tools = [{
      "type": "function",
      "function": {
          "name": "get_weather",
          "description": "Get current temperature for a given location.",
          "parameters": {
              "type": "object",
              "properties": {
                  "location": {
                      "type": "string",
                      "description": "City and country e.g. Bogotá, Colombia"
                  }
              },
              "required": [
                  "location"
              ],
              "additionalProperties": false
          },
          "strict": true
      }
  }];

  const completion = await openai.chat.completions.create({
      model: "zai-org/GLM-4.5-Air-FP8",
      messages: [{ role: "user", content: "What is the weather like in Paris today?" }],
      tools,
      store: true,
  });

  console.log(completion.choices[0].message.tool_calls);
```

Output:
```text
[
  {
    "id": "call_nu2ifnvqz083p5kngs3a3aqz",
    "function": {
      "arguments": "{\"location\":\"Paris, France\"}",
      "name": "get_weather"
    },
    "type": "function",
    "index": 0
  }
]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
