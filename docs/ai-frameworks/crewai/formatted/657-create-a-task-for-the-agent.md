---
title: "Crewai: Create a task for the agent"
description: "Create a task for the agent section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a task for the agent

analysis_task = Task(
    description="""
    Write Python code to:
    1. Generate a random dataset of 100 points with x and y coordinates
    2. Calculate the correlation coefficient between x and y
    3. Create a scatter plot of the data
    4. Print the correlation coefficient and save the plot as 'scatter.png'

    Make sure to handle any necessary imports and print the results.
    """,
    expected_output="The correlation coefficient and confirmation that the scatter plot has been saved.",
    agent=data_analyst,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./656-define-an-agent-that-uses-the-tool.md)

**Next:** [Run the task →](./658-run-the-task.md)
