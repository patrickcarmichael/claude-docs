---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Troubleshooting

### Skills Not Found

**Check settingSources configuration**: Skills are only loaded when you explicitly configure `settingSources`/`setting_sources`. This is the most common issue:
```python
  # Wrong - Skills won't be loaded

  options = ClaudeAgentOptions(
      allowed_tools=["Skill"]
  )

  # Correct - Skills will be loaded

  options = ClaudeAgentOptions(
      setting_sources=["user", "project"],  # Required to load Skills

      allowed_tools=["Skill"]
  )
```
```typescript
  // Wrong - Skills won't be loaded
  const options = {
    allowedTools: ["Skill"]
  };

  // Correct - Skills will be loaded
  const options = {
    settingSources: ["user", "project"],  // Required to load Skills
    allowedTools: ["Skill"]
  };
```

For more details on `settingSources`/`setting_sources`, see the [TypeScript SDK reference](/en/docs/agent-sdk/typescript#settingsource) or [Python SDK reference](/en/docs/agent-sdk/python#settingsource).

**Check working directory**: The SDK loads Skills relative to the `cwd` option. Ensure it points to a directory containing `.claude/skills/`:
```python
  # Ensure your cwd points to the directory containing .claude/skills/

  options = ClaudeAgentOptions(
      cwd="/path/to/project",  # Must contain .claude/skills/

      setting_sources=["user", "project"],  # Required to load Skills

      allowed_tools=["Skill"]
  )
```
```typescript
  // Ensure your cwd points to the directory containing .claude/skills/
  const options = {
    cwd: "/path/to/project",  // Must contain .claude/skills/
    settingSources: ["user", "project"],  // Required to load Skills
    allowedTools: ["Skill"]
  };
```

See the "Using Skills with the SDK" section above for the complete pattern.

**Verify filesystem location**:
```bash

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
