---
title: "Crewai: Create and run crew"
description: "Create and run crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create and run crew

crew = Crew(agents=[research_agent], tasks=[research_task])
result = crew.kickoff()
```

### Quick Start with Structured Configurations

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai.mcp import MCPServerStdio, MCPServerHTTP, MCPServerSSE

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create task](./582-create-task.md)

**Next:** [Create agent with structured MCP configurations →](./584-create-agent-with-structured-mcp-configurations.md)
