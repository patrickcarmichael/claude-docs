---
title: "Crewai: Quickstart Examples"
description: "Quickstart Examples section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Quickstart Examples


<Tip>
  For file-based Knowledge Sources, make sure to place your files in a `knowledge` directory at the root of your project.
  Also, use relative paths from the `knowledge` directory when creating the source.
</Tip>

### Vector store (RAG) client configuration

CrewAI exposes a provider-neutral RAG client abstraction for vector stores. The default provider is ChromaDB, and Qdrant is supported as well. You can switch providers using configuration utilities.

Supported today:

* ChromaDB (default)
* Qdrant

```python Code theme={null}
from crewai.rag.config.utils import set_rag_config, get_rag_client, clear_rag_config

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Overview](./127-overview.md)

**Next:** [ChromaDB (default) →](./129-chromadb-default.md)
