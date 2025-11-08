---
title: "Crewai: Option 2: Use local embeddings (no external API calls)"
description: "Option 2: Use local embeddings (no external API calls) section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Option 2: Use local embeddings (no external API calls)

crew = Crew(
    agents=[agent],
    tasks=[task],
    memory=True,
    embedder={
        "provider": "ollama",
        "config": {"model": "mxbai-embed-large"}
    }
)
```

### Debugging Storage Issues

#### Check Storage Permissions

```python  theme={null}
import os
from crewai.utilities.paths import db_storage_path

storage_path = db_storage_path()
print(f"Storage path: {storage_path}")
print(f"Path exists: {os.path.exists(storage_path)}")
print(f"Is writable: {os.access(storage_path, os.W_OK) if os.path.exists(storage_path) else 'Path does not exist'}")

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Option 1: Match your LLM provider](./220-option-1-match-your-llm-provider.md)

**Next:** [Create with proper permissions →](./222-create-with-proper-permissions.md)
