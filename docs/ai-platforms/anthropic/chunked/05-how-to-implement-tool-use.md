**Navigation:** [← Previous](./04-get-started-with-agent-skills-in-the-api.md) | [Index](./index.md) | [Next →](./06-text-editor-tool.md)

---

# How to implement tool use
Source: https://docs.claude.com/en/docs/agents-and-tools/tool-use/implement-tool-use



## Choosing a model

We recommend using the latest Claude Sonnet (4.5) or Claude Opus (4.1) model for complex tools and ambiguous queries; they handle multiple tools better and seek clarification when needed.

Use Claude Haiku models for straightforward tools, but note they may infer missing parameters.

<Tip>
  If using Claude with tool use and extended thinking, refer to our guide [here](/en/docs/build-with-claude/extended-thinking) for more information.
</Tip>

## Specifying client tools

Client tools (both Anthropic-defined and user-defined) are specified in the `tools` top-level parameter of the API request. Each tool definition includes:

| Parameter      | Description                                                                                         |
| :------------- | :-------------------------------------------------------------------------------------------------- |
| `name`         | The name of the tool. Must match the regex `^[a-zA-Z0-9_-]{1,64}$`.                                 |
| `description`  | A detailed plaintext description of what the tool does, when it should be used, and how it behaves. |
| `input_schema` | A [JSON Schema](https://json-schema.org/) object defining the expected parameters for the tool.     |

<Accordion title="Example simple tool definition">
  ```JSON JSON theme={null}
  {
    "name": "get_weather",
    "description": "Get the current weather in a given location",
    "input_schema": {
      "type": "object",
      "properties": {
        "location": {
          "type": "string",
          "description": "The city and state, e.g. San Francisco, CA"
        },
        "unit": {
          "type": "string",
          "enum": ["celsius", "fahrenheit"],
          "description": "The unit of temperature, either 'celsius' or 'fahrenheit'"
        }
      },
      "required": ["location"]
    }
  }
  ```

  This tool, named `get_weather`, expects an input object with a required `location` string and an optional `unit` string that must be either "celsius" or "fahrenheit".
</Accordion>

### Tool use system prompt

When you call the Claude API with the `tools` parameter, we construct a special system prompt from the tool definitions, tool configuration, and any user-specified system prompt. The constructed prompt is designed to instruct the model to use the specified tool(s) and provide the necessary context for the tool to operate properly:

```
In this environment you have access to a set of tools you can use to answer the user's question.
{{ FORMATTING INSTRUCTIONS }}
String and scalar parameters should be specified as is, while lists and objects should use JSON format. Note that spaces for string values are not stripped. The output is not expected to be valid XML and is parsed with regular expressions.
Here are the functions available in JSONSchema format:
{{ TOOL DEFINITIONS IN JSON SCHEMA }}
{{ USER SYSTEM PROMPT }}
{{ TOOL CONFIGURATION }}
```

### Best practices for tool definitions

To get the best performance out of Claude when using tools, follow these guidelines:

* **Provide extremely detailed descriptions.** This is by far the most important factor in tool performance. Your descriptions should explain every detail about the tool, including:
  * What the tool does
  * When it should be used (and when it shouldn't)
  * What each parameter means and how it affects the tool's behavior
  * Any important caveats or limitations, such as what information the tool does not return if the tool name is unclear. The more context you can give Claude about your tools, the better it will be at deciding when and how to use them. Aim for at least 3-4 sentences per tool description, more if the tool is complex.
* **Prioritize descriptions over examples.** While you can include examples of how to use a tool in its description or in the accompanying prompt, this is less important than having a clear and comprehensive explanation of the tool's purpose and parameters. Only add examples after you've fully fleshed out the description.

<AccordionGroup>
  <Accordion title="Example of a good tool description">
    ```JSON JSON theme={null}
    {
      "name": "get_stock_price",
      "description": "Retrieves the current stock price for a given ticker symbol. The ticker symbol must be a valid symbol for a publicly traded company on a major US stock exchange like NYSE or NASDAQ. The tool will return the latest trade price in USD. It should be used when the user asks about the current or most recent price of a specific stock. It will not provide any other information about the stock or company.",
      "input_schema": {
        "type": "object",
        "properties": {
          "ticker": {
            "type": "string",
            "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
          }
        },
        "required": ["ticker"]
      }
    }
    ```
  </Accordion>

  <Accordion title="Example poor tool description">
    ```JSON JSON theme={null}
    {
      "name": "get_stock_price",
      "description": "Gets the stock price for a ticker.",
      "input_schema": {
        "type": "object",
        "properties": {
          "ticker": {
            "type": "string"
          }
        },
        "required": ["ticker"]
      }
    }
    ```
  </Accordion>
</AccordionGroup>

The good description clearly explains what the tool does, when to use it, what data it returns, and what the `ticker` parameter means. The poor description is too brief and leaves Claude with many open questions about the tool's behavior and usage.

## Tool runner (beta)

The tool runner provides an out-of-the-box solution for executing tools with Claude. Instead of manually handling tool calls, tool results, and conversation management, the tool runner automatically:

* Executes tools when Claude calls them
* Handles the request/response cycle
* Manages conversation state
* Provides type safety and validation

We recommend that you use the tool runner for most tool use implementations.

<Note>
  The tool runner is currently in beta and only available in the [Python](https://github.com/anthropics/anthropic-sdk-python/blob/main/tools.md) and [TypeScript](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/helpers.md#tool-helpers) SDKs.
</Note>

<Tabs>
  <Tab title="Python">
    ### Basic usage

    Use the `@beta_tool` decorator to define tools and `client.beta.messages.tool_runner()` to execute them.

    <Note>
      If you're using the async client, replace `@beta_tool` with `@beta_async_tool` and define the function with `async def`.
    </Note>

    ```python  theme={null}
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

    ```json  theme={null}
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

    ```python  theme={null}
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

    ```python  theme={null}
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
    ```

    ### Streaming

    When enabling streaming with `stream=True`, each value emitted by the tool runner is a `BetaMessageStream` as returned from `anthropic.messages.stream()`. The `BetaMessageStream` is itself an iterable that yields streaming events from the Messages API.

    You can use `message_stream.get_final_message()` to let the SDK do the accumulation of streaming events into the final message for you.

    ```python  theme={null}
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

    ```typescript  theme={null}
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

    ```typescript  theme={null}
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
    ```

    ### Streaming

    When enabling streaming with `stream: true`, each value emitted by the tool runner is a `MessageStream` as returned from `anthropic.messages.stream()`. The `MessageStream` is itself an async iterable that yields streaming events from the Messages API.

    You can use `messageStream.finalMessage()` to let the SDK do the accumulation of streaming events into the final message for you.

    ```typescript  theme={null}
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

    <Note>
      The input generated by Claude will not be validated at runtime. Perform validation inside the `run` function if needed.
    </Note>

    ```typescript  theme={null}
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

    ```typescript  theme={null}
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
    ```

    ### Streaming

    When enabling streaming with `stream: true`, each value emitted by the tool runner is a `MessageStream` as returned from `anthropic.messages.stream()`. The `MessageStream` is itself an async iterable that yields streaming events from the Messages API.

    You can use `messageStream.finalMessage()` to let the SDK do the accumulation of streaming events into the final message for you.

    ```typescript  theme={null}
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

<Note>
  The SDK tool runner is in beta. The rest of this document covers manual tool implementation.
</Note>

## Controlling Claude's output

### Forcing tool use

In some cases, you may want Claude to use a specific tool to answer the user's question, even if Claude thinks it can provide an answer without using a tool. You can do this by specifying the tool in the `tool_choice` field like so:

```
tool_choice = {"type": "tool", "name": "get_weather"}
```

When working with the tool\_choice parameter, we have four possible options:

* `auto` allows Claude to decide whether to call any provided tools or not. This is the default value when `tools` are provided.
* `any` tells Claude that it must use one of the provided tools, but doesn't force a particular tool.
* `tool` allows us to force Claude to always use a particular tool.
* `none` prevents Claude from using any tools. This is the default value when no `tools` are provided.

<Note>
  When using [prompt caching](/en/docs/build-with-claude/prompt-caching#what-invalidates-the-cache), changes to the `tool_choice` parameter will invalidate cached message blocks. Tool definitions and system prompts remain cached, but message content must be reprocessed.
</Note>

This diagram illustrates how each option works:

<Frame>
  <img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/tool_choice.png?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=fb88b9fa0da23fc231e4fece253f4406" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/tool_choice.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/tool_choice.png?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=11a4cfd7ab7815ea14c21e0948d060d4 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/tool_choice.png?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=c889c279adce34f1fa479bc722b3fe6f 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/tool_choice.png?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=e16651305d256ded74250f1c0dadb622 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/tool_choice.png?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=a99b0dd3b603051efdf9536ba9307a34 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/tool_choice.png?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=5045888f298f7261d3ae2e1466e54027 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/tool_choice.png?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=8a9c615a15610a949a2dad3aaa8113b8 2500w" />
</Frame>

Note that when you have `tool_choice` as `any` or `tool`, we will prefill the assistant message to force a tool to be used. This means that the models will not emit a natural language response or explanation before `tool_use` content blocks, even if explicitly asked to do so.

<Note>
  When using [extended thinking](/en/docs/build-with-claude/extended-thinking) with tool use, `tool_choice: {"type": "any"}` and `tool_choice: {"type": "tool", "name": "..."}` are not supported and will result in an error. Only `tool_choice: {"type": "auto"}` (the default) and `tool_choice: {"type": "none"}` are compatible with extended thinking.
</Note>

Our testing has shown that this should not reduce performance. If you would like the model to provide natural language context or explanations while still requesting that the model use a specific tool, you can use `{"type": "auto"}` for `tool_choice` (the default) and add explicit instructions in a `user` message. For example: `What's the weather like in London? Use the get_weather tool in your response.`

### JSON output

Tools do not necessarily need to be client functions — you can use tools anytime you want the model to return JSON output that follows a provided schema. For example, you might use a `record_summary` tool with a particular schema. See [Tool use with Claude](/en/docs/agents-and-tools/tool-use/overview) for a full working example.

### Model responses with tools

When using tools, Claude will often comment on what it's doing or respond naturally to the user before invoking tools.

For example, given the prompt "What's the weather like in San Francisco right now, and what time is it there?", Claude might respond with:

```JSON JSON theme={null}
{
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "I'll help you check the current weather and time in San Francisco."
    },
    {
      "type": "tool_use",
      "id": "toolu_01A09q90qw90lq917835lq9",
      "name": "get_weather",
      "input": {"location": "San Francisco, CA"}
    }
  ]
}
```

This natural response style helps users understand what Claude is doing and creates a more conversational interaction. You can guide the style and content of these responses through your system prompts and by providing `<examples>` in your prompts.

It's important to note that Claude may use various phrasings and approaches when explaining its actions. Your code should treat these responses like any other assistant-generated text, and not rely on specific formatting conventions.

### Parallel tool use

By default, Claude may use multiple tools to answer a user query. You can disable this behavior by:

* Setting `disable_parallel_tool_use=true` when tool\_choice type is `auto`, which ensures that Claude uses **at most one** tool
* Setting `disable_parallel_tool_use=true` when tool\_choice type is `any` or `tool`, which ensures that Claude uses **exactly one** tool

<AccordionGroup>
  <Accordion title="Complete parallel tool use example">
    <Note>
      **Simpler with Tool runner**: The example below shows manual parallel tool handling. For most use cases, [tool runner](#tool-runner-beta) automatically handle parallel tool execution with much less code.
    </Note>

    Here's a complete example showing how to properly format parallel tool calls in the message history:

    <CodeGroup>
      ```python Python theme={null}
      import anthropic

      client = anthropic.Anthropic()

      # Define tools
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
          },
          {
              "name": "get_time",
              "description": "Get the current time in a given timezone",
              "input_schema": {
                  "type": "object",
                  "properties": {
                      "timezone": {
                          "type": "string",
                          "description": "The timezone, e.g. America/New_York"
                      }
                  },
                  "required": ["timezone"]
              }
          }
      ]

      # Initial request
      response = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=1024,
          tools=tools,
          messages=[
              {
                  "role": "user",
                  "content": "What's the weather in SF and NYC, and what time is it there?"
              }
          ]
      )

      # Claude's response with parallel tool calls
      print("Claude wants to use tools:", response.stop_reason == "tool_use")
      print("Number of tool calls:", len([c for c in response.content if c.type == "tool_use"]))

      # Build the conversation with tool results
      messages = [
          {
              "role": "user",
              "content": "What's the weather in SF and NYC, and what time is it there?"
          },
          {
              "role": "assistant",
              "content": response.content  # Contains multiple tool_use blocks
          },
          {
              "role": "user",
              "content": [
                  {
                      "type": "tool_result",
                      "tool_use_id": "toolu_01",  # Must match the ID from tool_use
                      "content": "San Francisco: 68°F, partly cloudy"
                  },
                  {
                      "type": "tool_result",
                      "tool_use_id": "toolu_02",
                      "content": "New York: 45°F, clear skies"
                  },
                  {
                      "type": "tool_result",
                      "tool_use_id": "toolu_03",
                      "content": "San Francisco time: 2:30 PM PST"
                  },
                  {
                      "type": "tool_result",
                      "tool_use_id": "toolu_04",
                      "content": "New York time: 5:30 PM EST"
                  }
              ]
          }
      ]

      # Get final response
      final_response = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=1024,
          tools=tools,
          messages=messages
      )

      print(final_response.content[0].text)
      ```

      ```typescript TypeScript theme={null}
      import { Anthropic } from '@anthropic-ai/sdk';

      const anthropic = new Anthropic();

      // Define tools
      const tools = [
        {
          name: "get_weather",
          description: "Get the current weather in a given location",
          input_schema: {
            type: "object",
            properties: {
              location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
              }
            },
            required: ["location"]
          }
        },
        {
          name: "get_time",
          description: "Get the current time in a given timezone",
          input_schema: {
            type: "object",
            properties: {
              timezone: {
                type: "string",
                description: "The timezone, e.g. America/New_York"
              }
            },
            required: ["timezone"]
          }
        }
      ];

      // Initial request
      const response = await anthropic.messages.create({
        model: "claude-sonnet-4-5",
        max_tokens: 1024,
        tools: tools,
        messages: [
          {
            role: "user",
            content: "What's the weather in SF and NYC, and what time is it there?"
          }
        ]
      });

      // Build conversation with tool results
      const messages = [
        {
          role: "user",
          content: "What's the weather in SF and NYC, and what time is it there?"
        },
        {
          role: "assistant",
          content: response.content  // Contains multiple tool_use blocks
        },
        {
          role: "user",
          content: [
            {
              type: "tool_result",
              tool_use_id: "toolu_01",  // Must match the ID from tool_use
              content: "San Francisco: 68°F, partly cloudy"
            },
            {
              type: "tool_result",
              tool_use_id: "toolu_02",
              content: "New York: 45°F, clear skies"
            },
            {
              type: "tool_result",
              tool_use_id: "toolu_03",
              content: "San Francisco time: 2:30 PM PST"
            },
            {
              type: "tool_result",
              tool_use_id: "toolu_04",
              content: "New York time: 5:30 PM EST"
            }
          ]
        }
      ];

      // Get final response
      const finalResponse = await anthropic.messages.create({
        model: "claude-sonnet-4-5",
        max_tokens: 1024,
        tools: tools,
        messages: messages
      });

      console.log(finalResponse.content[0].text);
      ```
    </CodeGroup>

    The assistant message with parallel tool calls would look like this:

    ```json  theme={null}
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "I'll check the weather and time for both San Francisco and New York City."
        },
        {
          "type": "tool_use",
          "id": "toolu_01",
          "name": "get_weather",
          "input": {"location": "San Francisco, CA"}
        },
        {
          "type": "tool_use",
          "id": "toolu_02",
          "name": "get_weather",
          "input": {"location": "New York, NY"}
        },
        {
          "type": "tool_use",
          "id": "toolu_03",
          "name": "get_time",
          "input": {"timezone": "America/Los_Angeles"}
        },
        {
          "type": "tool_use",
          "id": "toolu_04",
          "name": "get_time",
          "input": {"timezone": "America/New_York"}
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Complete test script for parallel tools">
    Here's a complete, runnable script to test and verify parallel tool calls are working correctly:

    <CodeGroup>
      ```python Python theme={null}
      #!/usr/bin/env python3
      """Test script to verify parallel tool calls with the Claude API"""

      import os
      from anthropic import Anthropic

      # Initialize client
      client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

      # Define tools
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
          },
          {
              "name": "get_time",
              "description": "Get the current time in a given timezone",
              "input_schema": {
                  "type": "object",
                  "properties": {
                      "timezone": {
                          "type": "string",
                          "description": "The timezone, e.g. America/New_York"
                      }
                  },
                  "required": ["timezone"]
              }
          }
      ]

      # Test conversation with parallel tool calls
      messages = [
          {
              "role": "user",
              "content": "What's the weather in SF and NYC, and what time is it there?"
          }
      ]

      # Make initial request
      print("Requesting parallel tool calls...")
      response = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=1024,
          messages=messages,
          tools=tools
      )

      # Check for parallel tool calls
      tool_uses = [block for block in response.content if block.type == "tool_use"]
      print(f"\n✓ Claude made {len(tool_uses)} tool calls")

      if len(tool_uses) > 1:
          print("✓ Parallel tool calls detected!")
          for tool in tool_uses:
              print(f"  - {tool.name}: {tool.input}")
      else:
          print("✗ No parallel tool calls detected")

      # Simulate tool execution and format results correctly
      tool_results = []
      for tool_use in tool_uses:
          if tool_use.name == "get_weather":
              if "San Francisco" in str(tool_use.input):
                  result = "San Francisco: 68°F, partly cloudy"
              else:
                  result = "New York: 45°F, clear skies"
          else:  # get_time
              if "Los_Angeles" in str(tool_use.input):
                  result = "2:30 PM PST"
              else:
                  result = "5:30 PM EST"

          tool_results.append({
              "type": "tool_result",
              "tool_use_id": tool_use.id,
              "content": result
          })

      # Continue conversation with tool results
      messages.extend([
          {"role": "assistant", "content": response.content},
          {"role": "user", "content": tool_results}  # All results in one message!
      ])

      # Get final response
      print("\nGetting final response...")
      final_response = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=1024,
          messages=messages,
          tools=tools
      )

      print(f"\nClaude's response:\n{final_response.content[0].text}")

      # Verify formatting
      print("\n--- Verification ---")
      print(f"✓ Tool results sent in single user message: {len(tool_results)} results")
      print("✓ No text before tool results in content array")
      print("✓ Conversation formatted correctly for future parallel tool use")
      ```

      ```typescript TypeScript theme={null}
      #!/usr/bin/env node
      // Test script to verify parallel tool calls with the Claude API

      import { Anthropic } from '@anthropic-ai/sdk';

      const anthropic = new Anthropic({
        apiKey: process.env.ANTHROPIC_API_KEY
      });

      // Define tools
      const tools = [
        {
          name: "get_weather",
          description: "Get the current weather in a given location",
          input_schema: {
            type: "object",
            properties: {
              location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
              }
            },
            required: ["location"]
          }
        },
        {
          name: "get_time",
          description: "Get the current time in a given timezone",
          input_schema: {
            type: "object",
            properties: {
              timezone: {
                type: "string",
                description: "The timezone, e.g. America/New_York"
              }
            },
            required: ["timezone"]
          }
        }
      ];

      async function testParallelTools() {
        // Make initial request
        console.log("Requesting parallel tool calls...");
        const response = await anthropic.messages.create({
          model: "claude-sonnet-4-5",
          max_tokens: 1024,
          messages: [{
            role: "user",
            content: "What's the weather in SF and NYC, and what time is it there?"
          }],
          tools: tools
        });

        // Check for parallel tool calls
        const toolUses = response.content.filter(block => block.type === "tool_use");
        console.log(`\n✓ Claude made ${toolUses.length} tool calls`);

        if (toolUses.length > 1) {
          console.log("✓ Parallel tool calls detected!");
          toolUses.forEach(tool => {
            console.log(`  - ${tool.name}: ${JSON.stringify(tool.input)}`);
          });
        } else {
          console.log("✗ No parallel tool calls detected");
        }

        // Simulate tool execution and format results correctly
        const toolResults = toolUses.map(toolUse => {
          let result;
          if (toolUse.name === "get_weather") {
            result = toolUse.input.location.includes("San Francisco")
              ? "San Francisco: 68°F, partly cloudy"
              : "New York: 45°F, clear skies";
          } else {
            result = toolUse.input.timezone.includes("Los_Angeles")
              ? "2:30 PM PST"
              : "5:30 PM EST";
          }

          return {
            type: "tool_result",
            tool_use_id: toolUse.id,
            content: result
          };
        });

        // Get final response with correct formatting
        console.log("\nGetting final response...");
        const finalResponse = await anthropic.messages.create({
          model: "claude-sonnet-4-5",
          max_tokens: 1024,
          messages: [
            { role: "user", content: "What's the weather in SF and NYC, and what time is it there?" },
            { role: "assistant", content: response.content },
            { role: "user", content: toolResults }  // All results in one message!
          ],
          tools: tools
        });

        console.log(`\nClaude's response:\n${finalResponse.content[0].text}`);

        // Verify formatting
        console.log("\n--- Verification ---");
        console.log(`✓ Tool results sent in single user message: ${toolResults.length} results`);
        console.log("✓ No text before tool results in content array");
        console.log("✓ Conversation formatted correctly for future parallel tool use");
      }

      testParallelTools().catch(console.error);
      ```
    </CodeGroup>

    This script demonstrates:

    * How to properly format parallel tool calls and results
    * How to verify that parallel calls are being made
    * The correct message structure that encourages future parallel tool use
    * Common mistakes to avoid (like text before tool results)

    Run this script to test your implementation and ensure Claude is making parallel tool calls effectively.
  </Accordion>
</AccordionGroup>

#### Maximizing parallel tool use

While Claude 4 models have excellent parallel tool use capabilities by default, you can increase the likelihood of parallel tool execution across all models with targeted prompting:

<AccordionGroup>
  <Accordion title="System prompts for parallel tool use">
    For Claude 4 models (Opus 4.1, Opus 4, and Sonnet 4), add this to your system prompt:

    ```text  theme={null}
    For maximum efficiency, whenever you need to perform multiple independent operations, invoke all relevant tools simultaneously rather than sequentially.
    ```

    For even stronger parallel tool use (recommended if the default isn't sufficient), use:

    ```text  theme={null}
    <use_parallel_tool_calls>
    For maximum efficiency, whenever you perform multiple independent operations, invoke all relevant tools simultaneously rather than sequentially. Prioritize calling tools in parallel whenever possible. For example, when reading 3 files, run 3 tool calls in parallel to read all 3 files into context at the same time. When running multiple read-only commands like `ls` or `list_dir`, always run all of the commands in parallel. Err on the side of maximizing parallel tool calls rather than running too many tools sequentially.
    </use_parallel_tool_calls>
    ```
  </Accordion>

  <Accordion title="User message prompting">
    You can also encourage parallel tool use within specific user messages:

    ```python  theme={null}
    # Instead of:
    "What's the weather in Paris? Also check London."

    # Use:
    "Check the weather in Paris and London simultaneously."

    # Or be explicit:
    "Please use parallel tool calls to get the weather for Paris, London, and Tokyo at the same time."
    ```
  </Accordion>
</AccordionGroup>

<Warning>
  **Parallel tool use with Claude Sonnet 3.7**

  Claude Sonnet 3.7 may be less likely to make make parallel tool calls in a response, even when you have not set `disable_parallel_tool_use`. To work around this, we recommend enabling [token-efficient tool use](/en/docs/agents-and-tools/tool-use/token-efficient-tool-use), which helps encourage Claude to use parallel tools. This beta feature also reduces latency and saves an average of 14% in output tokens.

  If you prefer not to opt into the token-efficient tool use beta, you can also introduce a "batch tool" that can act as a meta-tool to wrap invocations to other tools simultaneously. We find that if this tool is present, the model will use it to simultaneously call multiple tools in parallel for you.

  See [this example](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/parallel_tools_claude_3_7_sonnet.ipynb) in our cookbook for how to use this workaround.
</Warning>

## Handling tool use and tool result content blocks

<Note>
  **Simpler with Tool runner**: The manual tool handling described in this section is automatically managed by [tool runner](#tool-runner-beta). Use this section when you need custom control over tool execution.
</Note>

Claude's response differs based on whether it uses a client or server tool.

### Handling results from client tools

The response will have a `stop_reason` of `tool_use` and one or more `tool_use` content blocks that include:

* `id`: A unique identifier for this particular tool use block. This will be used to match up the tool results later.
* `name`: The name of the tool being used.
* `input`: An object containing the input being passed to the tool, conforming to the tool's `input_schema`.

<Accordion title="Example API response with a `tool_use` content block">
  ```JSON JSON theme={null}
  {
    "id": "msg_01Aq9w938a90dw8q",
    "model": "claude-sonnet-4-5",
    "stop_reason": "tool_use",
    "role": "assistant",
    "content": [
      {
        "type": "text",
        "text": "I'll check the current weather in San Francisco for you."
      },
      {
        "type": "tool_use",
        "id": "toolu_01A09q90qw90lq917835lq9",
        "name": "get_weather",
        "input": {"location": "San Francisco, CA", "unit": "celsius"}
      }
    ]
  }
  ```
</Accordion>

When you receive a tool use response for a client tool, you should:

1. Extract the `name`, `id`, and `input` from the `tool_use` block.
2. Run the actual tool in your codebase corresponding to that tool name, passing in the tool `input`.
3. Continue the conversation by sending a new message with the `role` of `user`, and a `content` block containing the `tool_result` type and the following information:
   * `tool_use_id`: The `id` of the tool use request this is a result for.
   * `content`: The result of the tool, as a string (e.g. `"content": "15 degrees"`), a list of nested content blocks (e.g. `"content": [{"type": "text", "text": "15 degrees"}]`), or a list of document blocks (e.g. `"content": ["type": "document", "source": {"type": "text", "media_type": "text/plain", "data": "15 degrees"}]`). These content blocks can use the `text`, `image`, or `document` types.
   * `is_error` (optional): Set to `true` if the tool execution resulted in an error.

<Note>
  **Important formatting requirements**:

  * Tool result blocks must immediately follow their corresponding tool use blocks in the message history. You cannot include any messages between the assistant's tool use message and the user's tool result message.
  * In the user message containing tool results, the tool\_result blocks must come FIRST in the content array. Any text must come AFTER all tool results.

  For example, this will cause a 400 error:

  ```json  theme={null}
  {"role": "user", "content": [
    {"type": "text", "text": "Here are the results:"},  // ❌ Text before tool_result
    {"type": "tool_result", "tool_use_id": "toolu_01", ...}
  ]}
  ```

  This is correct:

  ```json  theme={null}
  {"role": "user", "content": [
    {"type": "tool_result", "tool_use_id": "toolu_01", ...},
    {"type": "text", "text": "What should I do next?"}  // ✅ Text after tool_result
  ]}
  ```

  If you receive an error like "tool\_use ids were found without tool\_result blocks immediately after", check that your tool results are formatted correctly.
</Note>

<AccordionGroup>
  <Accordion title="Example of successful tool result">
    ```JSON JSON theme={null}
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "15 degrees"
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Example of tool result with images">
    ```JSON JSON theme={null}
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": [
            {"type": "text", "text": "15 degrees"},
            {
              "type": "image",
              "source": {
                "type": "base64",
                "media_type": "image/jpeg",
                "data": "/9j/4AAQSkZJRg...",
              }
            }
          ]
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Example of empty tool result">
    ```JSON JSON theme={null}
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Example of tool result with documents">
    ```JSON JSON theme={null}
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": [
            {"type": "text", "text": "The weather is"},
            {
              "type": "document",
              "source": {
                "type": "text",
                "media_type": "text/plain",
                "data": "15 degrees"
              }
            }
          ]
        }
      ]
    }
    ```
  </Accordion>
