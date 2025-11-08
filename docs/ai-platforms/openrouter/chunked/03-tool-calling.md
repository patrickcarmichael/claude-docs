**Navigation:** [← Previous](./02-image-generation.md) | [Index](./index.md) | [Next →](./04-list-all-models-and-their-properties.md)

---

# Tool Calling

> Integrate function calling with support for parallel execution and complex tool interactions using OpenRouter's Responses API Beta.

<Warning title="Beta API">
  This API is in **beta stage** and may have breaking changes.
</Warning>

The Responses API Beta supports comprehensive tool calling capabilities, allowing models to call functions, execute tools in parallel, and handle complex multi-step workflows.

## Basic Tool Definition

Define tools using the OpenAI function calling format:

<CodeGroup>
  ```typescript title="TypeScript"
  const weatherTool = {
    type: 'function' as const,
    name: 'get_weather',
    description: 'Get the current weather in a location',
    strict: null,
    parameters: {
      type: 'object',
      properties: {
        location: {
          type: 'string',
          description: 'The city and state, e.g. San Francisco, CA',
        },
        unit: {
          type: 'string',
          enum: ['celsius', 'fahrenheit'],
        },
      },
      required: ['location'],
    },
  };

  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: [
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'What is the weather in San Francisco?',
            },
          ],
        },
      ],
      tools: [weatherTool],
      tool_choice: 'auto',
      max_output_tokens: 9000,
    }),
  });

  const result = await response.json();
  console.log(result);
  ```

  ```python title="Python"
  import requests

  weather_tool = {
      'type': 'function',
      'name': 'get_weather',
      'description': 'Get the current weather in a location',
      'strict': None,
      'parameters': {
          'type': 'object',
          'properties': {
              'location': {
                  'type': 'string',
                  'description': 'The city and state, e.g. San Francisco, CA',
              },
              'unit': {
                  'type': 'string',
                  'enum': ['celsius', 'fahrenheit'],
              },
          },
          'required': ['location'],
      },
  }

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': [
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'What is the weather in San Francisco?',
                      },
                  ],
              },
          ],
          'tools': [weather_tool],
          'tool_choice': 'auto',
          'max_output_tokens': 9000,
      }
  )

  result = response.json()
  print(result)
  ```

  ```bash title="cURL"
  curl -X POST https://openrouter.ai/api/v1/responses \
    -H "Authorization: Bearer YOUR_OPENROUTER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/o4-mini",
      "input": [
        {
          "type": "message",
          "role": "user",
          "content": [
            {
              "type": "input_text",
              "text": "What is the weather in San Francisco?"
            }
          ]
        }
      ],
      "tools": [
        {
          "type": "function",
          "name": "get_weather",
          "description": "Get the current weather in a location",
          "strict": null,
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
            },
            "required": ["location"]
          }
        }
      ],
      "tool_choice": "auto",
      "max_output_tokens": 9000
    }'
  ```
</CodeGroup>

## Tool Choice Options

Control when and how tools are called:

| Tool Choice                             | Description                         |
| --------------------------------------- | ----------------------------------- |
| `auto`                                  | Model decides whether to call tools |
| `none`                                  | Model will not call any tools       |
| `{type: 'function', name: 'tool_name'}` | Force specific tool call            |

### Force Specific Tool

<CodeGroup>
  ```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: [
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'Hello, how are you?',
            },
          ],
        },
      ],
      tools: [weatherTool],
      tool_choice: { type: 'function', name: 'get_weather' },
      max_output_tokens: 9000,
    }),
  });
  ```

  ```python title="Python"
  import requests

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': [
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'Hello, how are you?',
                      },
                  ],
              },
          ],
          'tools': [weather_tool],
          'tool_choice': {'type': 'function', 'name': 'get_weather'},
          'max_output_tokens': 9000,
      }
  )
  ```
</CodeGroup>

### Disable Tool Calling

<CodeGroup>
  ```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: [
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'What is the weather in Paris?',
            },
          ],
        },
      ],
      tools: [weatherTool],
      tool_choice: 'none',
      max_output_tokens: 9000,
    }),
  });
  ```

  ```python title="Python"
  import requests

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': [
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'What is the weather in Paris?',
                      },
                  ],
              },
          ],
          'tools': [weather_tool],
          'tool_choice': 'none',
          'max_output_tokens': 9000,
      }
  )
  ```
</CodeGroup>

## Multiple Tools

Define multiple tools for complex workflows:

<CodeGroup>
  ```typescript title="TypeScript"
  const calculatorTool = {
    type: 'function' as const,
    name: 'calculate',
    description: 'Perform mathematical calculations',
    strict: null,
    parameters: {
      type: 'object',
      properties: {
        expression: {
          type: 'string',
          description: 'The mathematical expression to evaluate',
        },
      },
      required: ['expression'],
    },
  };

  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: [
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'What is 25 * 4?',
            },
          ],
        },
      ],
      tools: [weatherTool, calculatorTool],
      tool_choice: 'auto',
      max_output_tokens: 9000,
    }),
  });
  ```

  ```python title="Python"
  calculator_tool = {
      'type': 'function',
      'name': 'calculate',
      'description': 'Perform mathematical calculations',
      'strict': None,
      'parameters': {
          'type': 'object',
          'properties': {
              'expression': {
                  'type': 'string',
                  'description': 'The mathematical expression to evaluate',
              },
          },
          'required': ['expression'],
      },
  }

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': [
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'What is 25 * 4?',
                      },
                  ],
              },
          ],
          'tools': [weather_tool, calculator_tool],
          'tool_choice': 'auto',
          'max_output_tokens': 9000,
      }
  )
  ```
</CodeGroup>

## Parallel Tool Calls

The API supports parallel execution of multiple tools:

<CodeGroup>
  ```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: [
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'Calculate 10*5 and also tell me the weather in Miami',
            },
          ],
        },
      ],
      tools: [weatherTool, calculatorTool],
      tool_choice: 'auto',
      max_output_tokens: 9000,
    }),
  });

  const result = await response.json();
  console.log(result);
  ```

  ```python title="Python"
  import requests

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': [
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'Calculate 10*5 and also tell me the weather in Miami',
                      },
                  ],
              },
          ],
          'tools': [weather_tool, calculator_tool],
          'tool_choice': 'auto',
          'max_output_tokens': 9000,
      }
  )

  result = response.json()
  print(result)
  ```
</CodeGroup>

## Tool Call Response

When tools are called, the response includes function call information:

```json
{
  "id": "resp_1234567890",
  "object": "response",
  "created_at": 1234567890,
  "model": "openai/o4-mini",
  "output": [
    {
      "type": "function_call",
      "id": "fc_abc123",
      "call_id": "call_xyz789",
      "name": "get_weather",
      "arguments": "{\"location\":\"San Francisco, CA\"}"
    }
  ],
  "usage": {
    "input_tokens": 45,
    "output_tokens": 25,
    "total_tokens": 70
  },
  "status": "completed"
}
```

## Tool Responses in Conversation

Include tool responses in follow-up requests:

<CodeGroup>
  ```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: [
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'What is the weather in Boston?',
            },
          ],
        },
        {
          type: 'function_call',
          id: 'fc_1',
          call_id: 'call_123',
          name: 'get_weather',
          arguments: JSON.stringify({ location: 'Boston, MA' }),
        },
        {
          type: 'function_call_output',
          id: 'fc_output_1',
          call_id: 'call_123',
          output: JSON.stringify({ temperature: '72°F', condition: 'Sunny' }),
        },
        {
          type: 'message',
          role: 'assistant',
          id: 'msg_abc123',
          status: 'completed',
          content: [
            {
              type: 'output_text',
              text: 'The weather in Boston is currently 72°F and sunny. This looks like perfect weather for a picnic!',
              annotations: []
            }
          ]
        },
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'Is that good weather for a picnic?',
            },
          ],
        },
      ],
      max_output_tokens: 9000,
    }),
  });
  ```

  ```python title="Python"
  import requests

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': [
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'What is the weather in Boston?',
                      },
                  ],
              },
              {
                  'type': 'function_call',
                  'id': 'fc_1',
                  'call_id': 'call_123',
                  'name': 'get_weather',
                  'arguments': '{"location": "Boston, MA"}',
              },
              {
                  'type': 'function_call_output',
                  'id': 'fc_output_1',
                  'call_id': 'call_123',
                  'output': '{"temperature": "72°F", "condition": "Sunny"}',
              },
              {
                  'type': 'message',
                  'role': 'assistant',
                  'id': 'msg_abc123',
                  'status': 'completed',
                  'content': [
                      {
                          'type': 'output_text',
                          'text': 'The weather in Boston is currently 72°F and sunny. This looks like perfect weather for a picnic!',
                          'annotations': []
                      }
                  ]
              },
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'Is that good weather for a picnic?',
                      },
                  ],
              },
          ],
          'max_output_tokens': 9000,
      }
  )
  ```
</CodeGroup>

<Info title="Required Field">
  The `id` field is required for `function_call_output` objects when including tool responses in conversation history.
</Info>

## Streaming Tool Calls

Monitor tool calls in real-time with streaming:

<CodeGroup>
  ```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: [
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'What is the weather like in Tokyo, Japan? Please check the weather.',
            },
          ],
        },
      ],
      tools: [weatherTool],
      tool_choice: 'auto',
      stream: true,
      max_output_tokens: 9000,
    }),
  });

  const reader = response.body?.getReader();
  const decoder = new TextDecoder();

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    const chunk = decoder.decode(value);
    const lines = chunk.split('\n');

    for (const line of lines) {
      if (line.startsWith('data: ')) {
        const data = line.slice(6);
        if (data === '[DONE]') return;

        try {
          const parsed = JSON.parse(data);
          if (parsed.type === 'response.output_item.added' &&
              parsed.item?.type === 'function_call') {
            console.log('Function call:', parsed.item.name);
          }
          if (parsed.type === 'response.function_call_arguments.done') {
            console.log('Arguments:', parsed.arguments);
          }
        } catch (e) {
          // Skip invalid JSON
        }
      }
    }
  }
  ```

  ```python title="Python"
  import requests
  import json

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': [
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'What is the weather like in Tokyo, Japan? Please check the weather.',
                      },
                  ],
              },
          ],
          'tools': [weather_tool],
          'tool_choice': 'auto',
          'stream': True,
          'max_output_tokens': 9000,
      },
      stream=True
  )

  for line in response.iter_lines():
      if line:
          line_str = line.decode('utf-8')
          if line_str.startswith('data: '):
              data = line_str[6:]
              if data == '[DONE]':
                  break
              try:
                  parsed = json.loads(data)
                  if (parsed.get('type') == 'response.output_item.added' and
                      parsed.get('item', {}).get('type') == 'function_call'):
                      print(f"Function call: {parsed['item']['name']}")
                  if parsed.get('type') == 'response.function_call_arguments.done':
                      print(f"Arguments: {parsed.get('arguments', '')}")
              except json.JSONDecodeError:
                  continue
  ```
</CodeGroup>

## Tool Validation

Ensure tool calls have proper structure:

```json
{
  "type": "function_call",
  "id": "fc_abc123",
  "call_id": "call_xyz789",
  "name": "get_weather",
  "arguments": "{\"location\":\"Seattle, WA\"}"
}
```

Required fields:

* `type`: Always "function\_call"
* `id`: Unique identifier for the function call object
* `name`: Function name matching tool definition
* `arguments`: Valid JSON string with function parameters
* `call_id`: Unique identifier for the call

## Best Practices

1. **Clear descriptions**: Provide detailed function descriptions and parameter explanations
2. **Proper schemas**: Use valid JSON Schema for parameters
3. **Error handling**: Handle cases where tools might not be called
4. **Parallel execution**: Design tools to work independently when possible
5. **Conversation flow**: Include tool responses in follow-up requests for context

## Next Steps

* Learn about [Web Search](./web-search) integration
* Explore [Reasoning](./reasoning) with tools
* Review [Basic Usage](./basic-usage) fundamentals


# Web Search

> Enable web search capabilities with real-time information retrieval and citation annotations using OpenRouter's Responses API Beta.

