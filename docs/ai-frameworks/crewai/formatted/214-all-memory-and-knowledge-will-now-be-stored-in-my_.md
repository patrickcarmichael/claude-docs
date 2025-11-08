---
title: "Crewai: All memory and knowledge will now be stored in ./my_project_storage/"
description: "All memory and knowledge will now be stored in ./my_project_storage/ section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# All memory and knowledge will now be stored in ./my_project_storage/

crew = Crew(
    agents=[...],
    tasks=[...],
    memory=True
)
```

#### Option 2: Custom Storage Paths

```python  theme={null}
import os
from crewai import Crew
from crewai.memory import LongTermMemory
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Set custom storage location](./213-set-custom-storage-location.md)

**Next:** [Configure custom storage location →](./215-configure-custom-storage-location.md)
