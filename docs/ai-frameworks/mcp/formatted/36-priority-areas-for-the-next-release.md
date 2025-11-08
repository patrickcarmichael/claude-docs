---
title: "Mcp: Priority Areas for the Next Release"
description: "Priority Areas for the Next Release section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

## Priority Areas for the Next Release


### Asynchronous Operations

Currently, MCP is built around mostly synchronous operations. We're adding async support to allow servers to kick off long-running tasks while clients can check back later for results. This will enable operations that take minutes or hours without blocking.

Follow the progress in [SEP-1686](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1686).

### Statelessness and Scalability

As organizations deploy MCP servers at enterprise scale, we're addressing challenges around horizontal scaling. While [Streamable HTTP](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http) provides some stateless support, we're smoothing out rough edges around server startup and session handling to make it easier to run MCP servers in production.

The current focus point for this effort is [SEP-1442](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1442).

### Server Identity

We're enabling servers to advertise themselves through [`.well-known` URLs](https://en.wikipedia.org/wiki/Well-known_URI)—an established standard for providing metadata. This will allow clients to discover what a server can do without having to connect to it first, making discovery much more intuitive and enabling systems like our registry to automatically catalog capabilities. We are working closely across multiple projects in the industry to rely on a common standard on agent cards.

### Official Extensions

As MCP has grown, valuable patterns have emerged for specific industries and use cases. Rather than leaving everyone to reinvent the wheel, we're officially recognizing and documenting the most popular protocol extensions. This curated collection will give developers building for specialized domains like healthcare, finance, or education a solid starting point.

### SDK Support Standardization

We're introducing a clear tiering system for SDKs based on factors like specification compliance speed, maintenance responsiveness, and feature completeness. This will help developers understand exactly what level of support they're getting before committing to a dependency.

### MCP Registry General Availability

The [MCP Registry](https://github.com/modelcontextprotocol/registry) launched in preview in September 2025 and is progressing toward general availability. We're stabilizing the v0.1 API through real-world integrations and community feedback, with plans to transition from preview to a production-ready service. This will provide developers with a reliable, community-driven platform for discovering and sharing MCP servers.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Roadmap](./35-roadmap.md)

**Next:** [Validation →](./37-validation.md)