<Warning title="Beta API">
  This API is in **beta stage** and may have breaking changes.
</Warning>

The Responses API Beta supports web search integration, allowing models to access real-time information from the internet and provide responses with proper citations and annotations.

## Web Search Plugin

Enable web search using the `plugins` parameter:

<CodeGroup>
  ```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: 'What is OpenRouter?',
      plugins: [{ id: 'web', max_results: 3 }],
      max_output_tokens: 9000,
    }),
  });

  const result = await response.json();
  console.log(result);
  ```

  ```python title="Python"
  import requests

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': 'What is OpenRouter?',
          'plugins': [{'id': 'web', 'max_results': 3}],
          'max_output_tokens': 9000,
      }
  )

  result = response.json()
  print(result)
  ```

  ```bash title="cURL"
  curl -X POST https://openrouter.ai/api/v1/responses \
    -H "Authorization: Bearer YOUR_OPENROUTER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/o4-mini",
      "input": "What is OpenRouter?",
      "plugins": [{"id": "web", "max_results": 3}],
      "max_output_tokens": 9000
    }'
  ```
</CodeGroup>

## Plugin Configuration

Configure web search behavior:

| Parameter     | Type    | Description                               |
| ------------- | ------- | ----------------------------------------- |
| `id`          | string  | **Required.** Must be "web"               |
| `max_results` | integer | Maximum search results to retrieve (1-10) |

## Structured Message with Web Search

Use structured messages for more complex queries:

<CodeGroup>
  ```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: [
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'What was a positive news story from today?',
            },
          ],
        },
      ],
      plugins: [{ id: 'web', max_results: 2 }],
      max_output_tokens: 9000,
    }),
  });

  const result = await response.json();
  console.log(result);
  ```

  ```python title="Python"
  import requests

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': [
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'What was a positive news story from today?',
                      },
                  ],
              },
          ],
          'plugins': [{'id': 'web', 'max_results': 2}],
          'max_output_tokens': 9000,
      }
  )

  result = response.json()
  print(result)
  ```
</CodeGroup>

## Online Model Variants

Some models have built-in web search capabilities using the `:online` variant:

<CodeGroup>
  ```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini:online',
      input: 'What was a positive news story from today?',
      max_output_tokens: 9000,
    }),
  });

  const result = await response.json();
  console.log(result);
  ```

  ```python title="Python"
  import requests

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini:online',
          'input': 'What was a positive news story from today?',
          'max_output_tokens': 9000,
      }
  )

  result = response.json()
  print(result)
  ```
</CodeGroup>

## Response with Annotations

Web search responses include citation annotations:

```json
{
  "id": "resp_1234567890",
  "object": "response",
  "created_at": 1234567890,
  "model": "openai/o4-mini",
  "output": [
    {
      "type": "message",
      "id": "msg_abc123",
      "status": "completed",
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "OpenRouter is a unified API for accessing multiple Large Language Model providers through a single interface. It allows developers to access 100+ AI models from providers like OpenAI, Anthropic, Google, and others with intelligent routing and automatic failover.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://openrouter.ai/docs",
              "start_index": 0,
              "end_index": 85
            },
            {
              "type": "url_citation",
              "url": "https://openrouter.ai/models",
              "start_index": 120,
              "end_index": 180
            }
          ]
        }
      ]
    }
  ],
  "usage": {
    "input_tokens": 15,
    "output_tokens": 95,
    "total_tokens": 110
  },
  "status": "completed"
}
```

## Annotation Types

Web search responses can include different annotation types:

### URL Citation

```json
{
  "type": "url_citation",
  "url": "https://example.com/article",
  "start_index": 0,
  "end_index": 50
}
```

## Complex Search Queries

Handle multi-part search queries:

<CodeGroup>
  ```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: [
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'Compare OpenAI and Anthropic latest models',
            },
          ],
        },
      ],
      plugins: [{ id: 'web', max_results: 5 }],
      max_output_tokens: 9000,
    }),
  });

  const result = await response.json();
  console.log(result);
  ```

  ```python title="Python"
  import requests

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': [
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'Compare OpenAI and Anthropic latest models',
                      },
                  ],
              },
          ],
          'plugins': [{'id': 'web', 'max_results': 5}],
          'max_output_tokens': 9000,
      }
  )

  result = response.json()
  print(result)
  ```
</CodeGroup>

## Web Search in Conversation

Include web search in multi-turn conversations:

<CodeGroup>
  ```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: [
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'What is the latest version of React?',
            },
          ],
        },
        {
          type: 'message',
          id: 'msg_1',
          status: 'in_progress',
          role: 'assistant',
          content: [
            {
              type: 'output_text',
              text: 'Let me search for the latest React version.',
              annotations: [],
            },
          ],
        },
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'Yes, please find the most recent information',
            },
          ],
        },
      ],
      plugins: [{ id: 'web', max_results: 2 }],
      max_output_tokens: 9000,
    }),
  });

  const result = await response.json();
  console.log(result);
  ```

  ```python title="Python"
  import requests

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': [
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'What is the latest version of React?',
                      },
                  ],
              },
              {
                  'type': 'message',
                  'id': 'msg_1',
                  'status': 'in_progress',
                  'role': 'assistant',
                  'content': [
                      {
                          'type': 'output_text',
                          'text': 'Let me search for the latest React version.',
                          'annotations': [],
                      },
                  ],
              },
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'Yes, please find the most recent information',
                      },
                  ],
              },
          ],
          'plugins': [{'id': 'web', 'max_results': 2}],
          'max_output_tokens': 9000,
      }
  )

  result = response.json()
  print(result)
  ```
</CodeGroup>

## Streaming Web Search

Monitor web search progress with streaming:

<CodeGroup>
  ```typescript title="TypeScript"
  const response = await fetch('https://openrouter.ai/api/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/o4-mini',
      input: [
        {
          type: 'message',
          role: 'user',
          content: [
            {
              type: 'input_text',
              text: 'What is the latest news about AI?',
            },
          ],
        },
      ],
      plugins: [{ id: 'web', max_results: 2 }],
      stream: true,
      max_output_tokens: 9000,
    }),
  });

  const reader = response.body?.getReader();
  const decoder = new TextDecoder();

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    const chunk = decoder.decode(value);
    const lines = chunk.split('\n');

    for (const line of lines) {
      if (line.startsWith('data: ')) {
        const data = line.slice(6);
        if (data === '[DONE]') return;

        try {
          const parsed = JSON.parse(data);
          if (parsed.type === 'response.output_item.added' &&
              parsed.item?.type === 'message') {
            console.log('Message added');
          }
          if (parsed.type === 'response.completed') {
            const annotations = parsed.response?.output
              ?.find(o => o.type === 'message')
              ?.content?.find(c => c.type === 'output_text')
              ?.annotations || [];
            console.log('Citations:', annotations.length);
          }
        } catch (e) {
          // Skip invalid JSON
        }
      }
    }
  }
  ```

  ```python title="Python"
  import requests
  import json

  response = requests.post(
      'https://openrouter.ai/api/v1/responses',
      headers={
          'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY',
          'Content-Type': 'application/json',
      },
      json={
          'model': 'openai/o4-mini',
          'input': [
              {
                  'type': 'message',
                  'role': 'user',
                  'content': [
                      {
                          'type': 'input_text',
                          'text': 'What is the latest news about AI?',
                      },
                  ],
              },
          ],
          'plugins': [{'id': 'web', 'max_results': 2}],
          'stream': True,
          'max_output_tokens': 9000,
      },
      stream=True
  )

  for line in response.iter_lines():
      if line:
          line_str = line.decode('utf-8')
          if line_str.startswith('data: '):
              data = line_str[6:]
              if data == '[DONE]':
                  break
              try:
                  parsed = json.loads(data)
                  if (parsed.get('type') == 'response.output_item.added' and
                      parsed.get('item', {}).get('type') == 'message'):
                      print('Message added')
                  if parsed.get('type') == 'response.completed':
                      output = parsed.get('response', {}).get('output', [])
                      message = next((o for o in output if o.get('type') == 'message'), {})
                      content = message.get('content', [])
                      text_content = next((c for c in content if c.get('type') == 'output_text'), {})
                      annotations = text_content.get('annotations', [])
                      print(f'Citations: {len(annotations)}')
              except json.JSONDecodeError:
                  continue
  ```
</CodeGroup>

## Annotation Processing

Extract and process citation information:

<CodeGroup>
  ```typescript title="TypeScript"
  function extractCitations(response: any) {
    const messageOutput = response.output?.find((o: any) => o.type === 'message');
    const textContent = messageOutput?.content?.find((c: any) => c.type === 'output_text');
    const annotations = textContent?.annotations || [];

    return annotations
      .filter((annotation: any) => annotation.type === 'url_citation')
      .map((annotation: any) => ({
        url: annotation.url,
        text: textContent.text.slice(annotation.start_index, annotation.end_index),
        startIndex: annotation.start_index,
        endIndex: annotation.end_index,
      }));
  }

  const result = await response.json();
  const citations = extractCitations(result);
  console.log('Found citations:', citations);
  ```

  ```python title="Python"
  def extract_citations(response_data):
      output = response_data.get('output', [])
      message_output = next((o for o in output if o.get('type') == 'message'), {})
      content = message_output.get('content', [])
      text_content = next((c for c in content if c.get('type') == 'output_text'), {})
      annotations = text_content.get('annotations', [])
      text = text_content.get('text', '')

      citations = []
      for annotation in annotations:
          if annotation.get('type') == 'url_citation':
              citations.append({
                  'url': annotation.get('url'),
                  'text': text[annotation.get('start_index', 0):annotation.get('end_index', 0)],
                  'start_index': annotation.get('start_index'),
                  'end_index': annotation.get('end_index'),
              })

      return citations

  result = response.json()
  citations = extract_citations(result)
  print(f'Found citations: {citations}')
  ```
</CodeGroup>

## Best Practices

1. **Limit results**: Use appropriate `max_results` to balance quality and speed
2. **Handle annotations**: Process citation annotations for proper attribution
3. **Query specificity**: Make search queries specific for better results
4. **Error handling**: Handle cases where web search might fail
5. **Rate limits**: Be mindful of search rate limits

## Next Steps

* Learn about [Tool Calling](./tool-calling) integration
* Explore [Reasoning](./reasoning) capabilities
* Review [Basic Usage](./basic-usage) fundamentals


# Error Handling

> Learn how to handle errors in OpenRouter's Responses API Beta with the basic error response format.

<Warning title="Beta API">
  This API is in **beta stage** and may have breaking changes. Use with caution in production environments.
</Warning>

<Info title="Stateless Only">
  This API is **stateless** - each request is independent and no conversation state is persisted between requests. You must include the full conversation history in each request.
</Info>

The Responses API Beta returns structured error responses that follow a consistent format.

## Error Response Format

All errors follow this structure:

```json
{
  "error": {
    "code": "invalid_prompt",
    "message": "Detailed error description"
  },
  "metadata": null
}
```

### Error Codes

The API uses the following error codes:

| Code                  | Description               | Equivalent HTTP Status |
| --------------------- | ------------------------- | ---------------------- |
| `invalid_prompt`      | Request validation failed | 400                    |
| `rate_limit_exceeded` | Too many requests         | 429                    |
| `server_error`        | Internal server error     | 500+                   |


# Create a response

POST https://openrouter.ai/api/v1/responses
Content-Type: application/json

Creates a streaming or non-streaming response using OpenResponses API format

Reference: https://openrouter.ai/docs/api-reference/beta-responses/create-responses

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create a response
  version: endpoint_betaResponses.createResponses
