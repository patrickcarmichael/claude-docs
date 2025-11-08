---
title: "Crewai: Security Considerations"
description: "Security Considerations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Security Considerations


When using Streamable HTTP transport, general web security best practices are paramount:

* **Use HTTPS**: Always prefer HTTPS (HTTP Secure) for your MCP server URLs to encrypt data in transit.
* **Authentication**: Implement robust authentication mechanisms if your MCP server exposes sensitive tools or data.
* **Input Validation**: Ensure your MCP server validates all incoming requests and parameters.

For a comprehensive guide on securing your MCP integrations, please refer to our [Security Considerations](./security.mdx) page and the official [MCP Transport Security documentation](https://modelcontextprotocol.io/docs/concepts/transports#security-considerations).

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Connecting via Streamable HTTP](./624-connecting-via-streamable-http.md)

**Next:** [Quickstart →](./626-quickstart.md)
