---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## ! pip install -U cohere

import cohere
import json

co = cohere.ClientV2(
    "COHERE_API_KEY"
)  # Get your free API key here: https://dashboard.cohere.com/api-keys

messages = [
    {
        "role": "user",
        "content": "What's the weather in Madrid and Brasilia?",
    },
    {
        "role": "assistant",
        "tool_plan": "I will search for the weather in Madrid and Brasilia.",
        "tool_calls": [
            {
                "id": "get_weather_dkf0akqdazjb",
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "arguments": '{"location":"Madrid"}',
                },
            },
            {
                "id": "get_weather_gh65bt2tcdy1",
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "arguments": '{"location":"Brasilia"}',
                },
            },
        ],
    },
    {
        "role": "tool",
        "tool_call_id": "get_weather_dkf0akqdazjb",
        "content": [
            {
                "type": "document",
                "document": {
                    "data": '{"temperature": {"madrid": "24°C"}}',
                    "id": "1",
                },
            }
        ],
    },
    {
        "role": "tool",
        "tool_call_id": "get_weather_gh65bt2tcdy1",
        "content": [
            {
                "type": "document",
                "document": {
                    "data": '{"temperature": {"brasilia": "28°C"}}',
                    "id": "2",
                },
            }
        ],
    },
]
```
When document IDs are provided, the citation will refer to the documents using these IDs.

<CodeBlocks>
```python PYTHON
  response = co.chat(
      model="command-a-03-2025", messages=messages, tools=tools
  )

  print(response.message.content[0].text)

  for citation in response.message.citations:
      print(citation, "\n")
```
```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
    "model": "command-a-03-2025",
    "messages": [
      {
        "role": "user",
        "content": "What'\''s the weather in Madrid and Brasilia?"
      },
      {
        "role": "assistant",
        "tool_plan": "I will search for the weather in Madrid and Brasilia.",
        "tool_calls": [
          {
            "id": "get_weather_dkf0akqdazjb",
            "type": "function",
            "function": {
              "name": "get_weather",
              "arguments": "{\"location\":\"Madrid\"}"
            }
          },
          {
            "id": "get_weather_gh65bt2tcdy1",
            "type": "function",
            "function": {
              "name": "get_weather",
              "arguments": "{\"location\":\"Brasilia\"}"
            }
          }
        ]
      },
      {
        "role": "tool",
        "tool_call_id": "get_weather_dkf0akqdazjb",
        "content": [
          {
            "type": "document",
            "document": {
              "data": "{\"temperature\": {\"madrid\": \"24°C\"}}",
              "id": "1"
            }
          }
        ]
      },
      {
        "role": "tool",
        "tool_call_id": "get_weather_gh65bt2tcdy1",
        "content": [
          {
            "type": "document",
            "document": {
              "data": "{\"temperature\": {\"brasilia\": \"28°C\"}}",
              "id": "2"
            }
          }
        ]
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "gets the weather of a given location",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "the location to get the weather, example: San Francisco."
              }
            },
            "required": ["location"]
          }
        }
      }
    ]
  }'
```
</CodeBlocks>

Note the `id` fields in the citations, which refer to the IDs in the `document` object.

Example response:
```mdx wordWrap
It's 24°C in Madrid and 28°C in Brasilia.

start=5 end=9 text='24°C' sources=[ToolSource(type='tool', id='1', tool_output={'temperature': '{"madrid":"24°C"}'})] type='TEXT_CONTENT' 

start=24 end=28 text='28°C' sources=[ToolSource(type='tool', id='2', tool_output={'temperature': '{"brasilia":"28°C"}'})] type='TEXT_CONTENT' 
```
In contrast, here's an example citation when the IDs are not provided.

Example response:
```mdx wordWrap
It is currently 24°C in Madrid and 28°C in Brasilia.

start=16 end=20 text='24°C' sources=[ToolSource(type='tool', id='get_weather_dkf0akqdazjb:0', tool_output={'temperature': '{"madrid":"24°C"}'})] type='TEXT_CONTENT' 

start=35 end=39 text='28°C' sources=[ToolSource(type='tool', id='get_weather_gh65bt2tcdy1:0', tool_output={'temperature': '{"brasilia":"28°C"}'})] type='TEXT_CONTENT' 
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
