---
title: "Crewai: Initialize Qdrant search tool"
description: "Initialize Qdrant search tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Initialize Qdrant search tool

from crewai_tools import QdrantConfig

qdrant_tool = QdrantVectorSearchTool(
    qdrant_config=QdrantConfig(
        qdrant_url=os.getenv("QDRANT_URL"),
        qdrant_api_key=os.getenv("QDRANT_API_KEY"),
        collection_name=collection_name,
        limit=3,
        score_threshold=0.35
    )
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize Qdrant client and load data](./834-initialize-qdrant-client-and-load-data.md)

**Next:** [Create CrewAI agents →](./836-create-crewai-agents.md)
