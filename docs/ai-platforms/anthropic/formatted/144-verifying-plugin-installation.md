---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Verifying plugin installation

When plugins load successfully, they appear in the system initialization message. You can verify that your plugins are available:
```typescript
  import { query } from "@anthropic-ai/claude-agent-sdk";

  for await (const message of query({
    prompt: "Hello",
    options: {
      plugins: [{ type: "local", path: "./my-plugin" }]
    }
  })) {
    if (message.type === "system" && message.subtype === "init") {
      // Check loaded plugins
      console.log("Plugins:", message.plugins);
      // Example: [{ name: "my-plugin", path: "./my-plugin" }]

      // Check available commands from plugins
      console.log("Commands:", message.slash_commands);
      // Example: ["/help", "/compact", "my-plugin:custom-command"]
    }
  }
```
```python
  import asyncio
  from claude_agent_sdk import query

  async def main():
      async for message in query(
          prompt="Hello",
          options={"plugins": [{"type": "local", "path": "./my-plugin"}]}
      ):
          if message.type == "system" and message.subtype == "init":
              # Check loaded plugins

              print("Plugins:", message.data.get("plugins"))
              # Example: [{"name": "my-plugin", "path": "./my-plugin"}]

              # Check available commands from plugins

              print("Commands:", message.data.get("slash_commands"))
              # Example: ["/help", "/compact", "my-plugin:custom-command"]

  asyncio.run(main())
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
