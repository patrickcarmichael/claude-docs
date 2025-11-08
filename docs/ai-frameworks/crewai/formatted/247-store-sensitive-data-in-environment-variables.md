---
title: "Crewai: Store sensitive data in environment variables"
description: "Store sensitive data in environment variables section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Store sensitive data in environment variables

crew = Crew(
    memory=True,
    embedder={
        "provider": "openai",
        "config": {
            "api_key": os.getenv("OPENAI_API_KEY"),
            "model": "text-embedding-3-small"
        }
    }
)
```

### Storage Security

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

**Previous:** [← Security Best Practices](./246-security-best-practices.md)

**Next:** [Use secure storage paths →](./248-use-secure-storage-paths.md)
