---
title: "Crewai: Original MCP server has tools: "search", "analyze""
description: "Original MCP server has tools: "search", "analyze" section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Original MCP server has tools: "search", "analyze"

# CrewAI creates tools: "mcp_exa_ai_search", "mcp_exa_ai_analyze"

agent = Agent(
    role="Tool Organization Demo",
    goal="Show how tool naming works",
    backstory="Demonstrates automatic tool organization",
    mcps=[
        "https://mcp.exa.ai/mcp?api_key=key",      # Tools: mcp_exa_ai_*
        "https://weather.service.com/mcp",         # Tools: weather_service_com_*
        "crewai-amp:financial-data"                # Tools: financial_data_*
    ]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Tool Naming and Organization](./542-tool-naming-and-organization.md)

**Next:** [Each server's tools get unique prefixes based on the server name →](./544-each-servers-tools-get-unique-prefixes-based-on-th.md)
