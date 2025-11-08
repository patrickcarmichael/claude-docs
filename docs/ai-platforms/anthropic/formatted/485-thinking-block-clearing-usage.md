---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Thinking block clearing usage

Enable thinking block clearing to manage context and prompt caching effectively when extended thinking is enabled:
```bash
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "anthropic-beta: context-management-2025-06-27" \
      --data '{
          "model": "claude-sonnet-4-5-20250929",
          "max_tokens": 1024,
          "messages": [...],
          "thinking": {
              "type": "enabled",
              "budget_tokens": 10000
          },
          "context_management": {
              "edits": [
                  {
                      "type": "clear_thinking_20251015",
                      "keep": {
                          "type": "thinking_turns",
                          "value": 2
                      }
                  }
              ]
          }
      }'
```
```python
  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=1024,
      messages=[...],
      thinking={
          "type": "enabled",
          "budget_tokens": 10000
      },
      betas=["context-management-2025-06-27"],
      context_management={
          "edits": [
              {
                  "type": "clear_thinking_20251015",
                  "keep": {
                      "type": "thinking_turns",
                      "value": 2
                  }
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
    model: "claude-sonnet-4-5-20250929",
    max_tokens: 1024,
    messages: [...],
    thinking: {
      type: "enabled",
      budget_tokens: 10000
    },
    betas: ["context-management-2025-06-27"],
    context_management: {
      edits: [
        {
          type: "clear_thinking_20251015",
          keep: {
            type: "thinking_turns",
            value: 2
          }
        }
      ]
    }
  });
```

### Configuration options for thinking block clearing

The `clear_thinking_20251015` strategy supports the following configuration:

| Configuration option | Default                              | Description                                                                                                                                                                                              |
| -------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `keep`               | `{type: "thinking_turns", value: 1}` | Defines how many recent assistant turns with thinking blocks to preserve. Use `{type: "thinking_turns", value: N}` where N must be > 0 to keep the last N turns, or `"all"` to keep all thinking blocks. |

**Example configurations:**
```json
// Keep thinking blocks from the last 3 assistant turns
{
  "type": "clear_thinking_20251015",
  "keep": {
    "type": "thinking_turns",
    "value": 3
  }
}

// Keep all thinking blocks (maximizes cache hits)
{
  "type": "clear_thinking_20251015",
  "keep": "all"
}
```

### Combining strategies

You can use both thinking block clearing and tool result clearing together:

>   **📝 Note**
>
> When using multiple strategies, the `clear_thinking_20251015` strategy must be listed first in the `edits` array.
```python
  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=1024,
      messages=[...],
      thinking={
          "type": "enabled",
          "budget_tokens": 10000
      },
      tools=[...],
      betas=["context-management-2025-06-27"],
      context_management={
          "edits": [
              {
                  "type": "clear_thinking_20251015",
                  "keep": {
                      "type": "thinking_turns",
                      "value": 2
                  }
              },
              {
                  "type": "clear_tool_uses_20250919",
                  "trigger": {
                      "type": "input_tokens",
                      "value": 50000
                  },
                  "keep": {
                      "type": "tool_uses",
                      "value": 5
                  }
              }
          ]
      }
  )
```
```typescript
  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5-20250929",
    max_tokens: 1024,
    messages: [...],
    thinking: {
      type: "enabled",
      budget_tokens: 10000
    },
    tools: [...],
    betas: ["context-management-2025-06-27"],
    context_management: {
      edits: [
        {
          type: "clear_thinking_20251015",
          keep: {
            type: "thinking_turns",
            value: 2
          }
        },
        {
          type: "clear_tool_uses_20250919",
          trigger: {
            type: "input_tokens",
            value: 50000
          },
          keep: {
            type: "tool_uses",
            value: 5
          }
        }
      ]
    }
  });
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
