---
title: "Crewai: Connecting via SSE"
description: "Connecting via SSE section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Connecting via SSE


You can connect to an SSE-based MCP server using two main approaches for managing the connection lifecycle:

### 1. Fully Managed Connection (Recommended)

Using a Python context manager (`with` statement) is the recommended approach. It automatically handles establishing and closing the connection to the SSE MCP server.

```python  theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools import MCPServerAdapter

server_params = {
    "url": "http://localhost:8000/sse", # Replace with your actual SSE server URL
    "transport": "sse" 
}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Key Concepts](./611-key-concepts.md)

**Next:** [Using MCPServerAdapter with a context manager →](./613-using-mcpserveradapter-with-a-context-manager.md)
