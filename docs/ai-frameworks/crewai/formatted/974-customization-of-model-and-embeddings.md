---
title: "Crewai: Customization of Model and Embeddings"
description: "Customization of Model and Embeddings section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Customization of Model and Embeddings


The tool defaults to using OpenAI for embeddings and summarization. For customization, utilize a configuration dictionary as shown below:

```python Code theme={null}
from chromadb.config import Settings

tool = MDXSearchTool(
    config={
        "embedding_model": {
            "provider": "openai",
            "config": {
                "model": "text-embedding-3-small",
                # "api_key": "sk-...",
            },
        },
        "vectordb": {
            "provider": "chromadb",  # or "qdrant"
            "config": {
                # "settings": Settings(persist_directory="/content/chroma", allow_reset=True, is_persistent=True),
                # from qdrant_client.models import VectorParams, Distance
                # "vectors_config": VectorParams(size=384, distance=Distance.COSINE),
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

**Previous:** [← Parameters](./973-parameters.md)

**Next:** [OCR Tool →](./975-ocr-tool.md)
