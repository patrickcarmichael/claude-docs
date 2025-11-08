---
title: "Crewai: Example task to read a configuration file"
description: "Example task to read a configuration file section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example task to read a configuration file

read_task = Task(
    description="Read the configuration file from {my_bucket} and summarize its contents.",
    expected_output="A summary of the configuration file contents.",
    agent=file_reader_agent,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./751-define-an-agent-that-uses-the-tool.md)

**Next:** [Create and run the crew →](./753-create-and-run-the-crew.md)
