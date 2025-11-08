---
title: "Crewai: Hierarchical Process Overview"
description: "Hierarchical Process Overview section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Hierarchical Process Overview


By default, tasks in CrewAI are managed through a sequential process. However, adopting a hierarchical approach allows for a clear hierarchy in task management,
where a 'manager' agent coordinates the workflow, delegates tasks, and validates outcomes for streamlined and effective execution. This manager agent can now be either
automatically created by CrewAI or explicitly set by the user.

### Key Features

* **Task Delegation**: A manager agent allocates tasks among crew members based on their roles and capabilities.
* **Result Validation**: The manager evaluates outcomes to ensure they meet the required standards.
* **Efficient Workflow**: Emulates corporate structures, providing an organized approach to task management.
* **System Prompt Handling**: Optionally specify whether the system should use predefined prompts.
* **Stop Words Control**: Optionally specify whether stop words should be used, supporting various models including the o1 models.
* **Context Window Respect**: Prioritize important context by enabling respect of the context window, which is now the default behavior.
* **Delegation Control**: Delegation is now disabled by default to give users explicit control.
* **Max Requests Per Minute**: Configurable option to set the maximum number of requests per minute.
* **Max Iterations**: Limit the maximum number of iterations for obtaining a final answer.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Introduction](./2036-introduction.md)

**Next:** [Implementing the Hierarchical Process →](./2038-implementing-the-hierarchical-process.md)
