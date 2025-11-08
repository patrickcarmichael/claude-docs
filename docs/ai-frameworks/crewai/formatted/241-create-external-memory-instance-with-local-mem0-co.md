---
title: "Crewai: Create external memory instance with local Mem0 Configuration"
description: "Create external memory instance with local Mem0 Configuration section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create external memory instance with local Mem0 Configuration

external_memory = ExternalMemory(
    embedder_config={
        "provider": "mem0",
        "config": {
            "user_id": "john",
            "local_mem0_config": {
                "vector_store": {
                    "provider": "qdrant",
                    "config": {"host": "localhost", "port": 6333}
                },
                "llm": {
                    "provider": "openai",
                    "config": {"api_key": "your-api-key", "model": "gpt-4"}
                },
                "embedder": {
                    "provider": "openai",
                    "config": {"api_key": "your-api-key", "model": "text-embedding-3-small"}
                }
            },
            "infer": True # Optional defaults to True
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

### Advanced External Memory with Mem0 Client

When using Mem0 Client, you can customize the memory configuration further, by using parameters like 'includes', 'excludes', 'custom\_categories', 'infer' and 'run\_id' (this is only for short-term memory).
You can find more details in the [Mem0 documentation](https://docs.mem0.ai/).

```python  theme={null}
import os
from crewai import Agent, Crew, Process, Task
from crewai.memory.external.external_memory import ExternalMemory

new_categories = [
    {"lifestyle_management_concerns": "Tracks daily routines, habits, hobbies and interests including cooking, time management and work-life balance"},
    {"seeking_structure": "Documents goals around creating routines, schedules, and organized systems in various life areas"},
    {"personal_information": "Basic information about the user including name, preferences, and personality traits"}
]

os.environ["MEM0_API_KEY"] = "your-api-key"

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← 2. External Memory](./240-2-external-memory.md)

**Next:** [Create external memory instance with Mem0 Client →](./242-create-external-memory-instance-with-mem0-client.md)
