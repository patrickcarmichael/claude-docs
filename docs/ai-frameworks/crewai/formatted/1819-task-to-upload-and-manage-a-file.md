---
title: "Crewai: Task to upload and manage a file"
description: "Task to upload and manage a file section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to upload and manage a file

file_management_task = Task(
    description="Upload a text file named 'report.txt' with content 'This is a sample report for the project.' Then get information about the uploaded file.",
    agent=file_operator,
    expected_output="File uploaded successfully and file information retrieved."
)

crew = Crew(
    agents=[file_operator],
    tasks=[file_management_task]
)

crew.kickoff()
```

### File Organization and Sharing

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent focused on file operations](./1818-create-an-agent-focused-on-file-operations.md)

**Next:** [Create an agent for file organization and sharing →](./1820-create-an-agent-for-file-organization-and-sharing.md)
