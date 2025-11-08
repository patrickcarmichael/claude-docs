---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Basic Function Calling

Let's say our application has access to a `get_current_weather` function which takes in two named arguments,`location` and `unit`:
```python
  ## Hypothetical function that exists in our app

  get_current_weather(location="San Francisco, CA", unit="fahrenheit")
```
```typescript
  // Hypothetical function that exists in our app
  getCurrentWeather({
    location: "San Francisco, CA",
    unit: "fahrenheit",
  });
```

We can make this function available to our LLM by passing its description to the `tools` key alongside the user's query. Let's suppose the user asks, "What is the current temperature of New York?"
```python
  import json
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="Qwen/Qwen2.5-7B-Instruct-Turbo",
      messages=[
          {
              "role": "system",
              "content": "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls.",
          },
          {
              "role": "user",
              "content": "What is the current temperature of New York?",
          },
      ],
      tools=[
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
      ],
  )

  print(
      json.dumps(
          response.choices[0].message.model_dump()["tool_calls"],
          indent=2,
      )
  )
```
```typescript
  import Together from "together-ai";

  const together = new Together();

  const response = await together.chat.completions.create({
    model: "Qwen/Qwen2.5-7B-Instruct-Turbo",
    messages: [
      {
        role: "system",
        content:
          "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls.",
      },
      {
        role: "user",
        content: "What is the current temperature of New York?",
      },
    ],
    tools: [
      {
        type: "function",
        function: {
          name: "getCurrentWeather",
          description: "Get the current weather in a given location",
          parameters: {
            type: "object",
            properties: {
              location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA",
              },
              unit: {
                type: "string",
                description: "The unit of temperature",
                enum: ["celsius", "fahrenheit"],
              },
            },
          },
        },
      },
    ],
  });

  console.log(JSON.stringify(response.choices[0].message?.tool_calls, null, 2));
```
```bash
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "Qwen/Qwen2.5-7B-Instruct-Turbo",
         "messages": [
           {
             "role": "system",
             "content": "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls."
           },
           {
             "role": "user",
             "content": "What is the current temperature of New York?"
           }
         ],
         "tools": [
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
                     "description": "The city and state, e.g. San Francisco, CA"
                   },
                   "unit": {
                     "type": "string",
                     "enum": ["celsius", "fahrenheit"]
                   }
                 }
               }
             }
           }
         ]
       }'
```

The model will respond with a single function call in the `tool_calls` array, specifying the function name and arguments needed to get the weather for New York.
```json
[
  {
    "index": 0,
    "id": "call_aisak3q1px3m2lzb41ay6rwf",
    "type": "function",
    "function": {
      "arguments": "{\"location\":\"New York, NY\",\"unit\":\"fahrenheit\"}",
      "name": "get_current_weather"
    }
  }
]
```

As we can see, the LLM has given us a function call that we can programmatically execute to answer the user's question.

### Streaming

Function calling also works with streaming responses. When streaming is enabled, tool calls are returned incrementally and can be accessed from the `delta.tool_calls` object in each chunk.
```python
  from together import Together

  client = Together()

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

  stream = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[{"role": "user", "content": "What's the weather in NYC?"}],
      tools=tools,
      stream=True,
  )

  for chunk in stream:
      delta = chunk.choices[0].delta
      tool_calls = getattr(delta, "tool_calls", [])
      print(tool_calls)
```
```typescript
  import Together from "together-ai";

  const client = new Together();

  const tools = [
    {
      type: "function",
      function: {
        name: "get_weather",
        description: "Get current temperature for a given location.",
        parameters: {
          type: "object",
          properties: {
            location: {
              type: "string",
              description: "City and country e.g. Bogotá, Colombia",
            },
          },
          required: ["location"],
          additionalProperties: false,
        },
        strict: true,
      },
    },
  ];

  const stream = await client.chat.completions.create({
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages: [{ role: "user", content: "What's the weather in NYC?" }],
    tools,
    stream: true,
  });

  for await (const chunk of stream) {
    const delta = chunk.choices[0]?.delta;
    const toolCalls = delta?.tool_calls ?? [];
    console.log(toolCalls);
  }
```
```bash
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
         "messages": [
           {
             "role": "user",
             "content": "What'\''s the weather in NYC?"
           }
         ],
         "tools": [
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
                     "description": "City and country e.g. Bogotá, Colombia"
                   }
                 },
                 "required": ["location"],
                 "additionalProperties": false
               },
               "strict": true
             }
           }
         ],
         "stream": true
       }'
```

The model will respond with streamed function calls:
```json
[# delta 1

  {
    "index": 0,
    "id": "call_fwbx4e156wigo9ayq7tszngh",
    "type": "function",
    "function": {
      "name": "get_weather",
      "arguments": ""
    }
  }
]

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
