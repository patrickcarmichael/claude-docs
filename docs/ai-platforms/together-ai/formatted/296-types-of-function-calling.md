---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Types of Function Calling

Function calling can be implemented in six different patterns, each serving different use cases:

| **Type**              | **Description**                         | **Use Cases**                           |
| --------------------- | --------------------------------------- | --------------------------------------- |
| **Simple**            | One function, one call                  | Basic utilities, simple queries         |
| **Multiple**          | Choose from many functions              | Many tools, LLM has to choose           |
| **Parallel**          | Same function, multiple calls           | Complex prompts, multiple tools called  |
| **Parallel Multiple** | Multiple functions, parallel calls      | Complex single requests with many tools |
| **Multi-Step**        | Sequential function calling in one turn | Data processing workflows               |
| **Multi-Turn**        | Conversational context + functions      | AI Agents with humans in the loop       |

Understanding these types of function calling patterns helps you choose the right approach for your application, from simple utilities to sophisticated agentic behaviors.

### 1. Simple Function Calling

This is the most basic type of function calling where one function is defined and one user prompt triggers one function call. The model identifies the need to call the function and extracts the right parameters.

This is the example presented in the above code. Only one tool is provided to the model and it responds with one invocation of the tool.

### 2. Multiple Function Calling

Multiple function calling involves having several different functions available, with the model choosing the best function to call based on the user's intent. The model must understand the request and select the appropriate tool from the available options.

In the example below we provide two tools to the model and it responds with one tool invocation.
```python
  import json
  from together import Together

  client = Together()

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
      },
      {
          "type": "function",
          "function": {
              "name": "get_current_stock_price",
              "description": "Get the current stock price for a given stock symbol",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "symbol": {
                          "type": "string",
                          "description": "The stock symbol, e.g. AAPL, GOOGL, TSLA",
                      },
                      "exchange": {
                          "type": "string",
                          "description": "The stock exchange (optional)",
                          "enum": ["NYSE", "NASDAQ", "LSE", "TSX"],
                      },
                  },
                  "required": ["symbol"],
              },
          },
      },
  ]

  response = client.chat.completions.create(
      model="Qwen/Qwen2.5-7B-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": "What's the current price of Apple's stock?",
          },
      ],
      tools=tools,
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

  const tools = [
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
    {
      type: "function",
      function: {
        name: "getCurrentStockPrice",
        description: "Get the current stock price for a given stock symbol",
        parameters: {
          type: "object",
          properties: {
            symbol: {
              type: "string",
              description: "The stock symbol, e.g. AAPL, GOOGL, TSLA",
            },
            exchange: {
              type: "string",
              description: "The stock exchange (optional)",
              enum: ["NYSE", "NASDAQ", "LSE", "TSX"],
            },
          },
          required: ["symbol"],
        },
      },
    },
  ];

  const response = await together.chat.completions.create({
    model: "Qwen/Qwen2.5-7B-Instruct-Turbo",
    messages: [
      {
        role: "user",
        content: "What's the current price of Apple's stock?",
      },
    ],
    tools,
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
             "role": "user",
             "content": "What'\''s the current price of Apple'\''s stock?"
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
           },
           {
             "type": "function",
             "function": {
               "name": "get_current_stock_price",
               "description": "Get the current stock price for a given stock symbol",
               "parameters": {
                 "type": "object",
                 "properties": {
                   "symbol": {
                     "type": "string",
                     "description": "The stock symbol, e.g. AAPL, GOOGL, TSLA"
                   },
                   "exchange": {
                     "type": "string",
                     "description": "The stock exchange (optional)",
                     "enum": ["NYSE", "NASDAQ", "LSE", "TSX"]
                   }
                 },
                 "required": ["symbol"]
               }
             }
           }
         ]
       }'
```

In this example, even though both weather and stock functions are available, the model correctly identifies that the user is asking about stock prices and calls the `get_current_stock_price` function.

#### Selecting a specific tool

