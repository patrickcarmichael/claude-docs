---
title: "Mcp: Error Handling"
description: "Error Handling section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

## Error Handling


Servers **SHOULD** return standard JSON-RPC errors for common failure cases:

* Method not found: `-32601` (Capability not supported)
* Invalid prompt name: `-32602` (Invalid params)
* Missing required arguments: `-32602` (Invalid params)
* Internal errors: `-32603` (Internal error)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Data Types](./221-data-types.md)

**Next:** [Implementation Considerations →](./223-implementation-considerations.md)
