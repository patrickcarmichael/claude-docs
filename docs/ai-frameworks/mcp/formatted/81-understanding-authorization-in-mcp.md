---
title: "Mcp: Understanding Authorization in MCP"
description: "Understanding Authorization in MCP section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

# Understanding Authorization in MCP


Source: https://modelcontextprotocol.io/docs/tutorials/security/authorization

Learn how to implement secure authorization for MCP servers using OAuth 2.1 to protect sensitive resources and operations

Authorization in the Model Context Protocol (MCP) secures access to sensitive resources and operations exposed by MCP servers. If your MCP server handles user data or administrative actions, authorization ensures only permitted users can access its endpoints.

MCP uses standardized authorization flows to build trust between MCP clients and MCP servers. Its design doesn't focus on one specific authorization or identity system, but rather follows the conventions outlined for [OAuth 2.1](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13). For detailed information, see the [Authorization specification](/specification/2025-06-18/basic/authorization).

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Next steps](./80-next-steps.md)

**Next:** [When Should You Use Authorization? →](./82-when-should-you-use-authorization.md)
