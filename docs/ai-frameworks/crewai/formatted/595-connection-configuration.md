---
title: "Crewai: Connection Configuration"
description: "Connection Configuration section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Connection Configuration


The `MCPServerAdapter` supports several configuration options to customize the connection behavior:

* **`connect_timeout`** (optional): Maximum time in seconds to wait for establishing a connection to the MCP server. Defaults to 30 seconds if not specified. This is particularly useful for remote servers that may have variable response times.

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Advanced: MCPServerAdapter](./594-advanced-mcpserveradapter.md)

**Next:** [Example with custom connection timeout →](./596-example-with-custom-connection-timeout.md)
