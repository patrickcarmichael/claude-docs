---
title: "Crewai: Advanced OpenAI configuration"
description: "Advanced OpenAI configuration section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Advanced OpenAI configuration

crew = Crew(
    memory=True,
    embedder={
        "provider": "openai",
        "config": {
            "api_key": "your-openai-api-key",  # Optional: override env var
            "model": "text-embedding-3-large",
            "dimensions": 1536,  # Optional: reduce dimensions for smaller storage
            "organization_id": "your-org-id"  # Optional: for organization accounts
        }
    }
)
```

### Azure OpenAI Embeddings

For enterprise users with Azure OpenAI deployments.

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "openai",  # Use openai provider for Azure
        "config": {
            "api_key": "your-azure-api-key",
            "api_base": "https://your-resource.openai.azure.com/",
            "api_type": "azure",
            "api_version": "2023-05-15",
            "model": "text-embedding-3-small",
            "deployment_id": "your-deployment-name"  # Azure deployment name
        }
    }
)
```

### Google AI Embeddings

Use Google's text embedding models for integration with Google Cloud services.

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "google",
        "config": {
            "api_key": "your-google-api-key",
            "model": "text-embedding-004"  # or "text-embedding-preview-0409"
        }
    }
)
```

### Vertex AI Embeddings

For Google Cloud users with Vertex AI access.

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "vertexai",
        "config": {
            "project_id": "your-gcp-project-id",
            "region": "us-central1",  # or your preferred region
            "api_key": "your-service-account-key",
            "model_name": "textembedding-gecko"
        }
    }
)
```

### Ollama Embeddings (Local)

Run embeddings locally for privacy and cost savings.

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Basic OpenAI configuration (uses environment OPENAI_API_KEY)](./230-basic-openai-configuration-uses-environment-openai.md)

**Next:** [First, install and run Ollama locally, then pull an embedding model: →](./232-first-install-and-run-ollama-locally-then-pull-an-.md)
