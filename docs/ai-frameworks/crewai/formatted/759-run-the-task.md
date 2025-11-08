---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(agents=[file_reader_agent], tasks=[read_config_task])
result = crew.kickoff(inputs={"my_bucket": "s3://my-bucket/config/app-config.json"})
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create a task for the agent to read a specific file](./758-create-a-task-for-the-agent-to-read-a-specific-fil.md)

**Next:** [Error Handling →](./760-error-handling.md)
