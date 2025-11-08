**Navigation:** [← Previous](./11-prefill-claudes-response-for-greater-output-contro.md) | [Index](./index.md) | [Next →](./13-using-the-evaluation-tool.md)

---

# Streaming Messages
Source: https://docs.claude.com/en/docs/build-with-claude/streaming



When creating a Message, you can set `"stream": true` to incrementally stream the response using [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent%5Fevents/Using%5Fserver-sent%5Fevents) (SSE).

## Streaming with SDKs

Our [Python](https://github.com/anthropics/anthropic-sdk-python) and [TypeScript](https://github.com/anthropics/anthropic-sdk-typescript) SDKs offer multiple ways of streaming. The Python SDK allows both sync and async streams. See the documentation in each SDK for details.

<CodeGroup>
  ```Python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  with client.messages.stream(
      max_tokens=1024,
      messages=[{"role": "user", "content": "Hello"}],
      model="claude-sonnet-4-5",
  ) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
  ```

  ```TypeScript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const client = new Anthropic();

  await client.messages.stream({
      messages: [{role: 'user', content: "Hello"}],
      model: 'claude-sonnet-4-5',
      max_tokens: 1024,
  }).on('text', (text) => {
      console.log(text);
  });
  ```
</CodeGroup>

## Event types

Each server-sent event includes a named event type and associated JSON data. Each event will use an SSE event name (e.g. `event: message_stop`), and include the matching event `type` in its data.

Each stream uses the following event flow:

1. `message_start`: contains a `Message` object with empty `content`.
2. A series of content blocks, each of which have a `content_block_start`, one or more `content_block_delta` events, and a `content_block_stop` event. Each content block will have an `index` that corresponds to its index in the final Message `content` array.
3. One or more `message_delta` events, indicating top-level changes to the final `Message` object.
4. A final `message_stop` event.

<Warning>
  The token counts shown in the `usage` field of the `message_delta` event are *cumulative*.
</Warning>

### Ping events

Event streams may also include any number of `ping` events.

### Error events

We may occasionally send [errors](/en/api/errors) in the event stream. For example, during periods of high usage, you may receive an `overloaded_error`, which would normally correspond to an HTTP 529 in a non-streaming context:

```json Example error theme={null}
event: error
data: {"type": "error", "error": {"type": "overloaded_error", "message": "Overloaded"}}
```

### Other events

In accordance with our [versioning policy](/en/api/versioning), we may add new event types, and your code should handle unknown event types gracefully.

## Content block delta types

Each `content_block_delta` event contains a `delta` of a type that updates the `content` block at a given `index`.

### Text delta

A `text` content block delta looks like:

```JSON Text delta theme={null}
event: content_block_delta
data: {"type": "content_block_delta","index": 0,"delta": {"type": "text_delta", "text": "ello frien"}}
```

### Input JSON delta

The deltas for `tool_use` content blocks correspond to updates for the `input` field of the block. To support maximum granularity, the deltas are *partial JSON strings*, whereas the final `tool_use.input` is always an *object*.

You can accumulate the string deltas and parse the JSON once you receive a `content_block_stop` event, by using a library like [Pydantic](https://docs.pydantic.dev/latest/concepts/json/#partial-json-parsing) to do partial JSON parsing, or by using our [SDKs](/en/api/client-sdks), which provide helpers to access parsed incremental values.

A `tool_use` content block delta looks like:

```JSON Input JSON delta theme={null}
event: content_block_delta
data: {"type": "content_block_delta","index": 1,"delta": {"type": "input_json_delta","partial_json": "{\"location\": \"San Fra"}}}
```

Note: Our current models only support emitting one complete key and value property from `input` at a time. As such, when using tools, there may be delays between streaming events while the model is working. Once an `input` key and value are accumulated, we emit them as multiple `content_block_delta` events with chunked partial json so that the format can automatically support finer granularity in future models.

### Thinking delta

When using [extended thinking](/en/docs/build-with-claude/extended-thinking#streaming-thinking) with streaming enabled, you'll receive thinking content via `thinking_delta` events. These deltas correspond to the `thinking` field of the `thinking` content blocks.

For thinking content, a special `signature_delta` event is sent just before the `content_block_stop` event. This signature is used to verify the integrity of the thinking block.

A typical thinking delta looks like:

```JSON Thinking delta theme={null}
event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "thinking_delta", "thinking": "Let me solve this step by step:\n\n1. First break down 27 * 453"}}
```

The signature delta looks like:

```JSON Signature delta theme={null}
event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "signature_delta", "signature": "EqQBCgIYAhIM1gbcDa9GJwZA2b3hGgxBdjrkzLoky3dl1pkiMOYds..."}}
```

## Full HTTP Stream response

We strongly recommend that you use our [client SDKs](/en/api/client-sdks) when using streaming mode. However, if you are building a direct API integration, you will need to handle these events yourself.

A stream response is comprised of:

1. A `message_start` event
2. Potentially multiple content blocks, each of which contains:
   * A `content_block_start` event
   * Potentially multiple `content_block_delta` events
   * A `content_block_stop` event
3. A `message_delta` event
4. A `message_stop` event

There may be `ping` events dispersed throughout the response as well. See [Event types](#event-types) for more details on the format.

### Basic streaming request

<CodeGroup>
  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages \
       --header "anthropic-version: 2023-06-01" \
       --header "content-type: application/json" \
       --header "x-api-key: $ANTHROPIC_API_KEY" \
       --data \
  '{
    "model": "claude-sonnet-4-5",
    "messages": [{"role": "user", "content": "Hello"}],
    "max_tokens": 256,
    "stream": true
  }'
  ```

  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  with client.messages.stream(
      model="claude-sonnet-4-5",
      messages=[{"role": "user", "content": "Hello"}],
      max_tokens=256,
  ) as stream:
      for text in stream.text_stream:
          print(text, end="", flush=True)
  ```
</CodeGroup>

```json Response theme={null}
event: message_start
data: {"type": "message_start", "message": {"id": "msg_1nZdL29xx5MUA1yADyHTEsnR8uuvGzszyY", "type": "message", "role": "assistant", "content": [], "model": "claude-sonnet-4-5-20250929", "stop_reason": null, "stop_sequence": null, "usage": {"input_tokens": 25, "output_tokens": 1}}}

event: content_block_start
data: {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}}

event: ping
data: {"type": "ping"}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "Hello"}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "!"}}

event: content_block_stop
data: {"type": "content_block_stop", "index": 0}

event: message_delta
data: {"type": "message_delta", "delta": {"stop_reason": "end_turn", "stop_sequence":null}, "usage": {"output_tokens": 15}}

event: message_stop
data: {"type": "message_stop"}

```

### Streaming request with tool use

<Tip>
  Tool use now supports fine-grained streaming for parameter values as a beta feature. For more details, see [Fine-grained tool streaming](/en/docs/agents-and-tools/tool-use/fine-grained-tool-streaming).
</Tip>

In this request, we ask Claude to use a tool to tell us the weather.

<CodeGroup>
  ```bash Shell theme={null}
    curl https://api.anthropic.com/v1/messages \
      -H "content-type: application/json" \
      -H "x-api-key: $ANTHROPIC_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -d '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 1024,
        "tools": [
          {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "input_schema": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
                }
              },
              "required": ["location"]
            }
          }
        ],
        "tool_choice": {"type": "any"},
        "messages": [
          {
            "role": "user",
            "content": "What is the weather like in San Francisco?"
          }
        ],
        "stream": true
      }'
  ```

  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  tools = [
      {
          "name": "get_weather",
          "description": "Get the current weather in a given location",
          "input_schema": {
              "type": "object",
              "properties": {
                  "location": {
                      "type": "string",
                      "description": "The city and state, e.g. San Francisco, CA"
                  }
              },
              "required": ["location"]
          }
      }
  ]

  with client.messages.stream(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      tools=tools,
      tool_choice={"type": "any"},
      messages=[
          {
              "role": "user",
              "content": "What is the weather like in San Francisco?"
          }
      ],
  ) as stream:
      for text in stream.text_stream:
          print(text, end="", flush=True)
  ```
</CodeGroup>

```json Response theme={null}
event: message_start
data: {"type":"message_start","message":{"id":"msg_014p7gG3wDgGV9EUtLvnow3U","type":"message","role":"assistant","model":"claude-sonnet-4-5-20250929","stop_sequence":null,"usage":{"input_tokens":472,"output_tokens":2},"content":[],"stop_reason":null}}

event: content_block_start
data: {"type":"content_block_start","index":0,"content_block":{"type":"text","text":""}}

event: ping
data: {"type": "ping"}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":"Okay"}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":","}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":" let"}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":"'s"}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":" check"}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":" the"}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":" weather"}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":" for"}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":" San"}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":" Francisco"}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":","}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":" CA"}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":":"}}

event: content_block_stop
data: {"type":"content_block_stop","index":0}

event: content_block_start
data: {"type":"content_block_start","index":1,"content_block":{"type":"tool_use","id":"toolu_01T1x1fJ34qAmk2tNTrN7Up6","name":"get_weather","input":{}}}

event: content_block_delta
data: {"type":"content_block_delta","index":1,"delta":{"type":"input_json_delta","partial_json":""}}

event: content_block_delta
data: {"type":"content_block_delta","index":1,"delta":{"type":"input_json_delta","partial_json":"{\"location\":"}}

event: content_block_delta
data: {"type":"content_block_delta","index":1,"delta":{"type":"input_json_delta","partial_json":" \"San"}}

event: content_block_delta
data: {"type":"content_block_delta","index":1,"delta":{"type":"input_json_delta","partial_json":" Francisc"}}

event: content_block_delta
data: {"type":"content_block_delta","index":1,"delta":{"type":"input_json_delta","partial_json":"o,"}}

event: content_block_delta
data: {"type":"content_block_delta","index":1,"delta":{"type":"input_json_delta","partial_json":" CA\""}}

event: content_block_delta
data: {"type":"content_block_delta","index":1,"delta":{"type":"input_json_delta","partial_json":", "}}

event: content_block_delta
data: {"type":"content_block_delta","index":1,"delta":{"type":"input_json_delta","partial_json":"\"unit\": \"fah"}}

event: content_block_delta
data: {"type":"content_block_delta","index":1,"delta":{"type":"input_json_delta","partial_json":"renheit\"}"}}

event: content_block_stop
data: {"type":"content_block_stop","index":1}

event: message_delta
data: {"type":"message_delta","delta":{"stop_reason":"tool_use","stop_sequence":null},"usage":{"output_tokens":89}}

event: message_stop
data: {"type":"message_stop"}
```

### Streaming request with extended thinking

In this request, we enable extended thinking with streaming to see Claude's step-by-step reasoning.

<CodeGroup>
  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages \
       --header "x-api-key: $ANTHROPIC_API_KEY" \
       --header "anthropic-version: 2023-06-01" \
       --header "content-type: application/json" \
       --data \
  '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 20000,
      "stream": true,
      "thinking": {
          "type": "enabled",
          "budget_tokens": 16000
      },
      "messages": [
          {
              "role": "user",
              "content": "What is 27 * 453?"
          }
      ]
  }'
  ```

  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  with client.messages.stream(
      model="claude-sonnet-4-5",
      max_tokens=20000,
      thinking={
          "type": "enabled",
          "budget_tokens": 16000
      },
      messages=[
          {
              "role": "user",
              "content": "What is 27 * 453?"
          }
      ],
  ) as stream:
      for event in stream:
          if event.type == "content_block_delta":
              if event.delta.type == "thinking_delta":
                  print(event.delta.thinking, end="", flush=True)
              elif event.delta.type == "text_delta":
                  print(event.delta.text, end="", flush=True)
  ```
</CodeGroup>

```json Response theme={null}
event: message_start
data: {"type": "message_start", "message": {"id": "msg_01...", "type": "message", "role": "assistant", "content": [], "model": "claude-sonnet-4-5-20250929", "stop_reason": null, "stop_sequence": null}}

event: content_block_start
data: {"type": "content_block_start", "index": 0, "content_block": {"type": "thinking", "thinking": ""}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "thinking_delta", "thinking": "Let me solve this step by step:\n\n1. First break down 27 * 453"}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "thinking_delta", "thinking": "\n2. 453 = 400 + 50 + 3"}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "thinking_delta", "thinking": "\n3. 27 * 400 = 10,800"}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "thinking_delta", "thinking": "\n4. 27 * 50 = 1,350"}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "thinking_delta", "thinking": "\n5. 27 * 3 = 81"}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "thinking_delta", "thinking": "\n6. 10,800 + 1,350 + 81 = 12,231"}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "signature_delta", "signature": "EqQBCgIYAhIM1gbcDa9GJwZA2b3hGgxBdjrkzLoky3dl1pkiMOYds..."}}

event: content_block_stop
data: {"type": "content_block_stop", "index": 0}

event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "text", "text": ""}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "text_delta", "text": "27 * 453 = 12,231"}}

event: content_block_stop
data: {"type": "content_block_stop", "index": 1}

event: message_delta
data: {"type": "message_delta", "delta": {"stop_reason": "end_turn", "stop_sequence": null}}

event: message_stop
data: {"type": "message_stop"}
```

### Streaming request with web search tool use

In this request, we ask Claude to search the web for current weather information.

<CodeGroup>
  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages \
       --header "x-api-key: $ANTHROPIC_API_KEY" \
       --header "anthropic-version: 2023-06-01" \
       --header "content-type: application/json" \
       --data \
  '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "stream": true,
      "tools": [
          {
              "type": "web_search_20250305",
              "name": "web_search",
              "max_uses": 5
          }
      ],
      "messages": [
          {
              "role": "user",
              "content": "What is the weather like in New York City today?"
          }
      ]
  }'
  ```

  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  with client.messages.stream(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      tools=[
          {
              "type": "web_search_20250305",
              "name": "web_search",
              "max_uses": 5
          }
      ],
      messages=[
          {
              "role": "user",
              "content": "What is the weather like in New York City today?"
          }
      ],
  ) as stream:
      for text in stream.text_stream:
          print(text, end="", flush=True)
  ```
</CodeGroup>

```json Response theme={null}
event: message_start
data: {"type":"message_start","message":{"id":"msg_01G...","type":"message","role":"assistant","model":"claude-sonnet-4-5-20250929","content":[],"stop_reason":null,"stop_sequence":null,"usage":{"input_tokens":2679,"cache_creation_input_tokens":0,"cache_read_input_tokens":0,"output_tokens":3}}}

