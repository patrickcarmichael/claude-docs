---
title: "Crewai: Ensure only one CrewAI instance accesses storage"
description: "Ensure only one CrewAI instance accesses storage section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Ensure only one CrewAI instance accesses storage

import fcntl
import os

storage_path = db_storage_path()
lock_file = os.path.join(storage_path, ".crewai.lock")

with open(lock_file, 'w') as f:
    fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    # Your CrewAI code here
```

**Storage not persisting between runs:**

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Fix permissions](./226-fix-permissions.md)

**Next:** [Verify storage location is consistent →](./228-verify-storage-location-is-consistent.md)
