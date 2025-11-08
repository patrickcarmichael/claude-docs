---
title: "Crewai: ✅ Specific role - clear LLM requirements"
description: "✅ Specific role - clear LLM requirements section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# ✅ Specific role - clear LLM requirements

specific_agent = Agent(
    role="SaaS Revenue Operations Analyst",  # Clear domain expertise needed
    goal="Analyze recurring revenue metrics and identify growth opportunities",
    backstory="Specialist in SaaS business models with deep understanding of ARR, churn, and expansion revenue",
    llm=LLM(model="gpt-4o")  # Reasoning model justified for complex analysis
)
```

**Role-to-Model Mapping Strategy:**

* **"Research Analyst"** → Reasoning model (GPT-4o, Claude Sonnet) for complex analysis
* **"Content Editor"** → Creative model (Claude, GPT-4o) for writing quality
* **"Data Processor"** → Efficient model (GPT-4o-mini, Gemini Flash) for structured tasks
* **"API Coordinator"** → Function-calling optimized model (GPT-4o, Claude) for tool usage

### b. Backstory as Model Context Amplifier

<Info>
  Strategic backstories multiply your chosen LLM's effectiveness by providing domain-specific context that generic prompting cannot achieve.
</Info>

A well-crafted backstory transforms your LLM choice from generic capability to specialized expertise. This is especially crucial for cost optimization - a well-contextualized efficient model can outperform a premium model without proper context.

**Context-Driven Performance Example:**

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Optimizing Agent Configuration for LLM Performance](./2097-optimizing-agent-configuration-for-llm-performance.md)

**Next:** [Context amplifies model effectiveness →](./2099-context-amplifies-model-effectiveness.md)
