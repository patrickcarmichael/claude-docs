---
title: "Crewai: Storage Location Transparency"
description: "Storage Location Transparency section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Storage Location Transparency


<Info>
  **Understanding Storage Locations**: CrewAI uses platform-specific directories to store memory and knowledge files following OS conventions. Understanding these locations helps with production deployments, backups, and debugging.
</Info>

### Where CrewAI Stores Files

By default, CrewAI uses the `appdirs` library to determine storage locations following platform conventions. Here's exactly where your files are stored:

#### Default Storage Locations by Platform

**macOS:**

```
~/Library/Application Support/CrewAI/{project_name}/
├── knowledge/           # Knowledge base ChromaDB files
├── short_term_memory/   # Short-term memory ChromaDB files
├── long_term_memory/    # Long-term memory ChromaDB files
├── entities/            # Entity memory ChromaDB files
└── long_term_memory_storage.db  # SQLite database
```

**Linux:**

```
~/.local/share/CrewAI/{project_name}/
├── knowledge/
├── short_term_memory/
├── long_term_memory/
├── entities/
└── long_term_memory_storage.db
```

**Windows:**

```
C:\Users\{username}\AppData\Local\CrewAI\{project_name}\
├── knowledge\
├── short_term_memory\
├── long_term_memory\
├── entities\
└── long_term_memory_storage.db
```

### Finding Your Storage Location

To see exactly where CrewAI is storing files on your system:

```python  theme={null}
from crewai.utilities.paths import db_storage_path
import os

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Enable basic memory system](./209-enable-basic-memory-system.md)

**Next:** [Get the base storage path →](./211-get-the-base-storage-path.md)
