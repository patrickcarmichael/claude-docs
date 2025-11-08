---
title: "Crewai: Example: Summarize a new email"
description: "Example: Summarize a new email section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example: Summarize a new email


```python  theme={null}
from outlook_message_crew import OutlookMessageTrigger

crew = OutlookMessageTrigger().crew()
crew.kickoff({
    "crewai_trigger_payload": outlook_payload,
})
```

The crew extracts sender details, subject, body preview, and attachments before generating a structured response.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Enabling the Outlook Trigger](./1579-enabling-the-outlook-trigger.md)

**Next:** [Testing Locally →](./1581-testing-locally.md)
