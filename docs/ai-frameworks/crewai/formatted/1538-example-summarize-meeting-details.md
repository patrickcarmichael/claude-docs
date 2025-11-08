---
title: "Crewai: Example: Summarize meeting details"
description: "Example: Summarize meeting details section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example: Summarize meeting details


The snippet below mirrors the `calendar-event-crew.py` example in the trigger repository. It parses the payload, analyses the attendees and timing, and produces a meeting brief for downstream tools.

```python  theme={null}
from calendar_event_crew import GoogleCalendarEventTrigger

crew = GoogleCalendarEventTrigger().crew()
result = crew.kickoff({
    "crewai_trigger_payload": calendar_payload,
})
print(result.raw)
```

Use `crewai_trigger_payload` exactly as it is delivered by the trigger so the crew can extract the proper fields.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Enabling the Google Calendar Trigger](./1537-enabling-the-google-calendar-trigger.md)

**Next:** [Testing Locally →](./1539-testing-locally.md)