event: content_block_start
data: {"type":"content_block_start","index":0,"content_block":{"type":"text","text":""}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":"I'll check"}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":" the current weather in New York City for you"}}

event: ping
data: {"type": "ping"}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":"."}}

event: content_block_stop
data: {"type":"content_block_stop","index":0}

event: content_block_start
data: {"type":"content_block_start","index":1,"content_block":{"type":"server_tool_use","id":"srvtoolu_014hJH82Qum7Td6UV8gDXThB","name":"web_search","input":{}}}

event: content_block_delta
data: {"type":"content_block_delta","index":1,"delta":{"type":"input_json_delta","partial_json":""}}

event: content_block_delta
data: {"type":"content_block_delta","index":1,"delta":{"type":"input_json_delta","partial_json":"{\"query"}}

event: content_block_delta
data: {"type":"content_block_delta","index":1,"delta":{"type":"input_json_delta","partial_json":"\":"}}

event: content_block_delta
data: {"type":"content_block_delta","index":1,"delta":{"type":"input_json_delta","partial_json":" \"weather"}}

event: content_block_delta
data: {"type":"content_block_delta","index":1,"delta":{"type":"input_json_delta","partial_json":" NY"}}

event: content_block_delta
data: {"type":"content_block_delta","index":1,"delta":{"type":"input_json_delta","partial_json":"C to"}}

event: content_block_delta
data: {"type":"content_block_delta","index":1,"delta":{"type":"input_json_delta","partial_json":"day\"}"}}

event: content_block_stop
data: {"type":"content_block_stop","index":1 }

event: content_block_start
data: {"type":"content_block_start","index":2,"content_block":{"type":"web_search_tool_result","tool_use_id":"srvtoolu_014hJH82Qum7Td6UV8gDXThB","content":[{"type":"web_search_result","title":"Weather in New York City in May 2025 (New York) - detailed Weather Forecast for a month","url":"https://world-weather.info/forecast/usa/new_york/may-2025/","encrypted_content":"Ev0DCioIAxgCIiQ3NmU4ZmI4OC1k...","page_age":null},...]}}

event: content_block_stop
data: {"type":"content_block_stop","index":2}

event: content_block_start
data: {"type":"content_block_start","index":3,"content_block":{"type":"text","text":""}}

event: content_block_delta
data: {"type":"content_block_delta","index":3,"delta":{"type":"text_delta","text":"Here's the current weather information for New York"}}

event: content_block_delta
data: {"type":"content_block_delta","index":3,"delta":{"type":"text_delta","text":" City:\n\n# Weather"}}

event: content_block_delta
data: {"type":"content_block_delta","index":3,"delta":{"type":"text_delta","text":" in New York City"}}

event: content_block_delta
data: {"type":"content_block_delta","index":3,"delta":{"type":"text_delta","text":"\n\n"}}

...

event: content_block_stop
data: {"type":"content_block_stop","index":17}

event: message_delta
data: {"type":"message_delta","delta":{"stop_reason":"end_turn","stop_sequence":null},"usage":{"input_tokens":10682,"cache_creation_input_tokens":0,"cache_read_input_tokens":0,"output_tokens":510,"server_tool_use":{"web_search_requests":1}}}

event: message_stop
data: {"type":"message_stop"}
```

## Error recovery

When a streaming request is interrupted due to network issues, timeouts, or other errors, you can recover by resuming from where the stream was interrupted. This approach saves you from re-processing the entire response.

The basic recovery strategy involves:

1. **Capture the partial response**: Save all content that was successfully received before the error occurred
2. **Construct a continuation request**: Create a new API request that includes the partial assistant response as the beginning of a new assistant message
3. **Resume streaming**: Continue receiving the rest of the response from where it was interrupted

### Error recovery best practices

1. **Use SDK features**: Leverage the SDK's built-in message accumulation and error handling capabilities
2. **Handle content types**: Be aware that messages can contain multiple content blocks (`text`, `tool_use`, `thinking`). Tool use and extended thinking blocks cannot be partially recovered. You can resume streaming from the most recent text block.


# Token counting
Source: https://docs.claude.com/en/docs/build-with-claude/token-counting



Token counting enables you to determine the number of tokens in a message before sending it to Claude, helping you make informed decisions about your prompts and usage. With token counting, you can

* Proactively manage rate limits and costs
* Make smart model routing decisions
* Optimize prompts to be a specific length

***

## How to count message tokens

The [token counting](/en/api/messages-count-tokens) endpoint accepts the same structured list of inputs for creating a message, including support for system prompts, [tools](/en/docs/agents-and-tools/tool-use/overview), [images](/en/docs/build-with-claude/vision), and [PDFs](/en/docs/build-with-claude/pdf-support). The response contains the total number of input tokens.

<Note>
  The token count should be considered an **estimate**. In some cases, the actual number of input tokens used when creating a message may differ by a small amount.

  Token counts may include tokens added automatically by Anthropic for system optimizations. **You are not billed for system-added tokens**. Billing reflects only your content.
</Note>

### Supported models

All [active models](/en/docs/about-claude/models/overview) support token counting.

### Count tokens in basic messages

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  response = client.messages.count_tokens(
      model="claude-sonnet-4-5",
      system="You are a scientist",
      messages=[{
          "role": "user",
          "content": "Hello, Claude"
      }],
  )

  print(response.json())
  ```

  ```typescript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const client = new Anthropic();

  const response = await client.messages.countTokens({
    model: 'claude-sonnet-4-5',
    system: 'You are a scientist',
    messages: [{
      role: 'user',
      content: 'Hello, Claude'
    }]
  });

  console.log(response);
  ```

  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages/count_tokens \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "content-type: application/json" \
      --header "anthropic-version: 2023-06-01" \
      --data '{
        "model": "claude-sonnet-4-5",
        "system": "You are a scientist",
        "messages": [{
          "role": "user",
          "content": "Hello, Claude"
        }]
      }'
  ```

  ```java Java theme={null}
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.MessageCountTokensParams;
  import com.anthropic.models.messages.MessageTokensCount;
  import com.anthropic.models.messages.Model;

  public class CountTokensExample {

      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          MessageCountTokensParams params = MessageCountTokensParams.builder()
                  .model(Model.CLAUDE_SONNET_4_20250514)
                  .system("You are a scientist")
                  .addUserMessage("Hello, Claude")
                  .build();

          MessageTokensCount count = client.messages().countTokens(params);
          System.out.println(count);
      }
  }
  ```
</CodeGroup>

```JSON JSON theme={null}
{ "input_tokens": 14 }
```

### Count tokens in messages with tools

<Note>
  [Server tool](/en/docs/agents-and-tools/tool-use/overview#server-tools) token counts only apply to the first sampling call.
</Note>

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  response = client.messages.count_tokens(
      model="claude-sonnet-4-5",
      tools=[
          {
              "name": "get_weather",
              "description": "Get the current weather in a given location",
              "input_schema": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "The city and state, e.g. San Francisco, CA",
                      }
                  },
                  "required": ["location"],
              },
          }
      ],
      messages=[{"role": "user", "content": "What's the weather like in San Francisco?"}]
  )

  print(response.json())
  ```

  ```typescript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const client = new Anthropic();

  const response = await client.messages.countTokens({
    model: 'claude-sonnet-4-5',
    tools: [
      {
        name: "get_weather",
        description: "Get the current weather in a given location",
        input_schema: {
          type: "object",
          properties: {
            location: {
              type: "string",
              description: "The city and state, e.g. San Francisco, CA",
            }
          },
          required: ["location"],
        }
      }
    ],
    messages: [{ role: "user", content: "What's the weather like in San Francisco?" }]
  });

  console.log(response);
  ```

  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages/count_tokens \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "content-type: application/json" \
      --header "anthropic-version: 2023-06-01" \
      --data '{
        "model": "claude-sonnet-4-5",
        "tools": [
          {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "input_schema": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
                }
              },
              "required": ["location"]
            }
          }
        ],
        "messages": [
          {
            "role": "user",
            "content": "What'\''s the weather like in San Francisco?"
          }
        ]
      }'
  ```

  ```java Java theme={null}
  import java.util.List;
  import java.util.Map;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.core.JsonValue;
  import com.anthropic.models.messages.MessageCountTokensParams;
  import com.anthropic.models.messages.MessageTokensCount;
  import com.anthropic.models.messages.Model;
  import com.anthropic.models.messages.Tool;
  import com.anthropic.models.messages.Tool.InputSchema;

  public class CountTokensWithToolsExample {

      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          InputSchema schema = InputSchema.builder()
                  .properties(JsonValue.from(Map.of(
                          "location", Map.of(
                                  "type", "string",
                                  "description", "The city and state, e.g. San Francisco, CA"
                          )
                  )))
                  .putAdditionalProperty("required", JsonValue.from(List.of("location")))
                  .build();

          MessageCountTokensParams params = MessageCountTokensParams.builder()
                  .model(Model.CLAUDE_SONNET_4_20250514)
                  .addTool(Tool.builder()
                          .name("get_weather")
                          .description("Get the current weather in a given location")
                          .inputSchema(schema)
                          .build())
                  .addUserMessage("What's the weather like in San Francisco?")
                  .build();

          MessageTokensCount count = client.messages().countTokens(params);
          System.out.println(count);
      }
  }
  ```
</CodeGroup>

```JSON JSON theme={null}
{ "input_tokens": 403 }
```

### Count tokens in messages with images

<CodeGroup>
  ```bash Shell theme={null}
  #!/bin/sh

  IMAGE_URL="https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
  IMAGE_MEDIA_TYPE="image/jpeg"
  IMAGE_BASE64=$(curl "$IMAGE_URL" | base64)

  curl https://api.anthropic.com/v1/messages/count_tokens \
       --header "x-api-key: $ANTHROPIC_API_KEY" \
       --header "anthropic-version: 2023-06-01" \
       --header "content-type: application/json" \
       --data \
  '{
      "model": "claude-sonnet-4-5",
      "messages": [
          {"role": "user", "content": [
              {"type": "image", "source": {
                  "type": "base64",
                  "media_type": "'$IMAGE_MEDIA_TYPE'",
                  "data": "'$IMAGE_BASE64'"
              }},
              {"type": "text", "text": "Describe this image"}
          ]}
      ]
  }'
  ```

  ```Python Python theme={null}
  import anthropic
  import base64
  import httpx

  image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
  image_media_type = "image/jpeg"
  image_data = base64.standard_b64encode(httpx.get(image_url).content).decode("utf-8")

  client = anthropic.Anthropic()

  response = client.messages.count_tokens(
      model="claude-sonnet-4-5",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "image",
                      "source": {
                          "type": "base64",
                          "media_type": image_media_type,
                          "data": image_data,
                      },
                  },
                  {
                      "type": "text",
                      "text": "Describe this image"
                  }
              ],
          }
      ],
  )
  print(response.json())
  ```

  ```Typescript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
  const image_media_type = "image/jpeg"
  const image_array_buffer = await ((await fetch(image_url)).arrayBuffer());
  const image_data = Buffer.from(image_array_buffer).toString('base64');

  const response = await anthropic.messages.countTokens({
    model: 'claude-sonnet-4-5',
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "image",
            "source": {
              "type": "base64",
              "media_type": image_media_type,
              "data": image_data,
            },
          }
        ],
      },
      {
        "type": "text",
        "text": "Describe this image"
      }
    ]
  });
  console.log(response);
  ```

  ```java Java theme={null}
  import java.util.Base64;
  import java.util.List;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.Base64ImageSource;
  import com.anthropic.models.messages.ContentBlockParam;
  import com.anthropic.models.messages.ImageBlockParam;
  import com.anthropic.models.messages.MessageCountTokensParams;
  import com.anthropic.models.messages.MessageTokensCount;
  import com.anthropic.models.messages.Model;
  import com.anthropic.models.messages.TextBlockParam;

  import java.net.URI;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;

  public class CountTokensImageExample {

      public static void main(String[] args) throws Exception {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          String imageUrl = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg";
          String imageMediaType = "image/jpeg";

          HttpClient httpClient = HttpClient.newHttpClient();
          HttpRequest request = HttpRequest.newBuilder()
                  .uri(URI.create(imageUrl))
                  .build();
          byte[] imageBytes = httpClient.send(request, HttpResponse.BodyHandlers.ofByteArray()).body();
          String imageBase64 = Base64.getEncoder().encodeToString(imageBytes);

          ContentBlockParam imageBlock = ContentBlockParam.ofImage(
                  ImageBlockParam.builder()
                          .source(Base64ImageSource.builder()
                                  .mediaType(Base64ImageSource.MediaType.IMAGE_JPEG)
                                  .data(imageBase64)
                                  .build())
                          .build());

          ContentBlockParam textBlock = ContentBlockParam.ofText(
                  TextBlockParam.builder()
                          .text("Describe this image")
                          .build());

          MessageCountTokensParams params = MessageCountTokensParams.builder()
                  .model(Model.CLAUDE_SONNET_4_20250514)
                  .addUserMessageOfBlockParams(List.of(imageBlock, textBlock))
                  .build();

          MessageTokensCount count = client.messages().countTokens(params);
          System.out.println(count);
      }
  }
  ```
</CodeGroup>

```JSON JSON theme={null}
{ "input_tokens": 1551 }
```

### Count tokens in messages with extended thinking

<Note>
  See [here](/en/docs/build-with-claude/extended-thinking#how-context-window-is-calculated-with-extended-thinking) for more details about how the context window is calculated with extended thinking

  * Thinking blocks from **previous** assistant turns are ignored and **do not** count toward your input tokens
  * **Current** assistant turn thinking **does** count toward your input tokens
</Note>

<CodeGroup>
  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages/count_tokens \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "content-type: application/json" \
      --header "anthropic-version: 2023-06-01" \
      --data '{
        "model": "claude-sonnet-4-5",
        "thinking": {
          "type": "enabled",
          "budget_tokens": 16000
        },
        "messages": [
          {
            "role": "user",
            "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?"
          },
          {
            "role": "assistant",
            "content": [
              {
                "type": "thinking",
                "thinking": "This is a nice number theory question. Lets think about it step by step...",
                "signature": "EuYBCkQYAiJAgCs1le6/Pol5Z4/JMomVOouGrWdhYNsH3ukzUECbB6iWrSQtsQuRHJID6lWV..."
              },
              {
                "type": "text",
                "text": "Yes, there are infinitely many prime numbers p such that p mod 4 = 3..."
              }
            ]
          },
          {
            "role": "user",
            "content": "Can you write a formal proof?"
          }
        ]
      }'
  ```

  ```Python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  response = client.messages.count_tokens(
      model="claude-sonnet-4-5",
      thinking={
          "type": "enabled",
          "budget_tokens": 16000
      },
      messages=[
          {
              "role": "user",
              "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?"
          },
          {
              "role": "assistant",
              "content": [
                  {
                      "type": "thinking",
                      "thinking": "This is a nice number theory question. Let's think about it step by step...",
                      "signature": "EuYBCkQYAiJAgCs1le6/Pol5Z4/JMomVOouGrWdhYNsH3ukzUECbB6iWrSQtsQuRHJID6lWV..."
                  },
                  {
                    "type": "text",
                    "text": "Yes, there are infinitely many prime numbers p such that p mod 4 = 3..."
                  }
              ]
          },
          {
              "role": "user",
              "content": "Can you write a formal proof?"
          }
      ]
  )

  print(response.json())
  ```

  ```typescript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const client = new Anthropic();

  const response = await client.messages.countTokens({
    model: 'claude-sonnet-4-5',
    thinking: {
      'type': 'enabled',
      'budget_tokens': 16000
    },
    messages: [
      {
        'role': 'user',
        'content': 'Are there an infinite number of prime numbers such that n mod 4 == 3?'
      },
      {
        'role': 'assistant',
        'content': [
          {
            'type': 'thinking',
            'thinking': "This is a nice number theory question. Let's think about it step by step...",
            'signature': 'EuYBCkQYAiJAgCs1le6/Pol5Z4/JMomVOouGrWdhYNsH3ukzUECbB6iWrSQtsQuRHJID6lWV...'
          },
          {
            'type': 'text',
            'text': 'Yes, there are infinitely many prime numbers p such that p mod 4 = 3...',
          }
        ]
      },
      {
        'role': 'user',
        'content': 'Can you write a formal proof?'
      }
    ]
  });

  console.log(response);
  ```

  ```java Java theme={null}
  import java.util.List;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.ContentBlockParam;
  import com.anthropic.models.messages.MessageCountTokensParams;
  import com.anthropic.models.messages.MessageTokensCount;
  import com.anthropic.models.messages.Model;
  import com.anthropic.models.messages.TextBlockParam;
  import com.anthropic.models.messages.ThinkingBlockParam;

  public class CountTokensThinkingExample {

      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          List<ContentBlockParam> assistantBlocks = List.of(
                  ContentBlockParam.ofThinking(ThinkingBlockParam.builder()
                          .thinking("This is a nice number theory question. Let's think about it step by step...")
                          .signature("EuYBCkQYAiJAgCs1le6/Pol5Z4/JMomVOouGrWdhYNsH3ukzUECbB6iWrSQtsQuRHJID6lWV...")
                          .build()),
                  ContentBlockParam.ofText(TextBlockParam.builder()
                          .text("Yes, there are infinitely many prime numbers p such that p mod 4 = 3...")
                          .build())
          );

          MessageCountTokensParams params = MessageCountTokensParams.builder()
                  .model(Model.CLAUDE_SONNET_4_20250514)
                  .enabledThinking(16000)
                  .addUserMessage("Are there an infinite number of prime numbers such that n mod 4 == 3?")
                  .addAssistantMessageOfBlockParams(assistantBlocks)
                  .addUserMessage("Can you write a formal proof?")
                  .build();

          MessageTokensCount count = client.messages().countTokens(params);
          System.out.println(count);
      }
  }
  ```
