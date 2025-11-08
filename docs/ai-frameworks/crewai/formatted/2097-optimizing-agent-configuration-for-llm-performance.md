---
title: "Crewai: Optimizing Agent Configuration for LLM Performance"
description: "Optimizing Agent Configuration for LLM Performance section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Optimizing Agent Configuration for LLM Performance


### a. Role-Driven LLM Selection

<Warning>
  Generic agent roles make it impossible to select the right LLM. Specific roles enable targeted model optimization.
</Warning>

The specificity of your agent roles directly determines which LLM capabilities matter most for optimal performance. This creates a strategic opportunity to match precise model strengths with agent responsibilities.

**Generic vs. Specific Role Impact on LLM Choice:**

When defining roles, think about the specific domain knowledge, working style, and decision-making frameworks that would be most valuable for the tasks the agent will handle. The more specific and contextual the role definition, the better the model can embody that role effectively.

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task Definition Framework](./2096-task-definition-framework.md)

**Next:** [✅ Specific role - clear LLM requirements →](./2098-specific-role-clear-llm-requirements.md)
