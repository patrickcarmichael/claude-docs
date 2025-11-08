---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Usage example

This section provides an example of handling streamed objects in the tool use response generation step.

### Setup

First, import the Cohere library and create a client.

<Tabs>
  <Tab title="Cohere platform">
```python PYTHON
    # ! pip install -U cohere

    import cohere

    co = cohere.ClientV2(
        "COHERE_API_KEY"
    )  # Get your free API key here: https://dashboard.cohere.com/api-keys

```
  </Tab>

  <Tab title="Private deployment">
```python PYTHON
    # ! pip install -U cohere

    import cohere

    co = cohere.ClientV2(
        api_key="",  # Leave this blank

        base_url="<YOUR_DEPLOYMENT_URL>",
    )
```
  </Tab>
</Tabs>

### Tool definition

Next, define the tool and its associated schema.
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

### Streaming the response

Before streaming the response, first run through the tool calling and execution steps.

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
      print(response.message.tool_plan, "\n")
      print(response.message.tool_calls)

  import json

  if response.message.tool_calls:
      for tc in response.message.tool_calls:
          tool_result = functions_map[tc.function.name](
              **json.loads(tc.function.arguments)
          )
          tool_content = []
          for data in tool_result:
              # Optional: the "document" object can take an "id" field for use in citations, otherwise auto-generated

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

Example response:
```mdx wordWrap
I will use the get_weather tool to find the weather in Madrid and Brasilia. 

[
    ToolCallV2(
        id="get_weather_15c2p6g19s8f",
        type="function",
        function=ToolCallV2Function(
            name="get_weather", arguments='{"location":"Madrid"}'
        ),
    ),
    ToolCallV2(
        id="get_weather_n01pkywy0p2w",
        type="function",
        function=ToolCallV2Function(
            name="get_weather", arguments='{"location":"Brasilia"}'
        ),
    ),
]
```
Once the tool results have been received, we can now stream the response using the `chat_stream` endpoint.

The events are streamed as `chunk` objects. In the example below, we pick `content-delta` to display the text response and `citation-start` to display the citations.

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
        "tool_plan": "I will use the get_weather tool to find the weather in Madrid and Brasilia.",
        "tool_calls": [
          {
            "id": "get_weather_15c2p6g19s8f",
            "type": "function",
            "function": {
              "name": "get_weather",
              "arguments": "{\"location\":\"Madrid\"}"
            }
          },
          {
            "id": "get_weather_n01pkywy0p2w",
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
        "tool_call_id": "get_weather_15c2p6g19s8f",
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
        "tool_call_id": "get_weather_n01pkywy0p2w",
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
It's currently 24°C in Madrid and 28°C in Brasilia.

start=5 end=9 text='24°C' sources=[ToolSource(type='tool', id='get_weather_15c2p6g19s8f:0', tool_output={'temperature': '{"madrid":"24°C"}'})] type='TEXT_CONTENT' 

start=24 end=28 text='28°C' sources=[ToolSource(type='tool', id='get_weather_n01pkywy0p2w:0', tool_output={'temperature': '{"brasilia":"28°C"}'})] type='TEXT_CONTENT' 
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
