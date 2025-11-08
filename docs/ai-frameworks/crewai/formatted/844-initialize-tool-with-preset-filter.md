---
title: "Crewai: Initialize tool with preset filter"
description: "Initialize tool with preset filter section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Initialize tool with preset filter

qdrant_tool = QdrantVectorSearchTool(
    qdrant_config=QdrantConfig(
        qdrant_url="your_url",
        qdrant_api_key="your_key",
        collection_name="your_collection",
        filter=preset_filter  # Preset filter applied to all searches
    )
)
```

### Combining Filters

The tool automatically combines preset filters from `QdrantConfig` with dynamic filters from `filter_by` and `filter_value`:

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create a filter for specific conditions](./843-create-a-filter-for-specific-conditions.md)

**Next:** [If QdrantConfig has a preset filter for category="research" →](./845-if-qdrantconfig-has-a-preset-filter-for-categoryre.md)
