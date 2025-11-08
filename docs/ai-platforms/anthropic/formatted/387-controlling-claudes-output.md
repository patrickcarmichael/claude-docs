---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

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

>   **📝 Note**
>
> When using [prompt caching](/en/docs/build-with-claude/prompt-caching#what-invalidates-the-cache), changes to the `tool_choice` parameter will invalidate cached message blocks. Tool definitions and system prompts remain cached, but message content must be reprocessed.

This diagram illustrates how each option works:

<Frame>
  <img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/tool_choice.png?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=fb88b9fa0da23fc231e4fece253f4406" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/tool_choice.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/tool_choice.png?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=11a4cfd7ab7815ea14c21e0948d060d4 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/tool_choice.png?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=c889c279adce34f1fa479bc722b3fe6f 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/tool_choice.png?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=e16651305d256ded74250f1c0dadb622 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/tool_choice.png?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=a99b0dd3b603051efdf9536ba9307a34 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/tool_choice.png?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=5045888f298f7261d3ae2e1466e54027 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/tool_choice.png?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=8a9c615a15610a949a2dad3aaa8113b8 2500w" />
</Frame>

Note that when you have `tool_choice` as `any` or `tool`, we will prefill the assistant message to force a tool to be used. This means that the models will not emit a natural language response or explanation before `tool_use` content blocks, even if explicitly asked to do so.

>   **📝 Note**
>
> When using [extended thinking](/en/docs/build-with-claude/extended-thinking) with tool use, `tool_choice: {"type": "any"}` and `tool_choice: {"type": "tool", "name": "..."}` are not supported and will result in an error. Only `tool_choice: {"type": "auto"}` (the default) and `tool_choice: {"type": "none"}` are compatible with extended thinking.

Our testing has shown that this should not reduce performance. If you would like the model to provide natural language context or explanations while still requesting that the model use a specific tool, you can use `{"type": "auto"}` for `tool_choice` (the default) and add explicit instructions in a `user` message. For example: `What's the weather like in London? Use the get_weather tool in your response.`

### JSON output

Tools do not necessarily need to be client functions — you can use tools anytime you want the model to return JSON output that follows a provided schema. For example, you might use a `record_summary` tool with a particular schema. See [Tool use with Claude](/en/docs/agents-and-tools/tool-use/overview) for a full working example.

### Model responses with tools

When using tools, Claude will often comment on what it's doing or respond naturally to the user before invoking tools.

For example, given the prompt "What's the weather like in San Francisco right now, and what time is it there?", Claude might respond with:
```JSON
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
    >   **📝 Note**
>
>   **Simpler with Tool runner**: The example below shows manual parallel tool handling. For most use cases, [tool runner](#tool-runner-beta) automatically handle parallel tool execution with much less code.

    Here's a complete example showing how to properly format parallel tool calls in the message history:
```python
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
```typescript
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

    The assistant message with parallel tool calls would look like this:
```json
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
```python
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
```typescript
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
```text
    For maximum efficiency, whenever you need to perform multiple independent operations, invoke all relevant tools simultaneously rather than sequentially.
```
    For even stronger parallel tool use (recommended if the default isn't sufficient), use:
```text
    <use_parallel_tool_calls>
    For maximum efficiency, whenever you perform multiple independent operations, invoke all relevant tools simultaneously rather than sequentially. Prioritize calling tools in parallel whenever possible. For example, when reading 3 files, run 3 tool calls in parallel to read all 3 files into context at the same time. When running multiple read-only commands like `ls` or `list_dir`, always run all of the commands in parallel. Err on the side of maximizing parallel tool calls rather than running too many tools sequentially.
    </use_parallel_tool_calls>
```
  </Accordion>

  <Accordion title="User message prompting">
    You can also encourage parallel tool use within specific user messages:
```python
    # Instead of:

    "What's the weather in Paris? Also check London."

    # Use:

    "Check the weather in Paris and London simultaneously."

    # Or be explicit:

    "Please use parallel tool calls to get the weather for Paris, London, and Tokyo at the same time."
```
  </Accordion>
</AccordionGroup>

>   **⚠️ Warning**
>
>   **Parallel tool use with Claude Sonnet 3.7**

  Claude Sonnet 3.7 may be less likely to make make parallel tool calls in a response, even when you have not set `disable_parallel_tool_use`. To work around this, we recommend enabling [token-efficient tool use](/en/docs/agents-and-tools/tool-use/token-efficient-tool-use), which helps encourage Claude to use parallel tools. This beta feature also reduces latency and saves an average of 14% in output tokens.

  If you prefer not to opt into the token-efficient tool use beta, you can also introduce a "batch tool" that can act as a meta-tool to wrap invocations to other tools simultaneously. We find that if this tool is present, the model will use it to simultaneously call multiple tools in parallel for you.

  See [this example](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/parallel_tools_claude_3_7_sonnet.ipynb) in our cookbook for how to use this workaround.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
