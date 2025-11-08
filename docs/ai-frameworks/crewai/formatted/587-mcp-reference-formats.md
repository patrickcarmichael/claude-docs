---
title: "Crewai: MCP Reference Formats"
description: "MCP Reference Formats section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## MCP Reference Formats


The `mcps` field supports both **string references** (for quick setup) and **structured configurations** (for full control). You can mix both formats in the same list.

### String-Based References

#### External MCP Servers

```python  theme={null}
mcps=[
    # Full server - get all available tools
    "https://mcp.example.com/api",

    # Specific tool from server using # syntax
    "https://api.weather.com/mcp#get_current_weather",

    # Server with authentication parameters
    "https://mcp.exa.ai/mcp?api_key=your_key&profile=your_profile"
]
```

#### CrewAI AMP Marketplace

```python  theme={null}
mcps=[
    # Full AMP MCP service - get all available tools
    "crewai-amp:financial-data",

    # Specific tool from AMP service using # syntax
    "crewai-amp:research-tools#pubmed_search",

    # Multiple AMP services
    "crewai-amp:weather-service",
    "crewai-amp:market-analysis"
]
```

### Structured Configurations

#### Stdio Transport (Local Servers)

Perfect for local MCP servers that run as processes:

```python  theme={null}
from crewai.mcp import MCPServerStdio
from crewai.mcp.filters import create_static_tool_filter

mcps=[
    MCPServerStdio(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem"],
        env={"API_KEY": "your_key"},
        tool_filter=create_static_tool_filter(
            allowed_tool_names=["read_file", "write_file"]
        ),
        cache_tools_list=True,
    ),
    # Python-based server
    MCPServerStdio(
        command="python",
        args=["path/to/server.py"],
        env={"UV_PYTHON": "3.12", "API_KEY": "your_key"},
    ),
]
```

#### HTTP/Streamable HTTP Transport (Remote Servers)

For remote MCP servers over HTTP/HTTPS:

```python  theme={null}
from crewai.mcp import MCPServerHTTP

mcps=[
    # Streamable HTTP (default)
    MCPServerHTTP(
        url="https://api.example.com/mcp",
        headers={"Authorization": "Bearer your_token"},
        streamable=True,
        cache_tools_list=True,
    ),
    # Standard HTTP
    MCPServerHTTP(
        url="https://api.example.com/mcp",
        headers={"Authorization": "Bearer your_token"},
        streamable=False,
    ),
]
```

#### SSE Transport (Real-Time Streaming)

For remote servers using Server-Sent Events:

```python  theme={null}
from crewai.mcp import MCPServerSSE

mcps=[
    MCPServerSSE(
        url="https://stream.example.com/mcp/sse",
        headers={"Authorization": "Bearer your_token"},
        cache_tools_list=True,
    ),
]
```

### Mixed References

You can combine string references and structured configurations:

```python  theme={null}
from crewai.mcp import MCPServerStdio, MCPServerHTTP

mcps=[
    # String references
    "https://external-api.com/mcp",              # External server
    "crewai-amp:financial-insights",             # AMP service

    # Structured configurations
    MCPServerStdio(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem"],
    ),
    MCPServerHTTP(
        url="https://api.example.com/mcp",
        headers={"Authorization": "Bearer token"},
    ),
]
```

### Tool Filtering

Structured configurations support advanced tool filtering:

```python  theme={null}
from crewai.mcp import MCPServerStdio
from crewai.mcp.filters import create_static_tool_filter, create_dynamic_tool_filter, ToolFilterContext

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create and run crew](./586-create-and-run-crew.md)

**Next:** [Static filtering (allow/block lists) →](./588-static-filtering-allowblock-lists.md)
