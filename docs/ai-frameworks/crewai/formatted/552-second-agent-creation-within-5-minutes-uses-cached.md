---
title: "Crewai: Second agent creation (within 5 minutes) - uses cached tool schemas"
description: "Second agent creation (within 5 minutes) - uses cached tool schemas section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Second agent creation (within 5 minutes) - uses cached tool schemas

agent2 = Agent(role="Second", goal="Test", backstory="Test",
               mcps=["https://api.example.com/mcp"])  # Much faster!
```

### On-Demand Connections

Tool connections are established only when tools are actually used:

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← First agent creation - discovers tools from server](./551-first-agent-creation-discovers-tools-from-server.md)

**Next:** [Agent creation is fast - no MCP connections made yet →](./553-agent-creation-is-fast-no-mcp-connections-made-yet.md)
