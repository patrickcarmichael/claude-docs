---
title: "Crewai: For custom Ollama installations"
description: "For custom Ollama installations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# For custom Ollama installations

crew = Crew(
    memory=True,
    embedder={
        "provider": "ollama",
        "config": {
            "model": "mxbai-embed-large",
            "url": "http://your-ollama-server:11434/api/embeddings"
        }
    }
)
```

### Cohere Embeddings

Use Cohere's embedding models for multilingual support.

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "cohere",
        "config": {
            "api_key": "your-cohere-api-key",
            "model": "embed-english-v3.0"  # or "embed-multilingual-v3.0"
        }
    }
)
```

### VoyageAI Embeddings

High-performance embeddings optimized for retrieval tasks.

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "voyageai",
        "config": {
            "api_key": "your-voyage-api-key",
            "model": "voyage-large-2",  # or "voyage-code-2" for code
            "input_type": "document"  # or "query"
        }
    }
)
```

### AWS Bedrock Embeddings

For AWS users with Bedrock access.

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "bedrock",
        "config": {
            "aws_access_key_id": "your-access-key",
            "aws_secret_access_key": "your-secret-key",
            "region_name": "us-east-1",
            "model": "amazon.titan-embed-text-v1"
        }
    }
)
```

### Hugging Face Embeddings

Use open-source models from Hugging Face.

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "huggingface",
        "config": {
            "api_key": "your-hf-token",  # Optional for public models
            "model": "sentence-transformers/all-MiniLM-L6-v2",
            "api_url": "https://api-inference.huggingface.co"  # or your custom endpoint
        }
    }
)
```

### IBM Watson Embeddings

For IBM Cloud users.

```python  theme={null}
crew = Crew(
    memory=True,
    embedder={
        "provider": "watson",
        "config": {
            "api_key": "your-watson-api-key",
            "url": "your-watson-instance-url",
            "model": "ibm/slate-125m-english-rtrvr"
        }
    }
)
```

### Mem0 Provider

Short-Term Memory and Entity Memory both supports a tight integration with both Mem0 OSS and Mem0 Client as a provider. Here is how you can use Mem0 as a provider.

```python  theme={null}
from crewai.memory.short_term.short_term_memory import ShortTermMemory
from crewai.memory.entity_entity_memory import EntityMemory

mem0_oss_embedder_config = {
        "provider": "mem0",
        "config": {
            "user_id": "john",
            "local_mem0_config": {
                "vector_store": {"provider": "qdrant","config": {"host": "localhost", "port": 6333}},
                "llm": {"provider": "openai","config": {"api_key": "your-api-key", "model": "gpt-4"}},
                "embedder": {"provider": "openai","config": {"api_key": "your-api-key", "model": "text-embedding-3-small"}}
            },
            "infer": True # Optional defaults to True
        },
    }

mem0_client_embedder_config = {
        "provider": "mem0",
        "config": {
            "user_id": "john",
            "org_id": "my_org_id",        # Optional
            "project_id": "my_project_id", # Optional
            "api_key": "custom-api-key"    # Optional - overrides env var
            "run_id": "my_run_id",        # Optional - for short-term memory
            "includes": "include1",       # Optional 
            "excludes": "exclude1",       # Optional
            "infer": True                 # Optional defaults to True
            "custom_categories": new_categories  # Optional - custom categories for user memory
        },
    }

short_term_memory_mem0_oss = ShortTermMemory(embedder_config=mem0_oss_embedder_config) # Short Term Memory with Mem0 OSS
short_term_memory_mem0_client = ShortTermMemory(embedder_config=mem0_client_embedder_config) # Short Term Memory with Mem0 Client
entity_memory_mem0_oss = EntityMemory(embedder_config=mem0_oss_embedder_config) # Entity Memory with Mem0 OSS
entity_memory_mem0_client = EntityMemory(embedder_config=mem0_client_embedder_config) # Short Term Memory with Mem0 Client

crew = Crew(
    memory=True,
    short_term_memory=short_term_memory_mem0_oss, # or short_term_memory_mem0_client
    entity_memory=entity_memory_mem0_oss # or entity_memory_mem0_client
)
```

### Choosing the Right Embedding Provider

When selecting an embedding provider, consider factors like performance, privacy, cost, and integration needs.\
Below is a comparison to help you decide:

| Provider         | Best For                        | Pros                                | Cons                              |
| ---------------- | ------------------------------- | ----------------------------------- | --------------------------------- |
| **OpenAI**       | General use, high reliability   | High quality, widely tested         | Paid service, API key required    |
| **Ollama**       | Privacy-focused, cost savings   | Free, runs locally, fully private   | Requires local installation/setup |
| **Google AI**    | Integration in Google ecosystem | Strong performance, good support    | Google account required           |
| **Azure OpenAI** | Enterprise & compliance needs   | Enterprise-grade features, security | More complex setup process        |
| **Cohere**       | Multilingual content handling   | Excellent language support          | More niche use cases              |
| **VoyageAI**     | Information retrieval & search  | Optimized for retrieval tasks       | Relatively new provider           |
| **Mem0**         | Per-user personalization        | Search-optimized embeddings         | Paid service, API key required    |

### Environment Variable Configuration

For security, store API keys in environment variables:

```python  theme={null}
import os

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← First, install and run Ollama locally, then pull an embedding model:](./232-first-install-and-run-ollama-locally-then-pull-an-.md)

**Next:** [Set environment variables →](./234-set-environment-variables.md)
