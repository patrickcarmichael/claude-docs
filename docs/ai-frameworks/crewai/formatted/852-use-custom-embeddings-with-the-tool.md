---
title: "Crewai: Use custom embeddings with the tool"
description: "Use custom embeddings with the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Use custom embeddings with the tool

from crewai_tools import QdrantConfig

tool = QdrantVectorSearchTool(
    qdrant_config=QdrantConfig(
        qdrant_url="your_url",
        qdrant_api_key="your_key",
        collection_name="your_collection"
    ),
    custom_embedding_fn=custom_embeddings  # Pass your custom function
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Load model and tokenizer](./851-load-model-and-tokenizer.md)

**Next:** [Error Handling →](./853-error-handling.md)