If you'd like to manually select a specific tool to use for a completion, pass in the tool's name to the `tool_choice` parameter:
```python
  response = client.chat.completions.create(
      model="Qwen/Qwen2.5-7B-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": "What's the current price of Apple's stock?",
          },
      ],
      tools=tools,
      tool_choice={
          "type": "function",
          "function": {"name": "get_current_stock_price"},
      },
  )
```
```typescript
  const response = await together.chat.completions.create({
    model: "Qwen/Qwen2.5-7B-Instruct-Turbo",
    messages: [
      {
        role: "user",
        content: "What's the current price of Apple's stock?",
      },
    ],
    tools,
    tool_choice: { type: "function", function: { name: "getCurrentStockPrice" } },
  });
```
```bash
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "Qwen/Qwen2.5-7B-Instruct-Turbo",
         "messages": [
           {
             "role": "user",
             "content": "What'\''s the current price of Apple'\''s stock?"
           }
         ],
         "tools": [
           {
             "type": "function",
             "function": {
               "name": "get_current_stock_price",
               "description": "Get the current stock price for a given stock symbol",
               "parameters": {
                 "type": "object",
                 "properties": {
                   "symbol": {
                     "type": "string",
                     "description": "The stock symbol, e.g. AAPL, GOOGL, TSLA"
                   }
                 },
                 "required": ["symbol"]
               }
             }
           }
         ],
         "tool_choice": {
           "type": "function",
           "function": {
             "name": "get_current_stock_price"
           }
         }
       }'
```

This ensures the model will use the specified function when generating its response, regardless of the user's phrasing.

#### Understanding tool\_choice options

The `tool_choice` parameter controls how the model uses functions. It accepts:

**String values:**

* `"auto"` (default) - Model decides whether to call a function or generate a text response
* `"none"` - Model will never call functions, only generates text
* `"required"` - Model must call at least one function

### 3. Parallel Function Calling

In parallel function calling, the same function is called multiple times simultaneously with different parameters. This is more efficient than making sequential calls for similar operations.
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
              "content": "What is the current temperature of New York, San Francisco and Chicago?",
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
        content:
          "What is the current temperature of New York, San Francisco and Chicago?",
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
             "content": "What is the current temperature of New York, San Francisco and Chicago?"
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

In response, the `tool_calls` key of the LLM's response will look like this:
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
  },
  {
    "index": 1,
    "id": "call_agrjihqjcb0r499vrclwrgdj",
    "type": "function",
    "function": {
      "arguments": "{\"location\":\"San Francisco, CA\",\"unit\":\"fahrenheit\"}",
      "name": "get_current_weather"
    }
  },
  {
    "index": 2,
    "id": "call_17s148ekr4hk8m5liicpwzkk",
    "type": "function",
    "function": {
      "arguments": "{\"location\":\"Chicago, IL\",\"unit\":\"fahrenheit\"}",
      "name": "get_current_weather"
    }
  }
]
```

As we can see, the LLM has given us three function calls that we can programmatically execute to answer the user's question.

### 4. Parallel Multiple Function Calling

This pattern combines parallel and multiple function calling: multiple different functions are available, and one user prompt triggers multiple different function calls simultaneously. The model chooses which functions to call AND calls them in parallel.
```python
  import json
  from together import Together

  client = Together()

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
      },
      {
          "type": "function",
          "function": {
              "name": "get_current_stock_price",
              "description": "Get the current stock price for a given stock symbol",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "symbol": {
                          "type": "string",
                          "description": "The stock symbol, e.g. AAPL, GOOGL, TSLA",
                      },
                      "exchange": {
                          "type": "string",
                          "description": "The stock exchange (optional)",
                          "enum": ["NYSE", "NASDAQ", "LSE", "TSX"],
                      },
                  },
                  "required": ["symbol"],
              },
          },
      },
  ]

  response = client.chat.completions.create(
      model="Qwen/Qwen2.5-7B-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": "What's the current price of Apple and Google stock? What is the weather in New York, San Francisco and Chicago?",
          },
      ],
      tools=tools,
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

  const tools = [
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
              enum: ["celsius", "fahrenheit"],
            },
          },
        },
      },
    },
    {
      type: "function",
      function: {
        name: "getCurrentStockPrice",
        description: "Get the current stock price for a given stock symbol",
        parameters: {
          type: "object",
          properties: {
            symbol: {
              type: "string",
              description: "The stock symbol, e.g. AAPL, GOOGL, TSLA",
            },
            exchange: {
              type: "string",
              description: "The stock exchange (optional)",
              enum: ["NYSE", "NASDAQ", "LSE", "TSX"],
            },
          },
          required: ["symbol"],
        },
      },
    },
  ];

  const response = await together.chat.completions.create({
    model: "Qwen/Qwen2.5-7B-Instruct-Turbo",
    messages: [
      {
        role: "user",
        content:
          "What's the current price of Apple and Google stock? What is the weather in New York, San Francisco and Chicago?",
      },
    ],
    tools,
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
             "role": "user",
             "content": "What'\''s the current price of Apple and Google stock? What is the weather in New York, San Francisco and Chicago?"
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
           },
           {
             "type": "function",
             "function": {
               "name": "get_current_stock_price",
               "description": "Get the current stock price for a given stock symbol",
               "parameters": {
                 "type": "object",
                 "properties": {
                   "symbol": {
                     "type": "string",
                     "description": "The stock symbol, e.g. AAPL, GOOGL, TSLA"
                   },
                   "exchange": {
                     "type": "string",
                     "description": "The stock exchange (optional)",
                     "enum": ["NYSE", "NASDAQ", "LSE", "TSX"]
                   }
                 },
                 "required": ["symbol"]
               }
             }
           }
         ]
       }'
