---
title: "Crewai: Verify storage location consistency"
description: "Verify storage location consistency section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Verify storage location consistency

import os
from crewai.utilities.paths import db_storage_path

print("CREWAI_STORAGE_DIR:", os.getenv("CREWAI_STORAGE_DIR"))
print("Computed storage path:", db_storage_path())
print("Knowledge path:", os.path.join(db_storage_path(), "knowledge"))
```

### Knowledge Reset Commands

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Fix storage permissions](./188-fix-storage-permissions.md)

**Next:** [Reset only agent-specific knowledge →](./190-reset-only-agent-specific-knowledge.md)
