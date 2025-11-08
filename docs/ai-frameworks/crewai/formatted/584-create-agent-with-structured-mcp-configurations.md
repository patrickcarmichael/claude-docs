---
title: "Crewai: Create agent with structured MCP configurations"
description: "Create agent with structured MCP configurations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agent with structured MCP configurations

research_agent = Agent(
    role="Research Analyst",
    goal="Find and analyze information using advanced search tools",
    backstory="Expert researcher with access to multiple data sources",
    mcps=[
        # Local stdio server
        MCPServerStdio(
            command="python",
            args=["local_server.py"],
            env={"API_KEY": "your_key"},
        ),
        # Remote HTTP server
        MCPServerHTTP(
            url="https://api.research.com/mcp",
            headers={"Authorization": "Bearer your_token"},
        ),
    ]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create and run crew](./583-create-and-run-crew.md)

**Next:** [Create task →](./585-create-task.md)
