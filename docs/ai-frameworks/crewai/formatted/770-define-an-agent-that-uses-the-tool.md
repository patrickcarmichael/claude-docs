---
title: "Crewai: Define an agent that uses the tool"
description: "Define an agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define an agent that uses the tool

file_writer_agent = Agent(
    role="File Writer",
    goal="Write content to files in S3 buckets",
    backstory="An expert in storing and managing files in cloud storage.",
    tools=[s3_writer_tool],
    verbose=True,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool](./769-initialize-the-tool.md)

**Next:** [Example task to write a report →](./771-example-task-to-write-a-report.md)
