---
title: "Crewai: Use custom storage"
description: "Use custom storage section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Use custom storage

external_memory = ExternalMemory(storage=CustomStorage())

crew = Crew(
    agents=[...],
    tasks=[...],
    external_memory=external_memory
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create external memory instance with Mem0 Client](./242-create-external-memory-instance-with-mem0-client.md)

**Next:** [🧠 Memory System Comparison →](./244-memory-system-comparison.md)
