---
title: "Mcp: Implementation Guidelines"
description: "Implementation Guidelines section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

## Implementation Guidelines


1. Servers **SHOULD**:
   * Provide stable cursors
   * Handle invalid cursors gracefully

2. Clients **SHOULD**:
   * Treat a missing `nextCursor` as the end of results
   * Support both paginated and non-paginated flows

3. Clients **MUST** treat cursors as opaque tokens:
   * Don't make assumptions about cursor format
   * Don't attempt to parse or modify cursors
   * Don't persist cursors across sessions

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Operations Supporting Pagination](./239-operations-supporting-pagination.md)

**Next:** [Error Handling →](./241-error-handling.md)
