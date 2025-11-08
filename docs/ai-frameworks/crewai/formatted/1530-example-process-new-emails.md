---
title: "Crewai: Example: Process new emails"
description: "Example: Process new emails section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example: Process new emails


When a new email arrives, the Gmail Trigger will send the payload to your Crew or Flow. Below is a Crew example that parses and processes the trigger payload.

```python  theme={null}
@CrewBase
class GmailProcessingCrew:
    @agent
    def parser(self) -> Agent:
        return Agent(
            config=self.agents_config['parser'],
        )

    @task
    def parse_gmail_payload(self) -> Task:
        return Task(
            config=self.tasks_config['parse_gmail_payload'],
            agent=self.parser(),
        )

    @task
    def act_on_email(self) -> Task:
        return Task(
            config=self.tasks_config['act_on_email'],
            agent=self.parser(),
        )
```

The Gmail payload will be available via the standard context mechanisms.

### Testing Locally

Test your Gmail trigger integration locally using the CrewAI CLI:

```bash  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Enabling the Gmail Trigger](./1529-enabling-the-gmail-trigger.md)

**Next:** [View all available triggers →](./1531-view-all-available-triggers.md)
