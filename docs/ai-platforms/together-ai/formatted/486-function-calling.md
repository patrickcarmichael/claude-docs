---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Function Calling

```python
  import os
  import json
  import openai

  client = openai.OpenAI(
      base_url="https://api.together.xyz/v1",
      api_key=os.environ["TOGETHER_API_KEY"],
  )

  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_current_weather",
              "description": "Get the current weather in a given location",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "The city and state, e.g. San Francisco, CA",
                      },
                      "unit": {
                          "type": "string",
                          "enum": ["celsius", "fahrenheit"],
                      },
                  },
              },
          },
      }
  ]

  messages = [
      {
          "role": "system",
          "content": "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls.",
      },
      {
          "role": "user",
          "content": "What is the current temperature of New York, San Francisco and Chicago?",
      },
  ]

  response = client.chat.completions.create(
      model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
      messages=messages,
      tools=tools,
      tool_choice="auto",
  )

  print(
      json.dumps(
          response.choices[0].message.model_dump()["tool_calls"],
          indent=2,
      )
  )
```

### Output

```json
  [
    {
      "id": "call_1p75qwks0etzfy1g6noxvsgs",
      "function": {
        "arguments": "{\"location\":\"New York, NY\",\"unit\":\"fahrenheit\"}",
        "name": "get_current_weather"
      },
      "type": "function"
    },
    {
      "id": "call_aqjfgn65d0c280fjd3pbzpc6",
      "function": {
        "arguments": "{\"location\":\"San Francisco, CA\",\"unit\":\"fahrenheit\"}",
        "name": "get_current_weather"
      },
      "type": "function"
    },
    {
      "id": "call_rsg8muko8hymb4brkycu3dm5",
      "function": {
        "arguments": "{\"location\":\"Chicago, IL\",\"unit\":\"fahrenheit\"}",
        "name": "get_current_weather"
      },
      "type": "function"
    }
  ]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
