---
title: "Mcp: When Should You Use Authorization?"
description: "When Should You Use Authorization? section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

## When Should You Use Authorization?


While authorization for MCP servers is **optional**, it is strongly recommended when:

* Your server accesses user-specific data (emails, documents, databases)
* You need to audit who performed which actions
* Your server grants access to its APIs that require user consent
* You're building for enterprise environments with strict access controls
* You want to implement rate limiting or usage tracking per user

<Tip>
  **Authorization for Local MCP Servers**

  For MCP servers using the [STDIO transport](/specification/2025-06-18/basic/transports#stdio), you can use environment-based credentials or credentials provided by third-party libraries embedded directly in the MCP server instead. Because a STDIO-built MCP server runs locally, it has access to a range of flexible options when it comes to acquiring user credentials that may or may not rely on in-browser authentication and authorization flows.

  OAuth flows, in turn, are designed for HTTP-based transports where the MCP server is remotely-hosted and the client uses OAuth to establish that a user is authorized to access said remote server.
</Tip>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Understanding Authorization in MCP](./81-understanding-authorization-in-mcp.md)

**Next:** [The Authorization Flow: Step by Step →](./83-the-authorization-flow-step-by-step.md)
