---
title: "Crewai: Staying Safe with MCP"
description: "Staying Safe with MCP section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Staying Safe with MCP


<Warning>
  Always ensure that you trust an MCP Server before using it.
</Warning>

#### Security Warning: DNS Rebinding Attacks

SSE transports can be vulnerable to DNS rebinding attacks if not properly secured.
To prevent this:

1. **Always validate Origin headers** on incoming SSE connections to ensure they come from expected sources
2. **Avoid binding servers to all network interfaces** (0.0.0.0) when running locally - bind only to localhost (127.0.0.1) instead
3. **Implement proper authentication** for all SSE connections

Without these protections, attackers could use DNS rebinding to interact with local MCP servers from remote websites.

For more details, see the [Anthropic's MCP Transport Security docs](https://modelcontextprotocol.io/docs/concepts/transports#security-considerations).

### Limitations

* **Supported Primitives**: Currently, `MCPServerAdapter` primarily supports adapting MCP `tools`.
  Other MCP primitives like `prompts` or `resources` are not directly integrated as CrewAI components through this adapter at this time.
* **Output Handling**: The adapter typically processes the primary text output from an MCP tool (e.g., `.content[0].text`). Complex or multi-modal outputs might require custom handling if not fitting this pattern.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Explore MCP Integrations](./603-explore-mcp-integrations.md)

**Next:** [MCP Security Considerations →](./605-mcp-security-considerations.md)
