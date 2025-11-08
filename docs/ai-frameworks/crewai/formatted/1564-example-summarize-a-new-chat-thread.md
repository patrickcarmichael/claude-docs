---
title: "Crewai: Example: Summarize a new chat thread"
description: "Example: Summarize a new chat thread section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example: Summarize a new chat thread


```python  theme={null}
from teams_chat_created_crew import MicrosoftTeamsChatTrigger

crew = MicrosoftTeamsChatTrigger().crew()
result = crew.kickoff({
    "crewai_trigger_payload": teams_payload,
})
print(result.raw)
```

The crew parses thread metadata (subject, created time, roster) and generates an action plan for the receiving team.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Enabling the Microsoft Teams Trigger](./1563-enabling-the-microsoft-teams-trigger.md)

**Next:** [Testing Locally →](./1565-testing-locally.md)
