---
title: "Crewai: Create a task for the agent to write a specific file"
description: "Create a task for the agent to write a specific file section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a task for the agent to write a specific file

write_config_task = Task(
    description="""
    Create a configuration file with the following database settings:
    - host: db.example.com
    - port: 5432
    - username: app_user
    - password: secure_password
    
    Save this configuration as JSON to {my_bucket}.
    """,
    expected_output="Confirmation that the configuration file was successfully saved to S3.",
    agent=file_writer_agent,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example of using the tool with an agent](./776-example-of-using-the-tool-with-an-agent.md)

**Next:** [Run the task →](./778-run-the-task.md)
