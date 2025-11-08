---
title: "Crewai: Option 2: Use local embeddings (no external API calls)"
description: "Option 2: Use local embeddings (no external API calls) section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Option 2: Use local embeddings (no external API calls)

crew = Crew(
    agents=[agent],
    tasks=[...],
    knowledge_sources=[knowledge_source],
    embedder={
        "provider": "ollama",
        "config": {
            "model": "mxbai-embed-large",
            "url": "http://localhost:11434/api/embeddings"
        }
    }
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Option 1: Use Voyage AI (recommended by Anthropic for Claude users)](./169-option-1-use-voyage-ai-recommended-by-anthropic-fo.md)

**Next:** [Option 3: Agent-level embedding customization →](./171-option-3-agent-level-embedding-customization.md)
