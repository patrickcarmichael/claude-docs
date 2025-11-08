---
title: "Crewai: Create a task that requires code execution"
description: "Create a task that requires code execution section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a task that requires code execution

data_analysis_task = Task(
    description="Analyze the given dataset and calculate the average age of participants. Ages: {ages}",
    agent=coding_agent,
    expected_output="The average age calculated from the dataset"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with code execution enabled](./2075-create-an-agent-with-code-execution-enabled.md)

**Next:** [Create a crew and add the task →](./2077-create-a-crew-and-add-the-task.md)
