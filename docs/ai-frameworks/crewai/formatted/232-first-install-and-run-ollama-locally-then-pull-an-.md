---
title: "Crewai: First, install and run Ollama locally, then pull an embedding model:"
description: "First, install and run Ollama locally, then pull an embedding model: section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# First, install and run Ollama locally, then pull an embedding model:

# ollama pull mxbai-embed-large

crew = Crew(
    memory=True,
    embedder={
        "provider": "ollama",
        "config": {
            "model": "mxbai-embed-large",  # or "nomic-embed-text"
            "url": "http://localhost:11434/api/embeddings"  # Default Ollama URL
        }
    }
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Advanced OpenAI configuration](./231-advanced-openai-configuration.md)

**Next:** [For custom Ollama installations →](./233-for-custom-ollama-installations.md)
