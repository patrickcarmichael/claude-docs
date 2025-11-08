---
title: "Crewai: Custom Model and Embeddings"
description: "Custom Model and Embeddings section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Custom Model and Embeddings


The tool intends to use OpenAI for both embeddings and summarization by default. Users will have the option to customize the model using a config dictionary as follows:

```python Code theme={null}
tool = PGSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Arguments](./819-arguments.md)

**Next:** [Qdrant Vector Search Tool →](./821-qdrant-vector-search-tool.md)
