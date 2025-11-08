---
title: "Crewai: Task to send a follow-up email"
description: "Task to send a follow-up email section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to send a follow-up email

send_email_task = Task(
    description="Send a follow-up email to john@example.com about the project update meeting",
    agent=gmail_agent,
    expected_output="Email sent successfully with confirmation"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Gmail capabilities](./1659-create-an-agent-with-gmail-capabilities.md)

**Next:** [Run the task →](./1661-run-the-task.md)
