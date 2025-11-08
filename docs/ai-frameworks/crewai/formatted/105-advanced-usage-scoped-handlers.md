---
title: "Crewai: Advanced Usage: Scoped Handlers"
description: "Advanced Usage: Scoped Handlers section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Advanced Usage: Scoped Handlers


For temporary event handling (useful for testing or specific operations), you can use the `scoped_handlers` context manager:

```python  theme={null}
from crewai.events import crewai_event_bus, CrewKickoffStartedEvent

with crewai_event_bus.scoped_handlers():
    @crewai_event_bus.on(CrewKickoffStartedEvent)
    def temp_handler(source, event):
        print("This handler only exists within this context")

    # Do something that emits events

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Event Handler Structure](./104-event-handler-structure.md)

**Next:** [Outside the context, the temporary handler is removed →](./106-outside-the-context-the-temporary-handler-is-remov.md)
