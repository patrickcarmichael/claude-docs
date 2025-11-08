---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Handling tool use and tool result content blocks

>   **📝 Note**
>
>   **Simpler with Tool runner**: The manual tool handling described in this section is automatically managed by [tool runner](#tool-runner-beta). Use this section when you need custom control over tool execution.

Claude's response differs based on whether it uses a client or server tool.

### Handling results from client tools

The response will have a `stop_reason` of `tool_use` and one or more `tool_use` content blocks that include:

* `id`: A unique identifier for this particular tool use block. This will be used to match up the tool results later.
* `name`: The name of the tool being used.
* `input`: An object containing the input being passed to the tool, conforming to the tool's `input_schema`.

<Accordion title="Example API response with a `tool_use` content block">
```JSON
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

>   **📝 Note**
>
>   **Important formatting requirements**:

  * Tool result blocks must immediately follow their corresponding tool use blocks in the message history. You cannot include any messages between the assistant's tool use message and the user's tool result message.
  * In the user message containing tool results, the tool\_result blocks must come FIRST in the content array. Any text must come AFTER all tool results.

  For example, this will cause a 400 error:
```json
  {"role": "user", "content": [
    {"type": "text", "text": "Here are the results:"},  // ❌ Text before tool_result
    {"type": "tool_result", "tool_use_id": "toolu_01", ...}
  ]}
```
  This is correct:
```json
  {"role": "user", "content": [
    {"type": "tool_result", "tool_use_id": "toolu_01", ...},
    {"type": "text", "text": "What should I do next?"}  // ✅ Text after tool_result
  ]}
```
  If you receive an error like "tool\_use ids were found without tool\_result blocks immediately after", check that your tool results are formatted correctly.

<AccordionGroup>
  <Accordion title="Example of successful tool result">
```JSON
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
```JSON
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
```JSON
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
```JSON
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
```python
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
```typescript
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

#### Handling the `pause_turn` stop reason

When using server tools like web search, the API may return a `pause_turn` stop reason, indicating that the API has paused a long-running turn.

Here's how to handle the `pause_turn` stop reason:
```python
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
```typescript
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
```javascript

When handling `pause_turn`:

* **Continue the conversation**: Pass the paused response back as-is in a subsequent request to let Claude continue its turn
* **Modify if needed**: You can optionally modify the content before continuing if you want to interrupt or redirect the conversation
* **Preserve tool state**: Include the same tools in the continuation request to maintain functionality

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
