---
title: "Crewai: Create and run the crew"
description: "Create and run the crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create and run the crew

crew = Crew(agents=[file_reader_agent], tasks=[read_task])
result = crew.kickoff(inputs={"my_bucket": "s3://my-bucket/config/app-config.json"})
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example task to read a configuration file](./752-example-task-to-read-a-configuration-file.md)

**Next:** [Parameters →](./754-parameters.md)