paths:
  /responses:
    post:
      operationId: create-responses
      summary: Create a response
      description: >-
        Creates a streaming or non-streaming response using OpenResponses API
        format
      tags:
        - - subpackage_betaResponses
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OpenResponsesNonStreamingResponse'
        '400':
          description: Bad Request - Invalid request parameters or malformed input
          content: {}
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '402':
          description: Payment Required - Insufficient credits or quota to complete request
          content: {}
        '404':
          description: Not Found - Resource does not exist
          content: {}
        '408':
          description: Request Timeout - Operation exceeded time limit
          content: {}
        '413':
          description: Payload Too Large - Request payload exceeds size limits
          content: {}
        '422':
          description: Unprocessable Entity - Semantic validation failure
          content: {}
        '429':
          description: Too Many Requests - Rate limit exceeded
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
        '502':
          description: Bad Gateway - Provider/upstream API failure
          content: {}
        '503':
          description: Service Unavailable - Service temporarily unavailable
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OpenResponsesRequest'
components:
  schemas:
    OutputItemReasoningType:
      type: string
      enum:
        - value: reasoning
    ReasoningTextContentType:
      type: string
      enum:
        - value: reasoning_text
    ReasoningTextContent:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ReasoningTextContentType'
        text:
          type: string
      required:
        - type
        - text
    ReasoningSummaryTextType:
      type: string
      enum:
        - value: summary_text
    ReasoningSummaryText:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ReasoningSummaryTextType'
        text:
          type: string
      required:
        - type
        - text
    OutputItemReasoningStatus0:
      type: string
      enum:
        - value: completed
    OutputItemReasoningStatus1:
      type: string
      enum:
        - value: incomplete
    OutputItemReasoningStatus2:
      type: string
      enum:
        - value: in_progress
    OutputItemReasoningStatus:
      oneOf:
        - $ref: '#/components/schemas/OutputItemReasoningStatus0'
        - $ref: '#/components/schemas/OutputItemReasoningStatus1'
        - $ref: '#/components/schemas/OutputItemReasoningStatus2'
    OpenResponsesReasoningFormat:
      type: string
      enum:
        - value: unknown
        - value: openai-responses-v1
        - value: xai-responses-v1
        - value: anthropic-claude-v1
    OpenResponsesReasoning:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OutputItemReasoningType'
        id:
          type: string
        content:
          type: array
          items:
            $ref: '#/components/schemas/ReasoningTextContent'
        summary:
          type: array
          items:
            $ref: '#/components/schemas/ReasoningSummaryText'
        encrypted_content:
          type:
            - string
            - 'null'
        status:
          $ref: '#/components/schemas/OutputItemReasoningStatus'
        signature:
          type:
            - string
            - 'null'
        format:
          oneOf:
            - $ref: '#/components/schemas/OpenResponsesReasoningFormat'
            - type: 'null'
      required:
        - type
        - id
        - summary
    OpenResponsesEasyInputMessageType:
      type: string
      enum:
        - value: message
    OpenResponsesEasyInputMessageRole0:
      type: string
      enum:
        - value: user
    OpenResponsesEasyInputMessageRole1:
      type: string
      enum:
        - value: system
    OpenResponsesEasyInputMessageRole2:
      type: string
      enum:
        - value: assistant
    OpenResponsesEasyInputMessageRole3:
      type: string
      enum:
        - value: developer
    OpenResponsesEasyInputMessageRole:
      oneOf:
        - $ref: '#/components/schemas/OpenResponsesEasyInputMessageRole0'
        - $ref: '#/components/schemas/OpenResponsesEasyInputMessageRole1'
        - $ref: '#/components/schemas/OpenResponsesEasyInputMessageRole2'
        - $ref: '#/components/schemas/OpenResponsesEasyInputMessageRole3'
    ResponseInputTextType:
      type: string
      enum:
        - value: input_text
    ResponseInputText:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ResponseInputTextType'
        text:
          type: string
      required:
        - type
        - text
    ResponseInputImageType:
      type: string
      enum:
        - value: input_image
    ResponseInputImageDetail:
      type: string
      enum:
        - value: auto
        - value: high
        - value: low
    ResponseInputImage:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ResponseInputImageType'
        detail:
          $ref: '#/components/schemas/ResponseInputImageDetail'
        image_url:
          type:
            - string
            - 'null'
      required:
        - type
        - detail
    ResponseInputFileType:
      type: string
      enum:
        - value: input_file
    ResponseInputFile:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ResponseInputFileType'
        file_id:
          type:
            - string
            - 'null'
        file_data:
          type: string
        filename:
          type: string
        file_url:
          type: string
      required:
        - type
    ResponseInputAudioType:
      type: string
      enum:
        - value: input_audio
    ResponseInputAudioInputAudioFormat:
      type: string
      enum:
        - value: mp3
        - value: wav
    ResponseInputAudioInputAudio:
      type: object
      properties:
        data:
          type: string
        format:
          $ref: '#/components/schemas/ResponseInputAudioInputAudioFormat'
      required:
        - data
        - format
    ResponseInputAudio:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ResponseInputAudioType'
        input_audio:
          $ref: '#/components/schemas/ResponseInputAudioInputAudio'
      required:
        - type
        - input_audio
    OpenResponsesEasyInputMessageContentOneOf0Items:
      oneOf:
        - $ref: '#/components/schemas/ResponseInputText'
        - $ref: '#/components/schemas/ResponseInputImage'
        - $ref: '#/components/schemas/ResponseInputFile'
        - $ref: '#/components/schemas/ResponseInputAudio'
    OpenResponsesEasyInputMessageContent0:
      type: array
      items:
        $ref: '#/components/schemas/OpenResponsesEasyInputMessageContentOneOf0Items'
    OpenResponsesEasyInputMessageContent:
      oneOf:
        - $ref: '#/components/schemas/OpenResponsesEasyInputMessageContent0'
        - type: string
    OpenResponsesEasyInputMessage:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OpenResponsesEasyInputMessageType'
        role:
          $ref: '#/components/schemas/OpenResponsesEasyInputMessageRole'
        content:
          $ref: '#/components/schemas/OpenResponsesEasyInputMessageContent'
      required:
        - role
        - content
    OpenResponsesInputMessageItemType:
      type: string
      enum:
        - value: message
    OpenResponsesInputMessageItemRole0:
      type: string
      enum:
        - value: user
    OpenResponsesInputMessageItemRole1:
      type: string
      enum:
        - value: system
    OpenResponsesInputMessageItemRole2:
      type: string
      enum:
        - value: developer
    OpenResponsesInputMessageItemRole:
      oneOf:
        - $ref: '#/components/schemas/OpenResponsesInputMessageItemRole0'
        - $ref: '#/components/schemas/OpenResponsesInputMessageItemRole1'
        - $ref: '#/components/schemas/OpenResponsesInputMessageItemRole2'
    OpenResponsesInputMessageItemContentItems:
      oneOf:
        - $ref: '#/components/schemas/ResponseInputText'
        - $ref: '#/components/schemas/ResponseInputImage'
        - $ref: '#/components/schemas/ResponseInputFile'
        - $ref: '#/components/schemas/ResponseInputAudio'
    OpenResponsesInputMessageItem:
      type: object
      properties:
        id:
          type: string
        type:
          $ref: '#/components/schemas/OpenResponsesInputMessageItemType'
        role:
          $ref: '#/components/schemas/OpenResponsesInputMessageItemRole'
        content:
          type: array
          items:
            $ref: '#/components/schemas/OpenResponsesInputMessageItemContentItems'
      required:
        - role
        - content
    OpenResponsesFunctionToolCallType:
      type: string
      enum:
        - value: function_call
    ToolCallStatus:
      type: string
      enum:
        - value: in_progress
        - value: completed
        - value: incomplete
    OpenResponsesFunctionToolCall:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OpenResponsesFunctionToolCallType'
        call_id:
          type: string
        name:
          type: string
        arguments:
          type: string
        id:
          type: string
        status:
          $ref: '#/components/schemas/ToolCallStatus'
      required:
        - type
        - call_id
        - name
        - arguments
        - id
    OpenResponsesFunctionCallOutputType:
      type: string
      enum:
        - value: function_call_output
    OpenResponsesFunctionCallOutput:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OpenResponsesFunctionCallOutputType'
        id:
          type: string
        call_id:
          type: string
        output:
          type: string
        status:
          $ref: '#/components/schemas/ToolCallStatus'
      required:
        - type
        - id
        - call_id
        - output
    OutputMessageRole:
      type: string
      enum:
        - value: assistant
    OutputMessageType:
      type: string
      enum:
        - value: message
    OutputMessageStatus0:
      type: string
      enum:
        - value: completed
    OutputMessageStatus1:
      type: string
      enum:
        - value: incomplete
    OutputMessageStatus2:
      type: string
      enum:
        - value: in_progress
    OutputMessageStatus:
      oneOf:
        - $ref: '#/components/schemas/OutputMessageStatus0'
        - $ref: '#/components/schemas/OutputMessageStatus1'
        - $ref: '#/components/schemas/OutputMessageStatus2'
    ResponseOutputTextType:
      type: string
      enum:
        - value: output_text
    FileCitationType:
      type: string
      enum:
        - value: file_citation
    FileCitation:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/FileCitationType'
        file_id:
          type: string
        filename:
          type: string
        index:
          type: number
          format: double
      required:
        - type
        - file_id
        - filename
        - index
    UrlCitationType:
      type: string
      enum:
        - value: url_citation
    URLCitation:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/UrlCitationType'
        url:
          type: string
        title:
          type: string
        start_index:
          type: number
          format: double
        end_index:
          type: number
          format: double
      required:
        - type
        - url
        - title
        - start_index
        - end_index
    FilePathType:
      type: string
      enum:
        - value: file_path
    FilePath:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/FilePathType'
        file_id:
          type: string
        index:
          type: number
          format: double
      required:
        - type
        - file_id
        - index
    OpenAIResponsesAnnotation:
      oneOf:
        - $ref: '#/components/schemas/FileCitation'
        - $ref: '#/components/schemas/URLCitation'
        - $ref: '#/components/schemas/FilePath'
    ResponseOutputText:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ResponseOutputTextType'
        text:
          type: string
        annotations:
          type: array
          items:
            $ref: '#/components/schemas/OpenAIResponsesAnnotation'
      required:
        - type
        - text
    OpenAiResponsesRefusalContentType:
      type: string
      enum:
        - value: refusal
    OpenAIResponsesRefusalContent:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OpenAiResponsesRefusalContentType'
        refusal:
          type: string
      required:
        - type
        - refusal
    OutputMessageContentItems:
      oneOf:
        - $ref: '#/components/schemas/ResponseOutputText'
        - $ref: '#/components/schemas/OpenAIResponsesRefusalContent'
    ResponsesOutputMessage:
      type: object
      properties:
        id:
          type: string
        role:
          $ref: '#/components/schemas/OutputMessageRole'
        type:
          $ref: '#/components/schemas/OutputMessageType'
        status:
          $ref: '#/components/schemas/OutputMessageStatus'
        content:
          type: array
          items:
            $ref: '#/components/schemas/OutputMessageContentItems'
      required:
        - id
        - role
        - type
        - content
    ResponsesOutputItemReasoningType:
      type: string
      enum:
        - value: reasoning
    ResponsesOutputItemReasoningStatus0:
      type: string
      enum:
        - value: completed
    ResponsesOutputItemReasoningStatus1:
      type: string
      enum:
        - value: incomplete
    ResponsesOutputItemReasoningStatus2:
      type: string
      enum:
        - value: in_progress
    ResponsesOutputItemReasoningStatus:
      oneOf:
        - $ref: '#/components/schemas/ResponsesOutputItemReasoningStatus0'
        - $ref: '#/components/schemas/ResponsesOutputItemReasoningStatus1'
        - $ref: '#/components/schemas/ResponsesOutputItemReasoningStatus2'
    ResponsesOutputItemReasoning:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ResponsesOutputItemReasoningType'
        id:
          type: string
        content:
          type: array
          items:
            $ref: '#/components/schemas/ReasoningTextContent'
        summary:
          type: array
          items:
            $ref: '#/components/schemas/ReasoningSummaryText'
        encrypted_content:
          type:
            - string
            - 'null'
        status:
          $ref: '#/components/schemas/ResponsesOutputItemReasoningStatus'
      required:
        - type
        - summary
    OutputItemFunctionCallType:
      type: string
      enum:
        - value: function_call
    OutputItemFunctionCallStatus0:
      type: string
      enum:
        - value: completed
    OutputItemFunctionCallStatus1:
      type: string
      enum:
        - value: incomplete
    OutputItemFunctionCallStatus2:
      type: string
      enum:
        - value: in_progress
    OutputItemFunctionCallStatus:
      oneOf:
        - $ref: '#/components/schemas/OutputItemFunctionCallStatus0'
        - $ref: '#/components/schemas/OutputItemFunctionCallStatus1'
        - $ref: '#/components/schemas/OutputItemFunctionCallStatus2'
    ResponsesOutputItemFunctionCall:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OutputItemFunctionCallType'
        id:
          type: string
        name:
          type: string
        arguments:
          type: string
        call_id:
          type: string
        status:
          $ref: '#/components/schemas/OutputItemFunctionCallStatus'
      required:
        - type
        - name
        - arguments
        - call_id
    OutputItemWebSearchCallType:
      type: string
      enum:
        - value: web_search_call
    WebSearchStatus:
      type: string
      enum:
        - value: completed
        - value: searching
        - value: in_progress
        - value: failed
    ResponsesWebSearchCallOutput:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OutputItemWebSearchCallType'
        id:
          type: string
        status:
          $ref: '#/components/schemas/WebSearchStatus'
      required:
        - type
        - id
        - status
    OutputItemFileSearchCallType:
      type: string
      enum:
        - value: file_search_call
    ResponsesOutputItemFileSearchCall:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OutputItemFileSearchCallType'
        id:
          type: string
        queries:
          type: array
          items:
            type: string
        status:
          $ref: '#/components/schemas/WebSearchStatus'
      required:
        - type
        - id
        - queries
        - status
    OutputItemImageGenerationCallType:
      type: string
      enum:
        - value: image_generation_call
    ImageGenerationStatus:
      type: string
      enum:
        - value: in_progress
        - value: completed
        - value: generating
        - value: failed
    ResponsesImageGenerationCall:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OutputItemImageGenerationCallType'
        id:
          type: string
        result:
          type:
            - string
            - 'null'
        status:
          $ref: '#/components/schemas/ImageGenerationStatus'
      required:
        - type
        - id
        - result
        - status
    OpenResponsesInputOneOf1Items:
      oneOf:
        - $ref: '#/components/schemas/OpenResponsesReasoning'
        - $ref: '#/components/schemas/OpenResponsesEasyInputMessage'
        - $ref: '#/components/schemas/OpenResponsesInputMessageItem'
        - $ref: '#/components/schemas/OpenResponsesFunctionToolCall'
        - $ref: '#/components/schemas/OpenResponsesFunctionCallOutput'
        - $ref: '#/components/schemas/ResponsesOutputMessage'
        - $ref: '#/components/schemas/ResponsesOutputItemReasoning'
        - $ref: '#/components/schemas/ResponsesOutputItemFunctionCall'
        - $ref: '#/components/schemas/ResponsesWebSearchCallOutput'
        - $ref: '#/components/schemas/ResponsesOutputItemFileSearchCall'
        - $ref: '#/components/schemas/ResponsesImageGenerationCall'
    OpenResponsesInput1:
      type: array
      items:
        $ref: '#/components/schemas/OpenResponsesInputOneOf1Items'
    OpenResponsesInput:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/OpenResponsesInput1'
    OpenResponsesRequestMetadata:
      type: object
      additionalProperties:
        type: string
    OpenResponsesWebSearchPreviewToolType:
      type: string
      enum:
        - value: web_search_preview
    ResponsesSearchContextSize:
      type: string
      enum:
        - value: low
        - value: medium
        - value: high
    WebSearchPreviewToolUserLocationType:
      type: string
      enum:
        - value: approximate
    WebSearchPreviewToolUserLocation:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/WebSearchPreviewToolUserLocationType'
        city:
          type:
            - string
            - 'null'
        country:
          type:
            - string
            - 'null'
        region:
          type:
            - string
            - 'null'
        timezone:
          type:
            - string
            - 'null'
      required:
        - type
    OpenResponsesWebSearchPreviewTool:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OpenResponsesWebSearchPreviewToolType'
        search_context_size:
          $ref: '#/components/schemas/ResponsesSearchContextSize'
        user_location:
          $ref: '#/components/schemas/WebSearchPreviewToolUserLocation'
      required:
        - type
    OpenResponsesWebSearchPreview20250311ToolType:
      type: string
      enum:
        - value: web_search_preview_2025_03_11
    OpenResponsesWebSearchPreview20250311Tool:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OpenResponsesWebSearchPreview20250311ToolType'
        search_context_size:
          $ref: '#/components/schemas/ResponsesSearchContextSize'
        user_location:
          $ref: '#/components/schemas/WebSearchPreviewToolUserLocation'
      required:
        - type
    OpenResponsesWebSearchToolType:
      type: string
      enum:
        - value: web_search
    OpenResponsesWebSearchToolFilters:
      type: object
      properties:
        allowed_domains:
          type:
            - array
            - 'null'
          items:
            type: string
    ResponsesWebSearchUserLocationType:
      type: string
      enum:
        - value: approximate
    ResponsesWebSearchUserLocation:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ResponsesWebSearchUserLocationType'
        city:
          type:
            - string
            - 'null'
        country:
          type:
            - string
            - 'null'
        region:
          type:
            - string
            - 'null'
        timezone:
          type:
            - string
            - 'null'
    OpenResponsesWebSearchTool:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OpenResponsesWebSearchToolType'
        filters:
          oneOf:
            - $ref: '#/components/schemas/OpenResponsesWebSearchToolFilters'
            - type: 'null'
        search_context_size:
          $ref: '#/components/schemas/ResponsesSearchContextSize'
        user_location:
          $ref: '#/components/schemas/ResponsesWebSearchUserLocation'
      required:
        - type
    OpenResponsesWebSearch20250826ToolType:
      type: string
      enum:
        - value: web_search_2025_08_26
    OpenResponsesWebSearch20250826ToolFilters:
      type: object
      properties:
        allowed_domains:
          type:
            - array
            - 'null'
          items:
            type: string
    OpenResponsesWebSearch20250826Tool:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OpenResponsesWebSearch20250826ToolType'
        filters:
          oneOf:
            - $ref: '#/components/schemas/OpenResponsesWebSearch20250826ToolFilters'
            - type: 'null'
        search_context_size:
          $ref: '#/components/schemas/ResponsesSearchContextSize'
        user_location:
          $ref: '#/components/schemas/ResponsesWebSearchUserLocation'
      required:
        - type
    OpenResponsesRequestToolsItems:
      oneOf:
        - type: object
          additionalProperties:
            description: Any type
        - $ref: '#/components/schemas/OpenResponsesWebSearchPreviewTool'
        - $ref: '#/components/schemas/OpenResponsesWebSearchPreview20250311Tool'
        - $ref: '#/components/schemas/OpenResponsesWebSearchTool'
        - $ref: '#/components/schemas/OpenResponsesWebSearch20250826Tool'
    OpenAiResponsesToolChoice0:
      type: string
      enum:
        - value: auto
    OpenAiResponsesToolChoice1:
      type: string
      enum:
        - value: none
    OpenAiResponsesToolChoice2:
      type: string
      enum:
        - value: required
    OpenAiResponsesToolChoiceOneOf3Type:
      type: string
      enum:
        - value: function
    OpenAiResponsesToolChoice3:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OpenAiResponsesToolChoiceOneOf3Type'
        name:
          type: string
      required:
        - type
        - name
    OpenAiResponsesToolChoiceOneOf4Type0:
      type: string
      enum:
        - value: web_search_preview_2025_03_11
    OpenAiResponsesToolChoiceOneOf4Type1:
      type: string
      enum:
        - value: web_search_preview
    OpenAiResponsesToolChoiceOneOf4Type:
      oneOf:
        - $ref: '#/components/schemas/OpenAiResponsesToolChoiceOneOf4Type0'
        - $ref: '#/components/schemas/OpenAiResponsesToolChoiceOneOf4Type1'
    OpenAiResponsesToolChoice4:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OpenAiResponsesToolChoiceOneOf4Type'
      required:
        - type
    OpenAIResponsesToolChoice:
      oneOf:
        - $ref: '#/components/schemas/OpenAiResponsesToolChoice0'
        - $ref: '#/components/schemas/OpenAiResponsesToolChoice1'
        - $ref: '#/components/schemas/OpenAiResponsesToolChoice2'
        - $ref: '#/components/schemas/OpenAiResponsesToolChoice3'
        - $ref: '#/components/schemas/OpenAiResponsesToolChoice4'
    ResponsesFormatTextType:
      type: string
      enum:
        - value: text
    ResponsesFormatText:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ResponsesFormatTextType'
      required:
        - type
    ResponsesFormatJsonObjectType:
      type: string
      enum:
        - value: json_object
    ResponsesFormatJSONObject:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ResponsesFormatJsonObjectType'
      required:
        - type
    ResponsesFormatTextJsonSchemaConfigType:
      type: string
      enum:
        - value: json_schema
    ResponsesFormatTextJSONSchemaConfig:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ResponsesFormatTextJsonSchemaConfigType'
        name:
          type: string
        description:
          type: string
        strict:
          type:
            - boolean
            - 'null'
        schema:
          type: object
          additionalProperties:
            description: Any type
      required:
        - type
        - name
        - schema
    ResponseFormatTextConfig:
      oneOf:
        - $ref: '#/components/schemas/ResponsesFormatText'
        - $ref: '#/components/schemas/ResponsesFormatJSONObject'
        - $ref: '#/components/schemas/ResponsesFormatTextJSONSchemaConfig'
    ResponseTextConfigVerbosity:
      type: string
      enum:
        - value: high
        - value: low
        - value: medium
    OpenResponsesResponseText:
      type: object
      properties:
        format:
          $ref: '#/components/schemas/ResponseFormatTextConfig'
        verbosity:
          oneOf:
            - $ref: '#/components/schemas/ResponseTextConfigVerbosity'
            - type: 'null'
    OpenAIResponsesReasoningEffort:
      type: string
      enum:
        - value: high
        - value: medium
        - value: low
        - value: minimal
    ReasoningSummaryVerbosity:
      type: string
      enum:
        - value: auto
        - value: concise
        - value: detailed
    OpenResponsesReasoningConfig:
      type: object
      properties:
        effort:
          $ref: '#/components/schemas/OpenAIResponsesReasoningEffort'
        summary:
          $ref: '#/components/schemas/ReasoningSummaryVerbosity'
        max_tokens:
          type:
            - number
            - 'null'
          format: double
        enabled:
          type:
            - boolean
            - 'null'
    OpenAiResponsesPromptVariables:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ResponseInputText'
        - $ref: '#/components/schemas/ResponseInputImage'
        - $ref: '#/components/schemas/ResponseInputFile'
    OpenAIResponsesPrompt:
      type: object
      properties:
        id:
          type: string
        variables:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/OpenAiResponsesPromptVariables'
      required:
        - id
    OpenAIResponsesIncludable:
      type: string
      enum:
        - value: file_search_call.results
        - value: message.input_image.image_url
        - value: computer_call_output.output.image_url
        - value: reasoning.encrypted_content
        - value: code_interpreter_call.outputs
    OpenResponsesRequestServiceTier:
      type: object
      properties: {}
    OpenResponsesRequestTruncation:
      type: object
      properties: {}
    OpenResponsesRequestProviderDataCollection:
      type: string
      enum:
        - value: deny
        - value: allow
    ProviderName:
      type: string
      enum:
        - value: AnyScale
        - value: Cent-ML
        - value: HuggingFace
        - value: Hyperbolic 2
        - value: Lepton
        - value: Lynn 2
        - value: Lynn
        - value: Mancer
        - value: Modal
        - value: OctoAI
        - value: Recursal
        - value: Reflection
        - value: Replicate
        - value: SambaNova 2
        - value: SF Compute
        - value: Together 2
        - value: 01.AI
        - value: AI21
        - value: AionLabs
        - value: Alibaba
        - value: Amazon Bedrock
        - value: Anthropic
        - value: AtlasCloud
        - value: Atoma
        - value: Avian
        - value: Azure
        - value: BaseTen
        - value: Cerebras
        - value: Chutes
        - value: Cirrascale
        - value: Clarifai
        - value: Cloudflare
        - value: Cohere
        - value: CrofAI
        - value: Crusoe
        - value: DeepInfra
        - value: DeepSeek
        - value: Enfer
        - value: Featherless
        - value: Fireworks
        - value: Friendli
        - value: GMICloud
        - value: Google
        - value: Google AI Studio
        - value: Groq
        - value: Hyperbolic
        - value: Inception
        - value: InferenceNet
        - value: Infermatic
        - value: Inflection
        - value: InoCloud
        - value: Kluster
        - value: Lambda
        - value: Liquid
        - value: Mancer 2
        - value: Meta
        - value: Minimax
        - value: ModelRun
        - value: Mistral
        - value: Modular
        - value: Moonshot AI
        - value: Morph
        - value: NCompass
        - value: Nebius
        - value: NextBit
        - value: Nineteen
        - value: Novita
        - value: Nvidia
        - value: OpenAI
        - value: OpenInference
        - value: Parasail
        - value: Perplexity
        - value: Phala
        - value: Relace
        - value: SambaNova
        - value: SiliconFlow
        - value: Stealth
        - value: Switchpoint
        - value: Targon
        - value: Together
        - value: Ubicloud
        - value: Venice
        - value: WandB
        - value: xAI
        - value: Z.AI
        - value: FakeProvider
    OpenResponsesRequestProviderOrderItems:
      oneOf:
        - $ref: '#/components/schemas/ProviderName'
        - type: string
    OpenResponsesRequestProviderOnlyItems:
      oneOf:
        - $ref: '#/components/schemas/ProviderName'
        - type: string
    OpenResponsesRequestProviderIgnoreItems:
      oneOf:
        - $ref: '#/components/schemas/ProviderName'
        - type: string
    Quantization:
      type: string
      enum:
        - value: int4
        - value: int8
        - value: fp4
        - value: fp6
        - value: fp8
        - value: fp16
        - value: bf16
        - value: fp32
        - value: unknown
    OpenResponsesRequestProviderSort:
      type: string
      enum:
        - value: price
        - value: throughput
        - value: latency
    BigNumberUnion:
      oneOf:
        - type: number
          format: double
        - type: string
        - type: number
          format: double
    OpenResponsesRequestProviderMaxPrice:
      type: object
      properties:
        prompt:
          $ref: '#/components/schemas/BigNumberUnion'
        completion:
          $ref: '#/components/schemas/BigNumberUnion'
        image:
          $ref: '#/components/schemas/BigNumberUnion'
        audio:
          $ref: '#/components/schemas/BigNumberUnion'
        request:
          $ref: '#/components/schemas/BigNumberUnion'
    OpenResponsesRequestProvider:
      type: object
      properties:
        allow_fallbacks:
          type:
            - boolean
            - 'null'
        require_parameters:
          type:
            - boolean
            - 'null'
        data_collection:
          oneOf:
            - $ref: '#/components/schemas/OpenResponsesRequestProviderDataCollection'
            - type: 'null'
        zdr:
          type:
            - boolean
            - 'null'
        enforce_distillable_text:
          type:
            - boolean
            - 'null'
        order:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/OpenResponsesRequestProviderOrderItems'
        only:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/OpenResponsesRequestProviderOnlyItems'
        ignore:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/OpenResponsesRequestProviderIgnoreItems'
        quantizations:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/Quantization'
        sort:
          oneOf:
            - $ref: '#/components/schemas/OpenResponsesRequestProviderSort'
            - type: 'null'
        max_price:
          $ref: '#/components/schemas/OpenResponsesRequestProviderMaxPrice'
    OpenResponsesRequestPluginsItemsOneOf0Id:
      type: string
      enum:
        - value: moderation
    OpenResponsesRequestPluginsItems0:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/OpenResponsesRequestPluginsItemsOneOf0Id'
      required:
        - id
    OpenResponsesRequestPluginsItemsOneOf1Id:
      type: string
      enum:
        - value: web
    OpenResponsesRequestPluginsItemsOneOf1Engine:
      type: string
      enum:
        - value: native
        - value: exa
    OpenResponsesRequestPluginsItems1:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/OpenResponsesRequestPluginsItemsOneOf1Id'
        max_results:
          type: number
          format: double
        search_prompt:
          type: string
        engine:
          $ref: '#/components/schemas/OpenResponsesRequestPluginsItemsOneOf1Engine'
      required:
        - id
    OpenResponsesRequestPluginsItemsOneOf2Id:
      type: string
      enum:
        - value: file-parser
    OpenResponsesRequestPluginsItemsOneOf2PdfEngine:
      type: string
      enum:
        - value: mistral-ocr
        - value: pdf-text
        - value: native
    OpenResponsesRequestPluginsItemsOneOf2Pdf:
      type: object
      properties:
        engine:
          $ref: '#/components/schemas/OpenResponsesRequestPluginsItemsOneOf2PdfEngine'
    OpenResponsesRequestPluginsItems2:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/OpenResponsesRequestPluginsItemsOneOf2Id'
        max_files:
          type: number
          format: double
        pdf:
          $ref: '#/components/schemas/OpenResponsesRequestPluginsItemsOneOf2Pdf'
      required:
        - id
    OpenResponsesRequestPluginsItems:
      oneOf:
        - $ref: '#/components/schemas/OpenResponsesRequestPluginsItems0'
        - $ref: '#/components/schemas/OpenResponsesRequestPluginsItems1'
        - $ref: '#/components/schemas/OpenResponsesRequestPluginsItems2'
    OpenResponsesRequest:
      type: object
      properties:
        input:
          $ref: '#/components/schemas/OpenResponsesInput'
        instructions:
          type:
            - string
            - 'null'
        metadata:
          $ref: '#/components/schemas/OpenResponsesRequestMetadata'
        tools:
          type: array
          items:
            $ref: '#/components/schemas/OpenResponsesRequestToolsItems'
        tool_choice:
          $ref: '#/components/schemas/OpenAIResponsesToolChoice'
        parallel_tool_calls:
          type:
            - boolean
            - 'null'
        model:
          type: string
        models:
          type: array
          items:
            type: string
        text:
          $ref: '#/components/schemas/OpenResponsesResponseText'
        reasoning:
          $ref: '#/components/schemas/OpenResponsesReasoningConfig'
        max_output_tokens:
          type:
            - number
            - 'null'
          format: double
        temperature:
          type:
            - number
            - 'null'
          format: double
        top_p:
          type:
            - number
            - 'null'
          format: double
        top_k:
          type: number
          format: double
        prompt_cache_key:
          type:
            - string
            - 'null'
        previous_response_id:
          type:
            - string
            - 'null'
        prompt:
          $ref: '#/components/schemas/OpenAIResponsesPrompt'
        include:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/OpenAIResponsesIncludable'
        background:
          type:
            - boolean
            - 'null'
        safety_identifier:
          type:
            - string
            - 'null'
        store:
          type:
            - boolean
            - 'null'
        service_tier:
          $ref: '#/components/schemas/OpenResponsesRequestServiceTier'
        truncation:
          $ref: '#/components/schemas/OpenResponsesRequestTruncation'
        stream:
          type: boolean
        provider:
          oneOf:
            - $ref: '#/components/schemas/OpenResponsesRequestProvider'
            - type: 'null'
        plugins:
          type: array
          items:
            $ref: '#/components/schemas/OpenResponsesRequestPluginsItems'
        user:
          type: string
    OpenAiResponsesNonStreamingResponseObject:
      type: string
      enum:
        - value: response
    OpenAIResponsesResponseStatus:
      type: string
      enum:
        - value: completed
        - value: incomplete
        - value: in_progress
        - value: failed
        - value: cancelled
        - value: queued
    OutputMessage:
      type: object
      properties:
        id:
          type: string
        role:
          $ref: '#/components/schemas/OutputMessageRole'
        type:
          $ref: '#/components/schemas/OutputMessageType'
        status:
          $ref: '#/components/schemas/OutputMessageStatus'
        content:
          type: array
          items:
            $ref: '#/components/schemas/OutputMessageContentItems'
      required:
        - id
        - role
        - type
        - content
    OutputItemReasoning:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OutputItemReasoningType'
        id:
          type: string
        content:
          type: array
          items:
            $ref: '#/components/schemas/ReasoningTextContent'
        summary:
          type: array
          items:
            $ref: '#/components/schemas/ReasoningSummaryText'
        encrypted_content:
          type:
            - string
            - 'null'
        status:
          $ref: '#/components/schemas/OutputItemReasoningStatus'
      required:
        - type
        - id
        - summary
    OutputItemFunctionCall:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OutputItemFunctionCallType'
        id:
          type: string
        name:
          type: string
        arguments:
          type: string
        call_id:
          type: string
        status:
          $ref: '#/components/schemas/OutputItemFunctionCallStatus'
      required:
        - type
        - name
        - arguments
        - call_id
    OutputItemWebSearchCall:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OutputItemWebSearchCallType'
        id:
          type: string
        status:
          $ref: '#/components/schemas/WebSearchStatus'
      required:
        - type
        - id
        - status
    OutputItemFileSearchCall:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OutputItemFileSearchCallType'
        id:
          type: string
        queries:
          type: array
          items:
            type: string
        status:
          $ref: '#/components/schemas/WebSearchStatus'
      required:
        - type
        - id
        - queries
        - status
    OutputItemImageGenerationCall:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OutputItemImageGenerationCallType'
        id:
          type: string
        result:
          type:
            - string
            - 'null'
        status:
          $ref: '#/components/schemas/ImageGenerationStatus'
      required:
        - type
        - id
        - result
        - status
    OpenAiResponsesNonStreamingResponseOutputItems:
      oneOf:
        - $ref: '#/components/schemas/OutputMessage'
        - $ref: '#/components/schemas/OutputItemReasoning'
        - $ref: '#/components/schemas/OutputItemFunctionCall'
        - $ref: '#/components/schemas/OutputItemWebSearchCall'
        - $ref: '#/components/schemas/OutputItemFileSearchCall'
        - $ref: '#/components/schemas/OutputItemImageGenerationCall'
    ResponsesErrorFieldCode:
      type: string
      enum:
        - value: server_error
        - value: rate_limit_exceeded
        - value: invalid_prompt
        - value: vector_store_timeout
        - value: invalid_image
        - value: invalid_image_format
        - value: invalid_base64_image
        - value: invalid_image_url
        - value: image_too_large
        - value: image_too_small
        - value: image_parse_error
        - value: image_content_policy_violation
        - value: invalid_image_mode
        - value: image_file_too_large
        - value: unsupported_image_media_type
        - value: empty_image_file
        - value: failed_to_download_image
        - value: image_file_not_found
    ResponsesErrorField:
      type: object
      properties:
        code:
          $ref: '#/components/schemas/ResponsesErrorFieldCode'
        message:
          type: string
      required:
        - code
        - message
    OpenAiResponsesIncompleteDetailsReason:
      type: string
      enum:
        - value: max_output_tokens
        - value: content_filter
    OpenAIResponsesIncompleteDetails:
      type: object
      properties:
        reason:
          $ref: '#/components/schemas/OpenAiResponsesIncompleteDetailsReason'
    OpenAiResponsesUsageInputTokensDetails:
      type: object
      properties:
        cached_tokens:
          type: number
          format: double
      required:
        - cached_tokens
    OpenAiResponsesUsageOutputTokensDetails:
      type: object
      properties:
        reasoning_tokens:
          type: number
          format: double
      required:
        - reasoning_tokens
    OpenAIResponsesUsage:
      type: object
      properties:
        input_tokens:
          type: number
          format: double
        input_tokens_details:
          $ref: '#/components/schemas/OpenAiResponsesUsageInputTokensDetails'
        output_tokens:
          type: number
          format: double
        output_tokens_details:
          $ref: '#/components/schemas/OpenAiResponsesUsageOutputTokensDetails'
        total_tokens:
          type: number
          format: double
      required:
        - input_tokens
        - input_tokens_details
        - output_tokens
        - output_tokens_details
        - total_tokens
    OpenAiResponsesInputOneOf1ItemsOneOf0Type:
      type: string
      enum:
        - value: message
    OpenAiResponsesInputOneOf1ItemsOneOf0Role0:
      type: string
      enum:
        - value: user
    OpenAiResponsesInputOneOf1ItemsOneOf0Role1:
      type: string
      enum:
        - value: system
    OpenAiResponsesInputOneOf1ItemsOneOf0Role2:
      type: string
      enum:
        - value: assistant
    OpenAiResponsesInputOneOf1ItemsOneOf0Role3:
      type: string
      enum:
        - value: developer
    OpenAiResponsesInputOneOf1ItemsOneOf0Role:
      oneOf:
        - $ref: '#/components/schemas/OpenAiResponsesInputOneOf1ItemsOneOf0Role0'
        - $ref: '#/components/schemas/OpenAiResponsesInputOneOf1ItemsOneOf0Role1'
        - $ref: '#/components/schemas/OpenAiResponsesInputOneOf1ItemsOneOf0Role2'
        - $ref: '#/components/schemas/OpenAiResponsesInputOneOf1ItemsOneOf0Role3'
    OpenAiResponsesInputOneOf1ItemsOneOf0ContentOneOf0Items:
      oneOf:
        - $ref: '#/components/schemas/ResponseInputText'
        - $ref: '#/components/schemas/ResponseInputImage'
        - $ref: '#/components/schemas/ResponseInputFile'
        - $ref: '#/components/schemas/ResponseInputAudio'
    OpenAiResponsesInputOneOf1ItemsOneOf0Content0:
      type: array
      items:
        $ref: >-
          #/components/schemas/OpenAiResponsesInputOneOf1ItemsOneOf0ContentOneOf0Items
    OpenAiResponsesInputOneOf1ItemsOneOf0Content:
      oneOf:
        - $ref: '#/components/schemas/OpenAiResponsesInputOneOf1ItemsOneOf0Content0'
        - type: string
    OpenAiResponsesInputOneOf1Items0:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OpenAiResponsesInputOneOf1ItemsOneOf0Type'
        role:
          $ref: '#/components/schemas/OpenAiResponsesInputOneOf1ItemsOneOf0Role'
        content:
          $ref: '#/components/schemas/OpenAiResponsesInputOneOf1ItemsOneOf0Content'
      required:
        - role
        - content
    OpenAiResponsesInputOneOf1ItemsOneOf1Type:
      type: string
      enum:
        - value: message
    OpenAiResponsesInputOneOf1ItemsOneOf1Role0:
      type: string
      enum:
        - value: user
    OpenAiResponsesInputOneOf1ItemsOneOf1Role1:
      type: string
      enum:
        - value: system
    OpenAiResponsesInputOneOf1ItemsOneOf1Role2:
      type: string
      enum:
        - value: developer
    OpenAiResponsesInputOneOf1ItemsOneOf1Role:
      oneOf:
        - $ref: '#/components/schemas/OpenAiResponsesInputOneOf1ItemsOneOf1Role0'
        - $ref: '#/components/schemas/OpenAiResponsesInputOneOf1ItemsOneOf1Role1'
        - $ref: '#/components/schemas/OpenAiResponsesInputOneOf1ItemsOneOf1Role2'
    OpenAiResponsesInputOneOf1ItemsOneOf1ContentItems:
      oneOf:
        - $ref: '#/components/schemas/ResponseInputText'
        - $ref: '#/components/schemas/ResponseInputImage'
        - $ref: '#/components/schemas/ResponseInputFile'
        - $ref: '#/components/schemas/ResponseInputAudio'
    OpenAiResponsesInputOneOf1Items1:
      type: object
      properties:
        id:
          type: string
        type:
          $ref: '#/components/schemas/OpenAiResponsesInputOneOf1ItemsOneOf1Type'
        role:
          $ref: '#/components/schemas/OpenAiResponsesInputOneOf1ItemsOneOf1Role'
        content:
          type: array
          items:
            $ref: >-
              #/components/schemas/OpenAiResponsesInputOneOf1ItemsOneOf1ContentItems
      required:
        - id
        - role
        - content
    OpenAiResponsesInputOneOf1ItemsOneOf2Type:
      type: string
      enum:
        - value: function_call_output
    OpenAiResponsesInputOneOf1Items2:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OpenAiResponsesInputOneOf1ItemsOneOf2Type'
        id:
          type: string
        call_id:
          type: string
        output:
          type: string
        status:
          $ref: '#/components/schemas/ToolCallStatus'
      required:
        - type
        - id
        - call_id
        - output
    OpenAiResponsesInputOneOf1ItemsOneOf3Type:
      type: string
      enum:
        - value: function_call
    OpenAiResponsesInputOneOf1Items3:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OpenAiResponsesInputOneOf1ItemsOneOf3Type'
        call_id:
          type: string
        name:
          type: string
        arguments:
          type: string
        id:
          type: string
        status:
          $ref: '#/components/schemas/ToolCallStatus'
      required:
        - type
        - call_id
        - name
        - arguments
    OpenAiResponsesInputOneOf1Items:
      oneOf:
        - $ref: '#/components/schemas/OpenAiResponsesInputOneOf1Items0'
        - $ref: '#/components/schemas/OpenAiResponsesInputOneOf1Items1'
        - $ref: '#/components/schemas/OpenAiResponsesInputOneOf1Items2'
        - $ref: '#/components/schemas/OpenAiResponsesInputOneOf1Items3'
        - $ref: '#/components/schemas/OutputItemImageGenerationCall'
        - $ref: '#/components/schemas/OutputMessage'
    OpenAiResponsesInput1:
      type: array
      items:
        $ref: '#/components/schemas/OpenAiResponsesInputOneOf1Items'
    OpenAIResponsesInput:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/OpenAiResponsesInput1'
        - description: Any type
    OpenAiResponsesNonStreamingResponseToolsItems:
      oneOf:
        - type: object
          additionalProperties:
            description: Any type
        - $ref: '#/components/schemas/OpenResponsesWebSearchPreviewTool'
        - $ref: '#/components/schemas/OpenResponsesWebSearchPreview20250311Tool'
        - $ref: '#/components/schemas/OpenResponsesWebSearchTool'
        - $ref: '#/components/schemas/OpenResponsesWebSearch20250826Tool'
    OpenAIResponsesReasoningConfig:
      type: object
      properties:
        effort:
          $ref: '#/components/schemas/OpenAIResponsesReasoningEffort'
        summary:
          $ref: '#/components/schemas/ReasoningSummaryVerbosity'
    OpenAIResponsesServiceTier:
      type: string
      enum:
        - value: auto
        - value: default
        - value: flex
        - value: priority
        - value: scale
    OpenAIResponsesTruncation:
      type: string
      enum:
        - value: auto
        - value: disabled
    ResponseTextConfig:
      type: object
      properties:
        format:
          $ref: '#/components/schemas/ResponseFormatTextConfig'
        verbosity:
          oneOf:
            - $ref: '#/components/schemas/ResponseTextConfigVerbosity'
            - type: 'null'
    ResponsesOutputItem:
      oneOf:
        - $ref: '#/components/schemas/ResponsesOutputMessage'
        - $ref: '#/components/schemas/ResponsesOutputItemReasoning'
        - $ref: '#/components/schemas/ResponsesOutputItemFunctionCall'
        - $ref: '#/components/schemas/ResponsesWebSearchCallOutput'
        - $ref: '#/components/schemas/ResponsesOutputItemFileSearchCall'
        - $ref: '#/components/schemas/ResponsesImageGenerationCall'
    OpenResponsesUsageCostDetails:
      type: object
      properties:
        upstream_inference_cost:
          type:
            - number
            - 'null'
          format: double
        upstream_inference_input_cost:
          type: number
          format: double
        upstream_inference_output_cost:
          type: number
          format: double
      required:
        - upstream_inference_input_cost
        - upstream_inference_output_cost
    OpenResponsesUsage:
      type: object
      properties:
        input_tokens:
          type: number
          format: double
        input_tokens_details:
          $ref: '#/components/schemas/OpenAiResponsesUsageInputTokensDetails'
        output_tokens:
          type: number
          format: double
        output_tokens_details:
          $ref: '#/components/schemas/OpenAiResponsesUsageOutputTokensDetails'
        total_tokens:
          type: number
          format: double
        cost:
          type:
            - number
            - 'null'
          format: double
        is_byok:
          type: boolean
        cost_details:
          $ref: '#/components/schemas/OpenResponsesUsageCostDetails'
      required:
        - input_tokens
        - input_tokens_details
        - output_tokens
        - output_tokens_details
        - total_tokens
    OpenResponsesNonStreamingResponse:
      type: object
      properties:
        id:
          type: string
        object:
          $ref: '#/components/schemas/OpenAiResponsesNonStreamingResponseObject'
        created_at:
          type: number
          format: double
        model:
          type: string
        status:
          $ref: '#/components/schemas/OpenAIResponsesResponseStatus'
        output:
          type: array
          items:
            $ref: '#/components/schemas/ResponsesOutputItem'
        user:
          type:
            - string
            - 'null'
        output_text:
          type: string
        prompt_cache_key:
          type:
            - string
            - 'null'
        safety_identifier:
          type:
            - string
            - 'null'
        error:
          $ref: '#/components/schemas/ResponsesErrorField'
        incomplete_details:
          $ref: '#/components/schemas/OpenAIResponsesIncompleteDetails'
        usage:
          $ref: '#/components/schemas/OpenResponsesUsage'
        max_tool_calls:
          type:
            - number
            - 'null'
          format: double
        top_logprobs:
          type: number
          format: double
        max_output_tokens:
          type:
            - number
            - 'null'
          format: double
        temperature:
          type:
            - number
            - 'null'
          format: double
        top_p:
          type:
            - number
            - 'null'
          format: double
        instructions:
          $ref: '#/components/schemas/OpenAIResponsesInput'
        metadata:
          $ref: '#/components/schemas/OpenResponsesRequestMetadata'
        tools:
          type: array
          items:
            $ref: '#/components/schemas/OpenAiResponsesNonStreamingResponseToolsItems'
        tool_choice:
          $ref: '#/components/schemas/OpenAIResponsesToolChoice'
        parallel_tool_calls:
          type: boolean
        prompt:
          $ref: '#/components/schemas/OpenAIResponsesPrompt'
        background:
          type:
            - boolean
            - 'null'
        previous_response_id:
          type:
            - string
            - 'null'
        reasoning:
          $ref: '#/components/schemas/OpenAIResponsesReasoningConfig'
        service_tier:
          $ref: '#/components/schemas/OpenAIResponsesServiceTier'
        store:
          type: boolean
        truncation:
          $ref: '#/components/schemas/OpenAIResponsesTruncation'
        text:
          $ref: '#/components/schemas/ResponseTextConfig'
      required:
        - id
        - object
        - created_at
        - model
        - output
        - error
        - incomplete_details
        - temperature
        - top_p
        - instructions
        - metadata
        - tools
        - tool_choice
        - parallel_tool_calls

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/responses"

