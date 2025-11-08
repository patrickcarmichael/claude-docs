---
title: "Crewai: Task output validation flow"
description: "Task output validation flow section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task output validation flow

task_output = agent.execute_task(task)
validation_result = guardrail(task_output)

if validation_result.valid:
    # Task completes successfully
    return task_output
else:
    # Task fails with validation feedback
    raise ValidationError(validation_result.feedback)
```

### Event Tracking

The guardrail integrates with CrewAI's event system to provide observability:

* **Validation Started**: When guardrail evaluation begins
* **Validation Completed**: When evaluation finishes with results
* **Validation Failed**: When technical errors occur during evaluation

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Integration with Task System](./1463-integration-with-task-system.md)

**Next:** [Best Practices →](./1465-best-practices.md)
