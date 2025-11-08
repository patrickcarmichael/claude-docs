---
title: "Crewai: Use without exposing keys in code"
description: "Use without exposing keys in code section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Use without exposing keys in code

crew = Crew(
    memory=True,
    embedder={
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-small"
            # API key automatically loaded from environment
        }
    }
)
```

### Testing Different Embedding Providers

Compare embedding providers for your specific use case:

```python  theme={null}
from crewai import Crew
from crewai.utilities.paths import db_storage_path

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Set environment variables](./234-set-environment-variables.md)

**Next:** [Test different providers with the same data →](./236-test-different-providers-with-the-same-data.md)