payload = {
    "input": [
        {
            "type": "message",
            "role": "user",
            "content": "Hello, how are you?"
        }
    ],
    "tools": [
        {
            "type": "function",
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": { "location": { "type": "string" } }
            }
        }
    ],
    "model": "anthropic/claude-4.5-sonnet-20250929",
    "temperature": 0.7,
    "top_p": 0.9
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/responses';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"input":[{"type":"message","role":"user","content":"Hello, how are you?"}],"tools":[{"type":"function","name":"get_current_weather","description":"Get the current weather in a given location","parameters":{"type":"object","properties":{"location":{"type":"string"}}}}],"model":"anthropic/claude-4.5-sonnet-20250929","temperature":0.7,"top_p":0.9}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/responses"

	payload := strings.NewReader("{\n  \"input\": [\n    {\n      \"type\": \"message\",\n      \"role\": \"user\",\n      \"content\": \"Hello, how are you?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"name\": \"get_current_weather\",\n      \"description\": \"Get the current weather in a given location\",\n      \"parameters\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"location\": {\n            \"type\": \"string\"\n          }\n        }\n      }\n    }\n  ],\n  \"model\": \"anthropic/claude-4.5-sonnet-20250929\",\n  \"temperature\": 0.7,\n  \"top_p\": 0.9\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/responses")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"input\": [\n    {\n      \"type\": \"message\",\n      \"role\": \"user\",\n      \"content\": \"Hello, how are you?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"name\": \"get_current_weather\",\n      \"description\": \"Get the current weather in a given location\",\n      \"parameters\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"location\": {\n            \"type\": \"string\"\n          }\n        }\n      }\n    }\n  ],\n  \"model\": \"anthropic/claude-4.5-sonnet-20250929\",\n  \"temperature\": 0.7,\n  \"top_p\": 0.9\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://openrouter.ai/api/v1/responses")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"input\": [\n    {\n      \"type\": \"message\",\n      \"role\": \"user\",\n      \"content\": \"Hello, how are you?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"name\": \"get_current_weather\",\n      \"description\": \"Get the current weather in a given location\",\n      \"parameters\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"location\": {\n            \"type\": \"string\"\n          }\n        }\n      }\n    }\n  ],\n  \"model\": \"anthropic/claude-4.5-sonnet-20250929\",\n  \"temperature\": 0.7,\n  \"top_p\": 0.9\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://openrouter.ai/api/v1/responses', [
  'body' => '{
  "input": [
    {
      "type": "message",
      "role": "user",
      "content": "Hello, how are you?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string"
          }
        }
      }
    }
  ],
  "model": "anthropic/claude-4.5-sonnet-20250929",
  "temperature": 0.7,
  "top_p": 0.9
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/responses");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"input\": [\n    {\n      \"type\": \"message\",\n      \"role\": \"user\",\n      \"content\": \"Hello, how are you?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"name\": \"get_current_weather\",\n      \"description\": \"Get the current weather in a given location\",\n      \"parameters\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"location\": {\n            \"type\": \"string\"\n          }\n        }\n      }\n    }\n  ],\n  \"model\": \"anthropic/claude-4.5-sonnet-20250929\",\n  \"temperature\": 0.7,\n  \"top_p\": 0.9\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "input": [
    [
      "type": "message",
      "role": "user",
      "content": "Hello, how are you?"
    ]
  ],
  "tools": [
    [
      "type": "function",
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": [
        "type": "object",
        "properties": ["location": ["type": "string"]]
      ]
    ]
  ],
  "model": "anthropic/claude-4.5-sonnet-20250929",
  "temperature": 0.7,
  "top_p": 0.9
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/responses")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get user activity grouped by endpoint

