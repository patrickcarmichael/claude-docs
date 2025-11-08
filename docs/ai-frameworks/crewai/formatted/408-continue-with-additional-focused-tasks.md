---
title: "Crewai: Continue with additional focused tasks..."
description: "Continue with additional focused tasks... section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Continue with additional focused tasks...

```

### 3. Misaligned Description and Expected Output

**Problem:** The task description asks for one thing while the expected output specifies something different.

**Example of Poor Design:**

```yaml  theme={null}
analysis_task:
  description: "Analyze customer feedback to find areas of improvement."
  expected_output: "A marketing plan for the next quarter."
```

**Improved Version:**

```yaml  theme={null}
analysis_task:
  description: "Analyze customer feedback to identify the top 3 areas for product improvement."
  expected_output: "A report listing the 3 priority improvement areas with supporting customer quotes and data points."
```

### 4. Not Understanding the Process Yourself

**Problem:** Asking agents to execute tasks that you yourself don't fully understand.

**Solution:**

1. Try to perform the task manually first
2. Document your process, decision points, and information sources
3. Use this documentation as the basis for your task description

### 5. Premature Use of Hierarchical Structures

**Problem:** Creating unnecessarily complex agent hierarchies where sequential processes would work better.

**Solution:** Start with sequential processes and only move to hierarchical models when the workflow complexity truly requires it.

### 6. Vague or Generic Agent Definitions

**Problem:** Generic agent definitions lead to generic outputs.

**Example of Poor Design:**

```yaml  theme={null}
agent:
  role: "Business Analyst"
  goal: "Analyze business data"
  backstory: "You are good at business analysis."
```

**Improved Version:**

```yaml  theme={null}
agent:
  role: "SaaS Metrics Specialist focusing on growth-stage startups"
  goal: "Identify actionable insights from business data that can directly impact customer retention and revenue growth"
  backstory: "With 10+ years analyzing SaaS business models, you've developed a keen eye for the metrics that truly matter for sustainable growth. You've helped numerous companies identify the leverage points that turned around their business trajectory. You believe in connecting data to specific, actionable recommendations rather than general observations."
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task 2: Competitive Analysis](./407-task-2-competitive-analysis.md)

**Next:** [Advanced Agent Design Strategies →](./409-advanced-agent-design-strategies.md)