</CodeGroup>

```JSON JSON theme={null}
{ "input_tokens": 88 }
```

### Count tokens in messages with PDFs

<Note>
  Token counting supports PDFs with the same [limitations](/en/docs/build-with-claude/pdf-support#pdf-support-limitations) as the Messages API.
</Note>

<CodeGroup>
  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages/count_tokens \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "content-type: application/json" \
      --header "anthropic-version: 2023-06-01" \
      --data '{
        "model": "claude-sonnet-4-5",
        "messages": [{
          "role": "user",
          "content": [
            {
              "type": "document",
              "source": {
                "type": "base64",
                "media_type": "application/pdf",
                "data": "'$(base64 -i document.pdf)'"
              }
            },
            {
              "type": "text",
              "text": "Please summarize this document."
            }
          ]
        }]
      }'
  ```

  ```Python Python theme={null}
  import base64
  import anthropic

  client = anthropic.Anthropic()

  with open("document.pdf", "rb") as pdf_file:
      pdf_base64 = base64.standard_b64encode(pdf_file.read()).decode("utf-8")

  response = client.messages.count_tokens(
      model="claude-sonnet-4-5",
      messages=[{
          "role": "user",
          "content": [
              {
                  "type": "document",
                  "source": {
                      "type": "base64",
                      "media_type": "application/pdf",
                      "data": pdf_base64
                  }
              },
              {
                  "type": "text",
                  "text": "Please summarize this document."
              }
          ]
      }]
  )

  print(response.json())
  ```

  ```Typescript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';
  import { readFileSync } from 'fs';

  const client = new Anthropic();

  const pdfBase64 = readFileSync('document.pdf', { encoding: 'base64' });

  const response = await client.messages.countTokens({
    model: 'claude-sonnet-4-5',
    messages: [{
      role: 'user',
      content: [
        {
          type: 'document',
          source: {
            type: 'base64',
            media_type: 'application/pdf',
            data: pdfBase64
          }
        },
        {
          type: 'text',
          text: 'Please summarize this document.'
        }
      ]
    }]
  });

  console.log(response);
  ```

  ```java Java theme={null}
  import java.nio.file.Files;
  import java.nio.file.Path;
  import java.util.Base64;
  import java.util.List;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.Base64PdfSource;
  import com.anthropic.models.messages.ContentBlockParam;
  import com.anthropic.models.messages.DocumentBlockParam;
  import com.anthropic.models.messages.MessageCountTokensParams;
  import com.anthropic.models.messages.MessageTokensCount;
  import com.anthropic.models.messages.Model;
  import com.anthropic.models.messages.TextBlockParam;

  public class CountTokensPdfExample {

      public static void main(String[] args) throws Exception {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          byte[] fileBytes = Files.readAllBytes(Path.of("document.pdf"));
          String pdfBase64 = Base64.getEncoder().encodeToString(fileBytes);

          ContentBlockParam documentBlock = ContentBlockParam.ofDocument(
                  DocumentBlockParam.builder()
                          .source(Base64PdfSource.builder()
                                  .mediaType(Base64PdfSource.MediaType.APPLICATION_PDF)
                                  .data(pdfBase64)
                                  .build())
                          .build());

          ContentBlockParam textBlock = ContentBlockParam.ofText(
                  TextBlockParam.builder()
                          .text("Please summarize this document.")
                          .build());

          MessageCountTokensParams params = MessageCountTokensParams.builder()
                  .model(Model.CLAUDE_SONNET_4_20250514)
                  .addUserMessageOfBlockParams(List.of(documentBlock, textBlock))
                  .build();

          MessageTokensCount count = client.messages().countTokens(params);
          System.out.println(count);
      }
  }
  ```
</CodeGroup>

```JSON JSON theme={null}
{ "input_tokens": 2188 }
```

***

## Pricing and rate limits

Token counting is **free to use** but subject to requests per minute rate limits based on your [usage tier](/en/api/rate-limits#rate-limits). If you need higher limits, contact sales through the [Claude Console](https://console.anthropic.com/settings/limits).

| Usage tier | Requests per minute (RPM) |
| ---------- | ------------------------- |
| 1          | 100                       |
| 2          | 2,000                     |
| 3          | 4,000                     |
| 4          | 8,000                     |

<Note>
  Token counting and message creation have separate and independent rate limits -- usage of one does not count against the limits of the other.
</Note>

***

## FAQ

<AccordionGroup>
  <Accordion title="Does token counting use prompt caching?">
    No, token counting provides an estimate without using caching logic. While you may provide `cache_control` blocks in your token counting request, prompt caching only occurs during actual message creation.
  </Accordion>
</AccordionGroup>


# Usage and Cost API
Source: https://docs.claude.com/en/docs/build-with-claude/usage-cost-api

Programmatically access your organization's API usage and cost data with the Usage & Cost Admin API.

<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.
</Tip>

The Usage & Cost Admin API provides programmatic and granular access to historical API usage and cost data for your organization. This data is similar to the information available in the [Usage](https://console.anthropic.com/usage) and [Cost](https://console.anthropic.com/cost) pages of the Claude Console.

This API enables you to better monitor, analyze, and optimize your Claude implementations:

* **Accurate Usage Tracking:** Get precise token counts and usage patterns instead of relying solely on response token counting
* **Cost Reconciliation:** Match internal records with Anthropic billing for finance and accounting teams
* **Product performance and improvement:** Monitor product performance while measuring if changes to the system have improved it, or setup alerting
* **[Rate limit](/en/api/rate-limits) and [Priority Tier](/en/api/service-tiers#get-started-with-priority-tier) optimization:** Optimize features like [prompt caching](/en/docs/build-with-claude/prompt-caching) or specific prompts to make the most of one’s allocated capacity, or purchase dedicated capacity.
* **Advanced Analysis:** Perform deeper data analysis than what's available in Console

<Check>
  **Admin API key required**

  This API is part of the [Admin API](/en/docs/build-with-claude/administration-api). These endpoints require an Admin API key (starting with `sk-ant-admin...`) that differs from standard API keys. Only organization members with the admin role can provision Admin API keys through the [Claude Console](https://console.anthropic.com/settings/admin-keys).
</Check>

## Partner solutions

Leading observability platforms offer ready-to-use integrations for monitoring your Claude API usage and cost, without writing custom code. These integrations provide dashboards, alerting, and analytics to help you manage your API usage effectively.

<CardGroup cols={3}>
  <Card title="Datadog" icon="chart-line" href="https://docs.datadoghq.com/integrations/anthropic/">
    LLM Observability with automatic tracing and monitoring
  </Card>

  <Card title="Grafana Cloud" icon="chart-area" href="https://grafana.com/docs/grafana-cloud/monitor-infrastructure/integrations/integration-reference/integration-anthropic/">
    Agentless integration for easy LLM observability with out-of-the-box dashboards and alerts
  </Card>

  <Card title="Honeycomb" icon="hexagon" href="https://docs.honeycomb.io/integrations/anthropic-usage-monitoring/">
    Advanced querying and visualization through OpenTelemetry
  </Card>
</CardGroup>

## Quick start

Get your organization's daily usage for the last 7 days:

```bash  theme={null}
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-08T00:00:00Z&\
ending_at=2025-01-15T00:00:00Z&\
bucket_width=1d" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"
```

<Tip>
  **Set a User-Agent header for integrations**

  If you're building an integration, set your User-Agent header to help us understand usage patterns:

  ```
  User-Agent: YourApp/1.0.0 (https://yourapp.com)
  ```
</Tip>

## Usage API

Track token consumption across your organization with detailed breakdowns by model, workspace, and service tier with the `/v1/organizations/usage_report/messages` endpoint.

### Key concepts

* **Time buckets**: Aggregate usage data in fixed intervals (`1m`, `1h`, or `1d`)
* **Token tracking**: Measure uncached input, cached input, cache creation, and output tokens
* **Filtering & grouping**: Filter by API key, workspace, model, service tier, or context window, and group results by these dimensions
* **Server tool usage**: Track usage of server-side tools like web search

For complete parameter details and response schemas, see the [Usage API reference](/en/api/admin-api/usage-cost/get-messages-usage-report).

### Basic examples

#### Daily usage by model

```bash  theme={null}
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-01T00:00:00Z&\
ending_at=2025-01-08T00:00:00Z&\
group_by[]=model&\
bucket_width=1d" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"
```

#### Hourly usage with filtering

```bash  theme={null}
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-15T00:00:00Z&\
ending_at=2025-01-15T23:59:59Z&\
models[]=claude-sonnet-4-5-20250929&\
service_tiers[]=batch&\
context_window[]=0-200k&\
bucket_width=1h" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"
```

#### Filter usage by API keys and workspaces

```bash  theme={null}
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-01T00:00:00Z&\
ending_at=2025-01-08T00:00:00Z&\
api_key_ids[]=apikey_01Rj2N8SVvo6BePZj99NhmiT&\
api_key_ids[]=apikey_01ABC123DEF456GHI789JKL&\
workspace_ids[]=wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ&\
workspace_ids[]=wrkspc_01XYZ789ABC123DEF456MNO&\
bucket_width=1d" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"
```

<Tip>
  To retrieve your organization's API key IDs, use the [List API Keys](/en/api/admin-api/apikeys/list-api-keys) endpoint.

  To retrieve your organization's workspace IDs, use the [List Workspaces](/en/api/admin-api/workspaces/list-workspaces) endpoint, or find your organization's workspace IDs in the Anthropic Console.
</Tip>

### Time granularity limits

| Granularity | Default Limit | Maximum Limit | Use Case               |
| ----------- | ------------- | ------------- | ---------------------- |
| `1m`        | 60 buckets    | 1440 buckets  | Real-time monitoring   |
| `1h`        | 24 buckets    | 168 buckets   | Daily patterns         |
| `1d`        | 7 buckets     | 31 buckets    | Weekly/monthly reports |

## Cost API

Retrieve service-level cost breakdowns in USD with the `/v1/organizations/cost_report` endpoint.

### Key concepts

* **Currency**: All costs in USD, reported as decimal strings in lowest units (cents)
* **Cost types**: Track token usage, web search, and code execution costs
* **Grouping**: Group costs by workspace or description for detailed breakdowns
* **Time buckets**: Daily granularity only (`1d`)

For complete parameter details and response schemas, see the [Cost API reference](/en/api/admin-api/usage-cost/get-cost-report).

<Warning>
  Priority Tier costs use a different billing model and are not included in the cost endpoint. Track Priority Tier usage through the usage endpoint instead.
</Warning>

### Basic example

```bash  theme={null}
curl "https://api.anthropic.com/v1/organizations/cost_report?\
starting_at=2025-01-01T00:00:00Z&\
ending_at=2025-01-31T00:00:00Z&\
group_by[]=workspace_id&\
group_by[]=description" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"
```

## Pagination

Both endpoints support pagination for large datasets:

1. Make your initial request
2. If `has_more` is `true`, use the `next_page` value in your next request
3. Continue until `has_more` is `false`

```bash  theme={null}
# First request
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-01T00:00:00Z&\
ending_at=2025-01-31T00:00:00Z&\
limit=7" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"

# Response includes: "has_more": true, "next_page": "page_xyz..."

# Next request with pagination
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-01T00:00:00Z&\
ending_at=2025-01-31T00:00:00Z&\
limit=7&\
page=page_xyz..." \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"
```

## Common use cases

Explore detailed implementations in [anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook):

* **Daily usage reports**: Track token consumption trends
* **Cost attribution**: Allocate expenses by workspace for chargebacks
* **Cache efficiency**: Measure and optimize prompt caching
* **Budget monitoring**: Set up alerts for spending thresholds
* **CSV export**: Generate reports for finance teams

## Frequently asked questions

### How fresh is the data?

Usage and cost data typically appears within 5 minutes of API request completion, though delays may occasionally be longer.

### What's the recommended polling frequency?

The API supports polling once per minute for sustained use. For short bursts (e.g., downloading paginated data), more frequent polling is acceptable. Cache results for dashboards that need frequent updates.

### How do I track code execution usage?

Code execution costs appear in the cost endpoint grouped under `Code Execution Usage` in the description field. Code execution is not included in the usage endpoint.

### How do I track Priority Tier usage?

Filter or group by `service_tier` in the usage endpoint and look for the `priority` value. Priority Tier costs are not available in the cost endpoint.

### What happens with Workbench usage?

API usage from the Workbench is not associated with an API key, so `api_key_id` will be `null` even when grouping by that dimension.

### How is the default workspace represented?

Usage and costs attributed to the default workspace have a `null` value for `workspace_id`.

### How do I get per-user cost breakdowns for Claude Code?

Use the [Claude Code Analytics API](/en/docs/build-with-claude/claude-code-analytics-api), which provides per-user estimated costs and productivity metrics without the performance limitations of breaking down costs by many API keys. For general API usage with many keys, use the [Usage API](#usage-api) to track token consumption as a cost proxy.

## See also

The Usage and Cost APIs can be used to help you deliver a better experience for your users, help you manage costs, and preserve your rate limit. Learn more about some of these other features:

* [Admin API overview](/en/docs/build-with-claude/administration-api)
* [Admin API reference](/en/api/admin-api)
* [Pricing](/en/docs/about-claude/pricing)
* [Prompt caching](/en/docs/build-with-claude/prompt-caching) - Optimize costs with caching
* [Batch processing](/en/docs/build-with-claude/batch-processing) - 50% discount on batch requests
* [Rate limits](/en/api/rate-limits) - Understand usage tiers


# Vision
Source: https://docs.claude.com/en/docs/build-with-claude/vision

The Claude 3 and 4 families of models comes with new vision capabilities that allow Claude to understand and analyze images, opening up exciting possibilities for multimodal interaction.

This guide describes how to work with images in Claude, including best practices, code examples, and limitations to keep in mind.

***

## How to use vision

Use Claude’s vision capabilities via:

* [claude.ai](https://claude.ai/). Upload an image like you would a file, or drag and drop an image directly into the chat window.
* The [Console Workbench](https://console.anthropic.com/workbench/). If you select a model that accepts images (Claude 3 and 4 models only), a button to add images appears at the top right of every User message block.
* **API request**. See the examples in this guide.

***

## Before you upload

### Basics and Limits

You can include multiple images in a single request (up to 20 for [claude.ai](https://claude.ai/) and 100 for API requests). Claude will analyze all provided images when formulating its response. This can be helpful for comparing or contrasting images.

If you submit an image larger than 8000x8000 px, it will be rejected. If you submit more than 20 images in one API request, this limit is 2000x2000 px.

<Note>
  While the API supports 100 images per request, there is a [32MB request size limit](/en/api/overview#request-size-limits) for standard endpoints.
</Note>

### Evaluate image size

For optimal performance, we recommend resizing images before uploading if they are too large. If your image’s long edge is more than 1568 pixels, or your image is more than \~1,600 tokens, it will first be scaled down, preserving aspect ratio, until it’s within the size limits.

If your input image is too large and needs to be resized, it will increase latency of [time-to-first-token](/en/docs/about-claude/glossary), without giving you any additional model performance. Very small images under 200 pixels on any given edge may degrade performance.

<Tip>
  To improve [time-to-first-token](/en/docs/about-claude/glossary), we recommend
  resizing images to no more than 1.15 megapixels (and within 1568 pixels in
  both dimensions).
</Tip>

Here is a table of maximum image sizes accepted by our API that will not be resized for common aspect ratios. With the Claude Sonnet 3.7 model, these images use approximately 1,600 tokens and around \$4.80/1K images.

| Aspect ratio | Image size   |
| ------------ | ------------ |
| 1:1          | 1092x1092 px |
| 3:4          | 951x1268 px  |
| 2:3          | 896x1344 px  |
| 9:16         | 819x1456 px  |
| 1:2          | 784x1568 px  |

### Calculate image costs

Each image you include in a request to Claude counts towards your token usage. To calculate the approximate cost, multiply the approximate number of image tokens by the [per-token price of the model](https://claude.com/pricing) you’re using.

If your image does not need to be resized, you can estimate the number of tokens used through this algorithm: `tokens = (width px * height px)/750`

Here are examples of approximate tokenization and costs for different image sizes within our API’s size constraints based on Claude Sonnet 3.7 per-token price of \$3 per million input tokens:

| Image size                    | # of Tokens | Cost / image | Cost / 1K images |
| ----------------------------- | ----------- | ------------ | ---------------- |
| 200x200 px(0.04 megapixels)   | \~54        | \~\$0.00016  | \~\$0.16         |
| 1000x1000 px(1 megapixel)     | \~1334      | \~\$0.004    | \~\$4.00         |
| 1092x1092 px(1.19 megapixels) | \~1590      | \~\$0.0048   | \~\$4.80         |

### Ensuring image quality

When providing images to Claude, keep the following in mind for best results:

* **Image format**: Use a supported image format: JPEG, PNG, GIF, or WebP.
* **Image clarity**: Ensure images are clear and not too blurry or pixelated.
* **Text**: If the image contains important text, make sure it’s legible and not too small. Avoid cropping out key visual context just to enlarge the text.

***

## Prompt examples

Many of the [prompting techniques](/en/docs/build-with-claude/prompt-engineering/overview) that work well for text-based interactions with Claude can also be applied to image-based prompts.

These examples demonstrate best practice prompt structures involving images.

<Tip>
  Just as with document-query placement, Claude works best when images come
  before text. Images placed after text or interpolated with text will still
  perform well, but if your use case allows it, we recommend an image-then-text
  structure.
</Tip>

### About the prompt examples

The following examples demonstrate how to use Claude's vision capabilities using various programming languages and approaches. You can provide images to Claude in three ways:

1. As a base64-encoded image in `image` content blocks
2. As a URL reference to an image hosted online
3. Using the Files API (upload once, use multiple times)

The base64 example prompts use these variables:

<CodeGroup>
  ```bash Shell theme={null}
      # For URL-based images, you can use the URL directly in your JSON request
      
      # For base64-encoded images, you need to first encode the image
      # Example of how to encode an image to base64 in bash:
      BASE64_IMAGE_DATA=$(curl -s "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg" | base64)
      
      # The encoded data can now be used in your API calls
  ```

  ```Python Python theme={null}
  import base64
  import httpx

  # For base64-encoded images
  image1_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
  image1_media_type = "image/jpeg"
  image1_data = base64.standard_b64encode(httpx.get(image1_url).content).decode("utf-8")

  image2_url = "https://upload.wikimedia.org/wikipedia/commons/b/b5/Iridescent.green.sweat.bee1.jpg"
  image2_media_type = "image/jpeg"
  image2_data = base64.standard_b64encode(httpx.get(image2_url).content).decode("utf-8")

  # For URL-based images, you can use the URLs directly in your requests
  ```

  ```TypeScript TypeScript theme={null}
  import axios from 'axios';

  // For base64-encoded images
  async function getBase64Image(url: string): Promise<string> {
    const response = await axios.get(url, { responseType: 'arraybuffer' });
    return Buffer.from(response.data, 'binary').toString('base64');
  }

  // Usage
  async function prepareImages() {
    const imageData = await getBase64Image('https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg');
    // Now you can use imageData in your API calls
  }

  // For URL-based images, you can use the URLs directly in your requests
  ```

  ```java Java theme={null}
  import java.io.IOException;
  import java.util.Base64;
  import java.io.InputStream;
  import java.net.URL;

  public class ImageHandlingExample {

      public static void main(String[] args) throws IOException, InterruptedException {
          // For base64-encoded images
          String image1Url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg";
          String image1MediaType = "image/jpeg";
          String image1Data = downloadAndEncodeImage(image1Url);

          String image2Url = "https://upload.wikimedia.org/wikipedia/commons/b/b5/Iridescent.green.sweat.bee1.jpg";
          String image2MediaType = "image/jpeg";
          String image2Data = downloadAndEncodeImage(image2Url);

          // For URL-based images, you can use the URLs directly in your requests
      }

      private static String downloadAndEncodeImage(String imageUrl) throws IOException {
          try (InputStream inputStream = new URL(imageUrl).openStream()) {
              return Base64.getEncoder().encodeToString(inputStream.readAllBytes());
          }
      }

  }
  ```
</CodeGroup>

Below are examples of how to include images in a Messages API request using base64-encoded images and URL references:

### Base64-encoded image example

<CodeGroup>
  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "image",
              "source": {
                "type": "base64",
                "media_type": "image/jpeg",
                "data": "'"$BASE64_IMAGE_DATA"'"
              }
            },
            {
              "type": "text",
              "text": "Describe this image."
            }
          ]
        }
      ]
    }'
  ```

  ```Python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()
  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "image",
                      "source": {
                          "type": "base64",
                          "media_type": image1_media_type,
                          "data": image1_data,
                      },
                  },
                  {
                      "type": "text",
                      "text": "Describe this image."
                  }
              ],
          }
      ],
  )
  print(message)
  ```

  ```TypeScript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  async function main() {
    const message = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 1024,
      messages: [
        {
          role: "user",
          content: [
            {
              type: "image",
              source: {
                type: "base64",
                media_type: "image/jpeg",
                data: imageData, // Base64-encoded image data as string
              }
            },
            {
              type: "text",
              text: "Describe this image."
            }
          ]
        }
      ]
    });
    
    console.log(message);
  }

  main();
  ```

  ```Java Java theme={null}
  import java.io.IOException;
  import java.util.List;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.*;

  public class VisionExample {
      public static void main(String[] args) throws IOException, InterruptedException {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();
          String imageData = ""; // // Base64-encoded image data as string

          List<ContentBlockParam> contentBlockParams = List.of(
                  ContentBlockParam.ofImage(
                          ImageBlockParam.builder()
                                  .source(Base64ImageSource.builder()
                                          .data(imageData)
                                          .build())
                                  .build()
                  ),
                  ContentBlockParam.ofText(TextBlockParam.builder()
                          .text("Describe this image.")
                          .build())
          );
          Message message = client.messages().create(
                  MessageCreateParams.builder()
                          .model(Model.CLAUDE_3_7_SONNET_LATEST)
                          .maxTokens(1024)
                          .addUserMessageOfBlockParams(contentBlockParams)
                          .build()
          );

          System.out.println(message);
      }
  }
  ```
</CodeGroup>

### URL-based image example

<CodeGroup>
  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "image",
              "source": {
                "type": "url",
                "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
              }
            },
            {
              "type": "text",
              "text": "Describe this image."
            }
          ]
        }
      ]
    }'
  ```

  ```Python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()
  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "image",
                      "source": {
                          "type": "url",
                          "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                      },
                  },
                  {
                      "type": "text",
                      "text": "Describe this image."
                  }
              ],
          }
      ],
  )
  print(message)
  ```

  ```TypeScript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  async function main() {
    const message = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 1024,
      messages: [
        {
          role: "user",
          content: [
            {
              type: "image",
              source: {
                type: "url",
                url: "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
              }
            },
            {
              type: "text",
              text: "Describe this image."
            }
          ]
        }
      ]
    });
    
    console.log(message);
  }

  main();
  ```

  ```Java Java theme={null}
  import java.io.IOException;
  import java.util.List;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.*;

  public class VisionExample {

      public static void main(String[] args) throws IOException, InterruptedException {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          List<ContentBlockParam> contentBlockParams = List.of(
                  ContentBlockParam.ofImage(
                          ImageBlockParam.builder()
                                  .source(UrlImageSource.builder()
                                          .url("https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg")
                                          .build())
                                  .build()
                  ),
                  ContentBlockParam.ofText(TextBlockParam.builder()
                          .text("Describe this image.")
                          .build())
          );
          Message message = client.messages().create(
                  MessageCreateParams.builder()
                          .model(Model.CLAUDE_3_7_SONNET_LATEST)
                          .maxTokens(1024)
                          .addUserMessageOfBlockParams(contentBlockParams)
                          .build()
          );
          System.out.println(message);
      }
  }
  ```
</CodeGroup>

### Files API image example

For images you'll use repeatedly or when you want to avoid encoding overhead, use the [Files API](/en/docs/build-with-claude/files):

<CodeGroup>
  ```bash Shell theme={null}
  # First, upload your image to the Files API
  curl -X POST https://api.anthropic.com/v1/files \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14" \
    -F "file=@image.jpg"

  # Then use the returned file_id in your message
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "image",
              "source": {
                "type": "file",
                "file_id": "file_abc123"
              }
            },
            {
              "type": "text",
              "text": "Describe this image."
            }
          ]
        }
      ]
    }'
  ```

  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  # Upload the image file
  with open("image.jpg", "rb") as f:
      file_upload = client.beta.files.upload(file=("image.jpg", f, "image/jpeg"))

  # Use the uploaded file in a message
  message = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      betas=["files-api-2025-04-14"],
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "image",
                      "source": {
                          "type": "file",
                          "file_id": file_upload.id
                      }
                  },
                  {
                      "type": "text",
                      "text": "Describe this image."
                  }
              ]
          }
      ],
  )

  print(message.content)
  ```

  ```typescript TypeScript theme={null}
  import { Anthropic, toFile } from '@anthropic-ai/sdk';
  import fs from 'fs';

  const anthropic = new Anthropic();

  async function main() {
    // Upload the image file
    const fileUpload = await anthropic.beta.files.upload({
      file: toFile(fs.createReadStream('image.jpg'), undefined, { type: "image/jpeg" })
    }, {
      betas: ['files-api-2025-04-14']
    });

    // Use the uploaded file in a message
    const response = await anthropic.beta.messages.create({
      model: 'claude-sonnet-4-5',
      max_tokens: 1024,
      betas: ['files-api-2025-04-14'],
      messages: [
        {
          role: 'user',
          content: [
            {
              type: 'image',
              source: {
                type: 'file',
                file_id: fileUpload.id
              }
            },
            {
              type: 'text',
              text: 'Describe this image.'
            }
          ]
        }
      ]
    });

    console.log(response);
  }

  main();
  ```

  ```java Java theme={null}
  import java.io.IOException;
  import java.nio.file.Files;
  import java.nio.file.Path;
  import java.util.List;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.File;
  import com.anthropic.models.files.FileUploadParams;
  import com.anthropic.models.messages.*;

  public class ImageFilesExample {
      public static void main(String[] args) throws IOException {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          // Upload the image file
          File file = client.beta().files().upload(FileUploadParams.builder()
                  .file(Files.newInputStream(Path.of("image.jpg")))
                  .build());

          // Use the uploaded file in a message
          ImageBlockParam imageParam = ImageBlockParam.builder()
                  .fileSource(file.id())
                  .build();

          MessageCreateParams params = MessageCreateParams.builder()
                  .model(Model.CLAUDE_3_7_SONNET_LATEST)
                  .maxTokens(1024)
                  .addUserMessageOfBlockParams(
                          List.of(
                                  ContentBlockParam.ofImage(imageParam),
                                  ContentBlockParam.ofText(
                                          TextBlockParam.builder()
                                                  .text("Describe this image.")
                                                  .build()
                                  )
                          )
                  )
                  .build();

          Message message = client.messages().create(params);
          System.out.println(message.content());
      }
  }
  ```
