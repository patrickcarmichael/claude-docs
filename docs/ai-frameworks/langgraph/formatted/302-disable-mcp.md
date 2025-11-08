---
title: "Langgraph: Disable MCP"
description: "Disable MCP section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Disable MCP


To disable the MCP endpoint, set `disable_mcp` to `true` in your `langgraph.json` configuration file:

```json
{
  "http": {
    "disable_mcp": true
  }
}
```

This will prevent the server from exposing the `/mcp` endpoint.

---

concepts/langgraph_self_hosted_data_plane.md

---

---

search:
  boost: 2

---

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Authentication](./301-authentication.md)

**Next:** [Self-Hosted Data Plane →](./303-self-hosted-data-plane.md)
