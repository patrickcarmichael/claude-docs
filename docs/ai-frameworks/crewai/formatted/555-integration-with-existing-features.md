---
title: "Crewai: Integration with Existing Features"
description: "Integration with Existing Features section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Integration with Existing Features


MCP tools work seamlessly with other CrewAI features:

```python  theme={null}
from crewai.tools import BaseTool

class CustomTool(BaseTool):
    name: str = "custom_analysis"
    description: str = "Custom analysis tool"

    def _run(self, **kwargs):
        return "Custom analysis result"

agent = Agent(
    role="Full-Featured Agent",
    goal="Use all available tool types",
    backstory="Agent with comprehensive tool access",

    # All tool types work together
    tools=[CustomTool()],                          # Custom tools
    apps=["gmail", "slack"],                       # Platform integrations
    mcps=[                                         # MCP servers
        "https://mcp.exa.ai/mcp?api_key=key",
        "crewai-amp:research-tools"
    ],

    verbose=True,
    max_iter=15
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← MCP connection is made only when a tool is actually executed](./554-mcp-connection-is-made-only-when-a-tool-is-actuall.md)

**Next:** [Best Practices →](./556-best-practices.md)
