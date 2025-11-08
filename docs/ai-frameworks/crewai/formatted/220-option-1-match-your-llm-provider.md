---
title: "Crewai: Option 1: Match your LLM provider"
description: "Option 1: Match your LLM provider section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Option 1: Match your LLM provider

crew = Crew(
    agents=[agent],
    tasks=[task],
    memory=True,
    embedder={
        "provider": "anthropic", # Match your LLM provider
        "config": {
            "api_key": "your-anthropic-key",
            "model": "text-embedding-3-small"
        }
    }
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← CrewAI will use OpenAI embeddings by default for consistency](./219-crewai-will-use-openai-embeddings-by-default-for-c.md)

**Next:** [Option 2: Use local embeddings (no external API calls) →](./221-option-2-use-local-embeddings-no-external-api-call.md)
