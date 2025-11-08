---
title: "Crewai: Now all knowledge will be stored in your project directory"
description: "Now all knowledge will be stored in your project directory section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Now all knowledge will be stored in your project directory

```

### Default Embedding Provider Behavior

<Info>
  **Default Embedding Provider**: CrewAI defaults to OpenAI embeddings (`text-embedding-3-small`) for knowledge storage, even when using different LLM providers. You can easily customize this to match your setup.
</Info>

#### Understanding Default Behavior

```python  theme={null}
from crewai import Agent, Crew, LLM
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Store knowledge in project directory](./165-store-knowledge-in-project-directory.md)

**Next:** [When using Claude as your LLM... →](./167-when-using-claude-as-your-llm.md)
