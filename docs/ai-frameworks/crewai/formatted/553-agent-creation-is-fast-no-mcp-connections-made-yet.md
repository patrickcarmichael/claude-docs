---
title: "Crewai: Agent creation is fast - no MCP connections made yet"
description: "Agent creation is fast - no MCP connections made yet section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Agent creation is fast - no MCP connections made yet

agent = Agent(
    role="On-Demand Agent",
    goal="Use tools efficiently",
    backstory="Efficient agent that connects only when needed",
    mcps=["https://api.example.com/mcp"]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Second agent creation (within 5 minutes) - uses cached tool schemas](./552-second-agent-creation-within-5-minutes-uses-cached.md)

**Next:** [MCP connection is made only when a tool is actually executed →](./554-mcp-connection-is-made-only-when-a-tool-is-actuall.md)
