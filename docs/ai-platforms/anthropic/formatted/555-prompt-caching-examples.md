---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Prompt caching examples

To help you get started with prompt caching, we've prepared a [prompt caching cookbook](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/prompt_caching.ipynb) with detailed examples and best practices.

Below, we've included several code snippets that showcase various prompt caching patterns. These examples demonstrate how to implement caching in different scenarios, helping you understand the practical applications of this feature:

<AccordionGroup>
  <Accordion title="Large context caching example">
```bash
      curl https://api.anthropic.com/v1/messages \
           --header "x-api-key: $ANTHROPIC_API_KEY" \
           --header "anthropic-version: 2023-06-01" \
           --header "content-type: application/json" \
           --data \
      '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 1024,
          "system": [
              {
                  "type": "text",
                  "text": "You are an AI assistant tasked with analyzing legal documents."
              },
              {
                  "type": "text",
                  "text": "Here is the full text of a complex legal agreement: [Insert full text of a 50-page legal agreement here]",
                  "cache_control": {"type": "ephemeral"}
              }
          ],
          "messages": [
              {
                  "role": "user",
                  "content": "What are the key terms and conditions in this agreement?"
              }
          ]
      }'
```
```Python
      import anthropic
      client = anthropic.Anthropic()

      response = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=1024,
          system=[
              {
                  "type": "text",
                  "text": "You are an AI assistant tasked with analyzing legal documents."
              },
              {
                  "type": "text",
                  "text": "Here is the full text of a complex legal agreement: [Insert full text of a 50-page legal agreement here]",
                  "cache_control": {"type": "ephemeral"}
              }
          ],
          messages=[
              {
                  "role": "user",
                  "content": "What are the key terms and conditions in this agreement?"
              }
          ]
      )
      print(response.model_dump_json())
```
```typescript
      import Anthropic from '@anthropic-ai/sdk';

      const client = new Anthropic();

      const response = await client.messages.create({
        model: "claude-sonnet-4-5",
        max_tokens: 1024,
        system: [
          {
              "type": "text",
              "text": "You are an AI assistant tasked with analyzing legal documents."
          },
          {
              "type": "text",
              "text": "Here is the full text of a complex legal agreement: [Insert full text of a 50-page legal agreement here]",
              "cache_control": {"type": "ephemeral"}
          }
        ],
        messages: [
          {
              "role": "user",
              "content": "What are the key terms and conditions in this agreement?"
          }
        ]
      });
      console.log(response);
```
```java
      import java.util.List;

      import com.anthropic.client.AnthropicClient;
      import com.anthropic.client.okhttp.AnthropicOkHttpClient;
      import com.anthropic.models.messages.CacheControlEphemeral;
      import com.anthropic.models.messages.Message;
      import com.anthropic.models.messages.MessageCreateParams;
      import com.anthropic.models.messages.Model;
      import com.anthropic.models.messages.TextBlockParam;

      public class LegalDocumentAnalysisExample {

          public static void main(String[] args) {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              MessageCreateParams params = MessageCreateParams.builder()
                      .model(Model.CLAUDE_OPUS_4_20250514)
                      .maxTokens(1024)
                      .systemOfTextBlockParams(List.of(
                              TextBlockParam.builder()
                                      .text("You are an AI assistant tasked with analyzing legal documents.")
                                      .build(),
                              TextBlockParam.builder()
                                      .text("Here is the full text of a complex legal agreement: [Insert full text of a 50-page legal agreement here]")
                                      .cacheControl(CacheControlEphemeral.builder().build())
                                      .build()
                      ))
                      .addUserMessage("What are the key terms and conditions in this agreement?")
                      .build();

              Message message = client.messages().create(params);
              System.out.println(message);
          }
      }
```

    This example demonstrates basic prompt caching usage, caching the full text of the legal agreement as a prefix while keeping the user instruction uncached.

    For the first request:

    * `input_tokens`: Number of tokens in the user message only
    * `cache_creation_input_tokens`: Number of tokens in the entire system message, including the legal document
    * `cache_read_input_tokens`: 0 (no cache hit on first request)

    For subsequent requests within the cache lifetime:

    * `input_tokens`: Number of tokens in the user message only
    * `cache_creation_input_tokens`: 0 (no new cache creation)
    * `cache_read_input_tokens`: Number of tokens in the entire cached system message
  </Accordion>

  <Accordion title="Caching tool definitions">
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
                              "description": "The unit of temperature, either celsius or fahrenheit"
                          }
                      },
                      "required": ["location"]
                  }
              },
              # many more tools

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
                  },
                  "cache_control": {"type": "ephemeral"}
              }
          ],
          "messages": [
              {
                  "role": "user",
                  "content": "What is the weather and time in New York?"
              }
          ]
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
                  },
              },
              # many more tools

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
                  },
                  "cache_control": {"type": "ephemeral"}
              }
          ],
          messages=[
              {
                  "role": "user",
                  "content": "What's the weather and time in New York?"
              }
          ]
      )
      print(response.model_dump_json())
