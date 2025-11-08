---
title: "Crewai: Task to send an email"
description: "Task to send an email section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to send an email

send_email_task = Task(
    description="Send an email to 'colleague@example.com' with subject 'Project Update' and body 'Hi, here is the latest project update. Best regards.'",
    agent=outlook_agent,
    expected_output="Email sent successfully to colleague@example.com"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Microsoft Outlook capabilities](./1829-create-an-agent-with-microsoft-outlook-capabilitie.md)

**Next:** [Run the task →](./1831-run-the-task.md)
