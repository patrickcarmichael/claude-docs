---
title: "Crewai: Create agent with Slack search and user management capabilities"
description: "Create agent with Slack search and user management capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agent with Slack search and user management capabilities

analytics_agent = Agent(
    role="Communication Analyst",
    goal="Analyze team communication patterns and extract insights from conversations",
    backstory="An analytical AI that excels at understanding team dynamics through communication data.",
    apps=[
        'slack/search_messages',
        'slack/get_user_by_email',
        'slack/list_members'
    ]  # Using canonical action names from canonical_integrations.yml
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to send rich notifications](./1931-task-to-send-rich-notifications.md)

**Next:** [Complex task involving search and analysis →](./1933-complex-task-involving-search-and-analysis.md)
