---
title: "Crewai: During kickoff"
description: "During kickoff section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# During kickoff

for agent in self.agents:
    agent.crew = self  # Agent gets reference to crew
    agent.set_knowledge(crew_embedder=self.embedder)  # Agent knowledge initialized
    agent.create_agent_executor()
```

#### Storage Independence

Each knowledge level uses independent storage collections:

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← No crew-level knowledge required](./141-no-crew-level-knowledge-required.md)

**Next:** [Agent knowledge storage →](./143-agent-knowledge-storage.md)
