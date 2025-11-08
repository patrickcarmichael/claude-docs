---
title: "Crewai: Enable basic memory system"
description: "Enable basic memory system section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Enable basic memory system

crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,  # Enables short-term, long-term, and entity memory
    verbose=True
)
```

### How It Works

* **Short-Term Memory**: Uses ChromaDB with RAG for current context
* **Long-Term Memory**: Uses SQLite3 to store task results across sessions
* **Entity Memory**: Uses RAG to track entities (people, places, concepts)
* **Storage Location**: Platform-specific location via `appdirs` package
* **Custom Storage Directory**: Set `CREWAI_STORAGE_DIR` environment variable

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← 1. Basic Memory System (Recommended)](./208-1-basic-memory-system-recommended.md)

**Next:** [Storage Location Transparency →](./210-storage-location-transparency.md)