GET https://openrouter.ai/api/v1/activity

Returns user activity data grouped by endpoint for the last 30 (completed) UTC days

Reference: https://openrouter.ai/docs/api-reference/analytics/get-user-activity

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get user activity grouped by endpoint
  version: endpoint_analytics.getUserActivity
paths:
  /activity:
    get:
      operationId: get-user-activity
      summary: Get user activity grouped by endpoint
      description: >-
        Returns user activity data grouped by endpoint for the last 30
        (completed) UTC days
      tags:
        - - subpackage_analytics
      parameters:
        - name: date
          in: query
          description: Filter by a single UTC date in the last 30 days (YYYY-MM-DD format).
          required: false
          schema:
            type: string
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns user activity data grouped by endpoint
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Analytics_getUserActivity_Response_200'
        '400':
          description: Bad Request - Invalid date format or date range
          content: {}
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '403':
          description: Forbidden - Only provisioning keys can fetch activity
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
components:
  schemas:
    ActivityItem:
      type: object
      properties:
        date:
          type: string
        model:
          type: string
        model_permaslug:
          type: string
        endpoint_id:
          type: string
        provider_name:
          type: string
        usage:
          type: number
          format: double
        byok_usage_inference:
          type: number
          format: double
        requests:
          type: number
          format: double
        prompt_tokens:
          type: number
          format: double
        completion_tokens:
          type: number
          format: double
        reasoning_tokens:
          type: number
          format: double
      required:
        - date
        - model
        - model_permaslug
        - endpoint_id
        - provider_name
        - usage
        - byok_usage_inference
        - requests
        - prompt_tokens
        - completion_tokens
        - reasoning_tokens
    Analytics_getUserActivity_Response_200:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/ActivityItem'
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/activity"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/activity';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/activity"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/activity")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/activity")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/activity', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/activity");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/activity")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get remaining credits

