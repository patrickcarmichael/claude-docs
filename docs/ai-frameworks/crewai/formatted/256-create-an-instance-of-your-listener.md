---
title: "Crewai: Create an instance of your listener"
description: "Create an instance of your listener section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an instance of your listener

error_tracker = MemoryErrorTracker(notify_email="admin@example.com")
```

### Integrating with Analytics Platforms

Memory events can be forwarded to analytics and monitoring platforms to track performance metrics, detect anomalies, and visualize memory usage patterns:

```python  theme={null}
from crewai.events import (
    BaseEventListener,
    MemoryQueryCompletedEvent,
    MemorySaveCompletedEvent
)

class MemoryAnalyticsForwarder(BaseEventListener):
    def __init__(self, analytics_client):
        super().__init__()
        self.client = analytics_client

    def setup_listeners(self, crewai_event_bus):
        @crewai_event_bus.on(MemoryQueryCompletedEvent)
        def on_memory_query_completed(source, event: MemoryQueryCompletedEvent):
            # Forward query metrics to analytics platform
            self.client.track_metric({
                "event_type": "memory_query",
                "query": event.query,
                "duration_ms": event.query_time_ms,
                "result_count": len(event.results) if hasattr(event.results, "__len__") else 0,
                "timestamp": event.timestamp
            })

        @crewai_event_bus.on(MemorySaveCompletedEvent)
        def on_memory_save_completed(source, event: MemorySaveCompletedEvent):
            # Forward save metrics to analytics platform
            self.client.track_metric({
                "event_type": "memory_save",
                "agent_role": event.agent_role,
                "duration_ms": event.save_time_ms,
                "timestamp": event.timestamp
            })
```

### Best Practices for Memory Event Listeners

1. **Keep handlers lightweight**: Avoid complex processing in event handlers to prevent performance impacts
2. **Use appropriate logging levels**: Use INFO for normal operations, DEBUG for details, ERROR for issues
3. **Batch metrics when possible**: Accumulate metrics before sending to external systems
4. **Handle exceptions gracefully**: Ensure your event handlers don't crash due to unexpected data
5. **Consider memory consumption**: Be mindful of storing large amounts of event data

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Configure logging](./255-configure-logging.md)

**Next:** [Conclusion →](./257-conclusion.md)
