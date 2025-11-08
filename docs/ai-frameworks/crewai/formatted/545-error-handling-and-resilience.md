---
title: "Crewai: Error Handling and Resilience"
description: "Error Handling and Resilience section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Error Handling and Resilience


The MCP DSL is designed to be robust and user-friendly:

### Graceful Server Failures

```python  theme={null}
agent = Agent(
    role="Resilient Researcher",
    goal="Research despite server issues",
    backstory="Experienced researcher who adapts to available tools",
    mcps=[
        "https://primary-server.com/mcp",         # Primary data source
        "https://backup-server.com/mcp",          # Backup if primary fails
        "https://unreachable-server.com/mcp",     # Will be skipped with warning
        "crewai-amp:reliable-service"             # Reliable AMP service
    ]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Each server's tools get unique prefixes based on the server name](./544-each-servers-tools-get-unique-prefixes-based-on-th.md)

**Next:** [Agent will: →](./546-agent-will.md)
