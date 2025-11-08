---
title: "Crewai: Agent vs Crew Knowledge: Complete Guide"
description: "Agent vs Crew Knowledge: Complete Guide section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Agent vs Crew Knowledge: Complete Guide


<Info>
  **Understanding Knowledge Levels**: CrewAI supports knowledge at both agent and crew levels. This section clarifies exactly how each works, when they're initialized, and addresses common misconceptions about dependencies.
</Info>

### How Knowledge Initialization Actually Works

Here's exactly what happens when you use knowledge:

#### Agent-Level Knowledge (Independent)

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Supported Knowledge Sources](./138-supported-knowledge-sources.md)

**Next:** [Agent with its own knowledge - NO crew knowledge needed →](./140-agent-with-its-own-knowledge-no-crew-knowledge-nee.md)
