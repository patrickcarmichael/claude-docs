---
title: "Crewai: - embedding_model (required): choose provider + provider-specific config"
description: "- embedding_model (required): choose provider + provider-specific config section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# - embedding_model (required): choose provider + provider-specific config

# - vectordb (required): choose vector DB and pass its config

tool = PDFSearchTool(
    config={
        "embedding_model": {
            # Supported providers: "openai", "azure", "google-generativeai", "google-vertex",
            # "voyageai", "cohere", "huggingface", "jina", "sentence-transformer",
            # "text2vec", "ollama", "openclip", "instructor", "onnx", "roboflow", "watsonx", "custom"
            "provider": "openai",  # or: "google-generativeai", "cohere", "ollama", ...
            "config": {
                # Model identifier for the chosen provider. "model" will be auto-mapped to "model_name" internally.
                "model": "text-embedding-3-small",
                # Optional: API key. If omitted, the tool will use provider-specific env vars when available
                # (e.g., OPENAI_API_KEY for provider="openai").
                # "api_key": "sk-...",

                # Provider-specific examples:
                # --- Google Generative AI ---
                # (Set provider="google-generativeai" above)
                # "model": "models/embedding-001",
                # "task_type": "retrieval_document",
                # "title": "Embeddings",

                # --- Cohere ---
                # (Set provider="cohere" above)
                # "model": "embed-english-v3.0",

                # --- Ollama (local) ---
                # (Set provider="ollama" above)
                # "model": "nomic-embed-text",
            },
        },
        "vectordb": {
                    "provider": "chromadb",  # or "qdrant"
                    "config": {
                        # For ChromaDB: pass "settings" (chromadb.config.Settings) or rely on defaults.
                        # Example (uncomment and import):
                        # from chromadb.config import Settings
                        # "settings": Settings(
                        #     persist_directory="/content/chroma",
                        #     allow_reset=True,
                        #     is_persistent=True,
                        # ),

                        # For Qdrant: pass "vectors_config" (qdrant_client.models.VectorParams).
                        # Example (uncomment and import):
                        # from qdrant_client.models import VectorParams, Distance
                        # "vectors_config": VectorParams(size=384, distance=Distance.COSINE),

                        # Note: collection name is controlled by the tool (default: "rag_tool_collection"), not set here.
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

**Previous:** [← Custom model and embeddings](./1005-custom-model-and-embeddings.md)

**Next:** [TXT RAG Search →](./1007-txt-rag-search.md)
