---
title: "Langgraph: Usage overview"
description: "Usage overview section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Usage overview


To enable MCP:

- Upgrade to use langgraph-api>=0.2.3. If you are deploying LangGraph Platform, this will be done for you automatically if you create a new revision.
- MCP tools (agents) will be automatically exposed.
- Connect with any MCP-compliant client that supports Streamable HTTP.

### Client

Use an MCP-compliant client to connect to the LangGraph server. The following example shows how to connect using [langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters).

Install the adapter with:

```bash
pip install langchain-mcp-adapters
```

Here is an example of how to connect to a remote MCP endpoint and use an agent as a tool:

```python

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the graph](./297-run-the-graph.md)

**Next:** [Create server parameters for stdio connection →](./299-create-server-parameters-for-stdio-connection.md)
