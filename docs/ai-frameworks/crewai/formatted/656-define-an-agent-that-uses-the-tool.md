---
title: "Crewai: Define an agent that uses the tool"
description: "Define an agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define an agent that uses the tool

data_analyst = Agent(
    role="Data Analyst",
    goal="Analyze data using Python code",
    backstory="""You are an expert data analyst who specializes in using Python
    to analyze and visualize data. You can write efficient code to process
    large datasets and extract meaningful insights.""",
    tools=[code_interpreter],
    verbose=True,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool](./655-initialize-the-tool.md)

**Next:** [Create a task for the agent →](./657-create-a-task-for-the-agent.md)
