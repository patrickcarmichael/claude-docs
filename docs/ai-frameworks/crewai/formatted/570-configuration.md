---
title: "Crewai: Configuration"
description: "Configuration section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Configuration


To connect to multiple servers, you provide a list of server parameter dictionaries to `MCPServerAdapter`. Each dictionary in the list should define the parameters for one MCP server.

Supported transport types for each server in the list include `stdio`, `sse`, and `streamable-http`.

```python  theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters # Needed for Stdio example

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Overview](./569-overview.md)

**Next:** [Define parameters for multiple MCP servers →](./571-define-parameters-for-multiple-mcp-servers.md)
