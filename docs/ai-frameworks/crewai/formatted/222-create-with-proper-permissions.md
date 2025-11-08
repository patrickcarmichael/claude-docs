---
title: "Crewai: Create with proper permissions"
description: "Create with proper permissions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create with proper permissions

if not os.path.exists(storage_path):
    os.makedirs(storage_path, mode=0o755, exist_ok=True)
    print(f"Created storage directory: {storage_path}")
```

#### Inspect ChromaDB Collections

```python  theme={null}
import chromadb
from crewai.utilities.paths import db_storage_path

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Option 2: Use local embeddings (no external API calls)](./221-option-2-use-local-embeddings-no-external-api-call.md)

**Next:** [Connect to CrewAI's ChromaDB →](./223-connect-to-crewais-chromadb.md)
