---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool result clearing usage

The simplest way to enable tool result clearing is to specify only the strategy type, as all other [configuration options](#configuration-options-for-tool-result-clearing) will use their default values:
```bash
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "anthropic-beta: context-management-2025-06-27" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [
              {
                  "role": "user",
                  "content": "Search for recent developments in AI"
              }
          ],
          "tools": [
              {
                  "type": "web_search_20250305",
                  "name": "web_search"
              }
          ],
          "context_management": {
              "edits": [
                  {"type": "clear_tool_uses_20250919"}
              ]
          }
      }'
```
```python
  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=4096,
      messages=[
          {
              "role": "user",
              "content": "Search for recent developments in AI"
          }
      ],
      tools=[
          {
              "type": "web_search_20250305",
              "name": "web_search"
          }
      ],
      betas=["context-management-2025-06-27"],
      context_management={
          "edits": [
              {"type": "clear_tool_uses_20250919"}
          ]
      }
  )
```
```typescript
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content: "Search for recent developments in AI"
      }
    ],
    tools: [
      {
        type: "web_search_20250305",
        name: "web_search"
      }
    ],
    context_management: {
      edits: [
        { type: "clear_tool_uses_20250919" }
      ]
    },
    betas: ["context-management-2025-06-27"]
  });
```

### Advanced configuration

You can customize the tool result clearing behavior with additional parameters:
```bash
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "anthropic-beta: context-management-2025-06-27" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [
              {
                  "role": "user",
                  "content": "Create a simple command line calculator app using Python"
              }
          ],
          "tools": [
              {
                  "type": "text_editor_20250728",
                  "name": "str_replace_based_edit_tool",
                  "max_characters": 10000
              },
              {
                  "type": "web_search_20250305",
                  "name": "web_search",
                  "max_uses": 3
              }
          ],
          "context_management": {
              "edits": [
                  {
                      "type": "clear_tool_uses_20250919",
                      "trigger": {
                          "type": "input_tokens",
                          "value": 30000
                      },
                      "keep": {
                          "type": "tool_uses",
                          "value": 3
                      },
                      "clear_at_least": {
                          "type": "input_tokens",
                          "value": 5000
                      },
                      "exclude_tools": ["web_search"]
                  }
              ]
          }
      }'
```
```python
  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=4096,
      messages=[
          {
              "role": "user",
              "content": "Create a simple command line calculator app using Python"
          }
      ],
      tools=[
          {
              "type": "text_editor_20250728",
              "name": "str_replace_based_edit_tool",
              "max_characters": 10000
          },
          {
              "type": "web_search_20250305",
              "name": "web_search",
              "max_uses": 3
          }
      ],
      betas=["context-management-2025-06-27"],
      context_management={
          "edits": [
              {
                  "type": "clear_tool_uses_20250919",
                  # Trigger clearing when threshold is exceeded

                  "trigger": {
                      "type": "input_tokens",
                      "value": 30000
                  },
                  # Number of tool uses to keep after clearing

                  "keep": {
                      "type": "tool_uses",
                      "value": 3
                  },
                  # Optional: Clear at least this many tokens

                  "clear_at_least": {
                      "type": "input_tokens",
                      "value": 5000
                  },
                  # Exclude these tools from being cleared

                  "exclude_tools": ["web_search"]
              }
          ]
      }
  )
```
```typescript
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content: "Create a simple command line calculator app using Python"
      }
    ],
    tools: [
      {
        type: "text_editor_20250728",
        name: "str_replace_based_edit_tool",
        max_characters: 10000
      },
      {
        type: "web_search_20250305",
        name: "web_search",
        max_uses: 3
      }
    ],
    betas: ["context-management-2025-06-27"],
    context_management: {
      edits: [
        {
          type: "clear_tool_uses_20250919",
          // Trigger clearing when threshold is exceeded
          trigger: {
            type: "input_tokens",
            value: 30000
          },
          // Number of tool uses to keep after clearing
          keep: {
            type: "tool_uses",
            value: 3
          },
          // Optional: Clear at least this many tokens
          clear_at_least: {
            type: "input_tokens",
            value: 5000
          },
          // Exclude these tools from being cleared
          exclude_tools: ["web_search"]
        }
      ]
    }
  });
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
