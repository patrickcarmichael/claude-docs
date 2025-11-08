---
title: "Crewai: Connect to CrewAI's ChromaDB"
description: "Connect to CrewAI's ChromaDB section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Connect to CrewAI's ChromaDB

storage_path = db_storage_path()
chroma_path = os.path.join(storage_path, "knowledge")

if os.path.exists(chroma_path):
    client = chromadb.PersistentClient(path=chroma_path)
    collections = client.list_collections()

    print("ChromaDB Collections:")
    for collection in collections:
        print(f"  - {collection.name}: {collection.count()} documents")
else:
    print("No ChromaDB storage found")
```

#### Reset Storage (Debugging)

```python  theme={null}
from crewai import Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create with proper permissions](./222-create-with-proper-permissions.md)

**Next:** [Reset all memory storage →](./224-reset-all-memory-storage.md)
