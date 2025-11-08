---
title: "Mcp: Capabilities"
description: "Capabilities section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

## Capabilities


Clients that support elicitation **MUST** declare the `elicitation` capability during
[initialization](/specification/2025-06-18/basic/lifecycle#initialization):

```json  theme={null}
{
  "capabilities": {
    "elicitation": {}
  }
}
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← User Interaction Model](./133-user-interaction-model.md)

**Next:** [Protocol Messages →](./135-protocol-messages.md)
