---
title: "Crewai: Define parameters for multiple MCP servers"
description: "Define parameters for multiple MCP servers section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define parameters for multiple MCP servers

server_params_list = [
    # Streamable HTTP Server
    {
        "url": "http://localhost:8001/mcp", 
        "transport": "streamable-http"
    },
    # SSE Server
    {
        "url": "http://localhost:8000/sse",
        "transport": "sse"
    },
    # StdIO Server
    StdioServerParameters(
        command="python3",
        args=["servers/your_stdio_server.py"],
        env={"UV_PYTHON": "3.12", **os.environ},
    )
]

try:
    with MCPServerAdapter(server_params_list) as aggregated_tools:
        print(f"Available aggregated tools: {[tool.name for tool in aggregated_tools]}")

        multi_server_agent = Agent(
            role="Versatile Assistant",
            goal="Utilize tools from local Stdio, remote SSE, and remote HTTP MCP servers.",
            backstory="An AI agent capable of leveraging a diverse set of tools from multiple sources.",
            tools=aggregated_tools, # All tools are available here
            verbose=True,
        )

        ... # Your other agent, tasks, and crew code here

except Exception as e:
    print(f"Error connecting to or using multiple MCP servers (Managed): {e}")
    print("Ensure all MCP servers are running and accessible with correct configurations.")

```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Configuration](./570-configuration.md)

**Next:** [Connection Management →](./572-connection-management.md)
