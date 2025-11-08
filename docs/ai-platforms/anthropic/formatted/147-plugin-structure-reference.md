---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Plugin structure reference

A plugin directory must contain a `.claude-plugin/plugin.json` manifest file. It can optionally include:
```
my-plugin/
├── .claude-plugin/
│   └── plugin.json          # Required: plugin manifest

├── commands/                 # Custom slash commands

│   └── custom-cmd.md
├── agents/                   # Custom agents

│   └── specialist.md
├── skills/                   # Agent Skills

│   └── my-skill/
│       └── SKILL.md
├── hooks/                    # Event handlers

│   └── hooks.json
└── .mcp.json                # MCP server definitions

```

For detailed information on creating plugins, see:

* [Plugins](https://code.claude.com/docs/plugins) - Complete plugin development guide
* [Plugins reference](https://code.claude.com/docs/plugins-reference) - Technical specifications and schemas

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
