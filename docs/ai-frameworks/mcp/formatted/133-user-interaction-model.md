---
title: "Mcp: User Interaction Model"
description: "User Interaction Model section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

## User Interaction Model


Elicitation in MCP allows servers to implement interactive workflows by enabling user input
requests to occur *nested* inside other MCP server features.

Implementations are free to expose elicitation through any interface pattern that suits
their needs—the protocol itself does not mandate any specific user interaction
model.

<Warning>
  For trust & safety and security:

  * Servers **MUST NOT** use elicitation to request sensitive information.

  Applications **SHOULD**:

  * Provide UI that makes it clear which server is requesting information
  * Allow users to review and modify their responses before sending
  * Respect user privacy and provide clear decline and cancel options
</Warning>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Elicitation](./132-elicitation.md)

**Next:** [Capabilities →](./134-capabilities.md)
