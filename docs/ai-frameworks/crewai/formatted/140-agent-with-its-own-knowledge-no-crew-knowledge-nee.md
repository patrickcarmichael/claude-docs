---
title: "Crewai: Agent with its own knowledge - NO crew knowledge needed"
description: "Agent with its own knowledge - NO crew knowledge needed section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Agent with its own knowledge - NO crew knowledge needed

specialist_knowledge = StringKnowledgeSource(
    content="Specialized technical information for this agent only"
)

specialist_agent = Agent(
    role="Technical Specialist",
    goal="Provide technical expertise",
    backstory="Expert in specialized technical domains",
    knowledge_sources=[specialist_knowledge]  # Agent-specific knowledge
)

task = Task(
    description="Answer technical questions",
    agent=specialist_agent,
    expected_output="Technical answer"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Agent vs Crew Knowledge: Complete Guide](./139-agent-vs-crew-knowledge-complete-guide.md)

**Next:** [No crew-level knowledge required →](./141-no-crew-level-knowledge-required.md)