</AccordionGroup>

After receiving the tool result, Claude will use that information to continue generating a response to the original user prompt.

### Handling results from server tools

Claude executes the tool internally and incorporates the results directly into its response without requiring additional user interaction.

<Tip>
  **Differences from other APIs**

  Unlike APIs that separate tool use or use special roles like `tool` or `function`, the Claude API integrates tools directly into the `user` and `assistant` message structure.

  Messages contain arrays of `text`, `image`, `tool_use`, and `tool_result` blocks. `user` messages include client content and `tool_result`, while `assistant` messages contain AI-generated content and `tool_use`.
</Tip>

### Handling the `max_tokens` stop reason

If Claude's [response is cut off due to hitting the `max_tokens` limit](/en/docs/build-with-claude/handling-stop-reasons#max-tokens), and the truncated response contains an incomplete tool use block, you'll need to retry the request with a higher `max_tokens` value to get the full tool use.

<CodeGroup>
  ```python Python theme={null}
  # Check if response was truncated during tool use
  if response.stop_reason == "max_tokens":
      # Check if the last content block is an incomplete tool_use
      last_block = response.content[-1]
      if last_block.type == "tool_use":
          # Send the request with higher max_tokens
          response = client.messages.create(
              model="claude-sonnet-4-5",
              max_tokens=4096,  # Increased limit
              messages=messages,
              tools=tools
          )
  ```

  ```typescript TypeScript theme={null}
  // Check if response was truncated during tool use
  if (response.stop_reason === "max_tokens") {
    // Check if the last content block is an incomplete tool_use
    const lastBlock = response.content[response.content.length - 1];
    if (lastBlock.type === "tool_use") {
      // Send the request with higher max_tokens
      response = await anthropic.messages.create({
        model: "claude-sonnet-4-5",
        max_tokens: 4096, // Increased limit
        messages: messages,
        tools: tools
      });
    }
  }
  ```
