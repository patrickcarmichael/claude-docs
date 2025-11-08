---
title: "Mcp: Capabilities"
description: "Capabilities section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

## Capabilities


Clients that support sampling **MUST** declare the `sampling` capability during
[initialization](/specification/2025-06-18/basic/lifecycle#initialization):

```json  theme={null}
{
  "capabilities": {
    "sampling": {}
  }
}
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← User Interaction Model](./150-user-interaction-model.md)

**Next:** [Protocol Messages →](./152-protocol-messages.md)
