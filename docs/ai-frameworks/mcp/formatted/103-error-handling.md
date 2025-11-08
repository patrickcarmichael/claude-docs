---
title: "Mcp: Error Handling"
description: "Error Handling section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

## Error Handling


Implementations **SHOULD** be prepared to handle these error cases:

* Protocol version mismatch
* Failure to negotiate required capabilities
* Request [timeouts](#timeouts)

Example initialization error:

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32602,
    "message": "Unsupported protocol version",
    "data": {
      "supported": ["2024-11-05"],
      "requested": "1.0.0"
    }
  }
}
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Timeouts](./102-timeouts.md)

**Next:** [Security Best Practices →](./104-security-best-practices.md)
