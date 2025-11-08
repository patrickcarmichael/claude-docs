---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Streaming

<Accordion title="Using tool calls with streaming responses">
  Tool calls work with streaming responses. Arguments are sent incrementally as the model generates them:
```python
  import json
  import os
  from openai import OpenAI

  client = OpenAI(
      api_key=os.environ.get("FIREWORKS_API_KEY"),
      base_url="https://api.fireworks.ai/inference/v1"
  )

  tools = [{
      "type": "function",
      "function": {
          "name": "get_weather",
          "description": "Get the current weather for a city",
          "parameters": {
              "type": "object",
              "properties": {
                  "city": {"type": "string", "description": "City name"},
                  "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
              },
              "required": ["city"]
          }
      }
  }]

  stream = client.chat.completions.create(
      model="accounts/fireworks/models/kimi-k2-instruct-0905",
      messages=[{"role": "user", "content": "What's the weather in San Francisco?"}],
      tools=tools,
      stream=True,
      temperature=0.1
  )

  # Accumulate tool call data

  tool_calls = {}

  for chunk in stream:
      if chunk.choices[0].delta.tool_calls:
          for tool_call in chunk.choices[0].delta.tool_calls:
              index = tool_call.index
              
              if index not in tool_calls:
                  tool_calls[index] = {"id": "", "name": "", "arguments": ""}
              
              if tool_call.id:
                  tool_calls[index]["id"] = tool_call.id
              if tool_call.function and tool_call.function.name:
                  tool_calls[index]["name"] = tool_call.function.name
              if tool_call.function and tool_call.function.arguments:
                  tool_calls[index]["arguments"] += tool_call.function.arguments
      
      if chunk.choices[0].finish_reason == "tool_calls":
          for tool_call in tool_calls.values():
              args = json.loads(tool_call["arguments"])
              print(f"Calling {tool_call['name']} with {args}")
          break
```
</Accordion>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
