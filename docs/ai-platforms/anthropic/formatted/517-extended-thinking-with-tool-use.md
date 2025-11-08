---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Extended thinking with tool use

Extended thinking can be used alongside [tool use](/en/docs/agents-and-tools/tool-use/overview), allowing Claude to reason through tool selection and results processing.

When using extended thinking with tool use, be aware of the following limitations:

1. **Tool choice limitation**: Tool use with thinking only supports `tool_choice: {"type": "auto"}` (the default) or `tool_choice: {"type": "none"}`. Using `tool_choice: {"type": "any"}` or `tool_choice: {"type": "tool", "name": "..."}` will result in an error because these options force tool use, which is incompatible with extended thinking.

2. **Preserving thinking blocks**: During tool use, you must pass `thinking` blocks back to the API for the last assistant message. Include the complete unmodified block back to the API to maintain reasoning continuity.

### Toggling thinking modes in conversations

You cannot toggle thinking in the middle of an assistant turn, including during tool use loops. The entire assistant turn must operate in a single thinking mode:

* **If thinking is enabled**, the final assistant turn must start with a thinking block.
* **If thinking is disabled**, the final assistant turn must not contain any thinking blocks

From the model's perspective, **tool use loops are part of the assistant turn**. An assistant turn doesn't complete until Claude finishes its full response, which may include multiple tool calls and results.

For example, this sequence is all part of a **single assistant turn**:
```
User: "What's the weather in Paris?"
Assistant: [thinking] + [tool_use: get_weather]
User: [tool_result: "20°C, sunny"]
Assistant: [text: "The weather in Paris is 20°C and sunny"]
```
Even though there are multiple API messages, the tool use loop is conceptually part of one continuous assistant response.

#### Common error scenarios

You might encounter this error:
```
Expected `thinking` or `redacted_thinking`, but found `tool_use`.
When `thinking` is enabled, a final `assistant` message must start
with a thinking block (preceding the lastmost set of `tool_use` and
`tool_result` blocks).
```
This typically occurs when:

1. You had thinking **disabled** during a tool use sequence
2. You want to enable thinking again
3. Your last assistant message contains tool use blocks but no thinking block

#### Practical guidance

**✗ Invalid: Toggling thinking immediately after tool use**
```
User: "What's the weather?"
Assistant: [tool_use] (thinking disabled)
User: [tool_result]
// Cannot enable thinking here - still in the same assistant turn
```
**✓ Valid: Complete the assistant turn first**
```
User: "What's the weather?"
Assistant: [tool_use] (thinking disabled)
User: [tool_result]
Assistant: [text: "It's sunny"] 
User: "What about tomorrow?" (thinking disabled)
Assistant: [thinking] + [text: "..."] (thinking enabled - new turn)
```
**Best practice**: Plan your thinking strategy at the start of each turn rather than trying to toggle mid-turn.

