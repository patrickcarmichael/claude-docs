---
title: "Crewai: Connect to Weaviate"
description: "Connect to Weaviate section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Connect to Weaviate

client = weaviate.connect_to_weaviate_cloud(
    cluster_url="https://your-weaviate-cluster-url.com",
    auth_credentials=Auth.api_key("your-weaviate-api-key"),
    headers={"X-OpenAI-Api-Key": "your-openai-api-key"}
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Preloading Documents](./892-preloading-documents.md)

**Next:** [Get or create collection →](./894-get-or-create-collection.md)
