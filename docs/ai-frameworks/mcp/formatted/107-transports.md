---
title: "Mcp: Transports"
description: "Transports section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

# Transports


Source: https://modelcontextprotocol.io/specification/2025-06-18/basic/transports

<div id="enable-section-numbers" />

<Info>**Protocol Revision**: 2025-06-18</Info>

MCP uses JSON-RPC to encode messages. JSON-RPC messages **MUST** be UTF-8 encoded.

The protocol currently defines two standard transport mechanisms for client-server
communication:

1. [stdio](#stdio), communication over standard in and standard out
2. [Streamable HTTP](#streamable-http)

Clients **SHOULD** support stdio whenever possible.

It is also possible for clients and servers to implement
[custom transports](#custom-transports) in a pluggable fashion.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Attacks and Mitigations](./106-attacks-and-mitigations.md)

**Next:** [stdio →](./108-stdio.md)