```
```typescript
      import Anthropic from '@anthropic-ai/sdk';

      const client = new Anthropic();

      const response = await client.messages.create({
          model: "claude-sonnet-4-5",
          max_tokens: 1024,
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
                  },
              },
              // many more tools
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
                  },
                  "cache_control": {"type": "ephemeral"}
              }
          ],
          messages: [
              {
                  "role": "user",
                  "content": "What's the weather and time in New York?"
              }
          ]
      });
      console.log(response);
```
```java
      import java.util.List;
      import java.util.Map;

      import com.anthropic.client.AnthropicClient;
      import com.anthropic.client.okhttp.AnthropicOkHttpClient;
      import com.anthropic.core.JsonValue;
      import com.anthropic.models.messages.CacheControlEphemeral;
      import com.anthropic.models.messages.Message;
      import com.anthropic.models.messages.MessageCreateParams;
      import com.anthropic.models.messages.Model;
      import com.anthropic.models.messages.Tool;
      import com.anthropic.models.messages.Tool.InputSchema;

      public class ToolsWithCacheControlExample {

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
                                      "description", "The unit of temperature, either celsius or fahrenheit"
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
                      .model(Model.CLAUDE_OPUS_4_20250514)
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
                              .cacheControl(CacheControlEphemeral.builder().build())
                              .build())
                      .addUserMessage("What is the weather and time in New York?")
                      .build();

              Message message = client.messages().create(params);
              System.out.println(message);
          }
      }
```

    In this example, we demonstrate caching tool definitions.

    The `cache_control` parameter is placed on the final tool (`get_time`) to designate all of the tools as part of the static prefix.

    This means that all tool definitions, including `get_weather` and any other tools defined before `get_time`, will be cached as a single prefix.

    This approach is useful when you have a consistent set of tools that you want to reuse across multiple requests without re-processing them each time.

    For the first request:

    * `input_tokens`: Number of tokens in the user message
    * `cache_creation_input_tokens`: Number of tokens in all tool definitions and system prompt
    * `cache_read_input_tokens`: 0 (no cache hit on first request)

    For subsequent requests within the cache lifetime:

    * `input_tokens`: Number of tokens in the user message
    * `cache_creation_input_tokens`: 0 (no new cache creation)
    * `cache_read_input_tokens`: Number of tokens in all cached tool definitions and system prompt
  </Accordion>

  <Accordion title="Continuing a multi-turn conversation">
```bash
      curl https://api.anthropic.com/v1/messages \
           --header "x-api-key: $ANTHROPIC_API_KEY" \
           --header "anthropic-version: 2023-06-01" \
           --header "content-type: application/json" \
           --data \
      '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 1024,
          "system": [
              {
                  "type": "text",
                  "text": "...long system prompt",
                  "cache_control": {"type": "ephemeral"}
              }
          ],
          "messages": [
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "text",
                          "text": "Hello, can you tell me more about the solar system?",
                      }
                  ]
              },
              {
                  "role": "assistant",
                  "content": "Certainly! The solar system is the collection of celestial bodies that orbit our Sun. It consists of eight planets, numerous moons, asteroids, comets, and other objects. The planets, in order from closest to farthest from the Sun, are: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. Each planet has its own unique characteristics and features. Is there a specific aspect of the solar system you would like to know more about?"
              },
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "text",
                          "text": "Good to know."
                      },
                      {
                          "type": "text",
                          "text": "Tell me more about Mars.",
                          "cache_control": {"type": "ephemeral"}
                      }
                  ]
              }
          ]
      }'
