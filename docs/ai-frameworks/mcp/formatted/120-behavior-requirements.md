---
title: "Mcp: Behavior Requirements"
description: "Behavior Requirements section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

## Behavior Requirements


1. The receiver **MUST** respond promptly with an empty response:

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": "123",
  "result": {}
}
```

2. If no response is received within a reasonable timeout period, the sender **MAY**:
   * Consider the connection stale
   * Terminate the connection
   * Attempt reconnection procedures

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Message Format](./119-message-format.md)

**Next:** [Usage Patterns →](./121-usage-patterns.md)
