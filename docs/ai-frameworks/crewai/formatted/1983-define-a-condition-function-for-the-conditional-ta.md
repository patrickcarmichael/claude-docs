---
title: "Crewai: Define a condition function for the conditional task"
description: "Define a condition function for the conditional task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define a condition function for the conditional task

# If false, the task will be skipped, if true, then execute the task.
def is_data_missing(output: TaskOutput) -> bool:
    return len(output.pydantic.events) < 10  # this will skip this task

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example Usage](./1982-example-usage.md)

**Next:** [Define the agents →](./1984-define-the-agents.md)
