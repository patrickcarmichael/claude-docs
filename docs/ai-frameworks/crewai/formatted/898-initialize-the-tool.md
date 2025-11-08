---
title: "Crewai: Initialize the tool"
description: "Initialize the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Initialize the tool

weaviate_tool = WeaviateVectorSearchTool(
    collection_name='example_collections',
    limit=3,
    alpha=0.75,
    weaviate_cluster_url="https://your-weaviate-cluster-url.com",
    weaviate_api_key="your-weaviate-api-key",
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Agent Integration Example](./897-agent-integration-example.md)

**Next:** [Create an agent with the tool →](./899-create-an-agent-with-the-tool.md)
