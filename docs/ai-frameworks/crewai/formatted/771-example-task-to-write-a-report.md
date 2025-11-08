---
title: "Crewai: Example task to write a report"
description: "Example task to write a report section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example task to write a report

write_task = Task(
    description="Generate a summary report of the quarterly sales data and save it to {my_bucket}.",
    expected_output="Confirmation that the report was successfully saved to S3.",
    agent=file_writer_agent,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./770-define-an-agent-that-uses-the-tool.md)

**Next:** [Create and run the crew →](./772-create-and-run-the-crew.md)
