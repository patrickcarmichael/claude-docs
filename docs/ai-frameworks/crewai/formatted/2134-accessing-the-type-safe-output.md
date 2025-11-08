---
title: "Crewai: Accessing the type-safe output"
description: "Accessing the type-safe output section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Accessing the type-safe output

task_output: TaskOutput = result.tasks[0].output
crew_output: CrewOutput = result.output
```

### Note:

Each task in a sequential process **must** have an agent assigned. Ensure that every `Task` includes an `agent` parameter.

### Workflow in Action

1. **Initial Task**: In a sequential process, the first agent completes their task and signals completion.
2. **Subsequent Tasks**: Agents pick up their tasks based on the process type, with outcomes of preceding tasks or directives guiding their execution.
3. **Completion**: The process concludes once the final task is executed, leading to project completion.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Execute the crew](./2133-execute-the-crew.md)

**Next:** [Advanced Features →](./2135-advanced-features.md)
