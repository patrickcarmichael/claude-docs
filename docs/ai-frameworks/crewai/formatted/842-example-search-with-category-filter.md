---
title: "Crewai: Example: search with category filter"
description: "Example: search with category filter section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example: search with category filter

# Results will be filtered where category == "technology"
```

### Preset Filters with QdrantConfig

For complex filtering, use Qdrant Filter instances in your configuration:

```python  theme={null}
from qdrant_client.http import models as qmodels
from crewai_tools import QdrantVectorSearchTool, QdrantConfig

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Agent will use these parameters when calling the tool](./841-agent-will-use-these-parameters-when-calling-the-t.md)

**Next:** [Create a filter for specific conditions →](./843-create-a-filter-for-specific-conditions.md)
