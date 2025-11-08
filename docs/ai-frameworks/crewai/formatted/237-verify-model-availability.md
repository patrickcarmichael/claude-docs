---
title: "Crewai: Verify model availability"
description: "Verify model availability section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Verify model availability

from crewai.rag.embeddings.configurator import EmbeddingConfigurator

configurator = EmbeddingConfigurator()
try:
    embedder = configurator.configure_embedder({
        "provider": "ollama",
        "config": {"model": "mxbai-embed-large"}
    })
    print("Embedder configured successfully")
except Exception as e:
    print(f"Configuration error: {e}")
```

**API key issues:**

```python  theme={null}
import os

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Test different providers with the same data](./236-test-different-providers-with-the-same-data.md)

**Next:** [Check if API keys are set →](./238-check-if-api-keys-are-set.md)