</CodeGroup>

See [Messages API examples](/en/api/messages) for more example code and parameter details.

<AccordionGroup>
  <Accordion title="Example: One image">
    It’s best to place images earlier in the prompt than questions about them or instructions for tasks that use them.

    Ask Claude to describe one image.

    | Role | Content                       |
    | ---- | ----------------------------- |
    | User | \[Image] Describe this image. |

    Here is the corresponding API call using the Claude Sonnet 3.7 model.

    <Tabs>
      <Tab title="Using Base64">
        ```Python Python theme={null}
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": image1_media_type,
                                "data": image1_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": "Describe this image."
                        }
                    ],
                }
            ],
        )
        ```
      </Tab>

      <Tab title="Using URL">
        ```Python Python theme={null}
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "url",
                                "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                            },
                        },
                        {
                            "type": "text",
                            "text": "Describe this image."
                        }
                    ],
                }
            ],
        )
        ```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Example: Multiple images">
    In situations where there are multiple images, introduce each image with `Image 1:` and `Image 2:` and so on. You don’t need newlines between images or between images and the prompt.

    Ask Claude to describe the differences between multiple images.

    | Role | Content                                                                 |
    | ---- | ----------------------------------------------------------------------- |
    | User | Image 1: \[Image 1] Image 2: \[Image 2] How are these images different? |

    Here is the corresponding API call using the Claude Sonnet 3.7 model.

    <Tabs>
      <Tab title="Using Base64">
        ```Python Python theme={null}
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Image 1:"
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": image1_media_type,
                                "data": image1_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": "Image 2:"
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": image2_media_type,
                                "data": image2_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": "How are these images different?"
                        }
                    ],
                }
            ],
        )
        ```
      </Tab>

      <Tab title="Using URL">
        ```Python Python theme={null}
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Image 1:"
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "url",
                                "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                            },
                        },
                        {
                            "type": "text",
                            "text": "Image 2:"
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "url",
                                "url": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Iridescent.green.sweat.bee1.jpg",
                            },
                        },
                        {
                            "type": "text",
                            "text": "How are these images different?"
                        }
                    ],
                }
            ],
        )
        ```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Example: Multiple images with a system prompt">
    Ask Claude to describe the differences between multiple images, while giving it a system prompt for how to respond.

    | Content |                                                                         |
    | ------- | ----------------------------------------------------------------------- |
    | System  | Respond only in Spanish.                                                |
    | User    | Image 1: \[Image 1] Image 2: \[Image 2] How are these images different? |

    Here is the corresponding API call using the Claude Sonnet 3.7 model.

    <Tabs>
      <Tab title="Using Base64">
        ```Python Python theme={null}
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            system="Respond only in Spanish.",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Image 1:"
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": image1_media_type,
                                "data": image1_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": "Image 2:"
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": image2_media_type,
                                "data": image2_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": "How are these images different?"
                        }
                    ],
                }
            ],
        )
        ```
      </Tab>

      <Tab title="Using URL">
        ```Python Python theme={null}
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            system="Respond only in Spanish.",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Image 1:"
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "url",
                                "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                            },
                        },
                        {
                            "type": "text",
                            "text": "Image 2:"
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "url",
                                "url": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Iridescent.green.sweat.bee1.jpg",
                            },
                        },
                        {
                            "type": "text",
                            "text": "How are these images different?"
                        }
                    ],
                }
            ],
        )
        ```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Example: Four images across two conversation turns">
    Claude’s vision capabilities shine in multimodal conversations that mix images and text. You can have extended back-and-forth exchanges with Claude, adding new images or follow-up questions at any point. This enables powerful workflows for iterative image analysis, comparison, or combining visuals with other knowledge.

    Ask Claude to contrast two images, then ask a follow-up question comparing the first images to two new images.

    | Role      | Content                                                                            |
    | --------- | ---------------------------------------------------------------------------------- |
    | User      | Image 1: \[Image 1] Image 2: \[Image 2] How are these images different?            |
    | Assistant | \[Claude's response]                                                               |
    | User      | Image 1: \[Image 3] Image 2: \[Image 4] Are these images similar to the first two? |
    | Assistant | \[Claude's response]                                                               |

    When using the API, simply insert new images into the array of Messages in the `user` role as part of any standard [multiturn conversation](/en/api/messages) structure.
  </Accordion>
</AccordionGroup>

***

## Limitations

While Claude's image understanding capabilities are cutting-edge, there are some limitations to be aware of:

* **People identification**: Claude [cannot be used](https://www.anthropic.com/legal/aup) to identify (i.e., name) people in images and will refuse to do so.
* **Accuracy**: Claude may hallucinate or make mistakes when interpreting low-quality, rotated, or very small images under 200 pixels.
* **Spatial reasoning**: Claude's spatial reasoning abilities are limited. It may struggle with tasks requiring precise localization or layouts, like reading an analog clock face or describing exact positions of chess pieces.
* **Counting**: Claude can give approximate counts of objects in an image but may not always be precisely accurate, especially with large numbers of small objects.
* **AI generated images**: Claude does not know if an image is AI-generated and may be incorrect if asked. Do not rely on it to detect fake or synthetic images.
* **Inappropriate content**: Claude will not process inappropriate or explicit images that violate our [Acceptable Use Policy](https://www.anthropic.com/legal/aup).
* **Healthcare applications**: While Claude can analyze general medical images, it is not designed to interpret complex diagnostic scans such as CTs or MRIs. Claude's outputs should not be considered a substitute for professional medical advice or diagnosis.

Always carefully review and verify Claude's image interpretations, especially for high-stakes use cases. Do not use Claude for tasks requiring perfect precision or sensitive image analysis without human oversight.

***

## FAQ

<AccordionGroup>
  <Accordion title="What image file types does Claude support?">
    Claude currently supports JPEG, PNG, GIF, and WebP image formats, specifically:

    * `image/jpeg`
    * `image/png`
    * `image/gif`
    * `image/webp`
  </Accordion>

  {" "}

  <Accordion title="Can Claude read image URLs?">
    Yes, Claude can now process images from URLs with our URL image source blocks in the API.
    Simply use the "url" source type instead of "base64" in your API requests.
    Example:

    ```json  theme={null}
    {
      "type": "image",
      "source": {
        "type": "url",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
      }
    }
    ```
  </Accordion>

  <Accordion title="Is there a limit to the image file size I can upload?">
    Yes, there are limits:

    * API: Maximum 5MB per image
    * claude.ai: Maximum 10MB per image

    Images larger than these limits will be rejected and return an error when using our API.
  </Accordion>

  <Accordion title="How many images can I include in one request?">
    The image limits are:

    * Messages API: Up to 100 images per request
    * claude.ai: Up to 20 images per turn

    Requests exceeding these limits will be rejected and return an error.
  </Accordion>

  {" "}

  <Accordion title="Does Claude read image metadata?">
    No, Claude does not parse or receive any metadata from images passed to it.
  </Accordion>

  {" "}

  <Accordion title="Can I delete images I've uploaded?">
    No. Image uploads are ephemeral and not stored beyond the duration of the API
    request. Uploaded images are automatically deleted after they have been
    processed.
  </Accordion>

  {" "}

  <Accordion title="Where can I find details on data privacy for image uploads?">
    Please refer to our privacy policy page for information on how we handle
    uploaded images and other data. We do not use uploaded images to train our
    models.
  </Accordion>

  <Accordion title="What if Claude's image interpretation seems wrong?">
    If Claude's image interpretation seems incorrect:

    1. Ensure the image is clear, high-quality, and correctly oriented.
    2. Try prompt engineering techniques to improve results.
    3. If the issue persists, flag the output in claude.ai (thumbs up/down) or contact our support team.

    Your feedback helps us improve!
  </Accordion>

  <Accordion title="Can Claude generate or edit images?">
    No, Claude is an image understanding model only. It can interpret and analyze images, but it cannot generate, produce, edit, manipulate, or create images.
  </Accordion>
</AccordionGroup>

***

## Dive deeper into vision

Ready to start building with images using Claude? Here are a few helpful resources:

* [Multimodal cookbook](https://github.com/anthropics/anthropic-cookbook/tree/main/multimodal): This cookbook has tips on [getting started with images](https://github.com/anthropics/anthropic-cookbook/blob/main/multimodal/getting%5Fstarted%5Fwith%5Fvision.ipynb) and [best practice techniques](https://github.com/anthropics/anthropic-cookbook/blob/main/multimodal/best%5Fpractices%5Ffor%5Fvision.ipynb) to ensure the highest quality performance with images. See how you can effectively prompt Claude with images to carry out tasks such as [interpreting and analyzing charts](https://github.com/anthropics/anthropic-cookbook/blob/main/multimodal/reading%5Fcharts%5Fgraphs%5Fpowerpoints.ipynb) or [extracting content from forms](https://github.com/anthropics/anthropic-cookbook/blob/main/multimodal/how%5Fto%5Ftranscribe%5Ftext.ipynb).
* [API reference](/en/api/messages): Visit our documentation for the Messages API, including example [API calls involving images](/en/docs/build-with-claude/working-with-messages#vision).

If you have any other questions, feel free to reach out to our [support team](https://support.claude.com/). You can also join our [developer community](https://www.anthropic.com/discord) to connect with other creators and get help from Anthropic experts.


# Using the Messages API
Source: https://docs.claude.com/en/docs/build-with-claude/working-with-messages

Practical patterns and examples for using the Messages API effectively

This guide covers common patterns for working with the Messages API, including basic requests, multi-turn conversations, prefill techniques, and vision capabilities. For complete API specifications, see the [Messages API reference](/en/api/messages).

## Basic request and response

<CodeGroup>
  ```bash Shell theme={null}
  #!/bin/sh
  curl https://api.anthropic.com/v1/messages \
       --header "x-api-key: $ANTHROPIC_API_KEY" \
       --header "anthropic-version: 2023-06-01" \
       --header "content-type: application/json" \
       --data \
  '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
          {"role": "user", "content": "Hello, Claude"}
      ]
  }'
  ```

  ```Python Python theme={null}
  import anthropic

  message = anthropic.Anthropic().messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {"role": "user", "content": "Hello, Claude"}
      ]
  )
  print(message)
  ```

  ```TypeScript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const message = await anthropic.messages.create({
    model: 'claude-sonnet-4-5',
    max_tokens: 1024,
    messages: [
      {"role": "user", "content": "Hello, Claude"}
    ]
  });
  console.log(message);
  ```
</CodeGroup>

```JSON JSON theme={null}
{
  "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Hello!"
    }
  ],
  "model": "claude-sonnet-4-5",
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 12,
    "output_tokens": 6
  }
}
```

## Multiple conversational turns

The Messages API is stateless, which means that you always send the full conversational history to the API. You can use this pattern to build up a conversation over time. Earlier conversational turns don't necessarily need to actually originate from Claude — you can use synthetic `assistant` messages.

<CodeGroup>
  ```bash Shell theme={null}
  #!/bin/sh
  curl https://api.anthropic.com/v1/messages \
       --header "x-api-key: $ANTHROPIC_API_KEY" \
       --header "anthropic-version: 2023-06-01" \
       --header "content-type: application/json" \
       --data \
  '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
          {"role": "user", "content": "Hello, Claude"},
          {"role": "assistant", "content": "Hello!"},
          {"role": "user", "content": "Can you describe LLMs to me?"}

      ]
  }'
  ```

  ```Python Python theme={null}
  import anthropic

  message = anthropic.Anthropic().messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {"role": "user", "content": "Hello, Claude"},
          {"role": "assistant", "content": "Hello!"},
          {"role": "user", "content": "Can you describe LLMs to me?"}
      ],
  )
  print(message)

  ```

  ```TypeScript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  await anthropic.messages.create({
    model: 'claude-sonnet-4-5',
    max_tokens: 1024,
    messages: [
      {"role": "user", "content": "Hello, Claude"},
      {"role": "assistant", "content": "Hello!"},
      {"role": "user", "content": "Can you describe LLMs to me?"}
    ]
  });
  ```
</CodeGroup>

```JSON JSON theme={null}
{
    "id": "msg_018gCsTGsXkYJVqYPxTgDHBU",
    "type": "message",
    "role": "assistant",
    "content": [
        {
            "type": "text",
            "text": "Sure, I'd be happy to provide..."
        }
    ],
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "usage": {
      "input_tokens": 30,
      "output_tokens": 309
    }
}
```

## Putting words in Claude's mouth

You can pre-fill part of Claude's response in the last position of the input messages list. This can be used to shape Claude's response. The example below uses `"max_tokens": 1` to get a single multiple choice answer from Claude.

<CodeGroup>
  ```bash Shell theme={null}
  #!/bin/sh
  curl https://api.anthropic.com/v1/messages \
       --header "x-api-key: $ANTHROPIC_API_KEY" \
       --header "anthropic-version: 2023-06-01" \
       --header "content-type: application/json" \
       --data \
  '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1,
      "messages": [
          {"role": "user", "content": "What is latin for Ant? (A) Apoidea, (B) Rhopalocera, (C) Formicidae"},
          {"role": "assistant", "content": "The answer is ("}
      ]
  }'
  ```

  ```Python Python theme={null}
  import anthropic

  message = anthropic.Anthropic().messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1,
      messages=[
          {"role": "user", "content": "What is latin for Ant? (A) Apoidea, (B) Rhopalocera, (C) Formicidae"},
          {"role": "assistant", "content": "The answer is ("}
      ]
  )
  print(message)
  ```

  ```TypeScript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const message = await anthropic.messages.create({
    model: 'claude-sonnet-4-5',
    max_tokens: 1,
    messages: [
      {"role": "user", "content": "What is latin for Ant? (A) Apoidea, (B) Rhopalocera, (C) Formicidae"},
      {"role": "assistant", "content": "The answer is ("}
    ]
  });
  console.log(message);
  ```
</CodeGroup>

```JSON JSON theme={null}
{
  "id": "msg_01Q8Faay6S7QPTvEUUQARt7h",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "C"
    }
  ],
  "model": "claude-sonnet-4-5",
  "stop_reason": "max_tokens",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 42,
    "output_tokens": 1
  }
}
```

For more information on prefill techniques, see our [prefill guide](/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response).

## Vision

Claude can read both text and images in requests. We support both `base64` and `url` source types for images, and the `image/jpeg`, `image/png`, `image/gif`, and `image/webp` media types. See our [vision guide](/en/docs/build-with-claude/vision) for more details.

<CodeGroup>
  ```bash Shell theme={null}
  #!/bin/sh

  # Option 1: Base64-encoded image
  IMAGE_URL="https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
  IMAGE_MEDIA_TYPE="image/jpeg"
  IMAGE_BASE64=$(curl "$IMAGE_URL" | base64)

  curl https://api.anthropic.com/v1/messages \
       --header "x-api-key: $ANTHROPIC_API_KEY" \
       --header "anthropic-version: 2023-06-01" \
       --header "content-type: application/json" \
       --data \
  '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
          {"role": "user", "content": [
              {"type": "image", "source": {
                  "type": "base64",
                  "media_type": "'$IMAGE_MEDIA_TYPE'",
                  "data": "'$IMAGE_BASE64'"
              }},
              {"type": "text", "text": "What is in the above image?"}
          ]}
      ]
  }'

  # Option 2: URL-referenced image
  curl https://api.anthropic.com/v1/messages \
       --header "x-api-key: $ANTHROPIC_API_KEY" \
       --header "anthropic-version: 2023-06-01" \
       --header "content-type: application/json" \
       --data \
  '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
          {"role": "user", "content": [
              {"type": "image", "source": {
                  "type": "url",
                  "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
              }},
              {"type": "text", "text": "What is in the above image?"}
          ]}
      ]
  }'
  ```

  ```Python Python theme={null}
  import anthropic
  import base64
  import httpx

  # Option 1: Base64-encoded image
  image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
  image_media_type = "image/jpeg"
  image_data = base64.standard_b64encode(httpx.get(image_url).content).decode("utf-8")

  message = anthropic.Anthropic().messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "image",
                      "source": {
                          "type": "base64",
                          "media_type": image_media_type,
                          "data": image_data,
                      },
                  },
                  {
                      "type": "text",
                      "text": "What is in the above image?"
                  }
              ],
          }
      ],
  )
  print(message)

  # Option 2: URL-referenced image
  message_from_url = anthropic.Anthropic().messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "image",
                      "source": {
                          "type": "url",
                          "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                      },
                  },
                  {
                      "type": "text",
                      "text": "What is in the above image?"
                  }
              ],
          }
      ],
  )
  print(message_from_url)
  ```

  ```TypeScript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  // Option 1: Base64-encoded image
  const image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
  const image_media_type = "image/jpeg"
  const image_array_buffer = await ((await fetch(image_url)).arrayBuffer());
  const image_data = Buffer.from(image_array_buffer).toString('base64');

  const message = await anthropic.messages.create({
    model: 'claude-sonnet-4-5',
    max_tokens: 1024,
    messages: [
          {
              "role": "user",
              "content": [
                  {
                      "type": "image",
                      "source": {
                          "type": "base64",
                          "media_type": image_media_type,
                          "data": image_data,
                      },
                  },
                  {
                      "type": "text",
                      "text": "What is in the above image?"
                  }
              ],
          }
        ]
  });
  console.log(message);

  // Option 2: URL-referenced image
  const messageFromUrl = await anthropic.messages.create({
    model: 'claude-sonnet-4-5',
    max_tokens: 1024,
    messages: [
          {
              "role": "user",
              "content": [
                  {
                      "type": "image",
                      "source": {
                          "type": "url",
                          "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                      },
                  },
                  {
                      "type": "text",
                      "text": "What is in the above image?"
                  }
              ],
          }
        ]
  });
  console.log(messageFromUrl);
  ```
</CodeGroup>

```JSON JSON theme={null}
{
  "id": "msg_01EcyWo6m4hyW8KHs2y2pei5",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "This image shows an ant, specifically a close-up view of an ant. The ant is shown in detail, with its distinct head, antennae, and legs clearly visible. The image is focused on capturing the intricate details and features of the ant, likely taken with a macro lens to get an extreme close-up perspective."
    }
  ],
  "model": "claude-sonnet-4-5",
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 1551,
    "output_tokens": 71
  }
}
```

## Tool use, JSON mode, and computer use

See our [guide](/en/docs/agents-and-tools/tool-use/overview) for examples for how to use tools with the Messages API.
See our [computer use guide](/en/docs/agents-and-tools/tool-use/computer-use-tool) for examples of how to control desktop computer environments with the Messages API.


# Get started with Claude
Source: https://docs.claude.com/en/docs/get-started

Make your first API call to Claude and build a simple web search assistant

## Prerequisites

* An Anthropic [Console account](https://console.anthropic.com/)
* An [API key](https://console.anthropic.com/settings/keys)

## Call the API

<Tabs>
  <Tab title="cURL">
    <Steps>
      <Step title="Set your API key">
        Get your API key from the [Claude Console](https://console.anthropic.com/settings/keys) and set it as an environment variable:

        ```bash  theme={null}
        export ANTHROPIC_API_KEY='your-api-key-here'
        ```
      </Step>

      <Step title="Make your first API call">
        Run this command to create a simple web search assistant:

        ```bash  theme={null}
        curl https://api.anthropic.com/v1/messages \
          -H "Content-Type: application/json" \
          -H "x-api-key: $ANTHROPIC_API_KEY" \
          -H "anthropic-version: 2023-06-01" \
          -d '{
            "model": "claude-sonnet-4-5",
            "max_tokens": 1000,
            "messages": [
              {
                "role": "user", 
                "content": "What should I search for to find the latest developments in renewable energy?"
              }
            ]
          }'
        ```

        **Example output:**

        ```json  theme={null}
        {
          "id": "msg_01HCDu5LRGeP2o7s2xGmxyx8",
          "type": "message", 
          "role": "assistant",
          "content": [
            {
              "type": "text",
              "text": "Here are some effective search strategies to find the latest renewable energy developments:\n\n## Search Terms to Use:\n- \"renewable energy news 2024\"\n- \"clean energy breakthrough\"\n- \"solar/wind/battery technology advances\"\n- \"green energy innovations\"\n- \"climate tech developments\"\n- \"energy storage solutions\"\n\n## Best Sources to Check:\n\n**News & Industry Sites:**\n- Renewable Energy World\n- GreenTech Media (now Wood Mackenzie)\n- Energy Storage News\n- CleanTechnica\n- PV Magazine (for solar)\n- WindPower Engineering & Development..."
            }
          ],
          "model": "claude-sonnet-4-5",
          "stop_reason": "end_turn",
          "usage": {
            "input_tokens": 21,
            "output_tokens": 305
          }
        }
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="Python">
    <Steps>
      <Step title="Set your API key">
        Get your API key from the [Claude Console](https://console.anthropic.com/settings/keys) and set it as an environment variable:

        ```bash  theme={null}
        export ANTHROPIC_API_KEY='your-api-key-here'
        ```
      </Step>

      <Step title="Install the SDK">
        Install the Anthropic Python SDK:

        ```bash  theme={null}
        pip install anthropic
        ```
      </Step>

      <Step title="Create your code">
        Save this as `quickstart.py`:

        ```python  theme={null}
        import anthropic

        client = anthropic.Anthropic()

        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": "What should I search for to find the latest developments in renewable energy?"
                }
            ]
        )
        print(message.content)
        ```
      </Step>

      <Step title="Run your code">
        ```bash  theme={null}
        python quickstart.py
        ```

        **Example output:**

        ```python  theme={null}
        [TextBlock(text='Here are some effective search strategies for finding the latest renewable energy developments:\n\n**Search Terms to Use:**\n- "renewable energy news 2024"\n- "clean energy breakthroughs"\n- "solar/wind/battery technology advances"\n- "energy storage innovations"\n- "green hydrogen developments"\n- "renewable energy policy updates"\n\n**Reliable Sources to Check:**\n- **News & Analysis:** Reuters Energy, Bloomberg New Energy Finance, Greentech Media, Energy Storage News\n- **Industry Publications:** Renewable Energy World, PV Magazine, Wind Power Engineering\n- **Research Organizations:** International Energy Agency (IEA), National Renewable Energy Laboratory (NREL)\n- **Government Sources:** Department of Energy websites, EPA clean energy updates\n\n**Specific Topics to Explore:**\n- Perovskite and next-gen solar cells\n- Offshore wind expansion\n- Grid-scale battery storage\n- Green hydrogen production\n- Carbon capture technologies\n- Smart grid innovations\n- Energy policy changes and incentives...', type='text')]
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="TypeScript">
    <Steps>
      <Step title="Set your API key">
        Get your API key from the [Claude Console](https://console.anthropic.com/settings/keys) and set it as an environment variable:

        ```bash  theme={null}
        export ANTHROPIC_API_KEY='your-api-key-here'
        ```
      </Step>

      <Step title="Install the SDK">
        Install the Anthropic TypeScript SDK:

        ```bash  theme={null}
        npm install @anthropic-ai/sdk
        ```
      </Step>

      <Step title="Create your code">
        Save this as `quickstart.ts`:

        ```typescript  theme={null}
        import Anthropic from "@anthropic-ai/sdk";

        async function main() {
          const anthropic = new Anthropic();

          const msg = await anthropic.messages.create({
            model: "claude-sonnet-4-5",
            max_tokens: 1000,
            messages: [
              {
                role: "user",
                content: "What should I search for to find the latest developments in renewable energy?"
              }
            ]
          });
          console.log(msg);
        }

        main().catch(console.error);
        ```
      </Step>

      <Step title="Run your code">
        ```bash  theme={null}
        npx tsx quickstart.ts
        ```

        **Example output:**

        ```javascript  theme={null}
        {
          id: 'msg_01ThFHzad6Bh4TpQ6cHux9t8',
          type: 'message',
          role: 'assistant',
          model: 'claude-sonnet-4-5-20250929',
          content: [
            {
              type: 'text',
              text: 'Here are some effective search strategies to find the latest renewable energy developments:\n\n' +
                '## Search Terms to Use:\n' +
                '- "renewable energy news 2024"\n' +
                '- "clean energy breakthroughs"\n' +
                '- "solar wind technology advances"\n' +
                '- "energy storage innovations"\n' +
                '- "green hydrogen developments"\n' +
                '- "offshore wind projects"\n' +
                '- "battery technology renewable"\n\n' +
                '## Best Sources to Check:\n\n' +
                '**News & Industry Sites:**\n' +
                '- Renewable Energy World\n' +
                '- CleanTechnica\n' +
                '- GreenTech Media (now Wood Mackenzie)\n' +
                '- Energy Storage News\n' +
                '- PV Magazine (for solar)...'
            }
          ],
          stop_reason: 'end_turn',
          usage: {
            input_tokens: 21,
            output_tokens: 302
          }
        }
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="Java">
    <Steps>
      <Step title="Set your API key">
        Get your API key from the [Claude Console](https://console.anthropic.com/settings/keys) and set it as an environment variable:

        ```bash  theme={null}
        export ANTHROPIC_API_KEY='your-api-key-here'
        ```
      </Step>

      <Step title="Install the SDK">
        Add the Anthropic Java SDK to your project. First find the current version on [Maven Central](https://central.sonatype.com/artifact/com.anthropic/anthropic-java).

        **Gradle:**

        ```gradle  theme={null}
        implementation("com.anthropic:anthropic-java:1.0.0")
        ```

        **Maven:**

        ```xml  theme={null}
        <dependency>
          <groupId>com.anthropic</groupId>
          <artifactId>anthropic-java</artifactId>
          <version>1.0.0</version>
        </dependency>
        ```
      </Step>

      <Step title="Create your code">
        Save this as `QuickStart.java`:

        ```java  theme={null}
        import com.anthropic.client.AnthropicClient;
        import com.anthropic.client.okhttp.AnthropicOkHttpClient;
        import com.anthropic.models.messages.Message;
        import com.anthropic.models.messages.MessageCreateParams;

        public class QuickStart {
            public static void main(String[] args) {
                AnthropicClient client = AnthropicOkHttpClient.fromEnv();

                MessageCreateParams params = MessageCreateParams.builder()
                        .model("claude-sonnet-4-5-20250929")
                        .maxTokens(1000)
                        .addUserMessage("What should I search for to find the latest developments in renewable energy?")
                        .build();

                Message message = client.messages().create(params);
                System.out.println(message.content());
            }
        }
        ```
      </Step>

      <Step title="Run your code">
        ```bash  theme={null}
        javac QuickStart.java
        java QuickStart
        ```

        **Example output:**

        ```java  theme={null}
        [ContentBlock{text=TextBlock{text=Here are some effective search strategies to find the latest renewable energy developments:

        ## Search Terms to Use:
        - "renewable energy news 2024"
        - "clean energy breakthroughs"  
        - "solar/wind/battery technology advances"
        - "energy storage innovations"
        - "green hydrogen developments"
        - "renewable energy policy updates"

        ## Best Sources to Check:
        - **News & Analysis:** Reuters Energy, Bloomberg New Energy Finance, Greentech Media
        - **Industry Publications:** Renewable Energy World, PV Magazine, Wind Power Engineering
        - **Research Organizations:** International Energy Agency (IEA), National Renewable Energy Laboratory (NREL)
        - **Government Sources:** Department of Energy websites, EPA clean energy updates

        ## Specific Topics to Explore:
        - Perovskite and next-gen solar cells
        - Offshore wind expansion
        - Grid-scale battery storage
        - Green hydrogen production..., type=text}}]
        ```
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Next steps

Now that you have made your first Claude API request, it's time to explore what else is possible:

<CardGroup cols={3}>
  <Card title="Working with Messages" icon="messages" href="/en/docs/build-with-claude/working-with-messages">
    Learn common patterns for the Messages API.
  </Card>

  <Card title="Features Overview" icon="brain-circuit" href="/en/api/overview">
    Explore Claude's advanced features and capabilities.
  </Card>

  <Card title="Client SDKs" icon="code-simple" href="/en/api/client-sdks">
    Discover Anthropic client libraries.
  </Card>

  <Card title="Claude Cookbook" icon="hat-chef" href="https://github.com/anthropics/anthropic-cookbook">
    Learn with interactive Jupyter notebooks.
  </Card>
</CardGroup>


# Intro to Claude
Source: https://docs.claude.com/en/docs/intro

Claude is a highly performant, trustworthy, and intelligent AI platform built by Anthropic. Claude excels at tasks involving language, reasoning, analysis, coding, and more.

<Tip>The latest generation of Claude models:<br /><br />
**Claude Sonnet 4.5** - Our smartest model. Best for complex agents, coding, and most advanced tasks. [Learn more](https://www.anthropic.com/news/claude-sonnet-4-5).<br /><br />
**Claude Haiku 4.5** - Our fastest model with near-frontier intelligence. [Learn more](https://www.anthropic.com/news/claude-haiku-4-5).<br /><br />
**Claude Opus 4.1** - Exceptional model for specialized tasks requiring advanced reasoning. [Learn more](https://www.anthropic.com/news/claude-opus-4-1).</Tip>

<Note>
  Looking to chat with Claude? Visit [claude.ai](http://www.claude.ai)!
</Note>

## Get started

If you’re new to Claude, start here to learn the essentials and make your first API call.

<CardGroup cols={3}>
  <Card title="Get started" icon="check" href="/en/docs/get-started">
    Set up your development environment for building with Claude.
  </Card>

  <Card title="Learn about Claude" icon="head-side-gear" href="/en/docs/about-claude/models/overview">
    Learn about the family of Claude models.
  </Card>

  <Card title="Prompt Library" icon="books" href="/en/resources/prompt-library/library">
    Explore example prompts for inspiration.
  </Card>
</CardGroup>

***

## Develop with Claude

Anthropic has best-in-class developer tools to build scalable applications with Claude.

<CardGroup cols={3}>
  <Card title="Developer Console" icon="laptop" href="https://console.anthropic.com">
    Enjoy easier, more powerful prompting in your browser with the Workbench and prompt generator tool.
  </Card>

  <Card title="API Reference" icon="code" href="/en/api/overview">
    Explore, implement, and scale with the Claude API and SDKs.
  </Card>

  <Card title="Claude Cookbook" icon="hat-chef" href="https://github.com/anthropics/anthropic-cookbook">
    Learn with interactive Jupyter notebooks that demonstrate uploading PDFs, embeddings, and more.
  </Card>
</CardGroup>

***

## Key capabilities

Claude can assist with many tasks that involve text, code, and images.

<CardGroup cols={2}>
  <Card title="Text and code generation" icon="input-text" href="/en/docs/build-with-claude/text-generation">
    Summarize text, answer questions, extract data, translate text, and explain and generate code.
  </Card>

  <Card title="Vision" icon="image" href="/en/docs/build-with-claude/vision">
    Process and analyze visual input and generate text and code from images.
  </Card>
</CardGroup>

***

## Support

<CardGroup cols={2}>
  <Card title="Help Center" icon="circle-question" href="https://support.claude.com/en/">
    Find answers to frequently asked account and billing questions.
  </Card>

  <Card title="Service Status" icon="chart-line" href="https://www.claude.com/status">
    Check the status of Anthropic services.
  </Card>
</CardGroup>


# Define your success criteria
Source: https://docs.claude.com/en/docs/test-and-evaluate/define-success



Building a successful LLM-based application starts with clearly defining your success criteria. How will you know when your application is good enough to publish?

Having clear success criteria ensures that your prompt engineering & optimization efforts are focused on achieving specific, measurable goals.

***

## Building strong criteria

Good success criteria are:

* **Specific**: Clearly define what you want to achieve. Instead of "good performance," specify "accurate sentiment classification."
* **Measurable**: Use quantitative metrics or well-defined qualitative scales. Numbers provide clarity and scalability, but qualitative measures can be valuable if consistently applied *along* with quantitative measures.

  * Even "hazy" topics such as ethics and safety can be quantified:
    |      | Safety criteria                                                                            |
    | ---- | ------------------------------------------------------------------------------------------ |
    | Bad  | Safe outputs                                                                               |
    | Good | Less than 0.1% of outputs out of 10,000 trials flagged for toxicity by our content filter. |

  <Accordion title="Example metrics and measurement methods">
    **Quantitative metrics**:

    * Task-specific: F1 score, BLEU score, perplexity
    * Generic: Accuracy, precision, recall
    * Operational: Response time (ms), uptime (%)

    **Quantitative methods**:

    * A/B testing: Compare performance against a baseline model or earlier version.
    * User feedback: Implicit measures like task completion rates.
    * Edge case analysis: Percentage of edge cases handled without errors.

    **Qualitative scales**:

    * Likert scales: "Rate coherence from 1 (nonsensical) to 5 (perfectly logical)"
    * Expert rubrics: Linguists rating translation quality on defined criteria
  </Accordion>
* **Achievable**: Base your targets on industry benchmarks, prior experiments, AI research, or expert knowledge. Your success metrics should not be unrealistic to current frontier model capabilities.
* **Relevant**: Align your criteria with your application's purpose and user needs. Strong citation accuracy might be critical for medical apps but less so for casual chatbots.

<Accordion title="Example task fidelity criteria for sentiment analysis">
  |      | Criteria                                                                                                                                                                                                                               |
  | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Bad  | The model should classify sentiments well                                                                                                                                                                                              |
  | Good | Our sentiment analysis model should achieve an F1 score of at least 0.85 (Measurable, Specific) on a held-out test set\* of 10,000 diverse Twitter posts (Relevant), which is a 5% improvement over our current baseline (Achievable). |

  \**More on held-out test sets in the next section*
</Accordion>

***

## Common success criteria to consider

Here are some criteria that might be important for your use case. This list is non-exhaustive.

<AccordionGroup>
  <Accordion title="Task fidelity">
    How well does the model need to perform on the task? You may also need to consider edge case handling, such as how well the model needs to perform on rare or challenging inputs.
  </Accordion>

  <Accordion title="Consistency">
    How similar does the model's responses need to be for similar types of input? If a user asks the same question twice, how important is it that they get semantically similar answers?
  </Accordion>

  <Accordion title="Relevance and coherence">
    How well does the model directly address the user's questions or instructions? How important is it for the information to be presented in a logical, easy to follow manner?
  </Accordion>

  <Accordion title="Tone and style">
    How well does the model's output style match expectations? How appropriate is its language for the target audience?
  </Accordion>

  <Accordion title="Privacy preservation">
    What is a successful metric for how the model handles personal or sensitive information? Can it follow instructions not to use or share certain details?
  </Accordion>

  <Accordion title="Context utilization">
    How effectively does the model use provided context? How well does it reference and build upon information given in its history?
  </Accordion>

  <Accordion title="Latency">
    What is the acceptable response time for the model? This will depend on your application's real-time requirements and user expectations.
  </Accordion>

  <Accordion title="Price">
    What is your budget for running the model? Consider factors like the cost per API call, the size of the model, and the frequency of usage.
  </Accordion>
</AccordionGroup>

Most use cases will need multidimensional evaluation along several success criteria.

<Accordion title="Example multidimensional criteria for sentiment analysis">
  |      | Criteria                                                                                                                                                                                                                                                                                   |
  | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | Bad  | The model should classify sentiments well                                                                                                                                                                                                                                                  |
  | Good | On a held-out test set of 10,000 diverse Twitter posts, our sentiment analysis model should achieve:<br />- an F1 score of at least 0.85<br />- 99.5% of outputs are non-toxic<br />- 90% of errors are would cause inconvenience, not egregious error\*<br />- 95% response time \< 200ms |

  \**In reality, we would also define what "inconvenience" and "egregious" means.*
</Accordion>

***

## Next steps

<CardGroup cols={2}>
  <Card title="Brainstorm criteria" icon="link" href="https://claude.ai/">
    Brainstorm success criteria for your use case with Claude on claude.ai.<br /><br />**Tip**: Drop this page into the chat as guidance for Claude!
  </Card>

  <Card title="Design evaluations" icon="link" href="/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct">
    Learn to build strong test sets to gauge Claude's performance against your criteria.
  </Card>
</CardGroup>


# Create strong empirical evaluations
Source: https://docs.claude.com/en/docs/test-and-evaluate/develop-tests



After defining your success criteria, the next step is designing evaluations to measure LLM performance against those criteria. This is a vital part of the prompt engineering cycle.

<img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/how-to-prompt-eng.png?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=72e3d1e26bc86aab09b6652a1b456407" alt="" data-og-width="3558" width="3558" data-og-height="1182" height="1182" data-path="images/how-to-prompt-eng.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/how-to-prompt-eng.png?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=a710205481192fa01f13094bda8d7e5d 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/how-to-prompt-eng.png?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=44ea32b2d008b4fb2a0f6b972937fceb 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/how-to-prompt-eng.png?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=12607f3577a156763e4fda4137dfcc7d 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/how-to-prompt-eng.png?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=4c3dbff00bbafec3542ef04e0b781037 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/how-to-prompt-eng.png?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=80ee60f2986e703f5aad4f27115a1bea 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/how-to-prompt-eng.png?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=a9d9d0a8a42361c0644c2d527caef5dc 2500w" />

This guide focuses on how to develop your test cases.

## Building evals and test cases

### Eval design principles

1. **Be task-specific**: Design evals that mirror your real-world task distribution. Don't forget to factor in edge cases!
   <Accordion title="Example edge cases">
     * Irrelevant or nonexistent input data
     * Overly long input data or user input
     * \[Chat use cases] Poor, harmful, or irrelevant user input
     * Ambiguous test cases where even humans would find it hard to reach an assessment consensus
   </Accordion>
2. **Automate when possible**: Structure questions to allow for automated grading (e.g., multiple-choice, string match, code-graded, LLM-graded).
3. **Prioritize volume over quality**: More questions with slightly lower signal automated grading is better than fewer questions with high-quality human hand-graded evals.

### Example evals

<AccordionGroup>
  <Accordion title="Task fidelity (sentiment analysis) - exact match evaluation">
    **What it measures**: Exact match evals measure whether the model's output exactly matches a predefined correct answer. It's a simple, unambiguous metric that's perfect for tasks with clear-cut, categorical answers like sentiment analysis (positive, negative, neutral).

    **Example eval test cases**: 1000 tweets with human-labeled sentiments.

    ```python  theme={null}
    import anthropic

    tweets = [
        {"text": "This movie was a total waste of time. 👎", "sentiment": "negative"},
        {"text": "The new album is 🔥! Been on repeat all day.", "sentiment": "positive"},
        {"text": "I just love it when my flight gets delayed for 5 hours. #bestdayever", "sentiment": "negative"},  # Edge case: Sarcasm
        {"text": "The movie's plot was terrible, but the acting was phenomenal.", "sentiment": "mixed"},  # Edge case: Mixed sentiment
        # ... 996 more tweets
    ]

    client = anthropic.Anthropic()

    def get_completion(prompt: str):
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=50,
            messages=[
            {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text

    def evaluate_exact_match(model_output, correct_answer):
        return model_output.strip().lower() == correct_answer.lower()

    outputs = [get_completion(f"Classify this as 'positive', 'negative', 'neutral', or 'mixed': {tweet['text']}") for tweet in tweets]
    accuracy = sum(evaluate_exact_match(output, tweet['sentiment']) for output, tweet in zip(outputs, tweets)) / len(tweets)
    print(f"Sentiment Analysis Accuracy: {accuracy * 100}%")
    ```
  </Accordion>

  <Accordion title="Consistency (FAQ bot) - cosine similarity evaluation">
    **What it measures**: Cosine similarity measures the similarity between two vectors (in this case, sentence embeddings of the model's output using SBERT) by computing the cosine of the angle between them. Values closer to 1 indicate higher similarity. It's ideal for evaluating consistency because similar questions should yield semantically similar answers, even if the wording varies.

    **Example eval test cases**: 50 groups with a few paraphrased versions each.

    ```python  theme={null}
    from sentence_transformers import SentenceTransformer
    import numpy as np
    import anthropic

    faq_variations = [
        {"questions": ["What's your return policy?", "How can I return an item?", "Wut's yur retrn polcy?"], "answer": "Our return policy allows..."},  # Edge case: Typos
        {"questions": ["I bought something last week, and it's not really what I expected, so I was wondering if maybe I could possibly return it?", "I read online that your policy is 30 days but that seems like it might be out of date because the website was updated six months ago, so I'm wondering what exactly is your current policy?"], "answer": "Our return policy allows..."},  # Edge case: Long, rambling question
        {"questions": ["I'm Jane's cousin, and she said you guys have great customer service. Can I return this?", "Reddit told me that contacting customer service this way was the fastest way to get an answer. I hope they're right! What is the return window for a jacket?"], "answer": "Our return policy allows..."},  # Edge case: Irrelevant info
        # ... 47 more FAQs
    ]

    client = anthropic.Anthropic()

    def get_completion(prompt: str):
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=2048,
            messages=[
            {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text

    def evaluate_cosine_similarity(outputs):
        model = SentenceTransformer('all-MiniLM-L6-v2')
        embeddings = [model.encode(output) for output in outputs]

        cosine_similarities = np.dot(embeddings, embeddings.T) / (np.linalg.norm(embeddings, axis=1) * np.linalg.norm(embeddings, axis=1).T)
        return np.mean(cosine_similarities)

    for faq in faq_variations:
        outputs = [get_completion(question) for question in faq["questions"]]
        similarity_score = evaluate_cosine_similarity(outputs)
        print(f"FAQ Consistency Score: {similarity_score * 100}%")
    ```
  </Accordion>

  <Accordion title="Relevance and coherence (summarization) - ROUGE-L evaluation">
    **What it measures**: ROUGE-L (Recall-Oriented Understudy for Gisting Evaluation - Longest Common Subsequence) evaluates the quality of generated summaries. It measures the length of the longest common subsequence between the candidate and reference summaries. High ROUGE-L scores indicate that the generated summary captures key information in a coherent order.

    **Example eval test cases**: 200 articles with reference summaries.

    ```python  theme={null}
    from rouge import Rouge
    import anthropic

    articles = [
        {"text": "In a groundbreaking study, researchers at MIT...", "summary": "MIT scientists discover a new antibiotic..."},
        {"text": "Jane Doe, a local hero, made headlines last week for saving... In city hall news, the budget... Meteorologists predict...", "summary": "Community celebrates local hero Jane Doe while city grapples with budget issues."},  # Edge case: Multi-topic
        {"text": "You won't believe what this celebrity did! ... extensive charity work ...", "summary": "Celebrity's extensive charity work surprises fans"},  # Edge case: Misleading title
        # ... 197 more articles
    ]

    client = anthropic.Anthropic()

    def get_completion(prompt: str):
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=[
            {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text

    def evaluate_rouge_l(model_output, true_summary):
        rouge = Rouge()
        scores = rouge.get_scores(model_output, true_summary)
        return scores[0]['rouge-l']['f']  # ROUGE-L F1 score

    outputs = [get_completion(f"Summarize this article in 1-2 sentences:\n\n{article['text']}") for article in articles]
    relevance_scores = [evaluate_rouge_l(output, article['summary']) for output, article in zip(outputs, articles)]
    print(f"Average ROUGE-L F1 Score: {sum(relevance_scores) / len(relevance_scores)}")
    ```
  </Accordion>

  <Accordion title="Tone and style (customer service) - LLM-based Likert scale">
    **What it measures**: The LLM-based Likert scale is a psychometric scale that uses an LLM to judge subjective attitudes or perceptions. Here, it's used to rate the tone of responses on a scale from 1 to 5. It's ideal for evaluating nuanced aspects like empathy, professionalism, or patience that are difficult to quantify with traditional metrics.

    **Example eval test cases**: 100 customer inquiries with target tone (empathetic, professional, concise).

    ```python  theme={null}
    import anthropic

    inquiries = [
        {"text": "This is the third time you've messed up my order. I want a refund NOW!", "tone": "empathetic"},  # Edge case: Angry customer
        {"text": "I tried resetting my password but then my account got locked...", "tone": "patient"},  # Edge case: Complex issue
        {"text": "I can't believe how good your product is. It's ruined all others for me!", "tone": "professional"},  # Edge case: Compliment as complaint
        # ... 97 more inquiries
    ]

    client = anthropic.Anthropic()

    def get_completion(prompt: str):
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=2048,
            messages=[
            {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text

    def evaluate_likert(model_output, target_tone):
        tone_prompt = f"""Rate this customer service response on a scale of 1-5 for being {target_tone}:
        <response>{model_output}</response>
        1: Not at all {target_tone}
        5: Perfectly {target_tone}
        Output only the number."""

        # Generally best practice to use a different model to evaluate than the model used to generate the evaluated output 
        response = client.messages.create(model="claude-sonnet-4-5", max_tokens=50, messages=[{"role": "user", "content": tone_prompt}])
        return int(response.content[0].text.strip())

    outputs = [get_completion(f"Respond to this customer inquiry: {inquiry['text']}") for inquiry in inquiries]
    tone_scores = [evaluate_likert(output, inquiry['tone']) for output, inquiry in zip(outputs, inquiries)]
    print(f"Average Tone Score: {sum(tone_scores) / len(tone_scores)}")
    ```
  </Accordion>

  <Accordion title="Privacy preservation (medical chatbot) - LLM-based binary classification">
    **What it measures**: Binary classification determines if an input belongs to one of two classes. Here, it's used to classify whether a response contains PHI or not. This method can understand context and identify subtle or implicit forms of PHI that rule-based systems might miss.

    **Example eval test cases**: 500 simulated patient queries, some with PHI.

    ```python  theme={null}
    import anthropic

    patient_queries = [
        {"query": "What are the side effects of Lisinopril?", "contains_phi": False},
        {"query": "Can you tell me why John Doe, DOB 5/12/1980, was prescribed Metformin?", "contains_phi": True},  # Edge case: Explicit PHI
        {"query": "If my friend Alice, who was born on July 4, 1985, had diabetes, what...", "contains_phi": True},  # Edge case: Hypothetical PHI
        {"query": "I'm worried about my son. He's been prescribed the same medication as his father last year.", "contains_phi": True},  # Edge case: Implicit PHI
        # ... 496 more queries
    ]

    client = anthropic.Anthropic()

    def get_completion(prompt: str):
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=[
            {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text

    def evaluate_binary(model_output, query_contains_phi):
        if not query_contains_phi:
            return True

        binary_prompt = """Does this response contain or reference any Personal Health Information (PHI)?
        PHI refers to any individually identifiable health data that is created, used, or disclosed in the course of providing healthcare services. This includes information related to an individual's physical or mental health condition, the provision of healthcare to that individual, or payment for such care.
        Key aspects of PHI include:
        - Identifiers: Names, addresses, birthdates, Social Security numbers, medical record numbers, etc.
        - Health data: Diagnoses, treatment plans, test results, medication records, etc.
        - Financial information: Insurance details, payment records, etc.
        - Communication: Notes from healthcare providers, emails or messages about health.

        <response>{model_output}</response>
        Output only 'yes' or 'no'."""

        # Generally best practice to use a different model to evaluate than the model used to generate the evaluated output
        response = client.messages.create(model="claude-sonnet-4-5", max_tokens=50, messages=[{"role": "user", "content": binary_prompt}])
        return response.content[0].text.strip().lower() == "no"

    outputs = [get_completion(f"You are a medical assistant. Never reveal any PHI in your responses. PHI refers to any individually identifiable health data that is created, used, or disclosed in the course of providing healthcare services. This includes information related to an individual's physical or mental health condition, the provision of healthcare to that individual, or payment for such care. Here is the question: {query['query']}") for query in patient_queries]
    privacy_scores = [evaluate_binary(output, query['contains_phi']) for output, query in zip(outputs, patient_queries)]
    print(f"Privacy Preservation Score: {sum(privacy_scores) / len(privacy_scores) * 100}%")
    ```
  </Accordion>

  <Accordion title="Context utilization (conversation assistant) - LLM-based ordinal scale">
    **What it measures**: Similar to the Likert scale, the ordinal scale measures on a fixed, ordered scale (1-5). It's perfect for evaluating context utilization because it can capture the degree to which the model references and builds upon the conversation history, which is key for coherent, personalized interactions.

    **Example eval test cases**: 100 multi-turn conversations with context-dependent questions.

    ```python  theme={null}
    import anthropic

    conversations = [
        [
            {"role": "user", "content": "I just got a new pomeranian!"},
            {"role": "assistant", "content": "Congratulations on your new furry friend! Is this your first dog?"},
            {"role": "user", "content": "Yes, it is. I named her Luna."},
            {"role": "assistant", "content": "Luna is a lovely name! As a first-time dog owner, you might have some questions. What would you like to know about caring for Luna?"},
            ...
            {"role": "user", "content": "What should I know about caring for a dog of this specific breed?"}  # Edge case: Relies on context from much earlier
        ],
        [
            {"role": "user", "content": "I'm reading 'To Kill a Mockingbird' for my book club."},
            {"role": "assistant", "content": "Great choice! 'To Kill a Mockingbird' by Harper Lee is a classic that explores themes of racial injustice and moral growth. How are you finding it so far?"},
            {"role": "user", "content": "It's powerful. Hey, when was Scout's birthday again?"},  # Edge case: Abrupt topic shift
            {"role": "assistant", "content": "I apologize, but I don't recall the exact date of Scout's birthday being mentioned in 'To Kill a Mockingbird'. The novel doesn't focus on such specific details. Instead, it centers on Scout's growth and experiences over several years. Is there a particular part of the book or Scout's development that you're interested in discussing?"},
            {"role": "user", "content": "Oh, right. Well, can you suggest a recipe for a classic Southern cake?"}  # Edge case: Another topic shift
        ],
        # ... 98 more conversations
    ]

    client = anthropic.Anthropic()

    def get_completion(prompt: str):
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=[
            {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text

    def evaluate_ordinal(model_output, conversation):
        ordinal_prompt = f"""Rate how well this response utilizes the conversation context on a scale of 1-5:
        <conversation>
        {"".join(f"{turn['role']}: {turn['content']}\\n" for turn in conversation[:-1])}
        </conversation>
        <response>{model_output}</response>
        1: Completely ignores context
        5: Perfectly utilizes context
        Output only the number and nothing else."""

        # Generally best practice to use a different model to evaluate than the model used to generate the evaluated output
        response = client.messages.create(model="claude-sonnet-4-5", max_tokens=50, messages=[{"role": "user", "content": ordinal_prompt}])
        return int(response.content[0].text.strip())

    outputs = [get_completion(conversation) for conversation in conversations]
    context_scores = [evaluate_ordinal(output, conversation) for output, conversation in zip(outputs, conversations)]
    print(f"Average Context Utilization Score: {sum(context_scores) / len(context_scores)}")
    ```
  </Accordion>
</AccordionGroup>

<Tip>Writing hundreds of test cases can be hard to do by hand! Get Claude to help you generate more from a baseline set of example test cases.</Tip>
<Tip>If you don't know what eval methods might be useful to assess for your success criteria, you can also brainstorm with Claude!</Tip>

***

## Grading evals

When deciding which method to use to grade evals, choose the fastest, most reliable, most scalable method:

1. **Code-based grading**: Fastest and most reliable, extremely scalable, but also lacks nuance for more complex judgements that require less rule-based rigidity.
   * Exact match: `output == golden_answer`
   * String match: `key_phrase in output`

2. **Human grading**: Most flexible and high quality, but slow and expensive. Avoid if possible.

3. **LLM-based grading**: Fast and flexible, scalable and suitable for complex judgement. Test to ensure reliability first then scale.

### Tips for LLM-based grading

* **Have detailed, clear rubrics**: "The answer should always mention 'Acme Inc.' in the first sentence. If it does not, the answer is automatically graded as 'incorrect.'"
  <Note>A given use case, or even a specific success criteria for that use case, might require several rubrics for holistic evaluation.</Note>
* **Empirical or specific**: For example, instruct the LLM to output only 'correct' or 'incorrect', or to judge from a scale of 1-5. Purely qualitative evaluations are hard to assess quickly and at scale.
* **Encourage reasoning**: Ask the LLM to think first before deciding an evaluation score, and then discard the reasoning. This increases evaluation performance, particularly for tasks requiring complex judgement.

<Accordion title="Example: LLM-based grading">
  ```python  theme={null}
  import anthropic

  def build_grader_prompt(answer, rubric):
      return f"""Grade this answer based on the rubric:
      <rubric>{rubric}</rubric>
      <answer>{answer}</answer>
      Think through your reasoning in <thinking> tags, then output 'correct' or 'incorrect' in <result> tags.""

  def grade_completion(output, golden_answer):
      grader_response = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=2048,
          messages=[{"role": "user", "content": build_grader_prompt(output, golden_answer)}]
      ).content[0].text

      return "correct" if "correct" in grader_response.lower() else "incorrect"

  # Example usage
  eval_data = [
      {"question": "Is 42 the answer to life, the universe, and everything?", "golden_answer": "Yes, according to 'The Hitchhiker's Guide to the Galaxy'."},
      {"question": "What is the capital of France?", "golden_answer": "The capital of France is Paris."}
  ]

  def get_completion(prompt: str):
      message = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=1024,
          messages=[
          {"role": "user", "content": prompt}
          ]
      )
      return message.content[0].text

  outputs = [get_completion(q["question"]) for q in eval_data]
  grades = [grade_completion(output, a["golden_answer"]) for output, a in zip(outputs, eval_data)]
  print(f"Score: {grades.count('correct') / len(grades) * 100}%")
  ```
</Accordion>

## Next steps

<CardGroup cols={2}>
  <Card title="Brainstorm evaluations" icon="link" href="/en/docs/build-with-claude/prompt-engineering/overview">
    Learn how to craft prompts that maximize your eval scores.
  </Card>

  <Card title="Evals cookbook" icon="link" href="https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building%5Fevals.ipynb">
    More code examples of human-, code-, and LLM-graded evals.
  </Card>
</CardGroup>



---

**Navigation:** [← Previous](./11-prefill-claudes-response-for-greater-output-contro.md) | [Index](./index.md) | [Next →](./13-using-the-evaluation-tool.md)
