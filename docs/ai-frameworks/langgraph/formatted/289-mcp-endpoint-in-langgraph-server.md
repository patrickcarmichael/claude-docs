---
title: "Langgraph: MCP endpoint in LangGraph Server"
description: "MCP endpoint in LangGraph Server section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# MCP endpoint in LangGraph Server


The [Model Context Protocol (MCP)](./mcp.md) is an open protocol for describing tools and data sources in a model-agnostic format, enabling LLMs to discover and use them via a structured API.

[LangGraph Server](./langgraph_server.md) implements MCP using the [Streamable HTTP transport](https://spec.modelcontextprotocol.io/specification/2025-03-26/basic/transports/#streamable-http). This allows LangGraph **agents** to be exposed as **MCP tools**, making them usable with any MCP-compliant client supporting Streamable HTTP.

The MCP endpoint is available at `/mcp` on [LangGraph Server](./langgraph_server.md).

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Patterns](./288-patterns.md)

**Next:** [Requirements →](./290-requirements.md)