```
```Python
      import anthropic
      client = anthropic.Anthropic()

      response = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=1024,
          system=[
              {
                  "type": "text",
                  "text": "...long system prompt",
                  "cache_control": {"type": "ephemeral"}
              }
          ],
          messages=[
              # ...long conversation so far

              {
                  "role": "user",
                  "content": [
                      {
                          "type": "text",
                          "text": "Hello, can you tell me more about the solar system?",
                      }
                  ]
              },
              {
                  "role": "assistant",
                  "content": "Certainly! The solar system is the collection of celestial bodies that orbit our Sun. It consists of eight planets, numerous moons, asteroids, comets, and other objects. The planets, in order from closest to farthest from the Sun, are: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. Each planet has its own unique characteristics and features. Is there a specific aspect of the solar system you'd like to know more about?"
              },
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "text",
                          "text": "Good to know."
                      },
                      {
                          "type": "text",
                          "text": "Tell me more about Mars.",
                          "cache_control": {"type": "ephemeral"}
                      }
                  ]
              }
          ]
      )
      print(response.model_dump_json())
```
```typescript
      import Anthropic from '@anthropic-ai/sdk';

      const client = new Anthropic();

      const response = await client.messages.create({
          model: "claude-sonnet-4-5",
          max_tokens: 1024,
          system=[
              {
                  "type": "text",
                  "text": "...long system prompt",
                  "cache_control": {"type": "ephemeral"}
              }
          ],
          messages=[
              // ...long conversation so far
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "text",
                          "text": "Hello, can you tell me more about the solar system?",
                      }
                  ]
              },
              {
                  "role": "assistant",
                  "content": "Certainly! The solar system is the collection of celestial bodies that orbit our Sun. It consists of eight planets, numerous moons, asteroids, comets, and other objects. The planets, in order from closest to farthest from the Sun, are: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. Each planet has its own unique characteristics and features. Is there a specific aspect of the solar system you'd like to know more about?"
              },
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "text",
                          "text": "Good to know."
                      },
                      {
                          "type": "text",
                          "text": "Tell me more about Mars.",
                          "cache_control": {"type": "ephemeral"}
                      }
                  ]
              }
          ]
      });
      console.log(response);
```
```java
      import java.util.List;

      import com.anthropic.client.AnthropicClient;
      import com.anthropic.client.okhttp.AnthropicOkHttpClient;
      import com.anthropic.models.messages.CacheControlEphemeral;
      import com.anthropic.models.messages.ContentBlockParam;
      import com.anthropic.models.messages.Message;
      import com.anthropic.models.messages.MessageCreateParams;
      import com.anthropic.models.messages.Model;
      import com.anthropic.models.messages.TextBlockParam;

      public class ConversationWithCacheControlExample {

          public static void main(String[] args) {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              // Create ephemeral system prompt
              TextBlockParam systemPrompt = TextBlockParam.builder()
                      .text("...long system prompt")
                      .cacheControl(CacheControlEphemeral.builder().build())
                      .build();

              // Create message params
              MessageCreateParams params = MessageCreateParams.builder()
                      .model(Model.CLAUDE_OPUS_4_20250514)
                      .maxTokens(1024)
                      .systemOfTextBlockParams(List.of(systemPrompt))
                      // First user message (without cache control)
                      .addUserMessage("Hello, can you tell me more about the solar system?")
                      // Assistant response
                      .addAssistantMessage("Certainly! The solar system is the collection of celestial bodies that orbit our Sun. It consists of eight planets, numerous moons, asteroids, comets, and other objects. The planets, in order from closest to farthest from the Sun, are: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. Each planet has its own unique characteristics and features. Is there a specific aspect of the solar system you would like to know more about?")
                      // Second user message (with cache control)
                      .addUserMessageOfBlockParams(List.of(
                              ContentBlockParam.ofText(TextBlockParam.builder()
                                      .text("Good to know.")
                                      .build()),
                              ContentBlockParam.ofText(TextBlockParam.builder()
                                      .text("Tell me more about Mars.")
                                      .cacheControl(CacheControlEphemeral.builder().build())
                                      .build())
                      ))
                      .build();

              Message message = client.messages().create(params);
              System.out.println(message);
          }
      }
