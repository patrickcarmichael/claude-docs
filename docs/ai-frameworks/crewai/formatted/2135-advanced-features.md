---
title: "Crewai: Advanced Features"
description: "Advanced Features section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Advanced Features


### Task Delegation

In sequential processes, if an agent has `allow_delegation` set to `True`, they can delegate tasks to other agents in the crew.
This feature is automatically set up when there are multiple agents in the crew.

### Asynchronous Execution

Tasks can be executed asynchronously, allowing for parallel processing when appropriate.
To create an asynchronous task, set `async_execution=True` when defining the task.

### Memory and Caching

CrewAI supports both memory and caching features:

* **Memory**: Enable by setting `memory=True` when creating the Crew. This allows agents to retain information across tasks.
* **Caching**: By default, caching is enabled. Set `cache=False` to disable it.

### Callbacks

You can set callbacks at both the task and step level:

* `task_callback`: Executed after each task completion.
* `step_callback`: Executed after each step in an agent's execution.

### Usage Metrics

CrewAI tracks token usage across all tasks and agents. You can access these metrics after execution.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Accessing the type-safe output](./2134-accessing-the-type-safe-output.md)

**Next:** [Best Practices for Sequential Processes →](./2136-best-practices-for-sequential-processes.md)
