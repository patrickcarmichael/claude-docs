---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Citation modes

When running tool use in streaming mode, it’s possible to configure how citations are generated and presented. You can choose between fast citations or accurate citations, depending on your latency and precision needs.

### Accurate citations

The model produces its answer first, and then, after the entire response is generated, it provides citations that map to specific segments of the response text. This approach may incur slightly higher latency, but it ensures the citation indices are more precisely aligned with the final text segments of the model’s answer.

This is the default option, or you can explicitly specify it by adding the `citation_options={"mode": "accurate"}` argument in the API call.

Here is an example using the same list of pre-defined `messages` [as the above](#document-id).

With the `citation_options` mode set to `accurate`, we get the citations after the entire response is generated.

<CodeBlocks>
```python PYTHON
  # ! pip install -U cohere

  import cohere
  import json

  co = cohere.ClientV2(
      "COHERE_API_KEY"
  )  # Get your free API key here: https://dashboard.cohere.com/api-keys

  response = co.chat_stream(
      model="command-a-03-2025",
      messages=messages,
      tools=tools,
      citation_options={"mode": "accurate"},
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

  print("\n")
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
    ],
    "citation_options": {
      "mode": "accurate"
    },
    "stream": true
  }'
```
</CodeBlocks>

Example response:
```mdx wordWrap
It is currently 24°C in Madrid and 28°C in Brasilia.

start=16 end=20 text='24°C' sources=[ToolSource(type='tool', id='1', tool_output={'temperature': '{"madrid":"24°C"}'})] type='TEXT_CONTENT' 

start=35 end=39 text='28°C' sources=[ToolSource(type='tool', id='2', tool_output={'temperature': '{"brasilia":"28°C"}'})] type='TEXT_CONTENT' 
```

### Fast citations

The model generates citations inline, as the response is being produced. In streaming mode, you will see citations injected at the exact moment the model uses a particular piece of external context. This approach provides immediate traceability at the expense of slightly less precision in citation relevance.

You can specify it by adding the `citation_options={"mode": "fast"}` argument in the API call.

With the `citation_options` mode set to `fast`, we get the citations inline as the model generates the response.

<CodeBlocks>
```python PYTHON
  response = co.chat_stream(
      model="command-a-03-2025",
      messages=messages,
      tools=tools,
      citation_options={"mode": "fast"},
  )

  response_text = ""
  for chunk in response:
      if chunk:
          if chunk.type == "content-delta":
              response_text += chunk.delta.message.content.text
              print(chunk.delta.message.content.text, end="")
          if chunk.type == "citation-start":
              print(
                  f" [{chunk.delta.message.citations.sources[0].id}]",
                  end="",
              )
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
    ],
    "citation_options": {
      "mode": "fast"
    },
    "stream": true
  }'
```
</CodeBlocks>

Example response:
```mdx wordWrap
It is currently 24°C [1] in Madrid and 28°C [2] in Brasilia.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
