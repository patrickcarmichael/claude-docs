---
title: "Crewai: Connecting via Streamable HTTP"
description: "Connecting via Streamable HTTP section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Connecting via Streamable HTTP


You have two primary methods for managing the connection lifecycle with a Streamable HTTP MCP server:

### 1. Fully Managed Connection (Recommended)

The recommended approach is to use a Python context manager (`with` statement), which handles the connection's setup and teardown automatically.

```python  theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools import MCPServerAdapter

server_params = {
    "url": "http://localhost:8001/mcp", # Replace with your actual Streamable HTTP server URL
    "transport": "streamable-http"
}

try:
    with MCPServerAdapter(server_params) as tools:
        print(f"Available tools from Streamable HTTP MCP server: {[tool.name for tool in tools]}")

        http_agent = Agent(
            role="HTTP Service Integrator",
            goal="Utilize tools from a remote MCP server via Streamable HTTP.",
            backstory="An AI agent adept at interacting with complex web services.",
            tools=tools,
            verbose=True,
        )

        http_task = Task(
            description="Perform a complex data query using a tool from the Streamable HTTP server.",
            expected_output="The result of the complex data query.",
            agent=http_agent,
        )

        http_crew = Crew(
            agents=[http_agent],
            tasks=[http_task],
            verbose=True,
            process=Process.sequential
        )
        
        result = http_crew.kickoff() 
        print("\nCrew Task Result (Streamable HTTP - Managed):\n", result)

except Exception as e:
    print(f"Error connecting to or using Streamable HTTP MCP server (Managed): {e}")
    print("Ensure the Streamable HTTP MCP server is running and accessible at the specified URL.")

```

**Note:** Replace `"http://localhost:8001/mcp"` with the actual URL of your Streamable HTTP MCP server.

### 2. Manual Connection Lifecycle

For scenarios requiring more explicit control, you can manage the `MCPServerAdapter` connection manually.

<Info>
  It is **critical** to call `mcp_server_adapter.stop()` when you are done to close the connection and free up resources. A `try...finally` block is the safest way to ensure this.
</Info>

```python  theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools import MCPServerAdapter

server_params = {
    "url": "http://localhost:8001/mcp", # Replace with your actual Streamable HTTP server URL
    "transport": "streamable-http"
}

mcp_server_adapter = None 
try:
    mcp_server_adapter = MCPServerAdapter(server_params)
    mcp_server_adapter.start()
    tools = mcp_server_adapter.tools
    print(f"Available tools (manual Streamable HTTP): {[tool.name for tool in tools]}")

    manual_http_agent = Agent(
        role="Advanced Web Service User",
        goal="Interact with an MCP server using manually managed Streamable HTTP connections.",
        backstory="An AI specialist in fine-tuning HTTP-based service integrations.",
        tools=tools,
        verbose=True
    )
    
    data_processing_task = Task(
        description="Submit data for processing and retrieve results via Streamable HTTP.",
        expected_output="Processed data or confirmation.",
        agent=manual_http_agent
    )
    
    data_crew = Crew(
        agents=[manual_http_agent],
        tasks=[data_processing_task],
        verbose=True,
        process=Process.sequential
    )
    
    result = data_crew.kickoff()
    print("\nCrew Task Result (Streamable HTTP - Manual):\n", result)

except Exception as e:
    print(f"An error occurred during manual Streamable HTTP MCP integration: {e}")
    print("Ensure the Streamable HTTP MCP server is running and accessible.")
finally:
    if mcp_server_adapter and mcp_server_adapter.is_connected:
        print("Stopping Streamable HTTP MCP server connection (manual)...")
        mcp_server_adapter.stop()  # **Crucial: Ensure stop is called**
    elif mcp_server_adapter:
        print("Streamable HTTP MCP server adapter was not connected. No stop needed or start failed.")
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Key Concepts](./623-key-concepts.md)

**Next:** [Security Considerations →](./625-security-considerations.md)
