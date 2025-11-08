---
title: "Crewai: Create a task for the agent to read a specific file"
description: "Create a task for the agent to read a specific file section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a task for the agent to read a specific file

read_config_task = Task(
    description="Read the application configuration file from {my_bucket} and extract the database connection settings.",
    expected_output="The database connection settings from the configuration file.",
    agent=file_reader_agent,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example of using the tool with an agent](./757-example-of-using-the-tool-with-an-agent.md)

**Next:** [Run the task →](./759-run-the-task.md)
