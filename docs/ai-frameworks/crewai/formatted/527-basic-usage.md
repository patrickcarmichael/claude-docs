---
title: "Crewai: Basic Usage"
description: "Basic Usage section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Basic Usage


Add MCP servers to your agent using the `mcps` field:

```python  theme={null}
from crewai import Agent

agent = Agent(
    role="Research Assistant",
    goal="Help with research and analysis tasks",
    backstory="Expert assistant with access to advanced research tools",
    mcps=[
        "https://mcp.exa.ai/mcp?api_key=your_key&profile=research"
    ]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Overview](./526-overview.md)

**Next:** [MCP tools are now automatically available! →](./528-mcp-tools-are-now-automatically-available.md)