>   **📝 Note**
>
> Toggling thinking modes also invalidates prompt caching for message history. For more details, see the [Extended thinking with prompt caching](#extended-thinking-with-prompt-caching) section.

<AccordionGroup>
  <Accordion title="Example: Passing thinking blocks with tool results">
    Here's a practical example showing how to preserve thinking blocks when providing tool results:
```python
      weather_tool = {
          "name": "get_weather",
          "description": "Get current weather for a location",
          "input_schema": {
              "type": "object",
              "properties": {
                  "location": {"type": "string"}
              },
              "required": ["location"]
          }
      }

      # First request - Claude responds with thinking and tool request

      response = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=16000,
          thinking={
              "type": "enabled",
              "budget_tokens": 10000
          },
          tools=[weather_tool],
          messages=[
              {"role": "user", "content": "What's the weather in Paris?"}
          ]
      )
```
```typescript
      const weatherTool = {
        name: "get_weather",
        description: "Get current weather for a location",
        input_schema: {
          type: "object",
          properties: {
            location: { type: "string" }
          },
          required: ["location"]
        }
      };

      // First request - Claude responds with thinking and tool request
      const response = await client.messages.create({
        model: "claude-sonnet-4-5",
        max_tokens: 16000,
        thinking: {
          type: "enabled",
          budget_tokens: 10000
        },
        tools: [weatherTool],
        messages: [
          { role: "user", content: "What's the weather in Paris?" }
        ]
      });
```
```java
      import java.util.List;
      import java.util.Map;

      import com.anthropic.client.AnthropicClient;
      import com.anthropic.client.okhttp.AnthropicOkHttpClient;
      import com.anthropic.core.JsonValue;
      import com.anthropic.models.beta.messages.BetaMessage;
      import com.anthropic.models.beta.messages.MessageCreateParams;
      import com.anthropic.models.beta.messages.BetaThinkingConfigEnabled;
      import com.anthropic.models.beta.messages.BetaTool;
      import com.anthropic.models.beta.messages.BetaTool.InputSchema;
      import com.anthropic.models.messages.Model;

      public class ThinkingWithToolsExample {
          public static void main(String[] args) {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              InputSchema schema = InputSchema.builder()
                      .properties(JsonValue.from(Map.of(
                              "location", Map.of("type", "string")
                      )))
                      .putAdditionalProperty("required", JsonValue.from(List.of("location")))
                      .build();

              BetaTool weatherTool = BetaTool.builder()
                      .name("get_weather")
                      .description("Get current weather for a location")
                      .inputSchema(schema)
                      .build();

              BetaMessage response = client.beta().messages().create(
                      MessageCreateParams.builder()
                              .model(Model.CLAUDE_OPUS_4_0)
                              .maxTokens(16000)
                              .thinking(BetaThinkingConfigEnabled.builder().budgetTokens(10000).build())
                              .addTool(weatherTool)
                              .addUserMessage("What's the weather in Paris?")
                              .build()
              );

              System.out.println(response);
          }
      }
```

    The API response will include thinking, text, and tool\_use blocks:
```json
    {
        "content": [
            {
                "type": "thinking",
                "thinking": "The user wants to know the current weather in Paris. I have access to a function `get_weather`...",
                "signature": "BDaL4VrbR2Oj0hO4XpJxT28J5TILnCrrUXoKiiNBZW9P+nr8XSj1zuZzAl4egiCCpQNvfyUuFFJP5CncdYZEQPPmLxYsNrcs...."
            },
            {
                "type": "text",
                "text": "I can help you get the current weather information for Paris. Let me check that for you"
            },
            {
                "type": "tool_use",
                "id": "toolu_01CswdEQBMshySk6Y9DFKrfq",
                "name": "get_weather",
                "input": {
                    "location": "Paris"
                }
            }
        ]
    }
```
    Now let's continue the conversation and use the tool
```python
      # Extract thinking block and tool use block

      thinking_block = next((block for block in response.content
                            if block.type == 'thinking'), None)
      tool_use_block = next((block for block in response.content
                            if block.type == 'tool_use'), None)

      # Call your actual weather API, here is where your actual API call would go

      # let's pretend this is what we get back

      weather_data = {"temperature": 88}

      # Second request - Include thinking block and tool result

      # No new thinking blocks will be generated in the response

      continuation = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=16000,
          thinking={
              "type": "enabled",
              "budget_tokens": 10000
          },
          tools=[weather_tool],
          messages=[
              {"role": "user", "content": "What's the weather in Paris?"},
              # notice that the thinking_block is passed in as well as the tool_use_block

              # if this is not passed in, an error is raised

              {"role": "assistant", "content": [thinking_block, tool_use_block]},
              {"role": "user", "content": [{
                  "type": "tool_result",
                  "tool_use_id": tool_use_block.id,
                  "content": f"Current temperature: {weather_data['temperature']}°F"
              }]}
          ]
      )
```
```typescript
      // Extract thinking block and tool use block
      const thinkingBlock = response.content.find(block =>
        block.type === 'thinking');
      const toolUseBlock = response.content.find(block =>
        block.type === 'tool_use');

      // Call your actual weather API, here is where your actual API call would go
      // let's pretend this is what we get back
      const weatherData = { temperature: 88 };

      // Second request - Include thinking block and tool result
      // No new thinking blocks will be generated in the response
      const continuation = await client.messages.create({
        model: "claude-sonnet-4-5",
        max_tokens: 16000,
        thinking: {
          type: "enabled",
          budget_tokens: 10000
        },
        tools: [weatherTool],
        messages: [
          { role: "user", content: "What's the weather in Paris?" },
          // notice that the thinkingBlock is passed in as well as the toolUseBlock
          // if this is not passed in, an error is raised
          { role: "assistant", content: [thinkingBlock, toolUseBlock] },
          { role: "user", content: [{
            type: "tool_result",
            tool_use_id: toolUseBlock.id,
            content: `Current temperature: ${weatherData.temperature}°F`
          }]}
        ]
      });
```
```java
      import java.util.List;
      import java.util.Map;
      import java.util.Optional;

      import com.anthropic.client.AnthropicClient;
      import com.anthropic.client.okhttp.AnthropicOkHttpClient;
      import com.anthropic.core.JsonValue;
      import com.anthropic.models.beta.messages.*;
      import com.anthropic.models.beta.messages.BetaTool.InputSchema;
      import com.anthropic.models.messages.Model;

      public class ThinkingToolsResultExample {
          public static void main(String[] args) {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              InputSchema schema = InputSchema.builder()
                      .properties(JsonValue.from(Map.of(
                              "location", Map.of("type", "string")
                      )))
                      .putAdditionalProperty("required", JsonValue.from(List.of("location")))
                      .build();

              BetaTool weatherTool = BetaTool.builder()
                      .name("get_weather")
                      .description("Get current weather for a location")
                      .inputSchema(schema)
                      .build();

              BetaMessage response = client.beta().messages().create(
                      MessageCreateParams.builder()
                              .model(Model.CLAUDE_OPUS_4_0)
                              .maxTokens(16000)
                              .thinking(BetaThinkingConfigEnabled.builder().budgetTokens(10000).build())
                              .addTool(weatherTool)
                              .addUserMessage("What's the weather in Paris?")
                              .build()
              );

              // Extract thinking block and tool use block
              Optional<BetaThinkingBlock> thinkingBlockOpt = response.content().stream()
                      .filter(BetaContentBlock::isThinking)
                      .map(BetaContentBlock::asThinking)
                      .findFirst();

              Optional<BetaToolUseBlock> toolUseBlockOpt = response.content().stream()
                      .filter(BetaContentBlock::isToolUse)
                      .map(BetaContentBlock::asToolUse)
                      .findFirst();

              if (thinkingBlockOpt.isPresent() && toolUseBlockOpt.isPresent()) {
                  BetaThinkingBlock thinkingBlock = thinkingBlockOpt.get();
                  BetaToolUseBlock toolUseBlock = toolUseBlockOpt.get();

                  // Call your actual weather API, here is where your actual API call would go
                  // let's pretend this is what we get back
                  Map<String, Object> weatherData = Map.of("temperature", 88);

                  // Second request - Include thinking block and tool result
                  // No new thinking blocks will be generated in the response
                  BetaMessage continuation = client.beta().messages().create(
                          MessageCreateParams.builder()
                                  .model(Model.CLAUDE_OPUS_4_0)
                                  .maxTokens(16000)
                                  .thinking(BetaThinkingConfigEnabled.builder().budgetTokens(10000).build())
                                  .addTool(weatherTool)
                                  .addUserMessage("What's the weather in Paris?")
                                  .addAssistantMessageOfBetaContentBlockParams(
                                          // notice that the thinkingBlock is passed in as well as the toolUseBlock
                                          // if this is not passed in, an error is raised
                                          List.of(
                                                  BetaContentBlockParam.ofThinking(thinkingBlock.toParam()),
                                                  BetaContentBlockParam.ofToolUse(toolUseBlock.toParam())
                                          )
                                  )
                                  .addUserMessageOfBetaContentBlockParams(List.of(
                                          BetaContentBlockParam.ofToolResult(
                                                  BetaToolResultBlockParam.builder()
                                                          .toolUseId(toolUseBlock.id())
                                                          .content(String.format("Current temperature: %d°F", (Integer)weatherData.get("temperature")))
                                                          .build()
                                          )
                                  ))
                                  .build()
                  );

                  System.out.println(continuation);
              }
          }
      }
```

    The API response will now **only** include text
```json
    {
        "content": [
            {
                "type": "text",
                "text": "Currently in Paris, the temperature is 88°F (31°C)"
            }
        ]
    }
```
  </Accordion>
</AccordionGroup>

### Preserving thinking blocks

During tool use, you must pass `thinking` blocks back to the API, and you must include the complete unmodified block back to the API. This is critical for maintaining the model's reasoning flow and conversation integrity.

<Tip>
  While you can omit `thinking` blocks from prior `assistant` role turns, we suggest always passing back all thinking blocks to the API for any multi-turn conversation. The API will:

  * Automatically filter the provided thinking blocks
  * Use the relevant thinking blocks necessary to preserve the model's reasoning
  * Only bill for the input tokens for the blocks shown to Claude
</Tip>

>   **📝 Note**
>
> When toggling thinking modes during a conversation, remember that the entire assistant turn (including tool use loops) must operate in a single thinking mode. For more details, see [Toggling thinking modes in conversations](#toggling-thinking-modes-in-conversations).

When Claude invokes tools, it is pausing its construction of a response to await external information. When tool results are returned, Claude will continue building that existing response. This necessitates preserving thinking blocks during tool use, for a couple of reasons:

1. **Reasoning continuity**: The thinking blocks capture Claude's step-by-step reasoning that led to tool requests. When you post tool results, including the original thinking ensures Claude can continue its reasoning from where it left off.

2. **Context maintenance**: While tool results appear as user messages in the API structure, they're part of a continuous reasoning flow. Preserving thinking blocks maintains this conceptual flow across multiple API calls. For more information on context management, see our [guide on context windows](/en/docs/build-with-claude/context-windows).

**Important**: When providing `thinking` blocks, the entire sequence of consecutive `thinking` blocks must match the outputs generated by the model during the original request; you cannot rearrange or modify the sequence of these blocks.

### Interleaved thinking

Extended thinking with tool use in Claude 4 models supports interleaved thinking, which enables Claude to think between tool calls and make more sophisticated reasoning after receiving tool results.

With interleaved thinking, Claude can:

* Reason about the results of a tool call before deciding what to do next
* Chain multiple tool calls with reasoning steps in between
* Make more nuanced decisions based on intermediate results

To enable interleaved thinking, add [the beta header](/en/api/beta-headers) `interleaved-thinking-2025-05-14` to your API request.

Here are some important considerations for interleaved thinking:

* With interleaved thinking, the `budget_tokens` can exceed the `max_tokens` parameter, as it represents the total budget across all thinking blocks within one assistant turn.
* Interleaved thinking is only supported for [tools used via the Messages API](/en/docs/agents-and-tools/tool-use/overview).
* Interleaved thinking is supported for Claude 4 models only, with the beta header `interleaved-thinking-2025-05-14`.
* Direct calls to the Claude API allow you to pass `interleaved-thinking-2025-05-14` in requests to any model, with no effect.
* On 3rd-party platforms (e.g., [Amazon Bedrock](/en/docs/build-with-claude/claude-on-amazon-bedrock) and [Vertex AI](/en/docs/build-with-claude/claude-on-vertex-ai)), if you pass `interleaved-thinking-2025-05-14` to any model aside from Claude Opus 4.1, Opus 4, or Sonnet 4, your request will fail.

<AccordionGroup>
  <Accordion title="Tool use without interleaved thinking">
```python
      import anthropic

      client = anthropic.Anthropic()

      # Define tools

      calculator_tool = {
          "name": "calculator",
          "description": "Perform mathematical calculations",
          "input_schema": {
              "type": "object",
              "properties": {
                  "expression": {
                      "type": "string",
                      "description": "Mathematical expression to evaluate"
                  }
              },
              "required": ["expression"]
          }
      }

      database_tool = {
          "name": "database_query",
          "description": "Query product database",
          "input_schema": {
              "type": "object",
              "properties": {
                  "query": {
                      "type": "string",
                      "description": "SQL query to execute"
                  }
              },
              "required": ["query"]
          }
      }

      # First request - Claude thinks once before all tool calls

      response = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=16000,
          thinking={
              "type": "enabled",
              "budget_tokens": 10000
          },
          tools=[calculator_tool, database_tool],
          messages=[{
              "role": "user",
              "content": "What's the total revenue if we sold 150 units of product A at $50 each, and how does this compare to our average monthly revenue from the database?"
          }]
      )

      # Response includes thinking followed by tool uses

      # Note: Claude thinks once at the beginning, then makes all tool decisions

      print("First response:")
      for block in response.content:
          if block.type == "thinking":
              print(f"Thinking (summarized): {block.thinking}")
          elif block.type == "tool_use":
              print(f"Tool use: {block.name} with input {block.input}")
          elif block.type == "text":
              print(f"Text: {block.text}")

      # You would execute the tools and return results...

      # After getting both tool results back, Claude directly responds without additional thinking

```
```typescript
      import Anthropic from '@anthropic-ai/sdk';

      const client = new Anthropic();

      // Define tools
      const calculatorTool = {
        name: "calculator",
        description: "Perform mathematical calculations",
        input_schema: {
          type: "object",
          properties: {
            expression: {
              type: "string",
              description: "Mathematical expression to evaluate"
            }
          },
          required: ["expression"]
        }
      };

      const databaseTool = {
        name: "database_query",
        description: "Query product database",
        input_schema: {
          type: "object",
          properties: {
            query: {
              type: "string",
              description: "SQL query to execute"
            }
          },
          required: ["query"]
        }
      };

      // First request - Claude thinks once before all tool calls
      const response = await client.messages.create({
        model: "claude-sonnet-4-5",
        max_tokens: 16000,
        thinking: {
          type: "enabled",
          budget_tokens: 10000
        },
        tools: [calculatorTool, databaseTool],
        messages: [{
          role: "user",
          content: "What's the total revenue if we sold 150 units of product A at $50 each, and how does this compare to our average monthly revenue from the database?"
        }]
      });

      // Response includes thinking followed by tool uses
      // Note: Claude thinks once at the beginning, then makes all tool decisions
      console.log("First response:");
      for (const block of response.content) {
        if (block.type === "thinking") {
          console.log(`Thinking (summarized): ${block.thinking}`);
        } else if (block.type === "tool_use") {
          console.log(`Tool use: ${block.name} with input ${JSON.stringify(block.input)}`);
        } else if (block.type === "text") {
          console.log(`Text: ${block.text}`);
        }
      }

      // You would execute the tools and return results...
      // After getting both tool results back, Claude directly responds without additional thinking
```
```java
      import com.anthropic.client.AnthropicClient;
      import com.anthropic.client.okhttp.AnthropicOkHttpClient;
      import com.anthropic.core.JsonValue;
      import com.anthropic.models.beta.messages.*;
      import com.anthropic.models.messages.Model;
      import java.util.List;
      import java.util.Map;

      public class NonInterleavedThinkingExample {
          public static void main(String[] args) {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              // Define calculator tool
              BetaTool.InputSchema calculatorSchema = BetaTool.InputSchema.builder()
                      .properties(JsonValue.from(Map.of(
                              "expression", Map.of(
                                      "type", "string",
                                      "description", "Mathematical expression to evaluate"
                              )
                      )))
                      .putAdditionalProperty("required", JsonValue.from(List.of("expression")))
                      .build();

              BetaTool calculatorTool = BetaTool.builder()
                      .name("calculator")
                      .description("Perform mathematical calculations")
                      .inputSchema(calculatorSchema)
                      .build();

              // Define database tool
              BetaTool.InputSchema databaseSchema = BetaTool.InputSchema.builder()
                      .properties(JsonValue.from(Map.of(
                              "query", Map.of(
                                      "type", "string",
                                      "description", "SQL query to execute"
                              )
                      )))
                      .putAdditionalProperty("required", JsonValue.from(List.of("query")))
                      .build();

              BetaTool databaseTool = BetaTool.builder()
                      .name("database_query")
                      .description("Query product database")
                      .inputSchema(databaseSchema)
                      .build();

              // First request - Claude thinks once before all tool calls
              BetaMessage response = client.beta().messages().create(
                      MessageCreateParams.builder()
                              .model(Model.CLAUDE_OPUS_4_0)
                              .maxTokens(16000)
                              .thinking(BetaThinkingConfigEnabled.builder()
                                      .budgetTokens(10000)
                                      .build())
                              .addTool(calculatorTool)
                              .addTool(databaseTool)
                              .addUserMessage("What's the total revenue if we sold 150 units of product A at $50 each, and how does this compare to our average monthly revenue from the database?")
                              .build()
              );

              // Response includes thinking followed by tool uses
              // Note: Claude thinks once at the beginning, then makes all tool decisions
              System.out.println("First response:");
              for (BetaContentBlock block : response.content()) {
                  if (block.isThinking()) {
                      System.out.println("Thinking (summarized): " + block.asThinking().thinking());
                  } else if (block.isToolUse()) {
                      BetaToolUseBlock toolUse = block.asToolUse();
                      System.out.println("Tool use: " + toolUse.name() + " with input " + toolUse.input());
                  } else if (block.isText()) {
                      System.out.println("Text: " + block.asText().text());
                  }
              }

              // You would execute the tools and return results...
              // After getting both tool results back, Claude directly responds without additional thinking
          }
      }
```

    In this example without interleaved thinking:

    1. Claude thinks once at the beginning to understand the task
    2. Makes all tool use decisions upfront
    3. When tool results are returned, Claude immediately provides a response without additional thinking
  </Accordion>

  <Accordion title="Tool use with interleaved thinking">
```python
      import anthropic

      client = anthropic.Anthropic()

      # Same tool definitions as before

      calculator_tool = {
          "name": "calculator",
          "description": "Perform mathematical calculations",
          "input_schema": {
              "type": "object",
              "properties": {
                  "expression": {
                      "type": "string",
                      "description": "Mathematical expression to evaluate"
                  }
              },
              "required": ["expression"]
          }
      }

      database_tool = {
          "name": "database_query",
          "description": "Query product database",
          "input_schema": {
              "type": "object",
              "properties": {
                  "query": {
                      "type": "string",
                      "description": "SQL query to execute"
                  }
              },
              "required": ["query"]
          }
      }

      # First request with interleaved thinking enabled

      response = client.beta.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=16000,
          thinking={
              "type": "enabled",
              "budget_tokens": 10000
          },
          tools=[calculator_tool, database_tool],
          betas=["interleaved-thinking-2025-05-14"],
          messages=[{
              "role": "user",
              "content": "What's the total revenue if we sold 150 units of product A at $50 each, and how does this compare to our average monthly revenue from the database?"
          }]
      )

      print("Initial response:")
      thinking_blocks = []
      tool_use_blocks = []

      for block in response.content:
          if block.type == "thinking":
              thinking_blocks.append(block)
              print(f"Thinking: {block.thinking}")
          elif block.type == "tool_use":
              tool_use_blocks.append(block)
              print(f"Tool use: {block.name} with input {block.input}")
          elif block.type == "text":
              print(f"Text: {block.text}")

      # First tool result (calculator)

      calculator_result = "7500"  # 150 * 50

      # Continue with first tool result

      response2 = client.beta.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=16000,
          thinking={
              "type": "enabled",
              "budget_tokens": 10000
          },
          tools=[calculator_tool, database_tool],
          betas=["interleaved-thinking-2025-05-14"],
          messages=[
              {
                  "role": "user",
                  "content": "What's the total revenue if we sold 150 units of product A at $50 each, and how does this compare to our average monthly revenue from the database?"
              },
              {
                  "role": "assistant",
                  "content": [thinking_blocks[0], tool_use_blocks[0]]
              },
              {
                  "role": "user",
                  "content": [{
                      "type": "tool_result",
                      "tool_use_id": tool_use_blocks[0].id,
                      "content": calculator_result
                  }]
              }
          ]
      )

      print("\nAfter calculator result:")
      # With interleaved thinking, Claude can think about the calculator result

      # before deciding to query the database

      for block in response2.content:
          if block.type == "thinking":
              thinking_blocks.append(block)
              print(f"Interleaved thinking: {block.thinking}")
          elif block.type == "tool_use":
              tool_use_blocks.append(block)
              print(f"Tool use: {block.name} with input {block.input}")

      # Second tool result (database)

      database_result = "5200"  # Example average monthly revenue

      # Continue with second tool result

      response3 = client.beta.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=16000,
          thinking={
              "type": "enabled",
              "budget_tokens": 10000
          },
          tools=[calculator_tool, database_tool],
          betas=["interleaved-thinking-2025-05-14"],
          messages=[
              {
                  "role": "user",
                  "content": "What's the total revenue if we sold 150 units of product A at $50 each, and how does this compare to our average monthly revenue from the database?"
              },
              {
                  "role": "assistant",
                  "content": [thinking_blocks[0], tool_use_blocks[0]]
              },
              {
                  "role": "user",
                  "content": [{
                      "type": "tool_result",
                      "tool_use_id": tool_use_blocks[0].id,
                      "content": calculator_result
                  }]
              },
              {
                  "role": "assistant",
                  "content": thinking_blocks[1:] + tool_use_blocks[1:]
              },
              {
                  "role": "user",
                  "content": [{
                      "type": "tool_result",
                      "tool_use_id": tool_use_blocks[1].id,
                      "content": database_result
                  }]
              }
          ]
      )

      print("\nAfter database result:")
      # With interleaved thinking, Claude can think about both results

      # before formulating the final response

      for block in response3.content:
          if block.type == "thinking":
              print(f"Final thinking: {block.thinking}")
          elif block.type == "text":
              print(f"Final response: {block.text}")
```
```typescript
      import Anthropic from '@anthropic-ai/sdk';

      const client = new Anthropic();

      // Same tool definitions as before
      const calculatorTool = {
        name: "calculator",
        description: "Perform mathematical calculations",
        input_schema: {
          type: "object",
          properties: {
            expression: {
              type: "string",
              description: "Mathematical expression to evaluate"
            }
          },
          required: ["expression"]
        }
      };

      const databaseTool = {
        name: "database_query",
        description: "Query product database",
        input_schema: {
          type: "object",
          properties: {
            query: {
              type: "string",
              description: "SQL query to execute"
            }
          },
          required: ["query"]
        }
      };

      // First request with interleaved thinking enabled
      const response = await client.beta.messages.create({
        // Enable interleaved thinking
        betas: ["interleaved-thinking-2025-05-14"],
        model: "claude-sonnet-4-5",
        max_tokens: 16000,
        thinking: {
          type: "enabled",
          budget_tokens: 10000
        },
        tools: [calculatorTool, databaseTool],
        messages: [{
          role: "user",
          content: "What's the total revenue if we sold 150 units of product A at $50 each, and how does this compare to our average monthly revenue from the database?"
        }]
      });

      console.log("Initial response:");
      const thinkingBlocks = [];
      const toolUseBlocks = [];

      for (const block of response.content) {
        if (block.type === "thinking") {
          thinkingBlocks.push(block);
          console.log(`Thinking: ${block.thinking}`);
        } else if (block.type === "tool_use") {
          toolUseBlocks.push(block);
          console.log(`Tool use: ${block.name} with input ${JSON.stringify(block.input)}`);
        } else if (block.type === "text") {
          console.log(`Text: ${block.text}`);
        }
      }

      // First tool result (calculator)
      const calculatorResult = "7500"; // 150 * 50

      // Continue with first tool result
      const response2 = await client.beta.messages.create({
        betas: ["interleaved-thinking-2025-05-14"],
        model: "claude-sonnet-4-5",
        max_tokens: 16000,
        thinking: {
          type: "enabled",
          budget_tokens: 10000
        },
        tools: [calculatorTool, databaseTool],
        messages: [
          {
            role: "user",
            content: "What's the total revenue if we sold 150 units of product A at $50 each, and how does this compare to our average monthly revenue from the database?"
          },
          {
            role: "assistant",
            content: [thinkingBlocks[0], toolUseBlocks[0]]
          },
          {
            role: "user",
            content: [{
              type: "tool_result",
              tool_use_id: toolUseBlocks[0].id,
              content: calculatorResult
            }]
          }
        ]
      });

      console.log("\nAfter calculator result:");
      // With interleaved thinking, Claude can think about the calculator result
      // before deciding to query the database
      for (const block of response2.content) {
        if (block.type === "thinking") {
          thinkingBlocks.push(block);
          console.log(`Interleaved thinking: ${block.thinking}`);
        } else if (block.type === "tool_use") {
          toolUseBlocks.push(block);
          console.log(`Tool use: ${block.name} with input ${JSON.stringify(block.input)}`);
        }
      }

      // Second tool result (database)
      const databaseResult = "5200"; // Example average monthly revenue

      // Continue with second tool result
      const response3 = await client.beta.messages.create({
        betas: ["interleaved-thinking-2025-05-14"],
        model: "claude-sonnet-4-5",
        max_tokens: 16000,
        thinking: {
          type: "enabled",
          budget_tokens: 10000
        },
        tools: [calculatorTool, databaseTool],
        messages: [
          {
            role: "user",
            content: "What's the total revenue if we sold 150 units of product A at $50 each, and how does this compare to our average monthly revenue from the database?"
          },
          {
            role: "assistant",
            content: [thinkingBlocks[0], toolUseBlocks[0]]
          },
          {
            role: "user",
            content: [{
              type: "tool_result",
              tool_use_id: toolUseBlocks[0].id,
              content: calculatorResult
            }]
          },
          {
            role: "assistant",
            content: thinkingBlocks.slice(1).concat(toolUseBlocks.slice(1))
          },
          {
            role: "user",
            content: [{
              type: "tool_result",
              tool_use_id: toolUseBlocks[1].id,
              content: databaseResult
            }]
          }
        ]
      });

      console.log("\nAfter database result:");
      // With interleaved thinking, Claude can think about both results
      // before formulating the final response
      for (const block of response3.content) {
        if (block.type === "thinking") {
          console.log(`Final thinking: ${block.thinking}`);
        } else if (block.type === "text") {
          console.log(`Final response: ${block.text}`);
        }
      }
```
```java
      import com.anthropic.client.AnthropicClient;
      import com.anthropic.client.okhttp.AnthropicOkHttpClient;
      import com.anthropic.core.JsonValue;
      import com.anthropic.models.beta.messages.*;
      import com.anthropic.models.messages.Model;
      import java.util.*;
      import static java.util.stream.Collectors.toList;

      public class InterleavedThinkingExample {
          public static void main(String[] args) {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              // Define calculator tool
              BetaTool.InputSchema calculatorSchema = BetaTool.InputSchema.builder()
                      .properties(JsonValue.from(Map.of(
                              "expression", Map.of(
                                      "type", "string",
                                      "description", "Mathematical expression to evaluate"
                              )
                      )))
                      .putAdditionalProperty("required", JsonValue.from(List.of("expression")))
                      .build();

              BetaTool calculatorTool = BetaTool.builder()
                      .name("calculator")
                      .description("Perform mathematical calculations")
                      .inputSchema(calculatorSchema)
                      .build();

              // Define database tool
              BetaTool.InputSchema databaseSchema = BetaTool.InputSchema.builder()
                      .properties(JsonValue.from(Map.of(
                              "query", Map.of(
                                      "type", "string",
                                      "description", "SQL query to execute"
                              )
                      )))
                      .putAdditionalProperty("required", JsonValue.from(List.of("query")))
                      .build();

              BetaTool databaseTool = BetaTool.builder()
                      .name("database_query")
                      .description("Query product database")
                      .inputSchema(databaseSchema)
                      .build();

              // First request with interleaved thinking enabled
              BetaMessage response = client.beta().messages().create(
                      MessageCreateParams.builder()
                              .model(Model.CLAUDE_OPUS_4_0)
                              .maxTokens(16000)
                              .thinking(BetaThinkingConfigEnabled.builder()
                                      .budgetTokens(10000)
                                      .build())
                              .addTool(calculatorTool)
                              .addTool(databaseTool)
                              // Enable interleaved thinking with beta header
                              .putAdditionalHeader("anthropic-beta", "interleaved-thinking-2025-05-14")
                              .addUserMessage("What's the total revenue if we sold 150 units of product A at $50 each, and how does this compare to our average monthly revenue from the database?")
                              .build()
              );

              System.out.println("Initial response:");
              List<BetaThinkingBlock> thinkingBlocks = new ArrayList<>();
              List<BetaToolUseBlock> toolUseBlocks = new ArrayList<>();

              for (BetaContentBlock block : response.content()) {
                  if (block.isThinking()) {
                      BetaThinkingBlock thinking = block.asThinking();
                      thinkingBlocks.add(thinking);
                      System.out.println("Thinking: " + thinking.thinking());
                  } else if (block.isToolUse()) {
                      BetaToolUseBlock toolUse = block.asToolUse();
                      toolUseBlocks.add(toolUse);
                      System.out.println("Tool use: " + toolUse.name() + " with input " + toolUse.input());
                  } else if (block.isText()) {
                      System.out.println("Text: " + block.asText().text());
                  }
              }

              // First tool result (calculator)
              String calculatorResult = "7500"; // 150 * 50

              // Continue with first tool result
              BetaMessage response2 = client.beta().messages().create(
                      MessageCreateParams.builder()
                              .model(Model.CLAUDE_OPUS_4_0)
                              .maxTokens(16000)
                              .thinking(BetaThinkingConfigEnabled.builder()
                                      .budgetTokens(10000)
                                      .build())
                              .addTool(calculatorTool)
                              .addTool(databaseTool)
                              .putAdditionalHeader("anthropic-beta", "interleaved-thinking-2025-05-14")
                              .addUserMessage("What's the total revenue if we sold 150 units of product A at $50 each, and how does this compare to our average monthly revenue from the database?")
                              .addAssistantMessageOfBetaContentBlockParams(List.of(
                                      BetaContentBlockParam.ofThinking(thinkingBlocks.get(0).toParam()),
                                      BetaContentBlockParam.ofToolUse(toolUseBlocks.get(0).toParam())
                              ))
                              .addUserMessageOfBetaContentBlockParams(List.of(
                                      BetaContentBlockParam.ofToolResult(
                                              BetaToolResultBlockParam.builder()
                                                      .toolUseId(toolUseBlocks.get(0).id())
                                                      .content(calculatorResult)
                                                      .build()
                                      )
                              ))
                              .build()
              );

              System.out.println("\nAfter calculator result:");
              // With interleaved thinking, Claude can think about the calculator result
              // before deciding to query the database
              for (BetaContentBlock block : response2.content()) {
                  if (block.isThinking()) {
                      BetaThinkingBlock thinking = block.asThinking();
                      thinkingBlocks.add(thinking);
                      System.out.println("Interleaved thinking: " + thinking.thinking());
                  } else if (block.isToolUse()) {
                      BetaToolUseBlock toolUse = block.asToolUse();
                      toolUseBlocks.add(toolUse);
                      System.out.println("Tool use: " + toolUse.name() + " with input " + toolUse.input());
                  }
              }

              // Second tool result (database)
              String databaseResult = "5200"; // Example average monthly revenue

              // Prepare combined content for assistant message
              List<BetaContentBlockParam> combinedContent = new ArrayList<>();
              for (int i = 1; i < thinkingBlocks.size(); i++) {
                  combinedContent.add(BetaContentBlockParam.ofThinking(thinkingBlocks.get(i).toParam()));
              }
              for (int i = 1; i < toolUseBlocks.size(); i++) {
                  combinedContent.add(BetaContentBlockParam.ofToolUse(toolUseBlocks.get(i).toParam()));
              }

              // Continue with second tool result
              BetaMessage response3 = client.beta().messages().create(
                      MessageCreateParams.builder()
                              .model(Model.CLAUDE_OPUS_4_0)
                              .maxTokens(16000)
                              .thinking(BetaThinkingConfigEnabled.builder()
                                      .budgetTokens(10000)
                                      .build())
                              .addTool(calculatorTool)
                              .addTool(databaseTool)
                              .putAdditionalHeader("anthropic-beta", "interleaved-thinking-2025-05-14")
                              .addUserMessage("What's the total revenue if we sold 150 units of product A at $50 each, and how does this compare to our average monthly revenue from the database?")
                              .addAssistantMessageOfBetaContentBlockParams(List.of(
                                      BetaContentBlockParam.ofThinking(thinkingBlocks.get(0).toParam()),
                                      BetaContentBlockParam.ofToolUse(toolUseBlocks.get(0).toParam())
                              ))
                              .addUserMessageOfBetaContentBlockParams(List.of(
                                      BetaContentBlockParam.ofToolResult(
                                              BetaToolResultBlockParam.builder()
                                                      .toolUseId(toolUseBlocks.get(0).id())
                                                      .content(calculatorResult)
                                                      .build()
                                      )
                              ))
                              .addAssistantMessageOfBetaContentBlockParams(combinedContent)
                              .addUserMessageOfBetaContentBlockParams(List.of(
                                      BetaContentBlockParam.ofToolResult(
                                              BetaToolResultBlockParam.builder()
                                                      .toolUseId(toolUseBlocks.get(1).id())
                                                      .content(databaseResult)
                                                      .build()
                                      )
                              ))
                              .build()
              );

              System.out.println("\nAfter database result:");
              // With interleaved thinking, Claude can think about both results
              // before formulating the final response
              for (BetaContentBlock block : response3.content()) {
                  if (block.isThinking()) {
                      System.out.println("Final thinking: " + block.asThinking().thinking());
                  } else if (block.isText()) {
                      System.out.println("Final response: " + block.asText().text());
                  }
              }
          }
      }
```

    In this example with interleaved thinking:

    1. Claude thinks about the task initially
    2. After receiving the calculator result, Claude can think again about what that result means
    3. Claude then decides how to query the database based on the first result
    4. After receiving the database result, Claude thinks once more about both results before formulating a final response
    5. The thinking budget is distributed across all thinking blocks within the turn

    This pattern allows for more sophisticated reasoning chains where each tool's output informs the next decision.
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
