---
title: "Crewai: Example of using the tool with an agent"
description: "Example of using the tool with an agent section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example of using the tool with an agent

file_reader_agent = Agent(
    role="File Reader",
    goal="Read files from S3 buckets",
    backstory="An expert in retrieving and processing files from cloud storage.",
    tools=[s3_reader_tool],
    verbose=True,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage](./756-usage.md)

**Next:** [Create a task for the agent to read a specific file →](./758-create-a-task-for-the-agent-to-read-a-specific-fil.md)
