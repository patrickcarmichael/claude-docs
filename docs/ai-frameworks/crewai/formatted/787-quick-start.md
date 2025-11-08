---
title: "Crewai: Quick start"
description: "Quick start section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Quick start


```python Code theme={null}
from crewai_tools import MongoDBVectorSearchTool

tool = MongoDBVectorSearchTool(
  connection_string="mongodb+srv://...",
  database_name="mydb",
  collection_name="docs",
)

print(tool.run(query="how to create vector index"))
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Parameters](./786-parameters.md)

**Next:** [Index creation helpers →](./788-index-creation-helpers.md)
