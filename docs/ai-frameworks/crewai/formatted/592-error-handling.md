---
title: "Crewai: Error Handling"
description: "Error Handling section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Error Handling


The MCP DSL integration is designed to be resilient and handles failures gracefully:

```python  theme={null}
from crewai import Agent
from crewai.mcp import MCPServerStdio, MCPServerHTTP

agent = Agent(
    role="Resilient Agent",
    goal="Continue working despite server issues",
    backstory="Agent that handles failures gracefully",
    mcps=[
        # String references
        "https://reliable-server.com/mcp",        # Will work
        "https://unreachable-server.com/mcp",     # Will be skipped gracefully
        "crewai-amp:working-service",             # Will work

        # Structured configs
        MCPServerStdio(
            command="python",
            args=["reliable_server.py"],          # Will work
        ),
        MCPServerHTTP(
            url="https://slow-server.com/mcp",     # Will timeout gracefully
        ),
    ]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Key Features](./591-key-features.md)

**Next:** [Agent will use tools from working servers and log warnings for failing ones →](./593-agent-will-use-tools-from-working-servers-and-log-.md)
