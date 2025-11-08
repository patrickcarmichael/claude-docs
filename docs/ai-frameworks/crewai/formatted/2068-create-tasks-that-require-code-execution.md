---
title: "Crewai: Create tasks that require code execution"
description: "Create tasks that require code execution section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create tasks that require code execution

task_1 = Task(
    description="Analyze the first dataset and calculate the average age of participants. Ages: {ages}",
    agent=coding_agent,
    expected_output="The average age of the participants."
)

task_2 = Task(
    description="Analyze the second dataset and calculate the average age of participants. Ages: {ages}",
    agent=coding_agent,
    expected_output="The average age of the participants."
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with code execution enabled](./2067-create-an-agent-with-code-execution-enabled.md)

**Next:** [Create two crews and add tasks →](./2069-create-two-crews-and-add-tasks.md)
