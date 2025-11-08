---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool Restrictions

>   **📝 Note**
>
> The `allowed-tools` frontmatter field in SKILL.md is only supported when using Claude Code CLI directly. **It does not apply when using Skills through the SDK**.

  When using the SDK, control tool access through the main `allowedTools` option in your query configuration.

To restrict tools for Skills in SDK applications, use the `allowedTools` option:

>   **📝 Note**
>
> Import statements from the first example are assumed in the following code snippets.
```python
  options = ClaudeAgentOptions(
      setting_sources=["user", "project"],  # Load Skills from filesystem

      allowed_tools=["Skill", "Read", "Grep", "Glob"]  # Restricted toolset

  )

  async for message in query(
      prompt="Analyze the codebase structure",
      options=options
  ):
      print(message)
```
```typescript
  // Skills can only use Read, Grep, and Glob tools
  for await (const message of query({
    prompt: "Analyze the codebase structure",
    options: {
      settingSources: ["user", "project"],  // Load Skills from filesystem
      allowedTools: ["Skill", "Read", "Grep", "Glob"]  // Restricted toolset
    }
  })) {
    console.log(message);
  }
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
