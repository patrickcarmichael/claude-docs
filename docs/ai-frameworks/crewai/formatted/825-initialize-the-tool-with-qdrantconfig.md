---
title: "Crewai: Initialize the tool with QdrantConfig"
description: "Initialize the tool with QdrantConfig section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Initialize the tool with QdrantConfig

qdrant_tool = QdrantVectorSearchTool(
    qdrant_config=QdrantConfig(
        qdrant_url="your_qdrant_url",
        qdrant_api_key="your_qdrant_api_key",
        collection_name="your_collection"
    )
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Basic Usage](./824-basic-usage.md)

**Next:** [Create an agent that uses the tool →](./826-create-an-agent-that-uses-the-tool.md)
