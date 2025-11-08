---
title: "Crewai: Configuration Options"
description: "Configuration Options section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Configuration Options


The JSONSearchTool supports extensive customization through a configuration dictionary. This allows users to select different models for embeddings and summarization based on their requirements.

```python Code theme={null}
tool = JSONSearchTool(
    config={
        "llm": {
            "provider": "ollama",  # Other options include google, openai, anthropic, llama2, etc.
            "config": {
                "model": "llama2",
                # Additional optional configurations can be specified here.
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            },
        },
        "embedding_model": {
            "provider": "google", # or openai, ollama, ...
            "config": {
                "model": "models/embedding-001",
                "task_type": "retrieval_document",
                # Further customization options can be added here.
            },
        },
    }
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Arguments](./963-arguments.md)

**Next:** [MDX RAG Search →](./965-mdx-rag-search.md)
