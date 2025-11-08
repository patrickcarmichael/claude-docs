---
title: "Crewai: Option 1: Use Voyage AI (recommended by Anthropic for Claude users)"
description: "Option 1: Use Voyage AI (recommended by Anthropic for Claude users) section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Option 1: Use Voyage AI (recommended by Anthropic for Claude users)

crew = Crew(
    agents=[agent],
    tasks=[...],
    knowledge_sources=[knowledge_source],
    embedder={
        "provider": "voyageai",  # Recommended for Claude users
        "config": {
            "api_key": "your-voyage-api-key",
            "model": "voyage-3"  # or "voyage-3-large" for best quality
        }
    }
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← CrewAI will still use OpenAI embeddings by default for knowledge](./168-crewai-will-still-use-openai-embeddings-by-default.md)

**Next:** [Option 2: Use local embeddings (no external API calls) →](./170-option-2-use-local-embeddings-no-external-api-call.md)
