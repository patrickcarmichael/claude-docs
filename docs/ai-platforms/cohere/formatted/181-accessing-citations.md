---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Accessing citations

The Chat endpoint generates fine-grained citations for its tool use response. This capability is included out-of-the-box with the Command family of models.

The following sections describe how to access the citations in both the non-streaming and streaming modes.

### Non-streaming

First, define the tool and its associated schema.

<Tabs>
  <Tab title="Cohere platform">
```python PYTHON
    # ! pip install -U cohere

    import cohere
    import json

    co = cohere.ClientV2(
        "COHERE_API_KEY"
    )  # Get your free API key here: https://dashboard.cohere.com/api-keys

```
  </Tab>

  <Tab title="Private deployment">
```python PYTHON
    # ! pip install -U cohere

    import cohere
    import json

    co = cohere.ClientV2(
        api_key="",  # Leave this blank

        base_url="<YOUR_DEPLOYMENT_URL>",
    )
```
  </Tab>
</Tabs>
```python PYTHON
def get_weather(location):
    temperature = {
        "bern": "22°C",
        "madrid": "24°C",
        "brasilia": "28°C",
    }
    loc = location.lower()
    if loc in temperature:
        return [{"temperature": {loc: temperature[loc]}}]
    return [{"temperature": {loc: "Unknown"}}]


functions_map = {"get_weather": get_weather}

tools = [
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
                        "description": "the location to get the weather, example: San Francisco.",
                    }
                },
                "required": ["location"],
            },
        },
    }
]
```
Next, run the tool calling and execution steps.

<CodeBlocks>
```python PYTHON
  messages = [
      {
          "role": "user",
          "content": "What's the weather in Madrid and Brasilia?",
      }
  ]

  response = co.chat(
      model="command-a-03-2025", messages=messages, tools=tools
  )

  if response.message.tool_calls:
      messages.append(
          {
              "role": "assistant",
              "tool_plan": response.message.tool_plan,
              "tool_calls": response.message.tool_calls,
          }
      )

      for tc in response.message.tool_calls:
          tool_result = functions_map[tc.function.name](
              **json.loads(tc.function.arguments)
          )
          tool_content = []
          for data in tool_result:
              tool_content.append(
                  {
                      "type": "document",
                      "document": {"data": json.dumps(data)},
                  }
              )
          messages.append(
              {
                  "role": "tool",
                  "tool_call_id": tc.id,
                  "content": tool_content,
              }
          )
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

In the non-streaming mode (using `chat` to generate the model response), the citations are provided in the `message.citations` field of the response object.

Each citation object contains:

* `start` and `end`: the start and end indices of the text that cites a source(s)
* `text`: its corresponding span of text
* `sources`: the source(s) that it references

<CodeBlocks>
```python PYTHON
  response = co.chat(
      model="command-a-03-2025", messages=messages, tools=tools
  )

  messages.append(
      {"role": "assistant", "content": response.message.content[0].text}
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
            "id": "get_weather_14brd1n2kfqj",
            "type": "function",
            "function": {
              "name": "get_weather",
              "arguments": "{\"location\":\"Madrid\"}"
            }
          },
          {
            "id": "get_weather_vdr9cvj619fk",
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
        "tool_call_id": "get_weather_14brd1n2kfqj",
        "content": [
          {
            "type": "document",
            "document": {
              "data": "{\"temperature\": {\"madrid\": \"24°C\"}}"
            }
          }
        ]
      },
      {
        "role": "tool",
        "tool_call_id": "get_weather_vdr9cvj619fk",
        "content": [
          {
            "type": "document",
            "document": {
              "data": "{\"temperature\": {\"brasilia\": \"28°C\"}}"
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

Example response:
```mdx wordWrap
It is currently 24°C in Madrid and 28°C in Brasilia.

start=16 end=20 text='24°C' sources=[ToolSource(type='tool', id='get_weather_14brd1n2kfqj:0', tool_output={'temperature': '{"madrid":"24°C"}'})] type='TEXT_CONTENT' 

start=35 end=39 text='28°C' sources=[ToolSource(type='tool', id='get_weather_vdr9cvj619fk:0', tool_output={'temperature': '{"brasilia":"28°C"}'})] type='TEXT_CONTENT'
```

### Streaming

In a streaming scenario (using `chat_stream` to generate the model response), the citations are provided in the `citation-start` events.

Each citation object contains the same fields as the [non-streaming scenario](#non-streaming).

<CodeBlocks>
```python PYTHON
  response = co.chat_stream(
      model="command-a-03-2025", messages=messages, tools=tools
  )

  response_text = ""
  citations = []
  for chunk in response:
      if chunk:
          if chunk.type == "content-delta":
              response_text += chunk.delta.message.content.text
              print(chunk.delta.message.content.text, end="")
          if chunk.type == "citation-start":
              citations.append(chunk.delta.message.citations)

  messages.append({"role": "assistant", "content": response_text})

  for citation in citations:
      print(citation, "\n")
```
```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: text/event-stream' \
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
              "data": "{\"temperature\": {\"madrid\": \"24°C\"}}"
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
              "data": "{\"temperature\": {\"brasilia\": \"28°C\"}}"
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
    ],
    "stream": true
  }'
```
</CodeBlocks>

Example response:
```mdx wordWrap
It is currently 24°C in Madrid and 28°C in Brasilia.

start=16 end=20 text='24°C' sources=[ToolSource(type='tool', id='get_weather_dkf0akqdazjb:0', tool_output={'temperature': '{"madrid":"24°C"}'})] type='TEXT_CONTENT' 

start=35 end=39 text='28°C' sources=[ToolSource(type='tool', id='get_weather_gh65bt2tcdy1:0', tool_output={'temperature': '{"brasilia":"28°C"}'})] type='TEXT_CONTENT' 
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