GET https://openrouter.ai/api/v1/credits

Get total credits purchased and used for the authenticated user

Reference: https://openrouter.ai/docs/api-reference/credits/get-credits

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get remaining credits
  version: endpoint_credits.getCredits
paths:
  /credits:
    get:
      operationId: get-credits
      summary: Get remaining credits
      description: Get total credits purchased and used for the authenticated user
      tags:
        - - subpackage_credits
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns the total credits purchased and used
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Credits_getCredits_Response_200'
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '403':
          description: Forbidden - Only provisioning keys can fetch credits
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
components:
  schemas:
    Credits_getCredits_Response_200:
      type: object
      properties: {}

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/credits"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/credits';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/credits"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/credits")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/credits")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/credits', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/credits");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/credits")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Create a Coinbase charge for crypto payment

POST https://openrouter.ai/api/v1/credits/coinbase
Content-Type: application/json

Create a Coinbase charge for crypto payment

Reference: https://openrouter.ai/docs/api-reference/credits/create-coinbase-charge

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Create a Coinbase charge for crypto payment
  version: endpoint_credits.createCoinbaseCharge
paths:
  /credits/coinbase:
    post:
      operationId: create-coinbase-charge
      summary: Create a Coinbase charge for crypto payment
      description: Create a Coinbase charge for crypto payment
      tags:
        - - subpackage_credits
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns the calldata to fulfill the transaction
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Credits_createCoinbaseCharge_Response_200'
        '400':
          description: Bad Request - Invalid credit amount or request body
          content: {}
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '429':
          description: Too Many Requests - Rate limit exceeded
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateChargeRequest'
components:
  schemas:
    CreateChargeRequestChainId:
      type: string
      enum:
        - value: '1'
        - value: '137'
        - value: '8453'
    CreateChargeRequest:
      type: object
      properties:
        amount:
          type: number
          format: double
        sender:
          type: string
        chain_id:
          $ref: '#/components/schemas/CreateChargeRequestChainId'
      required:
        - amount
        - sender
        - chain_id
    CreditsCoinbasePostResponsesContentApplicationJsonSchemaDataWeb3DataTransferIntentCallData:
      type: object
      properties:
        deadline:
          type: string
        fee_amount:
          type: string
        id:
          type: string
        operator:
          type: string
        prefix:
          type: string
        recipient:
          type: string
        recipient_amount:
          type: string
        recipient_currency:
          type: string
        refund_destination:
          type: string
        signature:
          type: string
      required:
        - deadline
        - fee_amount
        - id
        - operator
        - prefix
        - recipient
        - recipient_amount
        - recipient_currency
        - refund_destination
        - signature
    CreditsCoinbasePostResponsesContentApplicationJsonSchemaDataWeb3DataTransferIntentMetadata:
      type: object
      properties:
        chain_id:
          type: number
          format: double
        contract_address:
          type: string
        sender:
          type: string
      required:
        - chain_id
        - contract_address
        - sender
    CreditsCoinbasePostResponsesContentApplicationJsonSchemaDataWeb3DataTransferIntent:
      type: object
      properties:
        call_data:
          $ref: >-
            #/components/schemas/CreditsCoinbasePostResponsesContentApplicationJsonSchemaDataWeb3DataTransferIntentCallData
        metadata:
          $ref: >-
            #/components/schemas/CreditsCoinbasePostResponsesContentApplicationJsonSchemaDataWeb3DataTransferIntentMetadata
      required:
        - call_data
        - metadata
    CreditsCoinbasePostResponsesContentApplicationJsonSchemaDataWeb3Data:
      type: object
      properties:
        transfer_intent:
          $ref: >-
            #/components/schemas/CreditsCoinbasePostResponsesContentApplicationJsonSchemaDataWeb3DataTransferIntent
      required:
        - transfer_intent
    CreditsCoinbasePostResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        id:
          type: string
        created_at:
          type: string
        expires_at:
          type: string
        web3_data:
          $ref: >-
            #/components/schemas/CreditsCoinbasePostResponsesContentApplicationJsonSchemaDataWeb3Data
      required:
        - id
        - created_at
        - expires_at
        - web3_data
    Credits_createCoinbaseCharge_Response_200:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/CreditsCoinbasePostResponsesContentApplicationJsonSchemaData
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/credits/coinbase"

