---
title: "Crewai: Create an agent focused on email management"
description: "Create an agent focused on email management section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent focused on email management

email_manager = Agent(
    role="Email Manager",
    goal="Retrieve, search, and organize email messages",
    backstory="An AI assistant skilled in email organization and management.",
    apps=['microsoft_outlook/get_messages']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1831-run-the-task.md)

**Next:** [Task to search and retrieve emails →](./1833-task-to-search-and-retrieve-emails.md)
