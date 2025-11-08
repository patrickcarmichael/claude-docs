---
title: "Crewai: Create agent with Gmail search and analysis capabilities"
description: "Create agent with Gmail search and analysis capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agent with Gmail search and analysis capabilities

email_analyst = Agent(
    role="Email Analyst",
    goal="Analyze email patterns and provide insights",
    backstory="An AI assistant that analyzes email data to provide actionable insights.",
    apps=['gmail/fetch_emails', 'gmail/get_message']  # Specific actions for email analysis
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to prepare and send emails](./1663-task-to-prepare-and-send-emails.md)

**Next:** [Task to analyze email patterns →](./1665-task-to-analyze-email-patterns.md)