payload = {
    "amount": 100,
    "sender": "0x1234567890123456789012345678901234567890",
    "chain_id": 1
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/credits/coinbase';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"amount":100,"sender":"0x1234567890123456789012345678901234567890","chain_id":1}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/credits/coinbase"

	payload := strings.NewReader("{\n  \"amount\": 100,\n  \"sender\": \"0x1234567890123456789012345678901234567890\",\n  \"chain_id\": 1\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/credits/coinbase")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"amount\": 100,\n  \"sender\": \"0x1234567890123456789012345678901234567890\",\n  \"chain_id\": 1\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://openrouter.ai/api/v1/credits/coinbase")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"amount\": 100,\n  \"sender\": \"0x1234567890123456789012345678901234567890\",\n  \"chain_id\": 1\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://openrouter.ai/api/v1/credits/coinbase', [
  'body' => '{
  "amount": 100,
  "sender": "0x1234567890123456789012345678901234567890",
  "chain_id": 1
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/credits/coinbase");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"amount\": 100,\n  \"sender\": \"0x1234567890123456789012345678901234567890\",\n  \"chain_id\": 1\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "amount": 100,
  "sender": "0x1234567890123456789012345678901234567890",
  "chain_id": 1
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/credits/coinbase")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Submit an embedding request

POST https://openrouter.ai/api/v1/embeddings
Content-Type: application/json

Submits an embedding request to the embeddings router

Reference: https://openrouter.ai/docs/api-reference/embeddings/create-embeddings

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Submit an embedding request
  version: endpoint_embeddings.createEmbeddings
paths:
  /embeddings:
    post:
      operationId: create-embeddings
      summary: Submit an embedding request
      description: Submits an embedding request to the embeddings router
      tags:
        - - subpackage_embeddings
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Embedding response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Embeddings_createEmbeddings_Response_200'
        '400':
          description: Bad Request - Invalid request parameters or malformed input
          content: {}
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '402':
          description: Payment Required - Insufficient credits or quota to complete request
          content: {}
        '404':
          description: Not Found - Resource does not exist
          content: {}
        '429':
          description: Too Many Requests - Rate limit exceeded
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
        '502':
          description: Bad Gateway - Provider/upstream API failure
          content: {}
        '503':
          description: Service Unavailable - Service temporarily unavailable
          content: {}
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                input:
                  $ref: >-
                    #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaInput
                model:
                  type: string
                provider:
                  $ref: >-
                    #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaProvider
                encoding_format:
                  $ref: >-
                    #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaEncodingFormat
                user:
                  type: string
              required:
                - input
                - model
