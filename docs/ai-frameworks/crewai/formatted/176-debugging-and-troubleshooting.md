---
title: "Crewai: Debugging and Troubleshooting"
description: "Debugging and Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Debugging and Troubleshooting


### Debugging Knowledge Issues

#### Check Agent Knowledge Initialization

```python  theme={null}
from crewai import Agent, Crew, Task
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

knowledge_source = StringKnowledgeSource(content="Test knowledge")

agent = Agent(
    role="Test Agent",
    goal="Test knowledge",
    backstory="Testing",
    knowledge_sources=[knowledge_source]
)

crew = Crew(agents=[agent], tasks=[Task(...)])

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an instance of your listener](./175-create-an-instance-of-your-listener.md)

**Next:** [Before kickoff - knowledge not initialized →](./177-before-kickoff-knowledge-not-initialized.md)