</CodeGroup>

#### Handling the `pause_turn` stop reason

When using server tools like web search, the API may return a `pause_turn` stop reason, indicating that the API has paused a long-running turn.

Here's how to handle the `pause_turn` stop reason:

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  # Initial request with web search
  response = client.messages.create(
      model="claude-3-7-sonnet-latest",
      max_tokens=1024,
      messages=[
          {
              "role": "user",
              "content": "Search for comprehensive information about quantum computing breakthroughs in 2025"
          }
      ],
      tools=[{
          "type": "web_search_20250305",
          "name": "web_search",
          "max_uses": 10
      }]
  )

  # Check if the response has pause_turn stop reason
  if response.stop_reason == "pause_turn":
      # Continue the conversation with the paused content
      messages = [
          {"role": "user", "content": "Search for comprehensive information about quantum computing breakthroughs in 2025"},
          {"role": "assistant", "content": response.content}
      ]

      # Send the continuation request
      continuation = client.messages.create(
          model="claude-3-7-sonnet-latest",
          max_tokens=1024,
          messages=messages,
          tools=[{
              "type": "web_search_20250305",
              "name": "web_search",
              "max_uses": 10
          }]
      )

      print(continuation)
  else:
      print(response)
  ```

  ```typescript TypeScript theme={null}
  import { Anthropic } from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  // Initial request with web search
  const response = await anthropic.messages.create({
    model: "claude-3-7-sonnet-latest",
    max_tokens: 1024,
    messages: [
      {
        role: "user",
        content: "Search for comprehensive information about quantum computing breakthroughs in 2025"
      }
    ],
    tools: [{
      type: "web_search_20250305",
      name: "web_search",
      max_uses: 10
    }]
  });

  // Check if the response has pause_turn stop reason
  if (response.stop_reason === "pause_turn") {
    // Continue the conversation with the paused content
    const messages = [
      { role: "user", content: "Search for comprehensive information about quantum computing breakthroughs in 2025" },
      { role: "assistant", content: response.content }
    ];

    // Send the continuation request
    const continuation = await anthropic.messages.create({
      model: "claude-3-7-sonnet-latest",
      max_tokens: 1024,
      messages: messages,
      tools: [{
        type: "web_search_20250305",
        name: "web_search",
        max_uses: 10
      }]
    });

    console.log(continuation);
  } else {
    console.log(response);
  }
  ```
</CodeGroup>

When handling `pause_turn`:

* **Continue the conversation**: Pass the paused response back as-is in a subsequent request to let Claude continue its turn
* **Modify if needed**: You can optionally modify the content before continuing if you want to interrupt or redirect the conversation
* **Preserve tool state**: Include the same tools in the continuation request to maintain functionality

## Troubleshooting errors

<Note>
  **Built-in Error Handling**: [Tool runner](#tool-runner-beta) provide automatic error handling for most common scenarios. This section covers manual error handling for advanced use cases.
</Note>

There are a few different types of errors that can occur when using tools with Claude:

<AccordionGroup>
  <Accordion title="Tool execution error">
    If the tool itself throws an error during execution (e.g. a network error when fetching weather data), you can return the error message in the `content` along with `"is_error": true`:

    ```JSON JSON theme={null}
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "ConnectionError: the weather service API is not available (HTTP 500)",
          "is_error": true
        }
      ]
    }
    ```

    Claude will then incorporate this error into its response to the user, e.g. "I'm sorry, I was unable to retrieve the current weather because the weather service API is not available. Please try again later."
  </Accordion>

  <Accordion title="Invalid tool name">
    If Claude's attempted use of a tool is invalid (e.g. missing required parameters), it usually means that the there wasn't enough information for Claude to use the tool correctly. Your best bet during development is to try the request again with more-detailed `description` values in your tool definitions.

    However, you can also continue the conversation forward with a `tool_result` that indicates the error, and Claude will try to use the tool again with the missing information filled in:

    ```JSON JSON theme={null}
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Missing required 'location' parameter",
          "is_error": true
        }
      ]
    }
    ```

    If a tool request is invalid or missing parameters, Claude will retry 2-3 times with corrections before apologizing to the user.
  </Accordion>

  <Accordion title="<search_quality_reflection> tags">
    To prevent Claude from reflecting on search quality with \<search\_quality\_reflection> tags, add "Do not reflect on the quality of the returned search results in your response" to your prompt.
  </Accordion>

  <Accordion title="Server tool errors">
    When server tools encounter errors (e.g., network issues with Web Search), Claude will transparently handle these errors and attempt to provide an alternative response or explanation to the user. Unlike client tools, you do not need to handle `is_error` results for server tools.

    For web search specifically, possible error codes include:

    * `too_many_requests`: Rate limit exceeded
    * `invalid_input`: Invalid search query parameter
    * `max_uses_exceeded`: Maximum web search tool uses exceeded
    * `query_too_long`: Query exceeds maximum length
    * `unavailable`: An internal error occurred
  </Accordion>

  <Accordion title="Parallel tool calls not working">
    If Claude isn't making parallel tool calls when expected, check these common issues:

    **1. Incorrect tool result formatting**

    The most common issue is formatting tool results incorrectly in the conversation history. This "teaches" Claude to avoid parallel calls.

    Specifically for parallel tool use:

    * ❌ **Wrong**: Sending separate user messages for each tool result
    * ✅ **Correct**: All tool results must be in a single user message

    ```json  theme={null}
    // ❌ This reduces parallel tool use
    [
      {"role": "assistant", "content": [tool_use_1, tool_use_2]},
      {"role": "user", "content": [tool_result_1]},
      {"role": "user", "content": [tool_result_2]}  // Separate message
    ]

    // ✅ This maintains parallel tool use
    [
      {"role": "assistant", "content": [tool_use_1, tool_use_2]},
      {"role": "user", "content": [tool_result_1, tool_result_2]}  // Single message
    ]
    ```

    See the [general formatting requirements above](#handling-tool-use-and-tool-result-content-blocks) for other formatting rules.

    **2. Weak prompting**

    Default prompting may not be sufficient. Use stronger language:

    ```text  theme={null}
    <use_parallel_tool_calls>
    For maximum efficiency, whenever you perform multiple independent operations,
    invoke all relevant tools simultaneously rather than sequentially.
    Prioritize calling tools in parallel whenever possible.
    </use_parallel_tool_calls>
    ```

    **3. Measuring parallel tool usage**

    To verify parallel tool calls are working:

    ```python  theme={null}
    # Calculate average tools per tool-calling message
    tool_call_messages = [msg for msg in messages if any(
        block.type == "tool_use" for block in msg.content
    )]
    total_tool_calls = sum(
        len([b for b in msg.content if b.type == "tool_use"])
        for msg in tool_call_messages
    )
    avg_tools_per_message = total_tool_calls / len(tool_call_messages)
    print(f"Average tools per message: {avg_tools_per_message}")
    # Should be > 1.0 if parallel calls are working
    ```

    **4. Model-specific behavior**

    * Claude Opus 4.1, Opus 4, and Sonnet 4: Excel at parallel tool use with minimal prompting
    * Claude Sonnet 3.7: May need stronger prompting or [token-efficient tool use](/en/docs/agents-and-tools/tool-use/token-efficient-tool-use)
    * Claude Haiku: Less likely to use parallel tools without explicit prompting
  </Accordion>
</AccordionGroup>


# Memory tool
Source: https://docs.claude.com/en/docs/agents-and-tools/tool-use/memory-tool



The memory tool enables Claude to store and retrieve information across conversations through a memory file directory. Claude can create, read, update, and delete files that persist between sessions, allowing it to build knowledge over time without keeping everything in the context window.

The memory tool operates client-side—you control where and how the data is stored through your own infrastructure.

<Note>
  The memory tool is currently in beta. To enable it, use the beta header `context-management-2025-06-27` in your API requests.

  Please reach out through our [feedback form](https://forms.gle/YXC2EKGMhjN1c4L88) to share your feedback on this feature.
</Note>

## Use cases

* Maintain project context across multiple agent executions
* Learn from past interactions, decisions, and feedback
* Build knowledge bases over time
* Enable cross-conversation learning where Claude improves at recurring workflows

## How it works

When enabled, Claude automatically checks its memory directory before starting tasks. Claude can create, read, update, and delete files in the `/memories` directory to store what it learns while working, then reference those memories in future conversations to handle similar tasks more effectively or pick up where it left off.

Since this is a client-side tool, Claude makes tool calls to perform memory operations, and your application executes those operations locally. This gives you complete control over where and how the memory is stored. For security, you should restrict all memory operations to the `/memories` directory.

### Example: How memory tool calls work

When you ask Claude to help with a task, Claude automatically checks its memory directory first. Here's what a typical interaction looks like:

**1. User request:**

```
"Help me respond to this customer service ticket."
```

**2. Claude checks the memory directory:**

```
"I'll help you respond to the customer service ticket. Let me check my memory for any previous context."
```

Claude calls the memory tool:

```json  theme={null}
{
  "type": "tool_use",
  "id": "toolu_01C4D5E6F7G8H9I0J1K2L3M4",
  "name": "memory",
  "input": {
    "command": "view",
    "path": "/memories"
  }
}
```

**3. Your application returns the directory contents:**

```json  theme={null}
{
  "type": "tool_result",
  "tool_use_id": "toolu_01C4D5E6F7G8H9I0J1K2L3M4",
  "content": "Directory: /memories\n- customer_service_guidelines.xml\n- refund_policies.xml"
}
```

**4. Claude reads relevant files:**

```json  theme={null}
{
  "type": "tool_use",
  "id": "toolu_01D5E6F7G8H9I0J1K2L3M4N5",
  "name": "memory",
  "input": {
    "command": "view",
    "path": "/memories/customer_service_guidelines.xml"
  }
}
```

**5. Your application returns the file contents:**

```json  theme={null}
{
  "type": "tool_result",
  "tool_use_id": "toolu_01D5E6F7G8H9I0J1K2L3M4N5",
  "content": "<guidelines>\n<addressing_customers>\n- Always address customers by their first name\n- Use empathetic language\n..."
}
```

**6. Claude uses the memory to help:**

```
"Based on your customer service guidelines, I can help you craft a response. Please share the ticket details..."
```

## Supported models

The memory tool is available on:

* Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`)
* Claude Sonnet 4 (`claude-sonnet-4-20250514`)
* Claude Haiku 4.5 (`claude-haiku-4-5-20251001`)
* Claude Opus 4.1 (`claude-opus-4-1-20250805`)
* Claude Opus 4 (`claude-opus-4-20250514`)

