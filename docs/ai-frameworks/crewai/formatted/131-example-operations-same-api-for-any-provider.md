---
title: "Crewai: Example operations (same API for any provider)"
description: "Example operations (same API for any provider) section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example operations (same API for any provider)

client = qdrant_client  # or chromadb_client
client.create_collection(collection_name="docs")
client.add_documents(
    collection_name="docs",
    documents=[{"id": "1", "content": "CrewAI enables collaborative AI agents."}],
)
results = client.search(collection_name="docs", query="collaborative agents", limit=3)

clear_rag_config()  # optional reset
```

This RAG client is separate from Knowledge’s built-in storage. Use it when you need direct vector-store control or custom retrieval pipelines.

### Basic String Knowledge Example

```python Code theme={null}
from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Qdrant](./130-qdrant.md)

**Next:** [Create a knowledge source →](./132-create-a-knowledge-source.md)
