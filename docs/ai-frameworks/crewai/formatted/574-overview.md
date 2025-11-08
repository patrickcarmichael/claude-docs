---
title: "Crewai: Overview"
description: "Overview section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Overview


The [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) provides a standardized way for AI agents to provide context to LLMs by communicating with external services, known as MCP Servers.

CrewAI offers **two approaches** for MCP integration:

### 🚀 **Simple DSL Integration** (Recommended)

Use the `mcps` field directly on agents for seamless MCP tool integration. The DSL supports both **string references** (for quick setup) and **structured configurations** (for full control).

#### String-Based References (Quick Setup)

Perfect for remote HTTPS servers and CrewAI AMP marketplace:

```python  theme={null}
from crewai import Agent

agent = Agent(
    role="Research Analyst",
    goal="Research and analyze information",
    backstory="Expert researcher with access to external tools",
    mcps=[
        "https://mcp.exa.ai/mcp?api_key=your_key",           # External MCP server
        "https://api.weather.com/mcp#get_forecast",          # Specific tool from server
        "crewai-amp:financial-data",                         # CrewAI AMP marketplace
        "crewai-amp:research-tools#pubmed_search"            # Specific AMP tool
    ]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← MCP Servers as Tools in CrewAI](./573-mcp-servers-as-tools-in-crewai.md)

**Next:** [MCP tools are now automatically available to your agent! →](./575-mcp-tools-are-now-automatically-available-to-your-.md)
