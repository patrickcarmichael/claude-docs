---
title: "Mcp: Message Format"
description: "Message Format section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

## Message Format


A ping request is a standard JSON-RPC request with no parameters:

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": "123",
  "method": "ping"
}
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Overview](./118-overview.md)

**Next:** [Behavior Requirements →](./120-behavior-requirements.md)
