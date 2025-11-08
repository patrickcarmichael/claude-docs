---
title: "Mcp: Custom Transports"
description: "Custom Transports section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

## Custom Transports


Clients and servers **MAY** implement additional custom transport mechanisms to suit
their specific needs. The protocol is transport-agnostic and can be implemented over any
communication channel that supports bidirectional message exchange.

Implementers who choose to support custom transports **MUST** ensure they preserve the
JSON-RPC message format and lifecycle requirements defined by MCP. Custom transports
**SHOULD** document their specific connection establishment and message exchange patterns
to aid interoperability.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Streamable HTTP](./109-streamable-http.md)

**Next:** [Cancellation →](./111-cancellation.md)
