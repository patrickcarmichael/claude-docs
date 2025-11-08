---
title: "Crewai: Agent will use tools from working servers and log warnings for failing ones"
description: "Agent will use tools from working servers and log warnings for failing ones section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Agent will use tools from working servers and log warnings for failing ones

```

All connection errors are handled gracefully:

* **Connection failures**: Logged as warnings, agent continues with available tools
* **Timeout errors**: Connections timeout after 30 seconds (configurable)
* **Authentication errors**: Logged clearly for debugging
* **Invalid configurations**: Validation errors are raised at agent creation time

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Error Handling](./592-error-handling.md)

**Next:** [Advanced: MCPServerAdapter →](./594-advanced-mcpserveradapter.md)
