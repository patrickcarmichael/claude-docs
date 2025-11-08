---
title: "Crewai: Or use consistent embedding providers"
description: "Or use consistent embedding providers section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Or use consistent embedding providers

crew = Crew(
    agents=[...],
    tasks=[...],
    knowledge_sources=[...],
    embedder={"provider": "openai", "config": {"model": "text-embedding-3-small"}}
)
```

**"ChromaDB permission denied" errors:**

```bash  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← This happens when switching embedding providers](./186-this-happens-when-switching-embedding-providers.md)

**Next:** [Fix storage permissions →](./188-fix-storage-permissions.md)
