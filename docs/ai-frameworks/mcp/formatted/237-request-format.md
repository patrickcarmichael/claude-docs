---
title: "Mcp: Request Format"
description: "Request Format section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

## Request Format


After receiving a cursor, the client can *continue* paginating by issuing a request
including that cursor:

```json  theme={null}
{
  "jsonrpc": "2.0",
  "id": "124",
  "method": "resources/list",
  "params": {
    "cursor": "eyJwYWdlIjogMn0="
  }
}
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Response Format](./236-response-format.md)

**Next:** [Pagination Flow →](./238-pagination-flow.md)
