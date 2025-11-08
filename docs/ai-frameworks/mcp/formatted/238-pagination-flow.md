---
title: "Mcp: Pagination Flow"
description: "Pagination Flow section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

## Pagination Flow


```mermaid  theme={null}
sequenceDiagram
    participant Client
    participant Server

    Client->>Server: List Request (no cursor)
    loop Pagination Loop
      Server-->>Client: Page of results + nextCursor
      Client->>Server: List Request (with cursor)
    end
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Request Format](./237-request-format.md)

**Next:** [Operations Supporting Pagination →](./239-operations-supporting-pagination.md)
