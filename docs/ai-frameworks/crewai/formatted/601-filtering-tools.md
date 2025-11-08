---
title: "Crewai: Filtering Tools"
description: "Filtering Tools section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Filtering Tools


There are two ways to filter tools:

1. Accessing a specific tool using dictionary-style indexing.
2. Pass a list of tool names to the `MCPServerAdapter` constructor.

### Accessing a specific tool using dictionary-style indexing.

```python  theme={null}
with MCPServerAdapter(server_params, connect_timeout=60) as mcp_tools:
    print(f"Available tools: {[tool.name for tool in mcp_tools]}")

    my_agent = Agent(
        role="MCP Tool User",
        goal="Utilize tools from an MCP server.",
        backstory="I can connect to MCP servers and use their tools.",
        tools=[mcp_tools["tool_name"]], # Pass the loaded tools to your agent
        reasoning=True,
        verbose=True
    )
    # ... rest of your crew setup ...
```

### Pass a list of tool names to the `MCPServerAdapter` constructor.

```python  theme={null}
with MCPServerAdapter(server_params, "tool_name", connect_timeout=60) as mcp_tools:
    print(f"Available tools: {[tool.name for tool in mcp_tools]}")

    my_agent = Agent(
        role="MCP Tool User",
        goal="Utilize tools from an MCP server.",
        backstory="I can connect to MCP servers and use their tools.",
        tools=mcp_tools, # Pass the loaded tools to your agent
        reasoning=True,
        verbose=True
    )
    # ... rest of your crew setup ...
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example usage (uncomment and adapt once server_params is set):](./600-example-usage-uncomment-and-adapt-once-server_para.md)

**Next:** [Using with CrewBase →](./602-using-with-crewbase.md)
