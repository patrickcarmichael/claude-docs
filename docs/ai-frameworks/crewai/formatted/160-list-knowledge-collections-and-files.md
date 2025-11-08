---
title: "Crewai: List knowledge collections and files"
description: "List knowledge collections and files section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# List knowledge collections and files

if os.path.exists(knowledge_path):
    print("\nKnowledge storage contents:")
    for item in os.listdir(knowledge_path):
        item_path = os.path.join(knowledge_path, item)
        if os.path.isdir(item_path):
            print(f"📁 Collection: {item}/")
            # Show collection contents
            try:
                for subitem in os.listdir(item_path):
                    print(f"   └── {subitem}")
            except PermissionError:
                print(f"   └── (permission denied)")
        else:
            print(f"📄 {item}")
else:
    print("No knowledge storage found yet.")
```

### Controlling Knowledge Storage Locations

#### Option 1: Environment Variable (Recommended)

```python  theme={null}
import os
from crewai import Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Get the knowledge storage path](./159-get-the-knowledge-storage-path.md)

**Next:** [Set custom storage location for all CrewAI data →](./161-set-custom-storage-location-for-all-crewai-data.md)