## Getting started

To use the memory tool:

1. Include the beta header `context-management-2025-06-27` in your API requests
2. Add the memory tool to your request
3. Implement client-side handlers for memory operations

<Note>
  To handle memory tool operations in your application, you need to implement handlers for each memory command. Our SDKs provide memory tool helpers that handle the tool interface—you can subclass `BetaAbstractMemoryTool` (Python) or use `betaMemoryTool` (TypeScript) to implement your own memory backend (file-based, database, cloud storage, encrypted files, etc.).

  For working examples, see:

  * Python: [examples/memory/basic.py](https://github.com/anthropics/anthropic-sdk-python/blob/main/examples/memory/basic.py)
  * TypeScript: [examples/tools-helpers-memory.ts](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/examples/tools-helpers-memory.ts)
</Note>

## Basic usage

<CodeGroup>
  ````bash cURL theme={null}
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "anthropic-beta: context-management-2025-06-27" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 2048,
          "messages": [
              {
                  "role": "user",
                  "content": "I'\''m working on a Python web scraper that keeps crashing with a timeout error. Here'\''s the problematic function:\n\n```python\ndef fetch_page(url, retries=3):\n    for i in range(retries):\n        try:\n            response = requests.get(url, timeout=5)\n            return response.text\n        except requests.exceptions.Timeout:\n            if i == retries - 1:\n                raise\n            time.sleep(1)\n```\n\nPlease help me debug this."
              }
          ],
          "tools": [{
              "type": "memory_20250818",
              "name": "memory"
          }]
      }'
  ````

  ````python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  message = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=2048,
      messages=[
          {
              "role": "user",
              "content": "I'm working on a Python web scraper that keeps crashing with a timeout error. Here's the problematic function:\n\n```python\ndef fetch_page(url, retries=3):\n    for i in range(retries):\n        try:\n            response = requests.get(url, timeout=5)\n            return response.text\n        except requests.exceptions.Timeout:\n            if i == retries - 1:\n                raise\n            time.sleep(1)\n```\n\nPlease help me debug this."
          }
      ],
      tools=[{
          "type": "memory_20250818",
          "name": "memory"
      }],
      betas=["context-management-2025-06-27"]
  )
  ````

  ````typescript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  const message = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 2048,
    messages: [
      {
        role: "user",
        content: "I'm working on a Python web scraper that keeps crashing with a timeout error. Here's the problematic function:\n\n```python\ndef fetch_page(url, retries=3):\n    for i in range(retries):\n        try:\n            response = requests.get(url, timeout=5)\n            return response.text\n        except requests.exceptions.Timeout:\n            if i == retries - 1:\n                raise\n            time.sleep(1)\n```\n\nPlease help me debug this."
      }
    ],
    tools: [{
      type: "memory_20250818",
      name: "memory"
    }],
    betas: ["context-management-2025-06-27"]
  });
  ````
</CodeGroup>

## Tool commands

Your client-side implementation needs to handle these memory tool commands:

### view

Shows directory contents or file contents with optional line ranges:

```json  theme={null}
{
  "command": "view",
  "path": "/memories",
  "view_range": [1, 10]  // Optional: view specific lines
}
```

### create

Create or overwrite a file:

```json  theme={null}
{
  "command": "create",
  "path": "/memories/notes.txt",
  "file_text": "Meeting notes:\n- Discussed project timeline\n- Next steps defined\n"
}
```

### str\_replace

Replace text in a file:

```json  theme={null}
{
  "command": "str_replace",
  "path": "/memories/preferences.txt",
  "old_str": "Favorite color: blue",
  "new_str": "Favorite color: green"
}
```

### insert

