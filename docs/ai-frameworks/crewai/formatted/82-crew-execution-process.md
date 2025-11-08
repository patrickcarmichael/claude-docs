---
title: "Crewai: Crew Execution Process"
description: "Crew Execution Process section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Crew Execution Process


* **Sequential Process**: Tasks are executed one after another, allowing for a linear flow of work.
* **Hierarchical Process**: A manager agent coordinates the crew, delegating tasks and validating outcomes before proceeding. **Note**: A `manager_llm` or `manager_agent` is required for this process and it's essential for validating the process flow.

### Kicking Off a Crew

Once your crew is assembled, initiate the workflow with the `kickoff()` method. This starts the execution process according to the defined process flow.

```python Code theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Access the crew's usage metrics](./81-access-the-crews-usage-metrics.md)

**Next:** [Start the crew's task execution →](./83-start-the-crews-task-execution.md)