```

This will result in five function calls: two for stock prices (Apple and Google) and three for weather information (New York, San Francisco, and Chicago), all executed in parallel.
```json
[
  {
    "id": "call_8b31727cf80f41099582a259",
    "type": "function",
    "function": {
      "name": "get_current_stock_price",
      "arguments": "{\"symbol\": \"AAPL\"}"
    },
    "index": null
  },
  {
    "id": "call_b54bcaadceec423d82f28611",
    "type": "function",
    "function": {
      "name": "get_current_stock_price",
      "arguments": "{\"symbol\": \"GOOGL\"}"
    },
    "index": null
  },
  {
    "id": "call_f1118a9601c644e1b78a4a8c",
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "arguments": "{\"location\": \"San Francisco, CA\"}"
    },
    "index": null
  },
  {
    "id": "call_95dc5028837e4d1e9b247388",
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "arguments": "{\"location\": \"New York, NY\"}"
    },
    "index": null
  },
  {
    "id": "call_1b8b58809d374f15a5a990d9",
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "arguments": "{\"location\": \"Chicago, IL\"}"
    },
    "index": null
  }
]
```

### 5. Multi-Step Function Calling

Multi-step function calling involves sequential function calls within one conversation turn. Functions are called, results are processed, then used to inform the final response. This demonstrates the complete flow from initial function calls to processing function results to final response incorporating all the data.

Here's an example of passing the result of a tool call from one completion into a second follow-up completion:
```python
  import json
  from together import Together

  client = Together()


  ## Example function to make available to model

  def get_current_weather(location, unit="fahrenheit"):
      """Get the weather for some location"""
      if "chicago" in location.lower():
          return json.dumps(
              {"location": "Chicago", "temperature": "13", "unit": unit}
          )
      elif "san francisco" in location.lower():
          return json.dumps(
              {"location": "San Francisco", "temperature": "55", "unit": unit}
          )
      elif "new york" in location.lower():
          return json.dumps(
              {"location": "New York", "temperature": "11", "unit": unit}
          )
      else:
          return json.dumps({"location": location, "temperature": "unknown"})


  # 1. Define a list of callable tools for the model

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
                          "description": "The unit of temperature",
                          "enum": ["celsius", "fahrenheit"],
                      },
                  },
              },
          },
      }
  ]

  # Create a running messages list we will add to over time

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

  # 2. Prompt the model with tools defined

  response = client.chat.completions.create(
      model="Qwen/Qwen2.5-7B-Instruct-Turbo",
      messages=messages,
      tools=tools,
  )

  # Save function call outputs for subsequent requests

  tool_calls = response.choices[0].message.tool_calls

  if tool_calls:
      # Add the assistant's response with tool calls to messages

      messages.append(
          {
              "role": "assistant",
              "content": "",
              "tool_calls": [tool_call.model_dump() for tool_call in tool_calls],
          }
      )

      # 3. Execute the function logic for each tool call

      for tool_call in tool_calls:
          function_name = tool_call.function.name
          function_args = json.loads(tool_call.function.arguments)

          if function_name == "get_current_weather":
              function_response = get_current_weather(
                  location=function_args.get("location"),
                  unit=function_args.get("unit"),
              )

              # 4. Provide function call results to the model

              messages.append(
                  {
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": function_name,
                      "content": function_response,
                  }
              )

      # 5. The model should be able to give a response with the function results!

      function_enriched_response = client.chat.completions.create(
          model="Qwen/Qwen2.5-7B-Instruct-Turbo",
          messages=messages,
      )
      print(
          json.dumps(
              function_enriched_response.choices[0].message.model_dump(),
              indent=2,
          )
      )
