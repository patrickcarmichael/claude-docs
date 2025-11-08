---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Using plugin commands

Commands from plugins are automatically namespaced with the plugin name to avoid conflicts. The format is `plugin-name:command-name`.
```typescript
  import { query } from "@anthropic-ai/claude-agent-sdk";

  // Load a plugin with a custom /greet command
  for await (const message of query({
    prompt: "/my-plugin:greet",  // Use plugin command with namespace
    options: {
      plugins: [{ type: "local", path: "./my-plugin" }]
    }
  })) {
    // Claude executes the custom greeting command from the plugin
    if (message.type === "assistant") {
      console.log(message.content);
    }
  }
```
```python
  import asyncio
  from claude_agent_sdk import query, AssistantMessage, TextBlock

  async def main():
      # Load a plugin with a custom /greet command

      async for message in query(
          prompt="/demo-plugin:greet",  # Use plugin command with namespace

          options={"plugins": [{"type": "local", "path": "./plugins/demo-plugin"}]}
      ):
          # Claude executes the custom greeting command from the plugin

          if isinstance(message, AssistantMessage):
              for block in message.content:
                  if isinstance(block, TextBlock):
                      print(f"Claude: {block.text}")

  asyncio.run(main())
```

>   **📝 Note**
>
> If you installed a plugin via the CLI (e.g., `/plugin install my-plugin@marketplace`), you can still use it in the SDK by providing its installation path. Check `~/.claude/plugins/` for CLI-installed plugins.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
