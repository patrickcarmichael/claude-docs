---
title: "Crewai: All knowledge will now be stored in ./my_project_storage/knowledge/"
description: "All knowledge will now be stored in ./my_project_storage/knowledge/ section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# All knowledge will now be stored in ./my_project_storage/knowledge/

crew = Crew(
    agents=[...],
    tasks=[...],
    knowledge_sources=[...]
)
```

#### Option 2: Custom Knowledge Storage

```python  theme={null}
from crewai.knowledge.storage.knowledge_storage import KnowledgeStorage
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Set custom storage location for all CrewAI data](./161-set-custom-storage-location-for-all-crewai-data.md)

**Next:** [Create custom storage with specific embedder →](./163-create-custom-storage-with-specific-embedder.md)