```
```typescript
  import Together from "together-ai";
  import { CompletionCreateParams } from "together-ai/resources/chat/completions.mjs";

  const together = new Together();

  // Example function to make available to model
  function getCurrentWeather({
    location,
    unit = "fahrenheit",
  }: {
    location: string;
    unit: "fahrenheit" | "celsius";
  }) {
    let result: { location: string; temperature: number | null; unit: string };
    if (location.toLowerCase().includes("chicago")) {
      result = {
        location: "Chicago",
        temperature: 13,
        unit,
      };
    } else if (location.toLowerCase().includes("san francisco")) {
      result = {
        location: "San Francisco",
        temperature: 55,
        unit,
      };
    } else if (location.toLowerCase().includes("new york")) {
      result = {
        location: "New York",
        temperature: 11,
        unit,
      };
    } else {
      result = {
        location,
        temperature: null,
        unit,
      };
    }

    return JSON.stringify(result);
  }

  const tools = [
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
              enum: ["celsius", "fahrenheit"],
            },
          },
        },
      },
    },
  ];

  const messages: CompletionCreateParams.Message[] = [
    {
      role: "system",
      content:
        "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls.",
    },
    {
      role: "user",
      content:
        "What is the current temperature of New York, San Francisco and Chicago?",
    },
  ];

  const response = await together.chat.completions.create({
    model: "Qwen/Qwen2.5-7B-Instruct-Turbo",
    messages,
    tools,
  });

  const toolCalls = response.choices[0].message?.tool_calls;
  if (toolCalls) {
    messages.push({
      role: "assistant",
      content: "",
      tool_calls: toolCalls,
    });
    for (const toolCall of toolCalls) {
      if (toolCall.function.name === "getCurrentWeather") {
        const args = JSON.parse(toolCall.function.arguments);
        const functionResponse = getCurrentWeather(args);

        messages.push({
          role: "tool",
          content: functionResponse,
        });
      }
    }

    const functionEnrichedResponse = await together.chat.completions.create({
      model: "Qwen/Qwen2.5-7B-Instruct-Turbo",
      messages,
      tools,
    });

    console.log(
      JSON.stringify(functionEnrichedResponse.choices[0].message, null, 2),
    );
  }