Insert text at a specific line:

```json  theme={null}
{
  "command": "insert",
  "path": "/memories/todo.txt",
  "insert_line": 2,
  "insert_text": "- Review memory tool documentation\n"
}
```

### delete

Delete a file or directory:

```json  theme={null}
{
  "command": "delete",
  "path": "/memories/old_file.txt"
}
```

### rename

Rename or move a file/directory:

```json  theme={null}
{
  "command": "rename",
  "old_path": "/memories/draft.txt",
  "new_path": "/memories/final.txt"
}
```

## Prompting guidance

We automatically include this instruction to the system prompt when the memory tool is included:

```
IMPORTANT: ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE.
MEMORY PROTOCOL:
1. Use the `view` command of your `memory` tool to check for earlier progress.
2. ... (work on the task) ...
     - As you make progress, record status / progress / thoughts etc in your memory.
ASSUME INTERRUPTION: Your context window might be reset at any moment, so you risk losing any progress that is not recorded in your memory directory.
```

If you observe Claude creating cluttered memory files, you can include this instruction:

> Note: when editing your memory folder, always try to keep its content up-to-date, coherent and organized. You can rename or delete files that are no longer relevant. Do not create new files unless necessary.

You can also guide what Claude writes to memory, e.g., "Only write down information relevant to \<topic> in your memory system."

## Security considerations

Here are important security concerns when implementing your memory store:

### Sensitive information

Claude will usually refuse to write down sensitive information in memory files. However, you may want to implement stricter validation that strips out potentially sensitive information.

### File storage size

Consider tracking memory file sizes and preventing files from growing too large. Consider adding a maximum number of characters the memory read command can return, and let Claude paginate through contents.

### Memory expiration

Consider clearing out memory files periodically that haven't been accessed in an extended time.

### Path traversal protection

<Warning>
  Malicious path inputs could attempt to access files outside the `/memories` directory. Your implementation **MUST** validate all paths to prevent directory traversal attacks.
</Warning>

Consider these safeguards:

* Validate that all paths start with `/memories`
* Resolve paths to their canonical form and verify they remain within the memory directory
* Reject paths containing sequences like `../`, `..\\`, or other traversal patterns
* Watch for URL-encoded traversal sequences (`%2e%2e%2f`)
* Use your language's built-in path security utilities (e.g., Python's `pathlib.Path.resolve()` and `relative_to()`)

## Error handling

