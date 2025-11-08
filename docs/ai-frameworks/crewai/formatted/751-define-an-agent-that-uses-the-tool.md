---
title: "Crewai: Define an agent that uses the tool"
description: "Define an agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define an agent that uses the tool

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

**Previous:** [← Initialize the tool](./750-initialize-the-tool.md)

**Next:** [Example task to read a configuration file →](./752-example-task-to-read-a-configuration-file.md)
