---
title: "Crewai: Example of using the tool with an agent"
description: "Example of using the tool with an agent section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example of using the tool with an agent

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

**Previous:** [← Usage](./775-usage.md)

**Next:** [Create a task for the agent to write a specific file →](./777-create-a-task-for-the-agent-to-write-a-specific-fi.md)
