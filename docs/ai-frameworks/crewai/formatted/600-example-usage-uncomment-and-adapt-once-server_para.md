---
title: "Crewai: Example usage (uncomment and adapt once server_params is set):"
description: "Example usage (uncomment and adapt once server_params is set): section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example usage (uncomment and adapt once server_params is set):

with MCPServerAdapter(server_params, connect_timeout=60) as mcp_tools:
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

This general pattern shows how to integrate tools. For specific examples tailored to each transport, refer to the detailed guides below.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← 3. Streamable HTTP Server:](./599-3-streamable-http-server.md)

**Next:** [Filtering Tools →](./601-filtering-tools.md)
