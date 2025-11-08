---
title: "Crewai: Dynamic filtering (context-aware)"
description: "Dynamic filtering (context-aware) section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Dynamic filtering (context-aware)

def dynamic_filter(context: ToolFilterContext, tool: dict) -> bool:
    # Block dangerous tools for certain agent roles
    if context.agent.role == "Code Reviewer":
        if "delete" in tool.get("name", "").lower():
            return False
    return True

mcps=[
    MCPServerStdio(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem"],
        tool_filter=static_filter,  # or dynamic_filter
    ),
]
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Static filtering (allow/block lists)](./588-static-filtering-allowblock-lists.md)

**Next:** [Configuration Parameters →](./590-configuration-parameters.md)
