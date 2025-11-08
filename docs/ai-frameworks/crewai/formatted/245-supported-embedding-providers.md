---
title: "Crewai: Supported Embedding Providers"
description: "Supported Embedding Providers section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Supported Embedding Providers


### OpenAI (Default)

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "openai",
        "config": {"model": "text-embedding-3-small"}
    }
)
```

### Ollama

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "ollama",
        "config": {"model": "mxbai-embed-large"}
    }
)
```

### Google AI

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "google",
        "config": {
            "api_key": "your-api-key",
            "model": "text-embedding-004"
        }
    }
)
```

### Azure OpenAI

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "openai",
        "config": {
            "api_key": "your-api-key",
            "api_base": "https://your-resource.openai.azure.com/",
            "api_version": "2023-05-15",
            "model_name": "text-embedding-3-small"
        }
    }
)
```

### Vertex AI

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "vertexai",
        "config": {
            "project_id": "your-project-id",
            "region": "your-region",
            "api_key": "your-api-key",
            "model_name": "textembedding-gecko"
        }
    }
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← 🧠 Memory System Comparison](./244-memory-system-comparison.md)

**Next:** [Security Best Practices →](./246-security-best-practices.md)
