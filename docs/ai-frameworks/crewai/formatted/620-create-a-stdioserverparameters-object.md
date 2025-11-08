---
title: "Crewai: Create a StdioServerParameters object"
description: "Create a StdioServerParameters object section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a StdioServerParameters object

stdio_params=StdioServerParameters(
    command="python3", 
    args=["servers/your_stdio_server.py"],
    env={"UV_PYTHON": "3.12", **os.environ},
)

mcp_server_adapter = MCPServerAdapter(server_params=stdio_params)
try:
    mcp_server_adapter.start()  # Manually start the connection and server process
    tools = mcp_server_adapter.tools
    print(f"Available tools (manual Stdio): {[tool.name for tool in tools]}")

    # Example: Using the tools with your Agent, Task, Crew setup
    manual_agent = Agent(
        role="Local Task Executor",
        goal="Execute a specific local task using a manually managed Stdio tool.",
        backstory="An AI proficient in controlling local processes via MCP.",
        tools=tools,
        verbose=True
    )
    
    manual_task = Task(
        description="Execute the 'perform_analysis' command via the Stdio tool.",
        expected_output="Results of the analysis.",
        agent=manual_agent
    )
    
    manual_crew = Crew(
        agents=[manual_agent],
        tasks=[manual_task],
        verbose=True,
        process=Process.sequential
    )
        
       
    result = manual_crew.kickoff() # Actual inputs depend on your tool
    print("\nCrew Task Result (Stdio - Manual):\n", result)
            
except Exception as e:
    print(f"An error occurred during manual Stdio MCP integration: {e}")
finally:
    if mcp_server_adapter and mcp_server_adapter.is_connected: # Check if connected before stopping
        print("Stopping Stdio MCP server connection (manual)...")
        mcp_server_adapter.stop()  # **Crucial: Ensure stop is called**
    elif mcp_server_adapter: # If adapter exists but not connected (e.g. start failed)
        print("Stdio MCP server adapter was not connected. No stop needed or start failed.")

```

Remember to replace placeholder paths and commands with your actual Stdio server details. The `env` parameter in `StdioServerParameters` can
be used to set environment variables for the server process, which can be useful for configuring its behavior or providing necessary paths (like `PYTHONPATH`).

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create a StdioServerParameters object](./619-create-a-stdioserverparameters-object.md)

**Next:** [Streamable HTTP Transport →](./621-streamable-http-transport.md)
