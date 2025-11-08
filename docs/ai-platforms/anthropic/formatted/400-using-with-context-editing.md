---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

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
```python
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
```typescript
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

You can also exclude memory tool calls from being cleared to ensure Claude always has access to recent memory operations:
```python
  context_management={
      "edits": [
          {
              "type": "clear_tool_uses_20250919",
              "exclude_tools": ["memory"]
          }
      ]
  }
```
```typescript
  context_management: {
    edits: [
      {
        type: "clear_tool_uses_20250919",
        exclude_tools: ["memory"]
      }
    ]
  }
```


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
