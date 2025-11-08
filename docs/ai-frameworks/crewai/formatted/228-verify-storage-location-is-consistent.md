---
title: "Crewai: Verify storage location is consistent"
description: "Verify storage location is consistent section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Verify storage location is consistent

import os
print("CREWAI_STORAGE_DIR:", os.getenv("CREWAI_STORAGE_DIR"))
print("Current working directory:", os.getcwd())
print("Computed storage path:", db_storage_path())
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Ensure only one CrewAI instance accesses storage](./227-ensure-only-one-crewai-instance-accesses-storage.md)

**Next:** [Custom Embedder Configuration →](./229-custom-embedder-configuration.md)
