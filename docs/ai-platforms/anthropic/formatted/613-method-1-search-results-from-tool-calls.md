---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Method 1: Search results from tool calls

The most powerful use case is returning search results from your custom tools. This enables dynamic RAG applications where tools fetch and return relevant content with automatic citations.

### Example: Knowledge base tool

```python
  from anthropic import Anthropic
  from anthropic.types import (
      MessageParam,
      TextBlockParam,
      SearchResultBlockParam,
      ToolResultBlockParam
  )

  client = Anthropic()

  # Define a knowledge base search tool

  knowledge_base_tool = {
      "name": "search_knowledge_base",
      "description": "Search the company knowledge base for information",
      "input_schema": {
          "type": "object",
          "properties": {
              "query": {
                  "type": "string",
                  "description": "The search query"
              }
          },
          "required": ["query"]
      }
  }

  # Function to handle the tool call

  def search_knowledge_base(query):
      # Your search logic here

      # Returns search results in the correct format

      return [
          SearchResultBlockParam(
              type="search_result",
              source="https://docs.company.com/product-guide",
              title="Product Configuration Guide",
              content=[
                  TextBlockParam(
                      type="text",
                      text="To configure the product, navigate to Settings > Configuration. The default timeout is 30 seconds, but can be adjusted between 10-120 seconds based on your needs."
                  )
              ],
              citations={"enabled": True}
          ),
          SearchResultBlockParam(
              type="search_result",
              source="https://docs.company.com/troubleshooting",
              title="Troubleshooting Guide",
              content=[
                  TextBlockParam(
                      type="text",
                      text="If you encounter timeout errors, first check the configuration settings. Common causes include network latency and incorrect timeout values."
                  )
              ],
              citations={"enabled": True}
          )
      ]

  # Create a message with the tool

  response = client.messages.create(
      model="claude-sonnet-4-5",  # Works with all supported models

      max_tokens=1024,
      tools=[knowledge_base_tool],
      messages=[
          MessageParam(
              role="user",
              content="How do I configure the timeout settings?"
          )
      ]
  )

  # When Claude calls the tool, provide the search results

  if response.content[0].type == "tool_use":
      tool_result = search_knowledge_base(response.content[0].input["query"])
      
      # Send the tool result back

      final_response = client.messages.create(
          model="claude-sonnet-4-5",  # Works with all supported models

          max_tokens=1024,
          messages=[
              MessageParam(role="user", content="How do I configure the timeout settings?"),
              MessageParam(role="assistant", content=response.content),
              MessageParam(
                  role="user",
                  content=[
                      ToolResultBlockParam(
                          type="tool_result",
                          tool_use_id=response.content[0].id,
                          content=tool_result  # Search results go here

                      )
                  ]
              )
          ]
      )
```
```typescript
  import { Anthropic } from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  // Define a knowledge base search tool
  const knowledgeBaseTool = {
    name: "search_knowledge_base",
    description: "Search the company knowledge base for information",
    input_schema: {
      type: "object",
      properties: {
        query: {
          type: "string",
          description: "The search query"
        }
      },
      required: ["query"]
    }
  };

  // Function to handle the tool call
  function searchKnowledgeBase(query: string) {
    // Your search logic here
    // Returns search results in the correct format
    return [
      {
        type: "search_result" as const,
        source: "https://docs.company.com/product-guide",
        title: "Product Configuration Guide",
        content: [
          {
            type: "text" as const,
            text: "To configure the product, navigate to Settings > Configuration. The default timeout is 30 seconds, but can be adjusted between 10-120 seconds based on your needs."
          }
        ],
        citations: { enabled: true }
      },
      {
        type: "search_result" as const,
        source: "https://docs.company.com/troubleshooting",
        title: "Troubleshooting Guide",
        content: [
          {
            type: "text" as const,
            text: "If you encounter timeout errors, first check the configuration settings. Common causes include network latency and incorrect timeout values."
          }
        ],
        citations: { enabled: true }
      }
    ];
  }

  // Create a message with the tool
  const response = await anthropic.messages.create({
    model: "claude-sonnet-4-5", // Works with all supported models
    max_tokens: 1024,
    tools: [knowledgeBaseTool],
    messages: [
      {
        role: "user",
        content: "How do I configure the timeout settings?"
      }
    ]
  });

  // Handle tool use and provide results
  if (response.content[0].type === "tool_use") {
    const toolResult = searchKnowledgeBase(response.content[0].input.query);
    
    const finalResponse = await anthropic.messages.create({
      model: "claude-sonnet-4-5", // Works with all supported models
      max_tokens: 1024,
        messages: [
        { role: "user", content: "How do I configure the timeout settings?" },
        { role: "assistant", content: response.content },
        {
          role: "user",
          content: [
            {
              type: "tool_result" as const,
              tool_use_id: response.content[0].id,
              content: toolResult  // Search results go here
            }
          ]
        }
      ]
    });
  }
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
