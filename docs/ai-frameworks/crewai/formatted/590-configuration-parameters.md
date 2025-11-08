---
title: "Crewai: Configuration Parameters"
description: "Configuration Parameters section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Configuration Parameters


Each transport type supports specific configuration options:

### MCPServerStdio Parameters

* **`command`** (required): Command to execute (e.g., `"python"`, `"node"`, `"npx"`, `"uvx"`)
* **`args`** (optional): List of command arguments (e.g., `["server.py"]` or `["-y", "@mcp/server"]`)
* **`env`** (optional): Dictionary of environment variables to pass to the process
* **`tool_filter`** (optional): Tool filter function for filtering available tools
* **`cache_tools_list`** (optional): Whether to cache the tool list for faster subsequent access (default: `False`)

### MCPServerHTTP Parameters

* **`url`** (required): Server URL (e.g., `"https://api.example.com/mcp"`)
* **`headers`** (optional): Dictionary of HTTP headers for authentication or other purposes
* **`streamable`** (optional): Whether to use streamable HTTP transport (default: `True`)
* **`tool_filter`** (optional): Tool filter function for filtering available tools
* **`cache_tools_list`** (optional): Whether to cache the tool list for faster subsequent access (default: `False`)

### MCPServerSSE Parameters

* **`url`** (required): Server URL (e.g., `"https://api.example.com/mcp/sse"`)
* **`headers`** (optional): Dictionary of HTTP headers for authentication or other purposes
* **`tool_filter`** (optional): Tool filter function for filtering available tools
* **`cache_tools_list`** (optional): Whether to cache the tool list for faster subsequent access (default: `False`)

### Common Parameters

All transport types support:

* **`tool_filter`**: Filter function to control which tools are available. Can be:
  * `None` (default): All tools are available
  * Static filter: Created with `create_static_tool_filter()` for allow/block lists
  * Dynamic filter: Created with `create_dynamic_tool_filter()` for context-aware filtering
* **`cache_tools_list`**: When `True`, caches the tool list after first discovery to improve performance on subsequent connections

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Dynamic filtering (context-aware)](./589-dynamic-filtering-context-aware.md)

**Next:** [Key Features →](./591-key-features.md)
