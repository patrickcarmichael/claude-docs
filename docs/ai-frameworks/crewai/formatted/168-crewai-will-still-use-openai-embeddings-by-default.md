---
title: "Crewai: CrewAI will still use OpenAI embeddings by default for knowledge"
description: "CrewAI will still use OpenAI embeddings by default for knowledge section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# CrewAI will still use OpenAI embeddings by default for knowledge

# This ensures consistency but may not match your LLM provider preference
knowledge_source = StringKnowledgeSource(content="Research data...")

crew = Crew(
    agents=[agent],
    tasks=[...],
    knowledge_sources=[knowledge_source]
    # Default: Uses OpenAI embeddings even with Claude LLM
)
```

#### Customizing Knowledge Embedding Providers

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← When using Claude as your LLM...](./167-when-using-claude-as-your-llm.md)

**Next:** [Option 1: Use Voyage AI (recommended by Anthropic for Claude users) →](./169-option-1-use-voyage-ai-recommended-by-anthropic-fo.md)