```

And here's the final output from the second call:
```json
{
  "content": "The current temperature in New York is 11 degrees Fahrenheit, in San Francisco it is 55 degrees Fahrenheit, and in Chicago it is 13 degrees Fahrenheit.",
  "role": "assistant"
}
```

We've successfully used our LLM to generate three tool call descriptions, iterated over those descriptions to execute each one, and passed the results into a follow-up message to get the LLM to produce a final answer!

### 6. Multi-Turn Function Calling

Multi-turn function calling represents the most sophisticated form of function calling, where context is maintained across multiple conversation turns and functions can be called at any point in the conversation. Previous function results inform future decisions, enabling truly agentic behavior.
```python
  import json
  from together import Together

  client = Together()

  # Define all available tools for the travel assistant

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
                          "description": "The unit of temperature",
                          "enum": ["celsius", "fahrenheit"],
                      },
                  },
                  "required": ["location"],
              },
          },
      },
      {
          "type": "function",
          "function": {
              "name": "get_restaurant_recommendations",
              "description": "Get restaurant recommendations for a specific location",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "The city and state, e.g. San Francisco, CA",
                      },
                      "cuisine_type": {
                          "type": "string",
                          "description": "Type of cuisine preferred",
                          "enum": [
                              "italian",
                              "chinese",
                              "mexican",
                              "american",
                              "french",
                              "japanese",
                              "any",
                          ],
                      },
                      "price_range": {
                          "type": "string",
                          "description": "Price range preference",
                          "enum": ["budget", "mid-range", "upscale", "any"],
                      },
                  },
                  "required": ["location"],
              },
          },
      },
  ]


  def get_current_weather(location, unit="fahrenheit"):
      """Get the weather for some location"""
      if "chicago" in location.lower():
          return json.dumps(
              {
                  "location": "Chicago",
                  "temperature": "13",
                  "unit": unit,
                  "condition": "cold and snowy",
              }
          )
      elif "san francisco" in location.lower():
          return json.dumps(
              {
                  "location": "San Francisco",
                  "temperature": "65",
                  "unit": unit,
                  "condition": "mild and partly cloudy",
              }
          )
      elif "new york" in location.lower():
          return json.dumps(
              {
                  "location": "New York",
                  "temperature": "28",
                  "unit": unit,
                  "condition": "cold and windy",
              }
          )
      else:
          return json.dumps(
              {
                  "location": location,
                  "temperature": "unknown",
                  "condition": "unknown",
              }
          )


  def get_restaurant_recommendations(
      location, cuisine_type="any", price_range="any"
  ):
      """Get restaurant recommendations for a location"""
      restaurants = {}

      if "san francisco" in location.lower():
          restaurants = {
              "italian": ["Tony's Little Star Pizza", "Perbacco"],
              "chinese": ["R&G Lounge", "Z&Y Restaurant"],
              "american": ["Zuni Café", "House of Prime Rib"],
              "seafood": ["Swan Oyster Depot", "Fisherman's Wharf restaurants"],
          }
      elif "chicago" in location.lower():
          restaurants = {
              "italian": ["Gibsons Italia", "Piccolo Sogno"],
              "american": ["Alinea", "Girl & Goat"],
              "pizza": ["Lou Malnati's", "Giordano's"],
              "steakhouse": ["Gibsons Bar & Steakhouse"],
          }
      elif "new york" in location.lower():
          restaurants = {
              "italian": ["Carbone", "Don Angie"],
              "american": ["The Spotted Pig", "Gramercy Tavern"],
              "pizza": ["Joe's Pizza", "Prince Street Pizza"],
              "fine_dining": ["Le Bernardin", "Eleven Madison Park"],
          }

      return json.dumps(
          {
              "location": location,
              "cuisine_filter": cuisine_type,
              "price_filter": price_range,
              "restaurants": restaurants,
          }
      )


  def handle_conversation_turn(messages, user_input):
      """Handle a single conversation turn with potential function calls"""
      # 3. Add user input to messages

      messages.append({"role": "user", "content": user_input})

      # 4. Get model response with tools

      response = client.chat.completions.create(
          model="Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8",
          messages=messages,
          tools=tools,
      )

      tool_calls = response.choices[0].message.tool_calls

      if tool_calls:
          # 5. Add assistant response with tool calls

          messages.append(
              {
                  "role": "assistant",
                  "content": response.choices[0].message.content or "",
                  "tool_calls": [
                      tool_call.model_dump() for tool_call in tool_calls
                  ],
              }
          )

          # 6. Execute each function call

          for tool_call in tool_calls:
              function_name = tool_call.function.name
              function_args = json.loads(tool_call.function.arguments)

              print(f"🔧 Calling {function_name} with args: {function_args}")

              # Route to appropriate function

              if function_name == "get_current_weather":
                  function_response = get_current_weather(
                      location=function_args.get("location"),
                      unit=function_args.get("unit", "fahrenheit"),
                  )
              elif function_name == "get_activity_suggestions":
                  function_response = get_activity_suggestions(
                      location=function_args.get("location"),
                      weather_condition=function_args.get("weather_condition"),
                      activity_type=function_args.get("activity_type", "both"),
                  )
              elif function_name == "get_restaurant_recommendations":
                  function_response = get_restaurant_recommendations(
                      location=function_args.get("location"),
                      cuisine_type=function_args.get("cuisine_type", "any"),
                      price_range=function_args.get("price_range", "any"),
                  )

              # 7. Add function response to messages

              messages.append(
                  {
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": function_name,
                      "content": function_response,
                  }
              )

          # 8. Get final response with function results

          final_response = client.chat.completions.create(
              model="Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8",
              messages=messages,
          )

          # 9. Add final assistant response to messages for context retention

          messages.append(
              {
                  "role": "assistant",
                  "content": final_response.choices[0].message.content,
              }
          )

          return final_response.choices[0].message.content


  # Initialize conversation with system message

  messages = [
      {
          "role": "system",
          "content": "You are a helpful travel planning assistant. You can access weather information and restaurant recommendations. Use the available tools to provide comprehensive travel advice based on the user's needs.",
      }
  ]

  # TURN 1: Initial weather request

  print("TURN 1:")
  print(
      "User: What is the current temperature of New York, San Francisco and Chicago?"
  )
  response1 = handle_conversation_turn(
      messages,
      "What is the current temperature of New York, San Francisco and Chicago?",
  )
  print(f"Assistant: {response1}")

  # TURN 2: Follow-up with activity and restaurant requests based on previous context

  print("\nTURN 2:")
  print(
      "User: Based on the weather, which city would be best for outdoor activities? And can you find some restaurant recommendations for that city?"
  )
  response2 = handle_conversation_turn(
      messages,
      "Based on the weather, which city would be best for outdoor activities? And can you find some restaurant recommendations for that city?",
  )
  print(f"Assistant: {response2}")
