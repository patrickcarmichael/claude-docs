---
title: "Crewai: Basic OpenAI configuration (uses environment OPENAI_API_KEY)"
description: "Basic OpenAI configuration (uses environment OPENAI_API_KEY) section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Basic OpenAI configuration (uses environment OPENAI_API_KEY)

crew = Crew(
    agents=[...],
    tasks=[...],
    memory=True,
    embedder={
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-small"  # or "text-embedding-3-large"
        }
    }
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Custom Embedder Configuration](./229-custom-embedder-configuration.md)

**Next:** [Advanced OpenAI configuration →](./231-advanced-openai-configuration.md)
