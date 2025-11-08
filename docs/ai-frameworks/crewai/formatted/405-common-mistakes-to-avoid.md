---
title: "Crewai: Common Mistakes to Avoid"
description: "Common Mistakes to Avoid section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Common Mistakes to Avoid


Based on lessons learned from real-world implementations, here are the most common pitfalls in agent and task design:

### 1. Unclear Task Instructions

**Problem:** Tasks lack sufficient detail, making it difficult for agents to execute effectively.

**Example of Poor Design:**

```yaml  theme={null}
research_task:
  description: "Research AI trends."
  expected_output: "A report on AI trends."
```

**Improved Version:**

```yaml  theme={null}
research_task:
  description: >
    Research the top emerging AI trends for 2024 with a focus on:
    1. Enterprise adoption patterns
    2. Technical breakthroughs in the past 6 months
    3. Regulatory developments affecting implementation

    For each trend, identify key companies, technologies, and potential business impacts.
  expected_output: >
    A comprehensive markdown report with:
    - Executive summary (5 bullet points)
    - 5-7 major trends with supporting evidence
    - For each trend: definition, examples, and business implications
    - References to authoritative sources
```

### 2. "God Tasks" That Try to Do Too Much

**Problem:** Tasks that combine multiple complex operations into one instruction set.

**Example of Poor Design:**

```yaml  theme={null}
comprehensive_task:
  description: "Research market trends, analyze competitor strategies, create a marketing plan, and design a launch timeline."
```

**Improved Version:**
Break this into sequential, focused tasks:

```yaml  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task 3](./404-task-3.md)

**Next:** [Task 1: Research →](./406-task-1-research.md)
