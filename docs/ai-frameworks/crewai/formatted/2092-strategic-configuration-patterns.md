---
title: "Crewai: Strategic Configuration Patterns"
description: "Strategic Configuration Patterns section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Strategic Configuration Patterns


### a. Multi-Model Approach

<Tip>
  Use different models for different purposes within the same crew to optimize both performance and cost.
</Tip>

The most sophisticated CrewAI implementations often employ multiple models strategically, assigning different models to different agents based on their specific roles and requirements. This approach allows teams to optimize for both performance and cost by using the most appropriate model for each type of work.

Planning agents benefit from reasoning models that can handle complex strategic thinking and multi-step analysis. These agents often serve as the "brain" of the operation, developing strategies and coordinating other agents' work. Content agents, on the other hand, perform best with creative models that excel at writing quality and audience engagement. Processing agents handling routine operations can use efficient models that prioritize speed and cost-effectiveness.

**Example: Research and Analysis Crew**

```python  theme={null}
from crewai import Agent, Task, Crew, LLM

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Core Selection Framework](./2091-core-selection-framework.md)

**Next:** [High-capability reasoning model for strategic planning →](./2093-high-capability-reasoning-model-for-strategic-plan.md)