components:
  schemas:
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaInput:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
        - type: array
          items:
            type: number
            format: double
        - type: array
          items:
            type: array
            items:
              type: number
              format: double
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderDataCollection:
      type: string
      enum:
        - value: deny
        - value: allow
    ProviderName:
      type: string
      enum:
        - value: AnyScale
        - value: Cent-ML
        - value: HuggingFace
        - value: Hyperbolic 2
        - value: Lepton
        - value: Lynn 2
        - value: Lynn
        - value: Mancer
        - value: Modal
        - value: OctoAI
        - value: Recursal
        - value: Reflection
        - value: Replicate
        - value: SambaNova 2
        - value: SF Compute
        - value: Together 2
        - value: 01.AI
        - value: AI21
        - value: AionLabs
        - value: Alibaba
        - value: Amazon Bedrock
        - value: Anthropic
        - value: AtlasCloud
        - value: Atoma
        - value: Avian
        - value: Azure
        - value: BaseTen
        - value: Cerebras
        - value: Chutes
        - value: Cirrascale
        - value: Clarifai
        - value: Cloudflare
        - value: Cohere
        - value: CrofAI
        - value: Crusoe
        - value: DeepInfra
        - value: DeepSeek
        - value: Enfer
        - value: Featherless
        - value: Fireworks
        - value: Friendli
        - value: GMICloud
        - value: Google
        - value: Google AI Studio
        - value: Groq
        - value: Hyperbolic
        - value: Inception
        - value: InferenceNet
        - value: Infermatic
        - value: Inflection
        - value: InoCloud
        - value: Kluster
        - value: Lambda
        - value: Liquid
        - value: Mancer 2
        - value: Meta
        - value: Minimax
        - value: ModelRun
        - value: Mistral
        - value: Modular
        - value: Moonshot AI
        - value: Morph
        - value: NCompass
        - value: Nebius
        - value: NextBit
        - value: Nineteen
        - value: Novita
        - value: Nvidia
        - value: OpenAI
        - value: OpenInference
        - value: Parasail
        - value: Perplexity
        - value: Phala
        - value: Relace
        - value: SambaNova
        - value: SiliconFlow
        - value: Stealth
        - value: Switchpoint
        - value: Targon
        - value: Together
        - value: Ubicloud
        - value: Venice
        - value: WandB
        - value: xAI
        - value: Z.AI
        - value: FakeProvider
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderOrderItems:
      oneOf:
        - $ref: '#/components/schemas/ProviderName'
        - type: string
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderOnlyItems:
      oneOf:
        - $ref: '#/components/schemas/ProviderName'
        - type: string
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderIgnoreItems:
      oneOf:
        - $ref: '#/components/schemas/ProviderName'
        - type: string
    Quantization:
      type: string
      enum:
        - value: int4
        - value: int8
        - value: fp4
        - value: fp6
        - value: fp8
        - value: fp16
        - value: bf16
        - value: fp32
        - value: unknown
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderSort:
      type: string
      enum:
        - value: price
        - value: throughput
        - value: latency
    BigNumberUnion:
      oneOf:
        - type: number
          format: double
        - type: string
        - type: number
          format: double
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderMaxPrice:
      type: object
      properties:
        prompt:
          $ref: '#/components/schemas/BigNumberUnion'
        completion:
          $ref: '#/components/schemas/BigNumberUnion'
        image:
          $ref: '#/components/schemas/BigNumberUnion'
        audio:
          $ref: '#/components/schemas/BigNumberUnion'
        request:
          $ref: '#/components/schemas/BigNumberUnion'
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaProvider:
      type: object
      properties:
        allow_fallbacks:
          type:
            - boolean
            - 'null'
        require_parameters:
          type:
            - boolean
            - 'null'
        data_collection:
          oneOf:
            - $ref: >-
                #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderDataCollection
            - type: 'null'
        zdr:
          type:
            - boolean
            - 'null'
        enforce_distillable_text:
          type:
            - boolean
            - 'null'
        order:
          type:
            - array
            - 'null'
          items:
            $ref: >-
              #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderOrderItems
        only:
          type:
            - array
            - 'null'
          items:
            $ref: >-
              #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderOnlyItems
        ignore:
          type:
            - array
            - 'null'
          items:
            $ref: >-
              #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderIgnoreItems
        quantizations:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/Quantization'
        sort:
          oneOf:
            - $ref: >-
                #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderSort
            - type: 'null'
        max_price:
          $ref: >-
            #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaProviderMaxPrice
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaEncodingFormat0:
      type: string
      enum:
        - value: float
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaEncodingFormat1:
      type: string
      enum:
        - value: base64
    EmbeddingsPostRequestBodyContentApplicationJsonSchemaEncodingFormat:
      oneOf:
        - $ref: >-
            #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaEncodingFormat0
        - $ref: >-
            #/components/schemas/EmbeddingsPostRequestBodyContentApplicationJsonSchemaEncodingFormat1
    EmbeddingsPostResponsesContentApplicationJsonSchemaObject:
      type: string
      enum:
        - value: list
    EmbeddingsPostResponsesContentApplicationJsonSchemaDataItemsObject:
      type: string
      enum:
        - value: embedding
    EmbeddingsPostResponsesContentApplicationJsonSchemaDataItemsEmbedding:
      oneOf:
        - type: array
          items:
            type: number
            format: double
        - type: string
    EmbeddingsPostResponsesContentApplicationJsonSchemaDataItems:
      type: object
      properties:
        object:
          $ref: >-
            #/components/schemas/EmbeddingsPostResponsesContentApplicationJsonSchemaDataItemsObject
        embedding:
          $ref: >-
            #/components/schemas/EmbeddingsPostResponsesContentApplicationJsonSchemaDataItemsEmbedding
        index:
          type: number
          format: double
      required:
        - object
        - embedding
    EmbeddingsPostResponsesContentApplicationJsonSchemaUsage:
      type: object
      properties:
        prompt_tokens:
          type: number
          format: double
        total_tokens:
          type: number
          format: double
        cost:
          type: number
          format: double
      required:
        - prompt_tokens
        - total_tokens
    Embeddings_createEmbeddings_Response_200:
      type: object
      properties:
        id:
          type: string
        object:
          $ref: >-
            #/components/schemas/EmbeddingsPostResponsesContentApplicationJsonSchemaObject
        data:
          type: array
          items:
            $ref: >-
              #/components/schemas/EmbeddingsPostResponsesContentApplicationJsonSchemaDataItems
        model:
          type: string
        usage:
          $ref: >-
            #/components/schemas/EmbeddingsPostResponsesContentApplicationJsonSchemaUsage
      required:
        - object
        - data
        - model

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/embeddings"

payload = {
    "input": "string",
    "model": "string"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/embeddings';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"input":"string","model":"string"}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/embeddings"

	payload := strings.NewReader("{\n  \"input\": \"string\",\n  \"model\": \"string\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/embeddings")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"input\": \"string\",\n  \"model\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.post("https://openrouter.ai/api/v1/embeddings")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"input\": \"string\",\n  \"model\": \"string\"\n}")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://openrouter.ai/api/v1/embeddings', [
  'body' => '{
  "input": "string",
  "model": "string"
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/embeddings");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"input\": \"string\",\n  \"model\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "input": "string",
  "model": "string"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/embeddings")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get request & usage metadata for a generation

GET https://openrouter.ai/api/v1/generation

Reference: https://openrouter.ai/docs/api-reference/generations/get-generation

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get request & usage metadata for a generation
  version: endpoint_generations.getGeneration
paths:
  /generation:
    get:
      operationId: get-generation
      summary: Get request & usage metadata for a generation
      tags:
        - - subpackage_generations
      parameters:
        - name: id
          in: query
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns the request metadata for this generation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Generations_getGeneration_Response_200'
        '401':
          description: Unauthorized - Authentication required or invalid credentials
          content: {}
        '402':
          description: Payment Required - Insufficient credits or quota to complete request
          content: {}
        '404':
          description: Not Found - Generation not found
          content: {}
        '429':
          description: Too Many Requests - Rate limit exceeded
          content: {}
        '500':
          description: Internal Server Error - Unexpected server error
          content: {}
        '502':
          description: Bad Gateway - Provider/upstream API failure
          content: {}
components:
  schemas:
    GenerationGetResponsesContentApplicationJsonSchemaDataApiType:
      type: string
      enum:
        - value: completions
        - value: embeddings
    GenerationGetResponsesContentApplicationJsonSchemaData:
      type: object
      properties:
        id:
          type: string
        upstream_id:
          type:
            - string
            - 'null'
        total_cost:
          type: number
          format: double
        cache_discount:
          type:
            - number
            - 'null'
          format: double
        upstream_inference_cost:
          type:
            - number
            - 'null'
          format: double
        created_at:
          type: string
        model:
          type: string
        app_id:
          type:
            - number
            - 'null'
          format: double
        streamed:
          type:
            - boolean
            - 'null'
        cancelled:
          type:
            - boolean
            - 'null'
        provider_name:
          type:
            - string
            - 'null'
        latency:
          type:
            - number
            - 'null'
          format: double
        moderation_latency:
          type:
            - number
            - 'null'
          format: double
        generation_time:
          type:
            - number
            - 'null'
          format: double
        finish_reason:
          type:
            - string
            - 'null'
        tokens_prompt:
          type:
            - number
            - 'null'
          format: double
        tokens_completion:
          type:
            - number
            - 'null'
          format: double
        native_tokens_prompt:
          type:
            - number
            - 'null'
          format: double
        native_tokens_completion:
          type:
            - number
            - 'null'
          format: double
        native_tokens_completion_images:
          type:
            - number
            - 'null'
          format: double
        native_tokens_reasoning:
          type:
            - number
            - 'null'
          format: double
        native_tokens_cached:
          type:
            - number
            - 'null'
          format: double
        num_media_prompt:
          type:
            - number
            - 'null'
          format: double
        num_input_audio_prompt:
          type:
            - number
            - 'null'
          format: double
        num_media_completion:
          type:
            - number
            - 'null'
          format: double
        num_search_results:
          type:
            - number
            - 'null'
          format: double
        origin:
          type: string
        usage:
          type: number
          format: double
        is_byok:
          type: boolean
        native_finish_reason:
          type:
            - string
            - 'null'
        external_user:
          type:
            - string
            - 'null'
        api_type:
          oneOf:
            - $ref: >-
                #/components/schemas/GenerationGetResponsesContentApplicationJsonSchemaDataApiType
            - type: 'null'
      required:
        - id
        - upstream_id
        - total_cost
        - cache_discount
        - upstream_inference_cost
        - created_at
        - model
        - app_id
        - streamed
        - cancelled
        - provider_name
        - latency
        - moderation_latency
        - generation_time
        - finish_reason
        - tokens_prompt
        - tokens_completion
        - native_tokens_prompt
        - native_tokens_completion
        - native_tokens_completion_images
        - native_tokens_reasoning
        - native_tokens_cached
        - num_media_prompt
        - num_input_audio_prompt
        - num_media_completion
        - num_search_results
        - origin
        - usage
        - is_byok
        - native_finish_reason
        - external_user
        - api_type
    Generations_getGeneration_Response_200:
      type: object
      properties:
        data:
          $ref: >-
            #/components/schemas/GenerationGetResponsesContentApplicationJsonSchemaData
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/generation"

querystring = {"id":"id"}

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/generation?id=id';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/generation?id=id"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/generation?id=id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/generation?id=id")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/generation?id=id', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/generation?id=id");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/generation?id=id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

# Get total count of available models

GET https://openrouter.ai/api/v1/models/count

Reference: https://openrouter.ai/docs/api-reference/models/list-models-count

## OpenAPI Specification

```yaml
openapi: 3.1.1
info:
  title: Get total count of available models
  version: endpoint_models.listModelsCount
paths:
  /models/count:
    get:
      operationId: list-models-count
      summary: Get total count of available models
      tags:
        - - subpackage_models
      parameters:
        - name: Authorization
          in: header
          description: API key as bearer token in Authorization header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Returns the total count of available models
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ModelsCountResponse'
        '500':
          description: Internal Server Error
          content: {}
components:
  schemas:
    ModelsCountResponseData:
      type: object
      properties:
        count:
          type: number
          format: double
      required:
        - count
    ModelsCountResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/ModelsCountResponseData'
      required:
        - data

```

## SDK Code Examples

```python
import requests

url = "https://openrouter.ai/api/v1/models/count"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://openrouter.ai/api/v1/models/count';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://openrouter.ai/api/v1/models/count"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://openrouter.ai/api/v1/models/count")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
HttpResponse<String> response = Unirest.get("https://openrouter.ai/api/v1/models/count")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://openrouter.ai/api/v1/models/count', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
var client = new RestClient("https://openrouter.ai/api/v1/models/count");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://openrouter.ai/api/v1/models/count")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```


---

**Navigation:** [← Previous](./02-image-generation.md) | [Index](./index.md) | [Next →](./04-list-all-models-and-their-properties.md)
