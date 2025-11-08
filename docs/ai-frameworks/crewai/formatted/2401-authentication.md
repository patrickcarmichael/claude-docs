---
title: "Crewai: Authentication"
description: "Authentication section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Authentication


All API requests require authentication using a Bearer token. Include your token in the `Authorization` header:

```bash  theme={null}
curl -H "Authorization: Bearer YOUR_CREW_TOKEN" \
  https://your-crew-url.crewai.com/inputs
```

### Token Types

| Token Type            | Scope                     | Use Case                                                     |
| :-------------------- | :------------------------ | :----------------------------------------------------------- |
| **Bearer Token**      | Organization-level access | Full crew operations, ideal for server-to-server integration |
| **User Bearer Token** | User-scoped access        | Limited permissions, suitable for user-specific operations   |

<Tip>
  You can find both token types in the Status tab of your crew's detail page in the CrewAI AMP dashboard.
</Tip>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Quick Start](./2400-quick-start.md)

**Next:** [Base URL →](./2402-base-url.md)
