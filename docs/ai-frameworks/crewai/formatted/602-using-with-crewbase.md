---
title: "Crewai: Using with CrewBase"
description: "Using with CrewBase section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Using with CrewBase


To use MCPServer tools within a CrewBase class, use the `get_mcp_tools` method. Server configurations should be provided via the `mcp_server_params` attribute. You can pass either a single configuration or a list of multiple server configurations.

```python  theme={null}
@CrewBase
class CrewWithMCP:
  # ... define your agents and tasks config file ...

  mcp_server_params = [
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

  @agent
  def your_agent(self):
      return Agent(config=self.agents_config["your_agent"], tools=self.get_mcp_tools()) # get all available tools

    # ... rest of your crew setup ...
```

<Tip>
  When a crew class is decorated with `@CrewBase`, the adapter lifecycle is managed for you:

  * The first call to `get_mcp_tools()` lazily creates a shared `MCPServerAdapter` that is reused by every agent in the crew.
  * The adapter automatically shuts down after `.kickoff()` completes thanks to an implicit after-kickoff hook injected by `@CrewBase`, so no manual cleanup is required.
  * If `mcp_server_params` is not defined, `get_mcp_tools()` simply returns an empty list, allowing the same code paths to run with or without MCP configured.

  This makes it safe to call `get_mcp_tools()` from multiple agent methods or selectively enable MCP per environment.
</Tip>

### Connection Timeout Configuration

You can configure the connection timeout for MCP servers by setting the `mcp_connect_timeout` class attribute. If no timeout is specified, it defaults to 30 seconds.

```python  theme={null}
@CrewBase
class CrewWithMCP:
  mcp_server_params = [...]
  mcp_connect_timeout = 60  # 60 seconds timeout for all MCP connections

  @agent
  def your_agent(self):
      return Agent(config=self.agents_config["your_agent"], tools=self.get_mcp_tools())
```

```python  theme={null}
@CrewBase
class CrewWithDefaultTimeout:
  mcp_server_params = [...]
  # No mcp_connect_timeout specified - uses default 30 seconds

  @agent
  def your_agent(self):
      return Agent(config=self.agents_config["your_agent"], tools=self.get_mcp_tools())
```

### Filtering Tools

You can filter which tools are available to your agent by passing a list of tool names to the `get_mcp_tools` method.

```python  theme={null}
@agent
def another_agent(self):
    return Agent(
      config=self.agents_config["your_agent"],
      tools=self.get_mcp_tools("tool_1", "tool_2") # get specific tools
    )
```

The timeout configuration applies to all MCP tool calls within the crew:

```python  theme={null}
@CrewBase
class CrewWithCustomTimeout:
  mcp_server_params = [...]
  mcp_connect_timeout = 90  # 90 seconds timeout for all MCP connections

  @agent
  def filtered_agent(self):
      return Agent(
        config=self.agents_config["your_agent"],
        tools=self.get_mcp_tools("tool_1", "tool_2") # specific tools with custom timeout
      )
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Filtering Tools](./601-filtering-tools.md)

**Next:** [Explore MCP Integrations →](./603-explore-mcp-integrations.md)