```
```typescript
  import Together from "together-ai";
  import { CompletionCreateParams } from "together-ai/resources/chat/completions.mjs";

  const together = new Together();

  const tools = [
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
          required: ["location"],
        },
      },
    },
    {
      type: "function",
      function: {
        name: "getRestaurantRecommendations",
        description: "Get restaurant recommendations for a specific location",
        parameters: {
          type: "object",
          properties: {
            location: {
              type: "string",
              description: "The city and state, e.g. San Francisco, CA",
            },
            cuisineType: {
              type: "string",
              description: "Type of cuisine preferred",
              enum: [
                "italian",
                "chinese",
                "mexican",
                "american",
                "french",
                "japanese",
                "any",
              ],
            },
            priceRange: {
              type: "string",
              description: "Price range preference",
              enum: ["budget", "mid-range", "upscale", "any"],
            },
          },
          required: ["location"],
        },
      },
    },
  ];

  function getCurrentWeather({
    location,
    unit = "fahrenheit",
  }: {
    location: string;
    unit?: string;
  }) {
    if (location.toLowerCase().includes("chicago")) {
      return JSON.stringify({
        location: "Chicago",
        temperature: "13",
        unit,
        condition: "cold and snowy",
      });
    } else if (location.toLowerCase().includes("san francisco")) {
      return JSON.stringify({
        location: "San Francisco",
        temperature: "65",
        unit,
        condition: "mild and partly cloudy",
      });
    } else if (location.toLowerCase().includes("new york")) {
      return JSON.stringify({
        location: "New York",
        temperature: "28",
        unit,
        condition: "cold and windy",
      });
    } else {
      return JSON.stringify({
        location,
        temperature: "unknown",
        condition: "unknown",
      });
    }
  }

  function getRestaurantRecommendations({
    location,
    cuisineType = "any",
    priceRange = "any",
  }: {
    location: string;
    cuisineType?: string;
    priceRange?: string;
  }) {
    let restaurants = {};

    if (location.toLowerCase().includes("san francisco")) {
      restaurants = {
        italian: ["Tony's Little Star Pizza", "Perbacco"],
        chinese: ["R&G Lounge", "Z&Y Restaurant"],
        american: ["Zuni Café", "House of Prime Rib"],
        seafood: ["Swan Oyster Depot", "Fisherman's Wharf restaurants"],
      };
    } else if (location.toLowerCase().includes("chicago")) {
      restaurants = {
        italian: ["Gibsons Italia", "Piccolo Sogno"],
        american: ["Alinea", "Girl & Goat"],
        pizza: ["Lou Malnati's", "Giordano's"],
        steakhouse: ["Gibsons Bar & Steakhouse"],
      };
    } else if (location.toLowerCase().includes("new york")) {
      restaurants = {
        italian: ["Carbone", "Don Angie"],
        american: ["The Spotted Pig", "Gramercy Tavern"],
        pizza: ["Joe's Pizza", "Prince Street Pizza"],
        fine_dining: ["Le Bernardin", "Eleven Madison Park"],
      };
    }

    return JSON.stringify({
      location,
      cuisine_filter: cuisineType,
      price_filter: priceRange,
      restaurants,
    });
  }

  async function handleConversationTurn(
    messages: CompletionCreateParams.Message[],
    userInput: string,
  ) {
    messages.push({ role: "user", content: userInput });

    const response = await together.chat.completions.create({
      model: "Qwen/Qwen2.5-7B-Instruct-Turbo",
      messages,
      tools,
    });

    const toolCalls = response.choices[0].message?.tool_calls;

    if (toolCalls) {
      messages.push({
        role: "assistant",
        content: response.choices[0].message?.content || "",
        tool_calls: toolCalls,
      });

      for (const toolCall of toolCalls) {
        const functionName = toolCall.function.name;
        const functionArgs = JSON.parse(toolCall.function.arguments);

        let functionResponse: string;

        if (functionName === "getCurrentWeather") {
          functionResponse = getCurrentWeather(functionArgs);
        } else if (functionName === "getRestaurantRecommendations") {
          functionResponse = getRestaurantRecommendations(functionArgs);
        } else {
          functionResponse = "Function not found";
        }

        messages.push({
          role: "tool",
          content: functionResponse,
        });
      }

      const finalResponse = await together.chat.completions.create({
        model: "Qwen/Qwen2.5-7B-Instruct-Turbo",
        messages,
      });

      const content = finalResponse.choices[0].message?.content || "";
      messages.push({
        role: "assistant",
        content,
      });

      return content;
    } else {
      const content = response.choices[0].message?.content || "";
      messages.push({
        role: "assistant",
        content,
      });
      return content;
    }
  }

  // Example usage
  async function runMultiTurnExample() {
    const messages: CompletionCreateParams.Message[] = [
      {
        role: "system",
        content:
          "You are a helpful travel planning assistant. You can access weather information and restaurant recommendations. Use the available tools to provide comprehensive travel advice based on the user's needs.",
      },
    ];

    console.log("TURN 1:");
    console.log(
      "User: What is the current temperature of New York, San Francisco and Chicago?",
    );
    const response1 = await handleConversationTurn(
      messages,
      "What is the current temperature of New York, San Francisco and Chicago?",
    );
    console.log(`Assistant: ${response1}`);

    console.log("\nTURN 2:");
    console.log(
      "User: Based on the weather, which city would be best for outdoor activities? And can you find some restaurant recommendations for that city?",
    );
    const response2 = await handleConversationTurn(
      messages,
      "Based on the weather, which city would be best for outdoor activities? And can you find some restaurant recommendations for that city?",
    );
    console.log(`Assistant: ${response2}`);
  }

  runMultiTurnExample();
```

In this example, the assistant:

1. **Turn 1**: Calls weather functions for three cities and provides temperature information
2. **Turn 2**: Remembers the previous weather data, analyzes which city is best for outdoor activities (San Francisco with 65°F), and automatically calls the restaurant recommendation function for that city

This demonstrates true agentic behavior where the AI maintains context across turns and makes informed decisions based on previous interactions.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
