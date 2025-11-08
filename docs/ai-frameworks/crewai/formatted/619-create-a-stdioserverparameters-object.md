---
title: "Crewai: Create a StdioServerParameters object"
description: "Create a StdioServerParameters object section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a StdioServerParameters object

server_params=StdioServerParameters(
    command="python3", 
    args=["servers/your_stdio_server.py"],
    env={"UV_PYTHON": "3.12", **os.environ},
)

with MCPServerAdapter(server_params) as tools:
    print(f"Available tools from Stdio MCP server: {[tool.name for tool in tools]}")

    # Example: Using the tools from the Stdio MCP server in a CrewAI Agent
    research_agent = Agent(
        role="Local Data Processor",
        goal="Process data using a local Stdio-based tool.",
        backstory="An AI that leverages local scripts via MCP for specialized tasks.",
        tools=tools,
        reasoning=True,
        verbose=True,
    )
    
    processing_task = Task(
        description="Process the input data file 'data.txt' and summarize its contents.",
        expected_output="A summary of the processed data.",
        agent=research_agent,
        markdown=True
    )
    
    data_crew = Crew(
        agents=[research_agent],
        tasks=[processing_task],
        verbose=True,
        process=Process.sequential 
    )
   
    result = data_crew.kickoff()
    print("\nCrew Task Result (Stdio - Managed):\n", result)

```

### 2. Manual Connection Lifecycle

If you need finer-grained control over when the Stdio MCP server process is started and stopped, you can manage the `MCPServerAdapter` lifecycle manually.

<Info>
  You **MUST** call `mcp_server_adapter.stop()` to ensure the server process is terminated and resources are released. Using a `try...finally` block is highly recommended.
</Info>

```python  theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters
import os

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Connecting via Stdio](./618-connecting-via-stdio.md)

**Next:** [Create a StdioServerParameters object →](./620-create-a-stdioserverparameters-object.md)
