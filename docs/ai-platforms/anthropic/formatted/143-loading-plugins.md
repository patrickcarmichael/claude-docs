---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Loading plugins

Load plugins by providing their local file system paths in your options configuration. The SDK supports loading multiple plugins from different locations.
```typescript
  import { query } from "@anthropic-ai/claude-agent-sdk";

  for await (const message of query({
    prompt: "Hello",
    options: {
      plugins: [
        { type: "local", path: "./my-plugin" },
        { type: "local", path: "/absolute/path/to/another-plugin" }
      ]
    }
  })) {
    // Plugin commands, agents, and other features are now available
  }
```
```python
  import asyncio
  from claude_agent_sdk import query

  async def main():
      async for message in query(
          prompt="Hello",
          options={
              "plugins": [
                  {"type": "local", "path": "./my-plugin"},
                  {"type": "local", "path": "/absolute/path/to/another-plugin"}
              ]
          }
      ):
          # Plugin commands, agents, and other features are now available

          pass

  asyncio.run(main())
```

### Path specifications

Plugin paths can be:

* **Relative paths**: Resolved relative to your current working directory (e.g., `"./plugins/my-plugin"`)
* **Absolute paths**: Full file system paths (e.g., `"/home/user/plugins/my-plugin"`)

>   **📝 Note**
>
> The path should point to the plugin's root directory (the directory containing `.claude-plugin/plugin.json`).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
