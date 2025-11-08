---
title: "Crewai: Using MCPServerAdapter with a context manager"
description: "Using MCPServerAdapter with a context manager section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Using MCPServerAdapter with a context manager

try:
    with MCPServerAdapter(server_params) as tools:
        print(f"Available tools from SSE MCP server: {[tool.name for tool in tools]}")

        # Example: Using a tool from the SSE MCP server
        sse_agent = Agent(
            role="Remote Service User",
            goal="Utilize a tool provided by a remote SSE MCP server.",
            backstory="An AI agent that connects to external services via SSE.",
            tools=tools,
            reasoning=True,
            verbose=True,
        )

        sse_task = Task(
            description="Fetch real-time stock updates for 'AAPL' using an SSE tool.",
            expected_output="The latest stock price for AAPL.",
            agent=sse_agent,
            markdown=True
        )

        sse_crew = Crew(
            agents=[sse_agent],
            tasks=[sse_task],
            verbose=True,
            process=Process.sequential
        )
        
        if tools: # Only kickoff if tools were loaded
            result = sse_crew.kickoff() # Add inputs={'stock_symbol': 'AAPL'} if tool requires it
            print("\nCrew Task Result (SSE - Managed):\n", result)
        else:
            print("Skipping crew kickoff as tools were not loaded (check server connection).")

except Exception as e:
    print(f"Error connecting to or using SSE MCP server (Managed): {e}")
    print("Ensure the SSE MCP server is running and accessible at the specified URL.")

```

<Note>
  Replace `"http://localhost:8000/sse"` with the actual URL of your SSE MCP server.
</Note>

### 2. Manual Connection Lifecycle

If you need finer-grained control, you can manage the `MCPServerAdapter` connection lifecycle manually.

<Info>
  You **MUST** call `mcp_server_adapter.stop()` to ensure the connection is closed and resources are released. Using a `try...finally` block is highly recommended.
</Info>

```python  theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools import MCPServerAdapter

server_params = {
    "url": "http://localhost:8000/sse", # Replace with your actual SSE server URL
    "transport": "sse"
}

mcp_server_adapter = None 
try:
    mcp_server_adapter = MCPServerAdapter(server_params)
    mcp_server_adapter.start()
    tools = mcp_server_adapter.tools
    print(f"Available tools (manual SSE): {[tool.name for tool in tools]}")

    manual_sse_agent = Agent(
        role="Remote Data Analyst",
        goal="Analyze data fetched from a remote SSE MCP server using manual connection management.",
        backstory="An AI skilled in handling SSE connections explicitly.",
        tools=tools,
        verbose=True
    )
    
    analysis_task = Task(
        description="Fetch and analyze the latest user activity trends from the SSE server.",
        expected_output="A summary report of user activity trends.",
        agent=manual_sse_agent
    )
    
    analysis_crew = Crew(
        agents=[manual_sse_agent],
        tasks=[analysis_task],
        verbose=True,
        process=Process.sequential
    )
    
    result = analysis_crew.kickoff()
    print("\nCrew Task Result (SSE - Manual):\n", result)

except Exception as e:
    print(f"An error occurred during manual SSE MCP integration: {e}")
    print("Ensure the SSE MCP server is running and accessible.")
finally:
    if mcp_server_adapter and mcp_server_adapter.is_connected:
        print("Stopping SSE MCP server connection (manual)...")
        mcp_server_adapter.stop()  # **Crucial: Ensure stop is called**
    elif mcp_server_adapter:
        print("SSE MCP server adapter was not connected. No stop needed or start failed.")

```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Connecting via SSE](./612-connecting-via-sse.md)

**Next:** [Security Considerations for SSE →](./614-security-considerations-for-sse.md)
