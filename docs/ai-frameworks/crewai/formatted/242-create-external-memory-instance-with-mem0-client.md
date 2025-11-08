---
title: "Crewai: Create external memory instance with Mem0 Client"
description: "Create external memory instance with Mem0 Client section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create external memory instance with Mem0 Client

external_memory = ExternalMemory(
    embedder_config={
        "provider": "mem0",
        "config": {
            "user_id": "john",
            "org_id": "my_org_id",        # Optional
            "project_id": "my_project_id", # Optional
            "api_key": "custom-api-key"    # Optional - overrides env var
            "run_id": "my_run_id",        # Optional - for short-term memory
            "includes": "include1",       # Optional 
            "excludes": "exclude1",       # Optional
            "infer": True                 # Optional defaults to True
            "custom_categories": new_categories  # Optional - custom categories for user memory
        },
    }
)

crew = Crew(
    agents=[...],
    tasks=[...],
    external_memory=external_memory, # Separate from basic memory
    process=Process.sequential,
    verbose=True
)
```

### Custom Storage Implementation

```python  theme={null}
from crewai.memory.external.external_memory import ExternalMemory
from crewai.memory.storage.interface import Storage

class CustomStorage(Storage):
    def __init__(self):
        self.memories = []

    def save(self, value, metadata=None, agent=None):
        self.memories.append({
            "value": value,
            "metadata": metadata,
            "agent": agent
        })

    def search(self, query, limit=10, score_threshold=0.5):
        # Implement your search logic here
        return [m for m in self.memories if query.lower() in str(m["value"]).lower()]

    def reset(self):
        self.memories = []

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create external memory instance with local Mem0 Configuration](./241-create-external-memory-instance-with-local-mem0-co.md)

**Next:** [Use custom storage →](./243-use-custom-storage.md)
