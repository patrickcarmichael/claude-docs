---
title: "Crewai: Security Considerations for SSE"
description: "Security Considerations for SSE section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Security Considerations for SSE


<Warning>
  **DNS Rebinding Attacks**: SSE transports can be vulnerable to DNS rebinding attacks if the MCP server is not properly secured. This could allow malicious websites to interact with local or intranet-based MCP servers.
</Warning>

To mitigate this risk:

* MCP server implementations should **validate `Origin` headers** on incoming SSE connections.
* When running local SSE MCP servers for development, **bind only to `localhost` (`127.0.0.1`)** rather than all network interfaces (`0.0.0.0`).
* Implement **proper authentication** for all SSE connections if they expose sensitive tools or data.

For a comprehensive overview of security best practices, please refer to our [Security Considerations](./security.mdx) page and the official [MCP Transport Security documentation](https://modelcontextprotocol.io/docs/concepts/transports#security-considerations).

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Using MCPServerAdapter with a context manager](./613-using-mcpserveradapter-with-a-context-manager.md)

**Next:** [Stdio Transport →](./615-stdio-transport.md)
