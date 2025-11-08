---
title: "Crewai: Create agent with multiple MCP sources"
description: "Create agent with multiple MCP sources section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agent with multiple MCP sources

multi_source_agent = Agent(
    role="Multi-Source Research Analyst",
    goal="Conduct comprehensive research using multiple data sources",
    backstory="""Expert researcher with access to web search, weather data,
    financial information, and academic research tools""",
    mcps=[
        # External MCP servers
        "https://mcp.exa.ai/mcp?api_key=your_exa_key&profile=research",
        "https://weather.api.com/mcp#get_current_conditions",

        # CrewAI AMP marketplace
        "crewai-amp:financial-insights",
        "crewai-amp:academic-research#pubmed_search",
        "crewai-amp:market-intelligence#competitor_analysis"
    ]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Complete Example](./538-complete-example.md)

**Next:** [Create comprehensive research task →](./540-create-comprehensive-research-task.md)
