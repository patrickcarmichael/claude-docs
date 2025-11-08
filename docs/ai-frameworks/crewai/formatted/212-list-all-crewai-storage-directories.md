---
title: "Crewai: List all CrewAI storage directories"
description: "List all CrewAI storage directories section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# List all CrewAI storage directories

if os.path.exists(storage_path):
    print("\nStored files and directories:")
    for item in os.listdir(storage_path):
        item_path = os.path.join(storage_path, item)
        if os.path.isdir(item_path):
            print(f"📁 {item}/")
            # Show ChromaDB collections
            if os.path.exists(item_path):
                for subitem in os.listdir(item_path):
                    print(f"   └── {subitem}")
        else:
            print(f"📄 {item}")
else:
    print("No CrewAI storage directory found yet.")
```

### Controlling Storage Locations

#### Option 1: Environment Variable (Recommended)

```python  theme={null}
import os
from crewai import Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Get the base storage path](./211-get-the-base-storage-path.md)

**Next:** [Set custom storage location →](./213-set-custom-storage-location.md)
