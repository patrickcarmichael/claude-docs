---
title: "Crewai: Setup custom model for vectorizer and generative model"
description: "Setup custom model for vectorizer and generative model section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Setup custom model for vectorizer and generative model

tool = WeaviateVectorSearchTool(
    collection_name='example_collections',
    limit=3,
    alpha=0.75,
    vectorizer=Configure.Vectorizer.text2vec_openai(model="nomic-embed-text"),
    generative_model=Configure.Generative.openai(model="gpt-4o-mini"),
    weaviate_cluster_url="https://your-weaviate-cluster-url.com",
    weaviate_api_key="your-weaviate-api-key",
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Advanced Configuration](./890-advanced-configuration.md)

**Next:** [Preloading Documents →](./892-preloading-documents.md)
