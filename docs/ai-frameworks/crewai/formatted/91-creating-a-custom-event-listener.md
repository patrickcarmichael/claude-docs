---
title: "Crewai: Creating a Custom Event Listener"
description: "Creating a Custom Event Listener section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Creating a Custom Event Listener


To create a custom event listener, you need to:

1. Create a class that inherits from `BaseEventListener`
2. Implement the `setup_listeners` method
3. Register handlers for the events you're interested in
4. Create an instance of your listener in the appropriate file

Here's a simple example of a custom event listener class:

```python  theme={null}
from crewai.events import (
    CrewKickoffStartedEvent,
    CrewKickoffCompletedEvent,
    AgentExecutionCompletedEvent,
)
from crewai.events import BaseEventListener

class MyCustomListener(BaseEventListener):
    def __init__(self):
        super().__init__()

    def setup_listeners(self, crewai_event_bus):
        @crewai_event_bus.on(CrewKickoffStartedEvent)
        def on_crew_started(source, event):
            print(f"Crew '{event.crew_name}' has started execution!")

        @crewai_event_bus.on(CrewKickoffCompletedEvent)
        def on_crew_completed(source, event):
            print(f"Crew '{event.crew_name}' has completed execution!")
            print(f"Output: {event.output}")

        @crewai_event_bus.on(AgentExecutionCompletedEvent)
        def on_agent_execution_completed(source, event):
            print(f"Agent '{event.agent.role}' completed task")
            print(f"Output: {event.output}")
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← How It Works](./90-how-it-works.md)

**Next:** [Properly Registering Your Listener →](./92-properly-registering-your-listener.md)
