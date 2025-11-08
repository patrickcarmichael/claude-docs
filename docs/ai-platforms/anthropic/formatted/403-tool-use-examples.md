---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool use examples

Here are a few code examples demonstrating various tool use patterns and techniques. For brevity's sake, the tools are simple tools, and the tool descriptions are shorter than would be ideal to ensure best performance.

<AccordionGroup>
  <Accordion title="Single tool example">
```bash
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
```Python
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
```java
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

    Claude will return a response similar to:
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
    You would then need to execute the `get_weather` function with the provided input, and return the result in a new `user` message:
```bash
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
```Python
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
```java
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

    This will print Claude's final response, incorporating the weather data:
```JSON
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

    >   **📝 Note**
>
>   **Important**: Tool results must be formatted correctly to avoid API errors and ensure Claude continues using parallel tools. See our [implementation guide](/en/docs/agents-and-tools/tool-use/implement-tool-use#parallel-tool-use) for detailed formatting requirements and complete code examples.

    For comprehensive examples, test scripts, and best practices for implementing parallel tool calls, see the [parallel tool use section](/en/docs/agents-and-tools/tool-use/implement-tool-use#parallel-tool-use) in our implementation guide.
  </Accordion>

  <Accordion title="Multiple tool example">
    You can provide Claude with multiple tools to choose from in a single request. Here's an example with both a `get_weather` and a `get_time` tool, along with a user query that asks for both.
```bash
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
```Python
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
```java
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

    In this case, Claude may either:

    * Use the tools sequentially (one at a time) — calling `get_weather` first, then `get_time` after receiving the weather result
    * Use parallel tool calls — outputting multiple `tool_use` blocks in a single response when the operations are independent

    When Claude makes parallel tool calls, you must return all tool results in a single `user` message, with each result in its own `tool_result` block.
  </Accordion>

  <Accordion title="Missing information">
    If the user's prompt doesn't include enough information to fill all the required parameters for a tool, Claude Opus is much more likely to recognize that a parameter is missing and ask for it. Claude Sonnet may ask, especially when prompted to think before outputting a tool request. But it may also do its best to infer a reasonable value.

    For example, using the `get_weather` tool above, if you ask Claude "What's the weather?" without specifying a location, Claude, particularly Claude Sonnet, may make a guess about tools inputs:
```JSON
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
```bash
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
```Python
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
```java
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
```bash
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
```Python
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
```java
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
```javascript
  </Accordion>
</AccordionGroup>

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
