---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool runner (beta)

The tool runner provides an out-of-the-box solution for executing tools with Claude. Instead of manually handling tool calls, tool results, and conversation management, the tool runner automatically:

* Executes tools when Claude calls them
* Handles the request/response cycle
* Manages conversation state
* Provides type safety and validation

We recommend that you use the tool runner for most tool use implementations.

>   **📝 Note**
>
> The tool runner is currently in beta and only available in the [Python](https://github.com/anthropics/anthropic-sdk-python/blob/main/tools.md) and [TypeScript](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/helpers.md#tool-helpers) SDKs.

<Tabs>
  <Tab title="Python">
    ### Basic usage

    Use the `@beta_tool` decorator to define tools and `client.beta.messages.tool_runner()` to execute them.

    >   **📝 Note**
>
> If you're using the async client, replace `@beta_tool` with `@beta_async_tool` and define the function with `async def`.
```python
    import anthropic
    import json
    from anthropic import beta_tool

    # Initialize client

    client = anthropic.Anthropic()

    # Define tools using the decorator

    @beta_tool
    def get_weather(location: str, unit: str = "fahrenheit") -> str:
        """Get the current weather in a given location.

        Args:
            location: The city and state, e.g. San Francisco, CA
            unit: Temperature unit, either 'celsius' or 'fahrenheit'
        """
        # In a full implementation, you'd call a weather API here

        return json.dumps({"temperature": "20°C", "condition": "Sunny"})

    @beta_tool
    def calculate_sum(a: int, b: int) -> str:
        """Add two numbers together.

        Args:
            a: First number
            b: Second number
        """
        return str(a + b)

    # Use the tool runner

    runner = client.beta.messages.tool_runner(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        tools=[get_weather, calculate_sum],
        messages=[
            {"role": "user", "content": "What's the weather like in Paris? Also, what's 15 + 27?"}
        ]
    )
    for message in runner:
        print(message.content[0].text)
```
    The decorated function must return a content block or content block array, including text, images, or document blocks. This allows tools to return rich, multimodal responses. Returned strings will be converted to a text content block.
    If you want to return a structured JSON object to Claude, encode it to a JSON string before returning it. Numbers, booleans or other non-string primitives also must be converted to strings.

    The `@beta_tool` decorator will inspect the function arguments and the docstring to extract a json schema representation of the given function, in the example above `calculate_sum` will be turned into:
```json
    {
      "name": "calculate_sum",
      "description": "Adds two integers together.",
      "input_schema": {
        "additionalProperties": false,
        "properties": {
          "left": {
            "description": "The first integer to add.",
            "title": "Left",
            "type": "integer"
          },
          "right": {
            "description": "The second integer to add.",
            "title": "Right",
            "type": "integer"
          }
        },
        "required": ["left", "right"],
        "type": "object"
      }
    }
```
    ### Iterating over the tool runner

    The tool runner returned by `tool_runner()` is an iterable, which you can iterate over with a `for` loop. This is often referred to as a "tool call loop".
    Each loop iteration yields a message that was returned by Claude.

    After your code has a chance to process the current message inside the loop, the tool runner will check the message to see if Claude requested a tool use. If so, it will call the tool and send the tool result back to Claude automatically, then yield the next message from Claude to start the next iteration of your loop.

    You may end the loop at any iteration with a simple `break` statement. The tool runner will loop until Claude returns a message without a tool use.

    If you don't care about intermediate messages, instead of using a loop, you can call the `until_done()` method, which will return the final message from Claude:
```python
    runner = client.beta.messages.tool_runner(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        tools=[get_weather, calculate_sum],
        messages=[
            {"role": "user", "content": "What's the weather like in Paris? Also, what's 15 + 27?"}
        ]
    )
    final_message = runner.until_done()
    print(final_message.content[0].text)
```
    ### Advanced usage

    Within the loop, you have the ability to fully customize the tool runner's next request to the Messages API.
    The method `runner.generate_tool_call_response()` will call the tool (if Claude triggered a tool use) and give you access to the tool result that will be sent back to the Messages API.
    The methods `runner.set_messages_params()` and `runner.append_messages()` allow you to modify the parameters for the next Messages API request.
```python
    runner = client.beta.messages.tool_runner(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        tools=[get_weather],
        messages=[{"role": "user", "content": "What's the weather in San Francisco?"}]
    )
    for message in runner:
        # Get the tool response that will be sent

        tool_response = runner.generate_tool_call_response()

        # Customize the next request

        runner.set_messages_params(lambda params: {
            **params,
            "max_tokens": 2048  # Increase tokens for next request

        })

        # Or add additional messages

        runner.append_messages(
            {"role": "user", "content": "Please be concise in your response."}
        )
```javascript
    ### Streaming

    When enabling streaming with `stream=True`, each value emitted by the tool runner is a `BetaMessageStream` as returned from `anthropic.messages.stream()`. The `BetaMessageStream` is itself an iterable that yields streaming events from the Messages API.

    You can use `message_stream.get_final_message()` to let the SDK do the accumulation of streaming events into the final message for you.
```python
    runner = client.beta.messages.tool_runner(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        tools=[calculate_sum],
        messages=[{"role": "user", "content": "What is 15 + 27?"}],
        stream=True
    )

    # When streaming, the runner returns BetaMessageStream

    for message_stream in runner:
        for event in message_stream:
            print('event:', event)
        print('message:', message_stream.get_final_message())

    print(runner.until_done())
```
  </Tab>

  <Tab title="TypeScript (Zod)">
    ### Basic usage

    Use `betaZodTool()` for type-safe tool definitions with Zod validation (requires Zod 3.25.0 or higher).
```typescript
    import { Anthropic } from '@anthropic-ai/sdk';
    import { betaZodTool, betaTool } from '@anthropic-ai/sdk/helpers/beta/zod';
    import { z } from 'zod';

    const anthropic = new Anthropic();

    // Using betaZodTool (requires Zod 3.25.0+)
    const getWeatherTool = betaZodTool({
      name: 'get_weather',
      description: 'Get the current weather in a given location',
      inputSchema: z.object({
        location: z.string().describe('The city and state, e.g. San Francisco, CA'),
        unit: z.enum(['celsius', 'fahrenheit']).default('fahrenheit')
          .describe('Temperature unit')
      }),
      run: async (input) => {
        // In a full implementation, you'd call a weather API here
        return JSON.stringify({temperature: '20°C', condition: 'Sunny'});
      }
    });

    // Use the tool runner
    const runner = anthropic.beta.messages.toolRunner({
      model: 'claude-sonnet-4-5',
      max_tokens: 1024,
      tools: [getWeatherTool],
      messages: [
        {
          role: 'user',
          content: "What's the weather like in Paris?"
        }
      ]
    });

    // Process messages as they come in
    for await (const message of runner) {
      console.log(message.content[0].text);
    }
```
    The `run` function must return a content block or content block array, including text, images, or document blocks. This allows tools to return rich, multimodal responses. Returned strings will be converted to a text content block.
    If you want to return a structured JSON object to Claude, stringify it to a JSON string before returning it. Numbers, booleans or other non-string primitives also must be converted to strings.

    ### Iterating over the tool runner

    The tool runner returned by `toolRunner()` is an async iterable, which you can iterate over with a `for await ... of` loop. This is often referred to as a "tool call loop".
    Each loop iteration yields a messages that was returned by Claude.

    After your code had a chance to process the current message inside the loop, the tool runner will check the message to see if Claude requested a tool use. If so, it will call the tool and send the tool result back to Claude automatically, then yield the next message from Claude to start the next iteration of your loop.

    You may end the loop at any iteration with a simple `break` statement. The tool runner will loop until Claude returns a message without a tool use.

    If you don't care about intermediate messages, instead of using a loop, you may simply `await` the tool runner, which will return the final message from Claude.

    ### Advanced usage

    Within the loop, you have the ability to fully customize the tool runner's next request to the Messages API.
    The method `runner.generateToolResponse()` will call the tool (if Claude triggered a tool use) and give you access to the tool result that will be sent back to the Messages API.
    The methods `runner.setMessagesParams()` and `runner.pushMessages()` allow you to modify the parameters for the next Messages API request. The current parameters are available under `runner.params`.
```typescript
    const runner = anthropic.beta.messages.toolRunner({
      model: 'claude-sonnet-4-5',
      max_tokens: 1024,
      tools: [getWeatherTool],
      messages: [
        { role: 'user', content: "What's the weather in San Francisco?" }
      ]
    });

    for await (const message of runner) {
      // Get the tool response that will be sent
      const toolResponse = await runner.generateToolResponse();

      // Customize the next request
      runner.setMessagesParams(params => ({
        ...params,
        max_tokens: 2048  // Increase tokens for next request
      }));

      // Or add additional messages
      runner.pushMessages(
        { role: 'user', content: 'Please be concise in your response.' }
      );
    }
```javascript
    ### Streaming

    When enabling streaming with `stream: true`, each value emitted by the tool runner is a `MessageStream` as returned from `anthropic.messages.stream()`. The `MessageStream` is itself an async iterable that yields streaming events from the Messages API.

    You can use `messageStream.finalMessage()` to let the SDK do the accumulation of streaming events into the final message for you.
```typescript
    const runner = anthropic.beta.messages.toolRunner({
      model: 'claude-sonnet-4-5-20250929',
      max_tokens: 1000,
      messages: [{ role: 'user', content: 'What is the weather in San Francisco?' }],
      tools: [calculatorTool],
      stream: true,
    });

    // When streaming, the runner returns BetaMessageStream
    for await (const messageStream of runner) {
      for await (const event of messageStream) {
        console.log('event:', event);
      }
      console.log('message:', await messageStream.finalMessage());
    }

    console.log(await runner);
```
  </Tab>

  <Tab title="TypeScript (JSON Schema)">
    ### Basic usage

    Use `betaTool()` for type-safe tool definitions based on JSON schemas. TypeScript and your editor will be aware of the type of the `input` parameter for autocompletion.

    >   **📝 Note**
>
> The input generated by Claude will not be validated at runtime. Perform validation inside the `run` function if needed.
```typescript
    import { Anthropic } from '@anthropic-ai/sdk';
    import { betaZodTool, betaTool } from '@anthropic-ai/sdk/helpers/beta/json-schema';
    import { z } from 'zod';

    const anthropic = new Anthropic();

    // Using betaTool with JSON schema (no Zod required)
    const calculateSumTool = betaTool({
      name: 'calculate_sum',
      description: 'Add two numbers together',
      inputSchema: {
        type: 'object',
        properties: {
          a: { type: 'number', description: 'First number' },
          b: { type: 'number', description: 'Second number' }
        },
        required: ['a', 'b']
      },
      run: async (input) => {
        return String(input.a + input.b);
      }
    });

    // Use the tool runner
    const runner = anthropic.beta.messages.toolRunner({
      model: 'claude-sonnet-4-5',
      max_tokens: 1024,
      tools: [getWeatherTool, calculateSumTool],
      messages: [
        {
          role: 'user',
          content: "What's 15 + 27?"
        }
      ]
    });

    // Process messages as they come in
    for await (const message of runner) {
      console.log(message.content[0].text);
    }
```
    The `run` function must return any content block or content block array, including text, image, or document blocks. This allows tools to return rich, multimodal responses. Returned strings will be converted to a text content block.
    If you want to return a structured JSON object to Claude, encode it to a JSON string before returning it. Numbers, booleans or other non-string primitives also must be converted to strings.

    ### Iterating over the tool runner

    The tool runner returned by `toolRunner()` is an async iterable, which you can iterate over with a `for await ... of` loop. This is often referred to as a "tool call loop".
    Each loop iteration yields a messages that was returned by Claude.

    After your code had a chance to process the current message inside the loop, the tool runner will check the message to see if Claude requested a tool use. If so, it will call the tool and send the tool result back to Claude automatically, then yield the next message from Claude to start the next iteration of your loop.

    You may end the loop at any iteration with a simple `break` statement. The tool runner will loop until Claude returns a message without a tool use.

    If you don't care about intermediate messages, instead of using a loop, you may simply `await` the tool runner, which will return the final message from Claude.

    ### Advanced usage

    Within the loop, you have the ability to fully customize the tool runner's next request to the Messages API.
    The method `runner.generateToolResponse()` will call the tool (if Claude triggered a tool use) and give you access to the tool result that will be sent back to the Messages API.
    The methods `runner.setMessagesParams()` and `runner.pushMessages()` allow you to modify the parameters for the next Messages API request. The current parameters are available under `runner.params`.
```typescript
    const runner = anthropic.beta.messages.toolRunner({
      model: 'claude-sonnet-4-5',
      max_tokens: 1024,
      tools: [getWeatherTool],
      messages: [
        { role: 'user', content: "What's the weather in San Francisco?" }
      ]
    });

    for await (const message of runner) {
      // Get the tool response that will be sent
      const toolResponse = await runner.generateToolResponse();

      // Customize the next request
      runner.setMessagesParams(params => ({
        ...params,
        max_tokens: 2048  // Increase tokens for next request
      }));

      // Or add additional messages
      runner.pushMessages(
        { role: 'user', content: 'Please be concise in your response.' }
      );
    }
```javascript
    ### Streaming

    When enabling streaming with `stream: true`, each value emitted by the tool runner is a `MessageStream` as returned from `anthropic.messages.stream()`. The `MessageStream` is itself an async iterable that yields streaming events from the Messages API.

    You can use `messageStream.finalMessage()` to let the SDK do the accumulation of streaming events into the final message for you.
```typescript
    const runner = anthropic.beta.messages.toolRunner({
      model: 'claude-sonnet-4-5-20250929',
      max_tokens: 1000,
      messages: [{ role: 'user', content: 'What is the weather in San Francisco?' }],
      tools: [calculatorTool],
      stream: true,
    });

    // When streaming, the runner returns BetaMessageStream
    for await (const messageStream of runner) {
      for await (const event of messageStream) {
        console.log('event:', event);
      }
      console.log('message:', await messageStream.finalMessage());
    }

    console.log(await runner);
```
  </Tab>
</Tabs>

>   **📝 Note**
>
> The SDK tool runner is in beta. The rest of this document covers manual tool implementation.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
