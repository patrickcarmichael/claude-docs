# Model Context Protocol (MCP)

**Open Protocol for Connecting AI Assistants to Data Sources** | 852KB

The Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context to LLMs. It enables secure, two-way connections between data sources and AI-powered tools.

- **Focus**: Standardized context integration, tool protocols, data connections
- **Type**: Protocol specification with SDKs
- **Language**: TypeScript, Python SDKs
- **Maturity**: Emerging standard, backed by Anthropic
- **Best For**: Connecting LLMs to external data, building AI integrations
- **Philosophy**: Open standard, secure context sharing, extensible integrations

📄 [Full Documentation](./llms-full.txt) | 📑 [Chunked Version](./chunked/index.md)

## Key Concepts

- **Servers**: Provide context, tools, and prompts to clients
- **Clients**: AI applications that consume MCP services (Claude, IDEs, etc.)
- **Resources**: File-like data sources (documents, logs, API responses)
- **Tools**: Functions that clients can invoke
- **Prompts**: Reusable prompt templates
- **Sampling**: LLM request delegation to clients

## Official Resources

- **Website**: https://modelcontextprotocol.io/
- **Documentation**: https://modelcontextprotocol.io/docs
- **Specification**: https://spec.modelcontextprotocol.io/
- **GitHub**: https://github.com/modelcontextprotocol

---

*Part of the [AI Frameworks documentation](../)*
