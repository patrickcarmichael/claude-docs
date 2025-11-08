---
title: "Crewai: Configure custom storage location"
description: "Configure custom storage location section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Configure custom storage location

custom_storage_path = "./storage"
os.makedirs(custom_storage_path, exist_ok=True)

crew = Crew(
    memory=True,
    long_term_memory=LongTermMemory(
        storage=LTMSQLiteStorage(
            db_path=f"{custom_storage_path}/memory.db"
        )
    )
)
```

#### Option 3: Project-Specific Storage

```python  theme={null}
import os
from pathlib import Path

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← All memory and knowledge will now be stored in ./my_project_storage/](./214-all-memory-and-knowledge-will-now-be-stored-in-my_.md)

**Next:** [Store in project directory →](./216-store-in-project-directory.md)