```

    In this example, we demonstrate how to use prompt caching in a multi-turn conversation.

    During each turn, we mark the final block of the final message with `cache_control` so the conversation can be incrementally cached. The system will automatically lookup and use the longest previously cached prefix for follow-up messages. That is, blocks that were previously marked with a `cache_control` block are later not marked with this, but they will still be considered a cache hit (and also a cache refresh!) if they are hit within 5 minutes.

    In addition, note that the `cache_control` parameter is placed on the system message. This is to ensure that if this gets evicted from the cache (after not being used for more than 5 minutes), it will get added back to the cache on the next request.

    This approach is useful for maintaining context in ongoing conversations without repeatedly processing the same information.

    When this is set up properly, you should see the following in the usage response of each request:

    * `input_tokens`: Number of tokens in the new user message (will be minimal)
    * `cache_creation_input_tokens`: Number of tokens in the new assistant and user turns
    * `cache_read_input_tokens`: Number of tokens in the conversation up to the previous turn
  </Accordion>

  <Accordion title="Putting it all together: Multiple cache breakpoints">
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
                  "name": "search_documents",
                  "description": "Search through the knowledge base",
                  "input_schema": {
                      "type": "object",
                      "properties": {
                          "query": {
                              "type": "string",
                              "description": "Search query"
                          }
                      },
                      "required": ["query"]
                  }
              },
              {
                  "name": "get_document",
                  "description": "Retrieve a specific document by ID",
                  "input_schema": {
                      "type": "object",
                      "properties": {
                          "doc_id": {
                              "type": "string",
                              "description": "Document ID"
                          }
                      },
                      "required": ["doc_id"]
                  },
                  "cache_control": {"type": "ephemeral"}
              }
          ],
          "system": [
              {
                  "type": "text",
                  "text": "You are a helpful research assistant with access to a document knowledge base.\n\n# Instructions\n- Always search for relevant documents before answering\n- Provide citations for your sources\n- Be objective and accurate in your responses\n- If multiple documents contain relevant information, synthesize them\n- Acknowledge when information is not available in the knowledge base",

                  "cache_control": {"type": "ephemeral"}
              },
              {
                  "type": "text",
                  "text": "# Knowledge Base Context\n\nHere are the relevant documents for this conversation:\n\n## Document 1: Solar System Overview\nThe solar system consists of the Sun and all objects that orbit it...\n\n## Document 2: Planetary Characteristics\nEach planet has unique features. Mercury is the smallest planet...\n\n## Document 3: Mars Exploration\nMars has been a target of exploration for decades...\n\n[Additional documents...]",

                  "cache_control": {"type": "ephemeral"}
              }
          ],
          "messages": [
              {
                  "role": "user",
                  "content": "Can you search for information about Mars rovers?"
              },
              {
                  "role": "assistant",
                  "content": [
                      {
                          "type": "tool_use",
                          "id": "tool_1",
                          "name": "search_documents",
                          "input": {"query": "Mars rovers"}
                      }
                  ]
              },
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "tool_result",
                          "tool_use_id": "tool_1",
                          "content": "Found 3 relevant documents: Document 3 (Mars Exploration), Document 7 (Rover Technology), Document 9 (Mission History)"
                      }
                  ]
              },
              {
                  "role": "assistant",
                  "content": [
                      {
                          "type": "text",
                          "text": "I found 3 relevant documents about Mars rovers. Let me get more details from the Mars Exploration document."
                      }
                  ]
              },
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "text",
                          "text": "Yes, please tell me about the Perseverance rover specifically.",
                          "cache_control": {"type": "ephemeral"}
                      }
                  ]
              }
          ]
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
                  "name": "search_documents",
                  "description": "Search through the knowledge base",
                  "input_schema": {
                      "type": "object",
                      "properties": {
                          "query": {
                              "type": "string",
                              "description": "Search query"
                          }
                      },
                      "required": ["query"]
                  }
              },
              {
                  "name": "get_document",
                  "description": "Retrieve a specific document by ID",
                  "input_schema": {
                      "type": "object",
                      "properties": {
                          "doc_id": {
                              "type": "string",
                              "description": "Document ID"
                          }
                      },
                      "required": ["doc_id"]
                  },
                  "cache_control": {"type": "ephemeral"}
              }
          ],
          system=[
              {
                  "type": "text",
                  "text": "You are a helpful research assistant with access to a document knowledge base.\n\n# Instructions\n- Always search for relevant documents before answering\n- Provide citations for your sources\n- Be objective and accurate in your responses\n- If multiple documents contain relevant information, synthesize them\n- Acknowledge when information is not available in the knowledge base",

                  "cache_control": {"type": "ephemeral"}
              },
              {
                  "type": "text",
                  "text": "# Knowledge Base Context\n\nHere are the relevant documents for this conversation:\n\n## Document 1: Solar System Overview\nThe solar system consists of the Sun and all objects that orbit it...\n\n## Document 2: Planetary Characteristics\nEach planet has unique features. Mercury is the smallest planet...\n\n## Document 3: Mars Exploration\nMars has been a target of exploration for decades...\n\n[Additional documents...]",

                  "cache_control": {"type": "ephemeral"}
              }
          ],
          messages=[
              {
                  "role": "user",
                  "content": "Can you search for information about Mars rovers?"
              },
              {
                  "role": "assistant",
                  "content": [
                      {
                          "type": "tool_use",
                          "id": "tool_1",
                          "name": "search_documents",
                          "input": {"query": "Mars rovers"}
                      }
                  ]
              },
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "tool_result",
                          "tool_use_id": "tool_1",
                          "content": "Found 3 relevant documents: Document 3 (Mars Exploration), Document 7 (Rover Technology), Document 9 (Mission History)"
                      }
                  ]
              },
              {
                  "role": "assistant",
                  "content": [
                      {
                          "type": "text",
                          "text": "I found 3 relevant documents about Mars rovers. Let me get more details from the Mars Exploration document."
                      }
                  ]
              },
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "text",
                          "text": "Yes, please tell me about the Perseverance rover specifically.",
                          "cache_control": {"type": "ephemeral"}
                      }
                  ]
              }
          ]
      )
      print(response.model_dump_json())
```
```typescript
      import Anthropic from '@anthropic-ai/sdk';

      const client = new Anthropic();

      const response = await client.messages.create({
          model: "claude-sonnet-4-5",
          max_tokens: 1024,
          tools: [
              {
                  name: "search_documents",
                  description: "Search through the knowledge base",
                  input_schema: {
                      type: "object",
                      properties: {
                          query: {
                              type: "string",
                              description: "Search query"
                          }
                      },
                      required: ["query"]
                  }
              },
              {
                  name: "get_document",
                  description: "Retrieve a specific document by ID",
                  input_schema: {
                      type: "object",
                      properties: {
                          doc_id: {
                              type: "string",
                              description: "Document ID"
                          }
                      },
                      required: ["doc_id"]
                  },
                  cache_control: { type: "ephemeral" }
              }
          ],
          system: [
              {
                  type: "text",
                  text: "You are a helpful research assistant with access to a document knowledge base.\n\n# Instructions\n- Always search for relevant documents before answering\n- Provide citations for your sources\n- Be objective and accurate in your responses\n- If multiple documents contain relevant information, synthesize them\n- Acknowledge when information is not available in the knowledge base",

                  cache_control: { type: "ephemeral" }
              },
              {
                  type: "text",
                  text: "# Knowledge Base Context\n\nHere are the relevant documents for this conversation:\n\n## Document 1: Solar System Overview\nThe solar system consists of the Sun and all objects that orbit it...\n\n## Document 2: Planetary Characteristics\nEach planet has unique features. Mercury is the smallest planet...\n\n## Document 3: Mars Exploration\nMars has been a target of exploration for decades...\n\n[Additional documents...]",

                  cache_control: { type: "ephemeral" }
              }
          ],
          messages: [
              {
                  role: "user",
                  content: "Can you search for information about Mars rovers?"
              },
              {
                  role: "assistant",
                  content: [
                      {
                          type: "tool_use",
                          id: "tool_1",
                          name: "search_documents",
                          input: { query: "Mars rovers" }
                      }
                  ]
              },
              {
                  role: "user",
                  content: [
                      {
                          type: "tool_result",
                          tool_use_id: "tool_1",
                          content: "Found 3 relevant documents: Document 3 (Mars Exploration), Document 7 (Rover Technology), Document 9 (Mission History)"
                      }
                  ]
              },
              {
                  role: "assistant",
                  content: [
                      {
                          type: "text",
                          text: "I found 3 relevant documents about Mars rovers. Let me get more details from the Mars Exploration document."
                      }
                  ]
              },
              {
                  role: "user",
                  content: [
                      {
                          type: "text",
                          text: "Yes, please tell me about the Perseverance rover specifically.",
                          cache_control: { type: "ephemeral" }
                      }
                  ]
              }
          ]
      });
      console.log(response);
```
```java
      import java.util.List;
      import java.util.Map;

      import com.anthropic.client.AnthropicClient;
      import com.anthropic.client.okhttp.AnthropicOkHttpClient;
      import com.anthropic.core.JsonValue;
      import com.anthropic.models.messages.CacheControlEphemeral;
      import com.anthropic.models.messages.ContentBlockParam;
      import com.anthropic.models.messages.Message;
      import com.anthropic.models.messages.MessageCreateParams;
      import com.anthropic.models.messages.Model;
      import com.anthropic.models.messages.TextBlockParam;
      import com.anthropic.models.messages.Tool;
      import com.anthropic.models.messages.Tool.InputSchema;
      import com.anthropic.models.messages.ToolResultBlockParam;
      import com.anthropic.models.messages.ToolUseBlockParam;

      public class MultipleCacheBreakpointsExample {

          public static void main(String[] args) {
              AnthropicClient client = AnthropicOkHttpClient.fromEnv();

              // Search tool schema
              InputSchema searchSchema = InputSchema.builder()
                      .properties(JsonValue.from(Map.of(
                              "query", Map.of(
                                      "type", "string",
                                      "description", "Search query"
                              )
                      )))
                      .putAdditionalProperty("required", JsonValue.from(List.of("query")))
                      .build();

              // Get document tool schema
              InputSchema getDocSchema = InputSchema.builder()
                      .properties(JsonValue.from(Map.of(
                              "doc_id", Map.of(
                                      "type", "string",
                                      "description", "Document ID"
                              )
                      )))
                      .putAdditionalProperty("required", JsonValue.from(List.of("doc_id")))
                      .build();

              MessageCreateParams params = MessageCreateParams.builder()
                      .model(Model.CLAUDE_OPUS_4_20250514)
                      .maxTokens(1024)
                      // Tools with cache control on the last one
                      .addTool(Tool.builder()
                              .name("search_documents")
                              .description("Search through the knowledge base")
                              .inputSchema(searchSchema)
                              .build())
                      .addTool(Tool.builder()
                              .name("get_document")
                              .description("Retrieve a specific document by ID")
                              .inputSchema(getDocSchema)
                              .cacheControl(CacheControlEphemeral.builder().build())
                              .build())
                      // System prompts with cache control on instructions and context separately
                      .systemOfTextBlockParams(List.of(
                              TextBlockParam.builder()
                                      .text("You are a helpful research assistant with access to a document knowledge base.\n\n# Instructions\n- Always search for relevant documents before answering\n- Provide citations for your sources\n- Be objective and accurate in your responses\n- If multiple documents contain relevant information, synthesize them\n- Acknowledge when information is not available in the knowledge base")

                                      .cacheControl(CacheControlEphemeral.builder().build())
                                      .build(),
                              TextBlockParam.builder()
                                      .text("# Knowledge Base Context\n\nHere are the relevant documents for this conversation:\n\n## Document 1: Solar System Overview\nThe solar system consists of the Sun and all objects that orbit it...\n\n## Document 2: Planetary Characteristics\nEach planet has unique features. Mercury is the smallest planet...\n\n## Document 3: Mars Exploration\nMars has been a target of exploration for decades...\n\n[Additional documents...]")

                                      .cacheControl(CacheControlEphemeral.builder().build())
                                      .build()
                      ))
                      // Conversation history
                      .addUserMessage("Can you search for information about Mars rovers?")
                      .addAssistantMessageOfBlockParams(List.of(
                              ContentBlockParam.ofToolUse(ToolUseBlockParam.builder()
                                      .id("tool_1")
                                      .name("search_documents")
                                      .input(JsonValue.from(Map.of("query", "Mars rovers")))
                                      .build())
                      ))
                      .addUserMessageOfBlockParams(List.of(
                              ContentBlockParam.ofToolResult(ToolResultBlockParam.builder()
                                      .toolUseId("tool_1")
                                      .content("Found 3 relevant documents: Document 3 (Mars Exploration), Document 7 (Rover Technology), Document 9 (Mission History)")
                                      .build())
                      ))
                      .addAssistantMessageOfBlockParams(List.of(
                              ContentBlockParam.ofText(TextBlockParam.builder()
                                      .text("I found 3 relevant documents about Mars rovers. Let me get more details from the Mars Exploration document.")
                                      .build())
                      ))
                      .addUserMessageOfBlockParams(List.of(
                              ContentBlockParam.ofText(TextBlockParam.builder()
                                      .text("Yes, please tell me about the Perseverance rover specifically.")
                                      .cacheControl(CacheControlEphemeral.builder().build())
                                      .build())
                      ))
                      .build();

              Message message = client.messages().create(params);
              System.out.println(message);
          }
      }
```

    This comprehensive example demonstrates how to use all 4 available cache breakpoints to optimize different parts of your prompt:

    1. **Tools cache** (cache breakpoint 1): The `cache_control` parameter on the last tool definition caches all tool definitions.

    2. **Reusable instructions cache** (cache breakpoint 2): The static instructions in the system prompt are cached separately. These instructions rarely change between requests.

    3. **RAG context cache** (cache breakpoint 3): The knowledge base documents are cached independently, allowing you to update the RAG documents without invalidating the tools or instructions cache.

    4. **Conversation history cache** (cache breakpoint 4): The assistant's response is marked with `cache_control` to enable incremental caching of the conversation as it progresses.

    This approach provides maximum flexibility:

    * If you only update the final user message, all four cache segments are reused
    * If you update the RAG documents but keep the same tools and instructions, the first two cache segments are reused
    * If you change the conversation but keep the same tools, instructions, and documents, the first three segments are reused
    * Each cache breakpoint can be invalidated independently based on what changes in your application

    For the first request:

    * `input_tokens`: Tokens in the final user message
    * `cache_creation_input_tokens`: Tokens in all cached segments (tools + instructions + RAG documents + conversation history)
    * `cache_read_input_tokens`: 0 (no cache hits)

    For subsequent requests with only a new user message:

    * `input_tokens`: Tokens in the new user message only
    * `cache_creation_input_tokens`: Any new tokens added to conversation history
    * `cache_read_input_tokens`: All previously cached tokens (tools + instructions + RAG documents + previous conversation)

    This pattern is especially powerful for:

    * RAG applications with large document contexts
    * Agent systems that use multiple tools
    * Long-running conversations that need to maintain context
    * Applications that need to optimize different parts of the prompt independently
  </Accordion>
</AccordionGroup>

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
