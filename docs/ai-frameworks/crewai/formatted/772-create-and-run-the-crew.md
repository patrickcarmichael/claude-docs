---
title: "Crewai: Create and run the crew"
description: "Create and run the crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create and run the crew

crew = Crew(agents=[file_writer_agent], tasks=[write_task])
result = crew.kickoff(inputs={"my_bucket": "s3://my-bucket/reports/quarterly-summary.txt"})
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example task to write a report](./771-example-task-to-write-a-report.md)

**Next:** [Parameters →](./773-parameters.md)
