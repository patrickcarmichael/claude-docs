---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Usage Reporting Structure

### Single vs Parallel Tool Use

When Claude executes tools, the usage reporting differs based on whether tools are executed sequentially or in parallel:
```typescript
  import { query } from "@anthropic-ai/claude-agent-sdk";

  // Example: Tracking usage in a conversation
  const result = await query({
    prompt: "Analyze this codebase and run tests",
    options: {
      onMessage: (message) => {
        if (message.type === 'assistant' && message.usage) {
          console.log(`Message ID: ${message.id}`);
          console.log(`Usage:`, message.usage);
        }
      }
    }
  });
```
```python
  from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage
  import asyncio

  # Example: Tracking usage in a conversation

  async def track_usage():
      # Process messages as they arrive

      async for message in query(
          prompt="Analyze this codebase and run tests"
      ):
          if isinstance(message, AssistantMessage) and hasattr(message, 'usage'):
              print(f"Message ID: {message.id}")
              print(f"Usage: {message.usage}")

  asyncio.run(track_usage())
```

### Message Flow Example

Here's how messages and usage are reported in a typical multi-step conversation:
```
<!-- Step 1: Initial request with parallel tool uses -->
assistant (text)      { id: "msg_1", usage: { output_tokens: 100, ... } }
assistant (tool_use)  { id: "msg_1", usage: { output_tokens: 100, ... } }
assistant (tool_use)  { id: "msg_1", usage: { output_tokens: 100, ... } }
assistant (tool_use)  { id: "msg_1", usage: { output_tokens: 100, ... } }
user (tool_result)
user (tool_result)
user (tool_result)

<!-- Step 2: Follow-up response -->
assistant (text)      { id: "msg_2", usage: { output_tokens: 98, ... } }
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
