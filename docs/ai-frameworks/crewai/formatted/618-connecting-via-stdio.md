---
title: "Crewai: Connecting via Stdio"
description: "Connecting via Stdio section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Connecting via Stdio


You can connect to an Stdio-based MCP server using two main approaches for managing the connection lifecycle:

### 1. Fully Managed Connection (Recommended)

Using a Python context manager (`with` statement) is the recommended approach. It automatically handles starting the MCP server process and stopping it when the context is exited.

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

**Previous:** [← Key Concepts](./617-key-concepts.md)

**Next:** [Create a StdioServerParameters object →](./619-create-a-stdioserverparameters-object.md)