The memory tool uses the same error handling patterns as the [text editor tool](/en/docs/agents-and-tools/tool-use/text-editor-tool#handle-errors). Common errors include file not found, permission errors, and invalid paths.

## Using with Context Editing

The memory tool can be combined with [context editing](/en/docs/build-with-claude/context-editing), which automatically clears old tool results when conversation context grows beyond a configured threshold. This combination enables long-running agentic workflows that would otherwise exceed context limits.

### How they work together

When context editing is enabled and your conversation approaches the clearing threshold, Claude automatically receives a warning notification. This prompts Claude to preserve any important information from tool results into memory files before those results are cleared from the context window.

After tool results are cleared, Claude can retrieve the stored information from memory files whenever needed, effectively treating memory as an extension of its working context. This allows Claude to:

* Continue complex, multi-step workflows without losing critical information
* Reference past work and decisions even after tool results are removed
* Maintain coherent context across conversations that would exceed typical context limits
* Build up a knowledge base over time while keeping the active context window manageable

### Example workflow

Consider a code refactoring project with many file operations:

1. Claude makes numerous edits to files, generating many tool results
2. As the context grows and approaches your threshold, Claude receives a warning
3. Claude summarizes the changes made so far to a memory file (e.g., `/memories/refactoring_progress.xml`)
4. Context editing clears the older tool results automatically
5. Claude continues working, referencing the memory file when it needs to recall what changes were already completed
6. The workflow can continue indefinitely, with Claude managing both active context and persistent memory

### Configuration

To use both features together:

<CodeGroup>
  ```python Python theme={null}
  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=4096,
      messages=[...],
      tools=[
          {
              "type": "memory_20250818",
              "name": "memory"
          },
          # Your other tools
      ],
      betas=["context-management-2025-06-27"],
      context_management={
          "edits": [
              {
                  "type": "clear_tool_uses_20250919",
                  "trigger": {
                      "type": "input_tokens",
                      "value": 100000
                  },
                  "keep": {
                      "type": "tool_uses",
                      "value": 3
                  }
              }
          ]
      }
  )
  ```

  ```typescript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 4096,
    messages: [...],
    tools: [
      {
        type: "memory_20250818",
        name: "memory"
      },
      // Your other tools
    ],
    betas: ["context-management-2025-06-27"],
    context_management: {
      edits: [
        {
          type: "clear_tool_uses_20250919",
          trigger: {
            type: "input_tokens",
            value: 100000
          },
          keep: {
            type: "tool_uses",
            value: 3
          }
        }
      ]
    }
  });
  ```
</CodeGroup>

You can also exclude memory tool calls from being cleared to ensure Claude always has access to recent memory operations:

<CodeGroup>
  ```python Python theme={null}
  context_management={
      "edits": [
          {
              "type": "clear_tool_uses_20250919",
              "exclude_tools": ["memory"]
          }
      ]
  }
  ```

  ```typescript TypeScript theme={null}
  context_management: {
    edits: [
      {
        type: "clear_tool_uses_20250919",
        exclude_tools: ["memory"]
      }
    ]
  }
  ```
</CodeGroup>


# Tool use with Claude
Source: https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview



Claude is capable of interacting with tools and functions, allowing you to extend Claude's capabilities to perform a wider variety of tasks.

<Tip>
  Learn everything you need to master tool use with Claude as part of our new [courses](https://anthropic.skilljar.com/)! Please
  continue to share your ideas and suggestions using this
  [form](https://forms.gle/BFnYc6iCkWoRzFgk7).
</Tip>

Here's an example of how to provide tools to Claude using the Messages API:

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
      "messages": [
        {
          "role": "user",
          "content": "What is the weather like in San Francisco?"
        }
      ]
    }'
  ```

  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  response = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
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
      messages=[{"role": "user", "content": "What's the weather like in San Francisco?"}],
  )
  print(response)
  ```

  ```typescript TypeScript theme={null}
  import { Anthropic } from '@anthropic-ai/sdk';

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY
  });

  async function main() {
    const response = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 1024,
      tools: [{
        name: "get_weather",
        description: "Get the current weather in a given location",
        input_schema: {
          type: "object",
          properties: {
            location: {
              type: "string",
              description: "The city and state, e.g. San Francisco, CA"
            }
          },
          required: ["location"]
        }
      }],
      messages: [{ 
        role: "user", 
        content: "Tell me the weather in San Francisco." 
      }]
    });

    console.log(response);
  }

  main().catch(console.error);
  ```

  ```java Java theme={null}
  import java.util.List;
  import java.util.Map;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.core.JsonValue;
  import com.anthropic.models.messages.Message;
  import com.anthropic.models.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;
  import com.anthropic.models.messages.Tool;
  import com.anthropic.models.messages.Tool.InputSchema;

  public class GetWeatherExample {

      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          InputSchema schema = InputSchema.builder()
                  .properties(JsonValue.from(Map.of(
                          "location",
                          Map.of(
                                  "type", "string",
                                  "description", "The city and state, e.g. San Francisco, CA"))))
                  .putAdditionalProperty("required", JsonValue.from(List.of("location")))
                  .build();

          MessageCreateParams params = MessageCreateParams.builder()
                  .model(Model.CLAUDE_OPUS_4_0)
                  .maxTokens(1024)
                  .addTool(Tool.builder()
                          .name("get_weather")
                          .description("Get the current weather in a given location")
                          .inputSchema(schema)
                          .build())
                  .addUserMessage("What's the weather like in San Francisco?")
                  .build();

          Message message = client.messages().create(params);
          System.out.println(message);
      }
  }
  ```
</CodeGroup>

***

## How tool use works

Claude supports two types of tools:

1. **Client tools**: Tools that execute on your systems, which include:
   * User-defined custom tools that you create and implement
   * Anthropic-defined tools like [computer use](/en/docs/agents-and-tools/tool-use/computer-use-tool) and [text editor](/en/docs/agents-and-tools/tool-use/text-editor-tool) that require client implementation

2. **Server tools**: Tools that execute on Anthropic's servers, like the [web search](/en/docs/agents-and-tools/tool-use/web-search-tool) and [web fetch](/en/docs/agents-and-tools/tool-use/web-fetch-tool) tools. These tools must be specified in the API request but don't require implementation on your part.

<Note>
  Anthropic-defined tools use versioned types (e.g., `web_search_20250305`, `text_editor_20250124`) to ensure compatibility across model versions.
</Note>

### Client tools

Integrate client tools with Claude in these steps:

<Steps>
  <Step title="Provide Claude with tools and a user prompt">
    * Define client tools with names, descriptions, and input schemas in your API request.
    * Include a user prompt that might require these tools, e.g., "What's the weather in San Francisco?"
  </Step>

  <Step title="Claude decides to use a tool">
    * Claude assesses if any tools can help with the user's query.
    * If yes, Claude constructs a properly formatted tool use request.
    * For client tools, the API response has a `stop_reason` of `tool_use`, signaling Claude's intent.
  </Step>

  <Step title="Execute the tool and return results">
    * Extract the tool name and input from Claude's request
    * Execute the tool code on your system
    * Return the results in a new `user` message containing a `tool_result` content block
  </Step>

  <Step title="Claude uses tool result to formulate a response">
    * Claude analyzes the tool results to craft its final response to the original user prompt.
  </Step>
</Steps>

Note: Steps 3 and 4 are optional. For some workflows, Claude's tool use request (step 2) might be all you need, without sending results back to Claude.

### Server tools

Server tools follow a different workflow:

<Steps>
  <Step title="Provide Claude with tools and a user prompt">
    * Server tools, like [web search](/en/docs/agents-and-tools/tool-use/web-search-tool) and [web fetch](/en/docs/agents-and-tools/tool-use/web-fetch-tool), have their own parameters.
    * Include a user prompt that might require these tools, e.g., "Search for the latest news about AI" or "Analyze the content at this URL."
  </Step>

  <Step title="Claude executes the server tool">
    * Claude assesses if a server tool can help with the user's query.
    * If yes, Claude executes the tool, and the results are automatically incorporated into Claude's response.
  </Step>

  <Step title="Claude uses the server tool result to formulate a response">
    * Claude analyzes the server tool results to craft its final response to the original user prompt.
    * No additional user interaction is needed for server tool execution.
  </Step>
</Steps>

***

## Tool use examples

Here are a few code examples demonstrating various tool use patterns and techniques. For brevity's sake, the tools are simple tools, and the tool descriptions are shorter than would be ideal to ensure best performance.

<AccordionGroup>
  <Accordion title="Single tool example">
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
          "tools": [{
              "name": "get_weather",
              "description": "Get the current weather in a given location",
              "input_schema": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "The city and state, e.g. San Francisco, CA"
                      },
                      "unit": {
                          "type": "string",
                          "enum": ["celsius", "fahrenheit"],
                          "description": "The unit of temperature, either \"celsius\" or \"fahrenheit\""
                      }
                  },
                  "required": ["location"]
              }
          }],
          "messages": [{"role": "user", "content": "What is the weather like in San Francisco?"}]
      }'
      ```

      ```Python Python theme={null}
      import anthropic
      client = anthropic.Anthropic()

      response = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=1024,
          tools=[
              {
                  "name": "get_weather",
                  "description": "Get the current weather in a given location",
                  "input_schema": {
                      "type": "object",
                      "properties": {
                          "location": {
                              "type": "string",
                              "description": "The city and state, e.g. San Francisco, CA"
                          },
                          "unit": {
                              "type": "string",
                              "enum": ["celsius", "fahrenheit"],
                              "description": "The unit of temperature, either \"celsius\" or \"fahrenheit\""
                          }
                      },
                      "required": ["location"]
                  }
              }
          ],
          messages=[{"role": "user", "content": "What is the weather like in San Francisco?"}]
      )

      print(response)
      ```

      ```java Java theme={null}
      import java.util.List;
      import java.util.Map;

      import com.anthropic.client.AnthropicClient;
      import com.anthropic.client.okhttp.AnthropicOkHttpClient;
      import com.anthropic.core.JsonValue;
      import com.anthropic.models.messages.Message;
      import com.anthropic.models.messages.MessageCreateParams;
      import com.anthropic.models.messages.Model;
      import com.anthropic.models.messages.Tool;
      import com.anthropic.models.messages.Tool.InputSchema;

      public class WeatherToolExample {

          public static void main(String[] args) {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              InputSchema schema = InputSchema.builder()
                      .properties(JsonValue.from(Map.of(
                              "location", Map.of(
                                      "type", "string",
                                      "description", "The city and state, e.g. San Francisco, CA"
                              ),
                              "unit", Map.of(
                                      "type", "string",
                                      "enum", List.of("celsius", "fahrenheit"),
                                      "description", "The unit of temperature, either \"celsius\" or \"fahrenheit\""
                              )
                      )))
                      .putAdditionalProperty("required", JsonValue.from(List.of("location")))
                      .build();

              MessageCreateParams params = MessageCreateParams.builder()
                      .model(Model.CLAUDE_OPUS_4_0)
                      .maxTokens(1024)
                      .addTool(Tool.builder()
                              .name("get_weather")
                              .description("Get the current weather in a given location")
                              .inputSchema(schema)
                              .build())
                      .addUserMessage("What is the weather like in San Francisco?")
                      .build();

              Message message = client.messages().create(params);
              System.out.println(message);
          }
      }
      ```
    </CodeGroup>

    Claude will return a response similar to:

    ```JSON JSON theme={null}
    {
      "id": "msg_01Aq9w938a90dw8q",
      "model": "claude-sonnet-4-5",
      "stop_reason": "tool_use",
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "I'll check the current weather in San Francisco for you."
        },
        {
          "type": "tool_use",
          "id": "toolu_01A09q90qw90lq917835lq9",
          "name": "get_weather",
          "input": {"location": "San Francisco, CA", "unit": "celsius"}
        }
      ]
    }
    ```

    You would then need to execute the `get_weather` function with the provided input, and return the result in a new `user` message:

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
                          },
                          "unit": {
                              "type": "string",
                              "enum": ["celsius", "fahrenheit"],
                              "description": "The unit of temperature, either \"celsius\" or \"fahrenheit\""
                          }
                      },
                      "required": ["location"]
                  }
              }
          ],
          "messages": [
              {
                  "role": "user",
                  "content": "What is the weather like in San Francisco?"
              },
              {
                  "role": "assistant",
                  "content": [
                      {
                          "type": "text",
                          "text": "I'll check the current weather in San Francisco for you."
                      },
                      {
                          "type": "tool_use",
                          "id": "toolu_01A09q90qw90lq917835lq9",
                          "name": "get_weather",
                          "input": {
                              "location": "San Francisco, CA",
                              "unit": "celsius"
                          }
                      }
                  ]
              },
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "tool_result",
                          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
                          "content": "15 degrees"
                      }
                  ]
              }
          ]
      }'
      ```

      ```Python Python theme={null}
      response = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=1024,
          tools=[
              {
                  "name": "get_weather",
                  "description": "Get the current weather in a given location",
                  "input_schema": {
                      "type": "object",
                      "properties": {
                          "location": {
                              "type": "string",
                              "description": "The city and state, e.g. San Francisco, CA"
                          },
                          "unit": {
                              "type": "string",
                              "enum": ["celsius", "fahrenheit"],
                              "description": "The unit of temperature, either 'celsius' or 'fahrenheit'"
                          }
                      },
                      "required": ["location"]
                  }
              }
          ],
          messages=[
              {
                  "role": "user",
                  "content": "What's the weather like in San Francisco?"
              },
              {
                  "role": "assistant",
                  "content": [
                      {
                          "type": "text",
                          "text": "I'll check the current weather in San Francisco for you."
                      },
                      {
                          "type": "tool_use",
                          "id": "toolu_01A09q90qw90lq917835lq9",
                          "name": "get_weather",
                          "input": {"location": "San Francisco, CA", "unit": "celsius"}
                      }
                  ]
              },
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "tool_result",
                          "tool_use_id": "toolu_01A09q90qw90lq917835lq9", # from the API response
                          "content": "65 degrees" # from running your tool
                      }
                  ]
              }
          ]
      )

      print(response)
      ```

      ```java Java theme={null}
       import java.util.List;
       import java.util.Map;

       import com.anthropic.client.AnthropicClient;
       import com.anthropic.client.okhttp.AnthropicOkHttpClient;
       import com.anthropic.core.JsonValue;
       import com.anthropic.models.messages.*;
       import com.anthropic.models.messages.Tool.InputSchema;

       public class ToolConversationExample {

           public static void main(String[] args) {
               AnthropicClient client = AnthropicOkHttpClient.fromEnv();

               InputSchema schema = InputSchema.builder()
                       .properties(JsonValue.from(Map.of(
                               "location", Map.of(
                                       "type", "string",
                                       "description", "The city and state, e.g. San Francisco, CA"
                               ),
                               "unit", Map.of(
                                       "type", "string",
                                       "enum", List.of("celsius", "fahrenheit"),
                                       "description", "The unit of temperature, either \"celsius\" or \"fahrenheit\""
                               )
                       )))
                       .putAdditionalProperty("required", JsonValue.from(List.of("location")))
                       .build();

               MessageCreateParams params = MessageCreateParams.builder()
                       .model(Model.CLAUDE_OPUS_4_0)
                       .maxTokens(1024)
                       .addTool(Tool.builder()
                               .name("get_weather")
                               .description("Get the current weather in a given location")
                               .inputSchema(schema)
                               .build())
                       .addUserMessage("What is the weather like in San Francisco?")
                       .addAssistantMessageOfBlockParams(
                               List.of(
                                       ContentBlockParam.ofText(
                                               TextBlockParam.builder()
                                                       .text("I'll check the current weather in San Francisco for you.")
                                                       .build()
                                       ),
                                       ContentBlockParam.ofToolUse(
                                               ToolUseBlockParam.builder()
                                                       .id("toolu_01A09q90qw90lq917835lq9")
                                                       .name("get_weather")
                                                       .input(JsonValue.from(Map.of(
                                                               "location", "San Francisco, CA",
                                                               "unit", "celsius"
                                                       )))
                                                       .build()
                                       )
                               )
                       )
                       .addUserMessageOfBlockParams(List.of(
                               ContentBlockParam.ofToolResult(
                                       ToolResultBlockParam.builder()
                                               .toolUseId("toolu_01A09q90qw90lq917835lq9")
                                               .content("15 degrees")
                                               .build()
                               )
                       ))
                       .build();

               Message message = client.messages().create(params);
               System.out.println(message);
           }
       }
      ```
    </CodeGroup>

    This will print Claude's final response, incorporating the weather data:

    ```JSON JSON theme={null}
    {
      "id": "msg_01Aq9w938a90dw8q",
      "model": "claude-sonnet-4-5",
      "stop_reason": "stop_sequence",
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "The current weather in San Francisco is 15 degrees Celsius (59 degrees Fahrenheit). It's a cool day in the city by the bay!"
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Parallel tool use">
    Claude can call multiple tools in parallel within a single response, which is useful for tasks that require multiple independent operations. When using parallel tools, all `tool_use` blocks are included in a single assistant message, and all corresponding `tool_result` blocks must be provided in the subsequent user message.

    <Note>
      **Important**: Tool results must be formatted correctly to avoid API errors and ensure Claude continues using parallel tools. See our [implementation guide](/en/docs/agents-and-tools/tool-use/implement-tool-use#parallel-tool-use) for detailed formatting requirements and complete code examples.
    </Note>

    For comprehensive examples, test scripts, and best practices for implementing parallel tool calls, see the [parallel tool use section](/en/docs/agents-and-tools/tool-use/implement-tool-use#parallel-tool-use) in our implementation guide.
  </Accordion>

  <Accordion title="Multiple tool example">
    You can provide Claude with multiple tools to choose from in a single request. Here's an example with both a `get_weather` and a `get_time` tool, along with a user query that asks for both.

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
          "tools": [{
              "name": "get_weather",
              "description": "Get the current weather in a given location",
              "input_schema": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "The city and state, e.g. San Francisco, CA"
                      },
                      "unit": {
                          "type": "string",
                          "enum": ["celsius", "fahrenheit"],
                          "description": "The unit of temperature, either 'celsius' or 'fahrenheit'"
                      }
                  },
                  "required": ["location"]
              }
          },
          {
              "name": "get_time",
              "description": "Get the current time in a given time zone",
              "input_schema": {
                  "type": "object",
                  "properties": {
                      "timezone": {
                          "type": "string",
                          "description": "The IANA time zone name, e.g. America/Los_Angeles"
                      }
                  },
                  "required": ["timezone"]
              }
          }],
          "messages": [{
              "role": "user",
              "content": "What is the weather like right now in New York? Also what time is it there?"
          }]
      }'
      ```

      ```Python Python theme={null}
      import anthropic
      client = anthropic.Anthropic()

      response = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=1024,
          tools=[
              {
                  "name": "get_weather",
                  "description": "Get the current weather in a given location",
                  "input_schema": {
                      "type": "object",
                      "properties": {
                          "location": {
                              "type": "string",
                              "description": "The city and state, e.g. San Francisco, CA"
                          },
                          "unit": {
                              "type": "string",
                              "enum": ["celsius", "fahrenheit"],
                              "description": "The unit of temperature, either 'celsius' or 'fahrenheit'"
                          }
                      },
                      "required": ["location"]
                  }
              },
              {
                  "name": "get_time",
                  "description": "Get the current time in a given time zone",
                  "input_schema": {
                      "type": "object",
                      "properties": {
                          "timezone": {
                              "type": "string",
                              "description": "The IANA time zone name, e.g. America/Los_Angeles"
                          }
                      },
                      "required": ["timezone"]
                  }
              }
          ],
          messages=[
              {
                  "role": "user",
                  "content": "What is the weather like right now in New York? Also what time is it there?"
              }
          ]
      )
      print(response)
      ```

      ```java Java theme={null}
      import java.util.List;
      import java.util.Map;

      import com.anthropic.client.AnthropicClient;
      import com.anthropic.client.okhttp.AnthropicOkHttpClient;
      import com.anthropic.core.JsonValue;
      import com.anthropic.models.messages.Message;
      import com.anthropic.models.messages.MessageCreateParams;
      import com.anthropic.models.messages.Model;
      import com.anthropic.models.messages.Tool;
      import com.anthropic.models.messages.Tool.InputSchema;

      public class MultipleToolsExample {

          public static void main(String[] args) {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              // Weather tool schema
              InputSchema weatherSchema = InputSchema.builder()
                      .properties(JsonValue.from(Map.of(
                              "location", Map.of(
                                      "type", "string",
                                      "description", "The city and state, e.g. San Francisco, CA"
                              ),
                              "unit", Map.of(
                                      "type", "string",
                                      "enum", List.of("celsius", "fahrenheit"),
                                      "description", "The unit of temperature, either \"celsius\" or \"fahrenheit\""
                              )
                      )))
                      .putAdditionalProperty("required", JsonValue.from(List.of("location")))
                      .build();

              // Time tool schema
              InputSchema timeSchema = InputSchema.builder()
                      .properties(JsonValue.from(Map.of(
                              "timezone", Map.of(
                                      "type", "string",
                                      "description", "The IANA time zone name, e.g. America/Los_Angeles"
                              )
                      )))
                      .putAdditionalProperty("required", JsonValue.from(List.of("timezone")))
                      .build();

              MessageCreateParams params = MessageCreateParams.builder()
                      .model(Model.CLAUDE_OPUS_4_0)
                      .maxTokens(1024)
                      .addTool(Tool.builder()
                              .name("get_weather")
                              .description("Get the current weather in a given location")
                              .inputSchema(weatherSchema)
                              .build())
                      .addTool(Tool.builder()
                              .name("get_time")
                              .description("Get the current time in a given time zone")
                              .inputSchema(timeSchema)
                              .build())
                      .addUserMessage("What is the weather like right now in New York? Also what time is it there?")
                      .build();

              Message message = client.messages().create(params);
              System.out.println(message);
          }
      }
      ```
    </CodeGroup>

    In this case, Claude may either:

    * Use the tools sequentially (one at a time) — calling `get_weather` first, then `get_time` after receiving the weather result
    * Use parallel tool calls — outputting multiple `tool_use` blocks in a single response when the operations are independent

    When Claude makes parallel tool calls, you must return all tool results in a single `user` message, with each result in its own `tool_result` block.
  </Accordion>

  <Accordion title="Missing information">
    If the user's prompt doesn't include enough information to fill all the required parameters for a tool, Claude Opus is much more likely to recognize that a parameter is missing and ask for it. Claude Sonnet may ask, especially when prompted to think before outputting a tool request. But it may also do its best to infer a reasonable value.

    For example, using the `get_weather` tool above, if you ask Claude "What's the weather?" without specifying a location, Claude, particularly Claude Sonnet, may make a guess about tools inputs:

    ```JSON JSON theme={null}
    {
      "type": "tool_use",
      "id": "toolu_01A09q90qw90lq917835lq9",
      "name": "get_weather",
      "input": {"location": "New York, NY", "unit": "fahrenheit"}
    }
    ```

    This behavior is not guaranteed, especially for more ambiguous prompts and for less intelligent models. If Claude Opus doesn't have enough context to fill in the required parameters, it is far more likely respond with a clarifying question instead of making a tool call.
  </Accordion>

  <Accordion title="Sequential tools">
    Some tasks may require calling multiple tools in sequence, using the output of one tool as the input to another. In such a case, Claude will call one tool at a time. If prompted to call the tools all at once, Claude is likely to guess parameters for tools further downstream if they are dependent on tool results for tools further upstream.

    Here's an example of using a `get_location` tool to get the user's location, then passing that location to the `get_weather` tool:

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
          "tools": [
              {
                  "name": "get_location",
                  "description": "Get the current user location based on their IP address. This tool has no parameters or arguments.",
                  "input_schema": {
                      "type": "object",
                      "properties": {}
                  }
              },
              {
                  "name": "get_weather",
                  "description": "Get the current weather in a given location",
                  "input_schema": {
                      "type": "object",
                      "properties": {
                          "location": {
                              "type": "string",
                              "description": "The city and state, e.g. San Francisco, CA"
                          },
                          "unit": {
                              "type": "string",
                              "enum": ["celsius", "fahrenheit"],
                              "description": "The unit of temperature, either 'celsius' or 'fahrenheit'"
                          }
                      },
                      "required": ["location"]
                  }
              }
          ],
          "messages": [{
              "role": "user",
              "content": "What is the weather like where I am?"
          }]
      }'
      ```

      ```Python Python theme={null}
      response = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=1024,
          tools=[
              {
                  "name": "get_location",
                  "description": "Get the current user location based on their IP address. This tool has no parameters or arguments.",
                  "input_schema": {
                      "type": "object",
                      "properties": {}
                  }
              },
              {
                  "name": "get_weather",
                  "description": "Get the current weather in a given location",
                  "input_schema": {
                      "type": "object",
                      "properties": {
                          "location": {
                              "type": "string",
                              "description": "The city and state, e.g. San Francisco, CA"
                          },
                          "unit": {
                              "type": "string",
                              "enum": ["celsius", "fahrenheit"],
                              "description": "The unit of temperature, either 'celsius' or 'fahrenheit'"
                          }
                      },
                      "required": ["location"]
                  }
              }
          ],
          messages=[{
         		  "role": "user",
          	  "content": "What's the weather like where I am?"
          }]
      )
      ```

      ```java Java theme={null}
      import java.util.List;
      import java.util.Map;

      import com.anthropic.client.AnthropicClient;
      import com.anthropic.client.okhttp.AnthropicOkHttpClient;
      import com.anthropic.core.JsonValue;
      import com.anthropic.models.messages.Message;
      import com.anthropic.models.messages.MessageCreateParams;
      import com.anthropic.models.messages.Model;
      import com.anthropic.models.messages.Tool;
      import com.anthropic.models.messages.Tool.InputSchema;

      public class EmptySchemaToolExample {

          public static void main(String[] args) {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              // Empty schema for location tool
              InputSchema locationSchema = InputSchema.builder()
                      .properties(JsonValue.from(Map.of()))
                      .build();

              // Weather tool schema
              InputSchema weatherSchema = InputSchema.builder()
                      .properties(JsonValue.from(Map.of(
                              "location", Map.of(
                                      "type", "string",
                                      "description", "The city and state, e.g. San Francisco, CA"
                              ),
                              "unit", Map.of(
                                      "type", "string",
                                      "enum", List.of("celsius", "fahrenheit"),
                                      "description", "The unit of temperature, either \"celsius\" or \"fahrenheit\""
                              )
                      )))
                      .putAdditionalProperty("required", JsonValue.from(List.of("location")))
                      .build();

              MessageCreateParams params = MessageCreateParams.builder()
                      .model(Model.CLAUDE_OPUS_4_0)
                      .maxTokens(1024)
                      .addTool(Tool.builder()
                              .name("get_location")
                              .description("Get the current user location based on their IP address. This tool has no parameters or arguments.")
                              .inputSchema(locationSchema)
                              .build())
                      .addTool(Tool.builder()
                              .name("get_weather")
                              .description("Get the current weather in a given location")
                              .inputSchema(weatherSchema)
                              .build())
                      .addUserMessage("What is the weather like where I am?")
                      .build();

              Message message = client.messages().create(params);
              System.out.println(message);
          }
      }
      ```
    </CodeGroup>

    In this case, Claude would first call the `get_location` tool to get the user's location. After you return the location in a `tool_result`, Claude would then call `get_weather` with that location to get the final answer.

    The full conversation might look like:

    | Role      | Content                                                                                                                                                                                                                       |
    | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | User      | What's the weather like where I am?                                                                                                                                                                                           |
    | Assistant | I'll find your current location first, then check the weather there. \[Tool use for get\_location]                                                                                                                            |
    | User      | \[Tool result for get\_location with matching id and result of San Francisco, CA]                                                                                                                                             |
    | Assistant | \[Tool use for get\_weather with the following input]\{ "location": "San Francisco, CA", "unit": "fahrenheit" }                                                                                                               |
    | User      | \[Tool result for get\_weather with matching id and result of "59°F (15°C), mostly cloudy"]                                                                                                                                   |
    | Assistant | Based on your current location in San Francisco, CA, the weather right now is 59°F (15°C) and mostly cloudy. It's a fairly cool and overcast day in the city. You may want to bring a light jacket if you're heading outside. |

    This example demonstrates how Claude can chain together multiple tool calls to answer a question that requires gathering data from different sources. The key steps are:

    1. Claude first realizes it needs the user's location to answer the weather question, so it calls the `get_location` tool.
    2. The user (i.e. the client code) executes the actual `get_location` function and returns the result "San Francisco, CA" in a `tool_result` block.
    3. With the location now known, Claude proceeds to call the `get_weather` tool, passing in "San Francisco, CA" as the `location` parameter (as well as a guessed `unit` parameter, as `unit` is not a required parameter).
    4. The user again executes the actual `get_weather` function with the provided arguments and returns the weather data in another `tool_result` block.
    5. Finally, Claude incorporates the weather data into a natural language response to the original question.
  </Accordion>

  <Accordion title="Chain of thought tool use">
    By default, Claude Opus is prompted to think before it answers a tool use query to best determine whether a tool is necessary, which tool to use, and the appropriate parameters. Claude Sonnet and Claude Haiku are prompted to try to use tools as much as possible and are more likely to call an unnecessary tool or infer missing parameters. To prompt Sonnet or Haiku to better assess the user query before making tool calls, the following prompt can be used:

    Chain of thought prompt

    `Answer the user's request using relevant tools (if they are available). Before calling a tool, do some analysis. First, think about which of the provided tools is the relevant tool to answer the user's request. Second, go through each of the required parameters of the relevant tool and determine if the user has directly provided or given enough information to infer a value. When deciding if the parameter can be inferred, carefully consider all the context to see if it supports a specific value. If all of the required parameters are present or can be reasonably inferred, proceed with the tool call. BUT, if one of the values for a required parameter is missing, DO NOT invoke the function (not even with fillers for the missing params) and instead, ask the user to provide the missing parameters. DO NOT ask for more information on optional parameters if it is not provided.
    `
  </Accordion>

  <Accordion title="JSON mode">
    You can use tools to get Claude produce JSON output that follows a schema, even if you don't have any intention of running that output through a tool or function.

    When using tools in this way:

    * You usually want to provide a **single** tool
    * You should set `tool_choice` (see [Forcing tool use](/en/docs/agents-and-tools/tool-use/implement-tool-use#forcing-tool-use)) to instruct the model to explicitly use that tool
    * Remember that the model will pass the `input` to the tool, so the name of the tool and description should be from the model's perspective.

    The following uses a `record_summary` tool to describe an image following a particular format.

    <CodeGroup>
      ```bash Shell theme={null}
      #!/bin/bash
      IMAGE_URL="https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
      IMAGE_MEDIA_TYPE="image/jpeg"
      IMAGE_BASE64=$(curl "$IMAGE_URL" | base64)

      curl https://api.anthropic.com/v1/messages \
           --header "content-type: application/json" \
           --header "x-api-key: $ANTHROPIC_API_KEY" \
           --header "anthropic-version: 2023-06-01" \
           --data \
      '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 1024,
          "tools": [{
              "name": "record_summary",
              "description": "Record summary of an image using well-structured JSON.",
              "input_schema": {
                  "type": "object",
                  "properties": {
                      "key_colors": {
                          "type": "array",
                          "items": {
                              "type": "object",
                              "properties": {
                                  "r": { "type": "number", "description": "red value [0.0, 1.0]" },
                                  "g": { "type": "number", "description": "green value [0.0, 1.0]" },
                                  "b": { "type": "number", "description": "blue value [0.0, 1.0]" },
                                  "name": { "type": "string", "description": "Human-readable color name in snake_case, e.g. \"olive_green\" or \"turquoise\"" }
                              },
                              "required": [ "r", "g", "b", "name" ]
                          },
                          "description": "Key colors in the image. Limit to less than four."
                      },
                      "description": {
                          "type": "string",
                          "description": "Image description. One to two sentences max."
                      },
                      "estimated_year": {
                          "type": "integer",
                          "description": "Estimated year that the image was taken, if it is a photo. Only set this if the image appears to be non-fictional. Rough estimates are okay!"
                      }
                  },
                  "required": [ "key_colors", "description" ]
              }
          }],
          "tool_choice": {"type": "tool", "name": "record_summary"},
          "messages": [
              {"role": "user", "content": [
                  {"type": "image", "source": {
                      "type": "base64",
                      "media_type": "'$IMAGE_MEDIA_TYPE'",
                      "data": "'$IMAGE_BASE64'"
                  }},
                  {"type": "text", "text": "Describe this image."}
              ]}
          ]
      }'
      ```

      ```Python Python theme={null}
      import base64
      import anthropic
      import httpx

      image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
      image_media_type = "image/jpeg"
      image_data = base64.standard_b64encode(httpx.get(image_url).content).decode("utf-8")

      message = anthropic.Anthropic().messages.create(
          model="claude-sonnet-4-5",
          max_tokens=1024,
          tools=[
              {
                  "name": "record_summary",
                  "description": "Record summary of an image using well-structured JSON.",
                  "input_schema": {
                      "type": "object",
                      "properties": {
                          "key_colors": {
                              "type": "array",
                              "items": {
                                  "type": "object",
                                  "properties": {
                                      "r": {
                                          "type": "number",
                                          "description": "red value [0.0, 1.0]",
                                      },
                                      "g": {
                                          "type": "number",
                                          "description": "green value [0.0, 1.0]",
                                      },
                                      "b": {
                                          "type": "number",
                                          "description": "blue value [0.0, 1.0]",
                                      },
                                      "name": {
                                          "type": "string",
                                          "description": "Human-readable color name in snake_case, e.g. \"olive_green\" or \"turquoise\""
                                      },
                                  },
                                  "required": ["r", "g", "b", "name"],
                              },
                              "description": "Key colors in the image. Limit to less than four.",
                          },
                          "description": {
                              "type": "string",
                              "description": "Image description. One to two sentences max.",
                          },
                          "estimated_year": {
                              "type": "integer",
                              "description": "Estimated year that the image was taken, if it is a photo. Only set this if the image appears to be non-fictional. Rough estimates are okay!",
                          },
                      },
                      "required": ["key_colors", "description"],
                  },
              }
          ],
          tool_choice={"type": "tool", "name": "record_summary"},
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
                      {"type": "text", "text": "Describe this image."},
                  ],
              }
          ],
      )
      print(message)
      ```

      ```java Java theme={null}
      import java.io.IOException;
      import java.io.InputStream;
      import java.net.URL;
      import java.util.Base64;
      import java.util.List;
      import java.util.Map;

      import com.anthropic.client.AnthropicClient;
      import com.anthropic.client.okhttp.AnthropicOkHttpClient;
      import com.anthropic.core.JsonValue;
      import com.anthropic.models.messages.*;
      import com.anthropic.models.messages.Tool.InputSchema;

      public class ImageToolExample {

          public static void main(String[] args) throws Exception {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              String imageBase64 = downloadAndEncodeImage("https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg");
              // Create nested schema for colors
              Map<String, Object> colorProperties = Map.of(
                      "r", Map.of(
                              "type", "number",
                              "description", "red value [0.0, 1.0]"
                      ),
                      "g", Map.of(
                              "type", "number",
                              "description", "green value [0.0, 1.0]"
                      ),
                      "b", Map.of(
                              "type", "number",
                              "description", "blue value [0.0, 1.0]"
                      ),
                      "name", Map.of(
                              "type", "string",
                              "description", "Human-readable color name in snake_case, e.g. \"olive_green\" or \"turquoise\""
                      )
              );

              // Create the input schema
              InputSchema schema = InputSchema.builder()
                      .properties(JsonValue.from(Map.of(
                              "key_colors", Map.of(
                                      "type", "array",
                                      "items", Map.of(
                                              "type", "object",
                                              "properties", colorProperties,
                                              "required", List.of("r", "g", "b", "name")
                                      ),
                                      "description", "Key colors in the image. Limit to less than four."
                              ),
                              "description", Map.of(
                                      "type", "string",
                                      "description", "Image description. One to two sentences max."
                              ),
                              "estimated_year", Map.of(
                                      "type", "integer",
                                      "description", "Estimated year that the image was taken, if it is a photo. Only set this if the image appears to be non-fictional. Rough estimates are okay!"
                              )
                      )))
                      .putAdditionalProperty("required", JsonValue.from(List.of("key_colors", "description")))
                      .build();

              // Create the tool
              Tool tool = Tool.builder()
                      .name("record_summary")
                      .description("Record summary of an image using well-structured JSON.")
                      .inputSchema(schema)
                      .build();

              // Create the content blocks for the message
              ContentBlockParam imageContent = ContentBlockParam.ofImage(
                      ImageBlockParam.builder()
                              .source(Base64ImageSource.builder()
                                      .mediaType(Base64ImageSource.MediaType.IMAGE_JPEG)
                                      .data(imageBase64)
                                      .build())
                              .build()
              );

              ContentBlockParam textContent = ContentBlockParam.ofText(TextBlockParam.builder().text("Describe this image.").build());

              // Create the message
              MessageCreateParams params = MessageCreateParams.builder()
                      .model(Model.CLAUDE_OPUS_4_0)
                      .maxTokens(1024)
                      .addTool(tool)
                      .toolChoice(ToolChoiceTool.builder().name("record_summary").build())
                      .addUserMessageOfBlockParams(List.of(imageContent, textContent))
                      .build();

              Message message = client.messages().create(params);
              System.out.println(message);
          }

          private static String downloadAndEncodeImage(String imageUrl) throws IOException {
              try (InputStream inputStream = new URL(imageUrl).openStream()) {
                  return Base64.getEncoder().encodeToString(inputStream.readAllBytes());
              }
          }
      }
      ```
    </CodeGroup>
  </Accordion>
</AccordionGroup>

***

## Pricing

Tool use requests are priced based on:

1. The total number of input tokens sent to the model (including in the `tools` parameter)
2. The number of output tokens generated
3. For server-side tools, additional usage-based pricing (e.g., web search charges per search performed)

Client-side tools are priced the same as any other Claude API request, while server-side tools may incur additional charges based on their specific usage.

The additional tokens from tool use come from:

* The `tools` parameter in API requests (tool names, descriptions, and schemas)
* `tool_use` content blocks in API requests and responses
* `tool_result` content blocks in API requests

When you use `tools`, we also automatically include a special system prompt for the model which enables tool use. The number of tool use tokens required for each model are listed below (excluding the additional tokens listed above). Note that the table assumes at least 1 tool is provided. If no `tools` are provided, then a tool choice of `none` uses 0 additional system prompt tokens.

| Model                                                                      | Tool choice                                        | Tool use system prompt token count          |
| -------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------- |
| Claude Opus 4.1                                                            | `auto`, `none`<hr className="my-2" />`any`, `tool` | 346 tokens<hr className="my-2" />313 tokens |
| Claude Opus 4                                                              | `auto`, `none`<hr className="my-2" />`any`, `tool` | 346 tokens<hr className="my-2" />313 tokens |
| Claude Sonnet 4.5                                                          | `auto`, `none`<hr className="my-2" />`any`, `tool` | 346 tokens<hr className="my-2" />313 tokens |
| Claude Sonnet 4                                                            | `auto`, `none`<hr className="my-2" />`any`, `tool` | 346 tokens<hr className="my-2" />313 tokens |
| Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) | `auto`, `none`<hr className="my-2" />`any`, `tool` | 346 tokens<hr className="my-2" />313 tokens |
| Claude Haiku 4.5                                                           | `auto`, `none`<hr className="my-2" />`any`, `tool` | 346 tokens<hr className="my-2" />313 tokens |
| Claude Haiku 3.5                                                           | `auto`, `none`<hr className="my-2" />`any`, `tool` | 264 tokens<hr className="my-2" />340 tokens |
| Claude Opus 3 ([deprecated](/en/docs/about-claude/model-deprecations))     | `auto`, `none`<hr className="my-2" />`any`, `tool` | 530 tokens<hr className="my-2" />281 tokens |
| Claude Sonnet 3                                                            | `auto`, `none`<hr className="my-2" />`any`, `tool` | 159 tokens<hr className="my-2" />235 tokens |
| Claude Haiku 3                                                             | `auto`, `none`<hr className="my-2" />`any`, `tool` | 264 tokens<hr className="my-2" />340 tokens |

These token counts are added to your normal input and output tokens to calculate the total cost of a request.

Refer to our [models overview table](/en/docs/about-claude/models/overview#model-comparison-table) for current per-model prices.

When you send a tool use prompt, just like any other API request, the response will output both input and output token counts as part of the reported `usage` metrics.

***

## Next Steps

Explore our repository of ready-to-implement tool use code examples in our cookbooks:

<CardGroup cols={3}>
  <Card title="Calculator Tool" icon="calculator" href="https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/calculator_tool.ipynb">
    Learn how to integrate a simple calculator tool with Claude for precise numerical computations.
  </Card>

  {" "}

  <Card title="Customer Service Agent" icon="headset" href="https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/customer_service_agent.ipynb">
    Build a responsive customer service bot that leverages client tools to
    enhance support.
  </Card>

  <Card title="JSON Extractor" icon="brackets-curly" href="https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/extracting_structured_json.ipynb">
    See how Claude and tool use can extract structured data from unstructured text.
  </Card>
</CardGroup>



---

**Navigation:** [← Previous](./04-get-started-with-agent-skills-in-the-api.md) | [Index](./index.md) | [Next →](./06-text-editor-tool.md)
