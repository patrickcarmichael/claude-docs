---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(agents=[file_writer_agent], tasks=[write_config_task])
result = crew.kickoff(inputs={"my_bucket": "s3://my-bucket/config/db-config.json"})
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create a task for the agent to write a specific file](./777-create-a-task-for-the-agent-to-write-a-specific-fi.md)

**Next:** [Error Handling →](./779-error-handling.md)
