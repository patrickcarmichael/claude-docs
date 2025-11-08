---
title: "Crewai: Create agent with MCP tools using string references"
description: "Create agent with MCP tools using string references section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agent with MCP tools using string references

research_agent = Agent(
    role="Research Analyst",
    goal="Find and analyze information using advanced search tools",
    backstory="Expert researcher with access to multiple data sources",
    mcps=[
        "https://mcp.exa.ai/mcp?api_key=your_key&profile=your_profile",
        "crewai-amp:weather-service#current_conditions"
    ]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Quick Start: Simple DSL Integration](./580-quick-start-simple-dsl-integration.md)

**Next:** [Create task →](./582-create-task.md)
