---
title: "Crewai: Crafting Effective Tasks for Your Agents"
description: "Crafting Effective Tasks for Your Agents section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Crafting Effective Tasks for Your Agents


While agent design is important, task design is critical for successful execution. Here are best practices for designing tasks that set your agents up for success:

### The Anatomy of an Effective Task

A well-designed task has two key components that serve different purposes:

#### Task Description: The Process

The description should focus on what to do and how to do it, including:

* Detailed instructions for execution
* Context and background information
* Scope and constraints
* Process steps to follow

#### Expected Output: The Deliverable

The expected output should define what the final result should look like:

* Format specifications (markdown, JSON, etc.)
* Structure requirements
* Quality criteria
* Examples of good outputs (when possible)

### Task Design Best Practices

#### 1. Single Purpose, Single Output

Tasks perform best when focused on one clear objective:

**Bad Example (Too Broad):**

```yaml  theme={null}
task_description: "Research market trends, analyze the data, and create a visualization."
```

**Good Example (Focused):**

```yaml  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Practical Examples: Before and After](./400-practical-examples-before-and-after.md)

**Next:** [Task 1 →](./402-task-1.md)
