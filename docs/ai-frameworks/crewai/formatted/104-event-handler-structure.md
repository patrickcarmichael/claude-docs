---
title: "Crewai: Event Handler Structure"
description: "Event Handler Structure section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Event Handler Structure


Each event handler receives two parameters:

1. **source**: The object that emitted the event
2. **event**: The event instance, containing event-specific data

The structure of the event object depends on the event type, but all events inherit from `BaseEvent` and include:

* **timestamp**: The time when the event was emitted
* **type**: A string identifier for the event type

Additional fields vary by event type. For example, `CrewKickoffCompletedEvent` includes `crew_name` and `output` fields.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Available Event Types](./103-available-event-types.md)

**Next:** [Advanced Usage: Scoped Handlers →](./105-advanced-usage-scoped-handlers.md)
