---
title: "Crewai: After kickoff - knowledge initialized"
description: "After kickoff - knowledge initialized section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# After kickoff - knowledge initialized

print(f"After kickoff - Agent knowledge: {agent.knowledge}")
print(f"Agent knowledge collection: {agent.knowledge.storage.collection_name}")
print(f"Number of sources: {len(agent.knowledge.sources)}")
```

#### Verify Knowledge Storage Locations

```python  theme={null}
import os
from crewai.utilities.paths import db_storage_path

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Before kickoff - knowledge not initialized](./177-before-kickoff-knowledge-not-initialized.md)

**Next:** [Check storage structure →](./179-check-storage-structure.md)
