---
title: "Crewai: Create a RAG tool with custom configuration"
description: "Create a RAG tool with custom configuration section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a RAG tool with custom configuration

config = {
    "vectordb": {
        "provider": "qdrant",
        "config": {
            "collection_name": "my-collection"
        }
    },
    "embedding_model": {
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-small"
        }
    }
}

rag_tool = RagTool(config=config, summarize=True)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Advanced Configuration](./714-advanced-configuration.md)

**Next:** [Conclusion →](./716-conclusion.md)
