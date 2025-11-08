---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Using with the Memory Tool

Context editing can be combined with the [memory tool](/en/docs/agents-and-tools/tool-use/memory-tool). When your conversation context approaches the configured clearing threshold, Claude receives an automatic warning to preserve important information. This enables Claude to save tool results or context to its memory files before they're cleared from the conversation history.

This combination allows you to:

* **Preserve important context**: Claude can write essential information from tool results to memory files before those results are cleared
* **Maintain long-running workflows**: Enable agentic workflows that would otherwise exceed context limits by offloading information to persistent storage
* **Access information on demand**: Claude can look up previously cleared information from memory files when needed, rather than keeping everything in the active context window

For example, in a file editing workflow where Claude performs many operations, Claude can summarize completed changes to memory files as the context grows. When tool results are cleared, Claude retains access to that information through its memory system and can continue working effectively.

To use both features together, enable them in your API request:
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
        { type: "clear_tool_uses_20250919" }
      ]
    }
  });
```


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
