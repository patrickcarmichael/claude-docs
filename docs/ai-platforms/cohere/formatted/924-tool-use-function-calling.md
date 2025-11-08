---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool use (function calling)

You can utilize the tool use feature by passing a list of tools to the `tools` parameter in the API call.

Specifying the `strict` parameter to `True` in the tool calling step will guarantee that every generated tool call follows the specified tool schema.

<Tabs>
  <Tab title="Python">
```python PYTHON
    from openai import OpenAI

    client = OpenAI(
        base_url="https://api.cohere.ai/compatibility/v1",
        api_key="COHERE_API_KEY",
    )

    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_flight_info",
                "description": "Get flight information between two cities or airports",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "loc_origin": {
                            "type": "string",
                            "description": "The departure airport, e.g. MIA",
                        },
                        "loc_destination": {
                            "type": "string",
                            "description": "The destination airport, e.g. NYC",
                        },
                    },
                    "required": ["loc_origin", "loc_destination"],
                },
            },
        }
    ]

    messages = [
        {"role": "developer", "content": "Today is April 30th"},
        {
            "role": "user",
            "content": "When is the next flight from Miami to Seattle?",
        },
        {
            "role": "assistant",
            "tool_calls": [
                {
                    "function": {
                        "arguments": '{ "loc_destination": "Seattle", "loc_origin": "Miami" }',
                        "name": "get_flight_info",
                    },
                    "id": "get_flight_info0",
                    "type": "function",
                }
            ],
        },
        {
            "role": "tool",
            "name": "get_flight_info",
            "tool_call_id": "get_flight_info0",
            "content": "Miami to Seattle, May 1st, 10 AM.",
        },
    ]

    completion = client.chat.completions.create(
        model="command-a-03-2025",
        messages=messages,
        tools=tools,
        temperature=0.7,
    )

    print(completion.choices[0].message)
```
  </Tab>

  <Tab title="TypeScript">
```typescript TYPESCRIPT
    import OpenAI from "openai";

    const openai = new OpenAI({
        baseURL: "https://api.cohere.ai/compatibility/v1",
        apiKey: "COHERE_API_KEY",
        });

    const completion = await openai.chat.completions.create({
        model: "command-a-03-2025",
        messages: [
            {
                role: "developer", 
                content: "Today is April 30th"
            },
            {
                role: "user",
                content: "When is the next flight from Miami to Seattle?"
            },
            {
                role: "assistant",
                tool_calls: [
                    {
                        function: {
                            arguments: '{ "loc_destination": "Seattle", "loc_origin": "Miami" }',
                            name: "get_flight_info"
                        },
                        id: "get_flight_info0",
                        type: "function"
                    }
                ]
            },
            {
                role: "tool",
                name: "get_flight_info",
                tool_call_id: "get_flight_info0", 
                content: "Miami to Seattle, May 1st, 10 AM."
            }
        ],
        tools: [
            {
                type: "function",
                function: {
                    name: "get_flight_info",
                    description: "Get flight information between two cities or airports",
                    parameters: {
                        type: "object",
                        properties: {
                            loc_origin: {
                                type: "string",
                                description: "The departure airport, e.g. MIA"
                            },
                            loc_destination: {
                                type: "string",
                                description: "The destination airport, e.g. NYC"
                            }
                        },
                        required: ["loc_origin", "loc_destination"]
                    }
                }
            }
        ],
        temperature: 0.7
    });

    console.log(completion.choices[0].message);
```
  </Tab>

  <Tab title="cURL">
```bash
    curl --request POST \
        --url https://api.cohere.ai/compatibility/v1/chat/completions \
        --header 'Authorization: Bearer COHERE_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
        "model": "command-a-03-2025",
        "messages": [
            {
            "role": "developer",
            "content": "Today is April 30th"
        },
        {
            "role": "user",
            "content": "When is the next flight from Miami to Seattle?"
        },
            {
            "role": "assistant",
            "tool_calls": [
                {
                    "function": {
                        "arguments": "{ \"loc_destination\": \"Seattle\", \"loc_origin\": \"Miami\" }",
                        "name": "get_flight_info"
                    },
                    "id": "get_flight_info0",
                    "type": "function"
                }
            ]
        },
        {
            "role": "tool",
            "name": "get_flight_info",
            "tool_call_id": "get_flight_info0",
            "content": "Miami to Seattle, May 1st, 10 AM."
        }],
        "tools": [
        {
            "type": "function",
            "function": {
                "name":"get_flight_info",
                "description": "Get flight information between two cities or airports",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "loc_origin": {
                            "type": "string",
                            "description": "The departure airport, e.g. MIA"
                        },
                        "loc_destination": {
                            "type": "string",
                            "description": "The destination airport, e.g. NYC"
                        }
                    },
                    "required": ["loc_origin", "loc_destination"]
                }
            }
            }
        ],
        "temperature": 0.7
    }'
```
  </Tab>
</Tabs>

Example response (via the Python SDK):
```mdx
ChatCompletionMessage(content='The next flight from Miami to Seattle is on May 1st, 10 AM.', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
