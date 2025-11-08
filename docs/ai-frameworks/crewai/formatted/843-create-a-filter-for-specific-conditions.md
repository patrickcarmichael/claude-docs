---
title: "Crewai: Create a filter for specific conditions"
description: "Create a filter for specific conditions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a filter for specific conditions

preset_filter = qmodels.Filter(
    must=[
        qmodels.FieldCondition(
            key="category",
            match=qmodels.MatchValue(value="research")
        ),
        qmodels.FieldCondition(
            key="year",
            match=qmodels.MatchValue(value=2024)
        )
    ]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example: search with category filter](./842-example-search-with-category-filter.md)

**Next:** [Initialize tool with preset filter →](./844-initialize-tool-with-preset-filter.md)
