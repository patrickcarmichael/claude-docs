---
title: "Crewai: Custom model and embeddings"
description: "Custom model and embeddings section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Custom model and embeddings


By default, the tool uses OpenAI for both embeddings and summarization.
To customize the model, you can use a config dictionary as follows:

```python Code theme={null}
from chromadb.config import Settings

tool = TXTSearchTool(
    config={
        # Required: embeddings provider + config
        "embedding_model": {
            "provider": "openai",  # or google-generativeai, cohere, ollama, ...
            "config": {
                "model": "text-embedding-3-small",
                # "api_key": "sk-...",  # optional if env var is set
                # Provider examples:
                # Google → model: "models/embedding-001", task_type: "retrieval_document"
                # Cohere → model: "embed-english-v3.0"
                # Ollama → model: "nomic-embed-text"
            },
        },

        # Required: vector database config
        "vectordb": {
            "provider": "chromadb",  # or "qdrant"
            "config": {
                # Chroma settings (optional persistence)
                # "settings": Settings(
                #     persist_directory="/content/chroma",
                #     allow_reset=True,
                #     is_persistent=True,
                # ),

                # Qdrant vector params example:
                # from qdrant_client.models import VectorParams, Distance
                # "vectors_config": VectorParams(size=384, distance=Distance.COSINE),

                # Note: collection name is controlled by the tool (default: "rag_tool_collection").
            }
        },
    }
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Arguments](./1014-arguments.md)

**Next:** [XML RAG Search →](./1016-xml-rag-search.md)
