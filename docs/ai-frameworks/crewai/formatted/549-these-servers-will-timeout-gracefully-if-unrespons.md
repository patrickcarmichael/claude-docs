---
title: "Crewai: These servers will timeout gracefully if unresponsive"
description: "These servers will timeout gracefully if unresponsive section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# These servers will timeout gracefully if unresponsive

mcps=[
    "https://slow-server.com/mcp",        # Will timeout after 10s if unresponsive
    "https://overloaded-api.com/mcp"      # Will timeout if discovery takes > 15s
]
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← 4. Not crash or hang on server failures](./548-4-not-crash-or-hang-on-server-failures.md)

**Next:** [Performance Features →](./550-performance-features.md)
