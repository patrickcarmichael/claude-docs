---
title: "Crewai: Knowledge Configuration"
description: "Knowledge Configuration section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Knowledge Configuration


You can configure the knowledge configuration for the crew or agent.

```python Code theme={null}
from crewai.knowledge.knowledge_config import KnowledgeConfig

knowledge_config = KnowledgeConfig(results_limit=10, score_threshold=0.5)

agent = Agent(
    ...
    knowledge_config=knowledge_config
)
```

<Tip>
  `results_limit`: is the number of relevant documents to return. Default is 3.
  `score_threshold`: is the minimum score for a document to be considered relevant. Default is 0.35.
</Tip>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Each agent gets only their specific knowledge](./155-each-agent-gets-only-their-specific-knowledge.md)

**Next:** [Supported Knowledge Parameters →](./157-supported-knowledge-parameters.md)
