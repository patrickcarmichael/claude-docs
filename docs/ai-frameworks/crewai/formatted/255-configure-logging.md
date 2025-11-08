---
title: "Crewai: Configure logging"
description: "Configure logging section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Configure logging

logger = logging.getLogger('memory_errors')

class MemoryErrorTracker(BaseEventListener):
    def __init__(self, notify_email: Optional[str] = None):
        super().__init__()
        self.notify_email = notify_email
        self.error_count = 0

    def setup_listeners(self, crewai_event_bus):
        @crewai_event_bus.on(MemorySaveFailedEvent)
        def on_memory_save_failed(source, event: MemorySaveFailedEvent):
            self.error_count += 1
            agent_info = f"Agent '{event.agent_role}'" if event.agent_role else "Unknown agent"
            error_message = f"Memory save failed: {event.error}. {agent_info}"
            logger.error(error_message)

            if self.notify_email and self.error_count % 5 == 0:
                self._send_notification(error_message)

        @crewai_event_bus.on(MemoryQueryFailedEvent)
        def on_memory_query_failed(source, event: MemoryQueryFailedEvent):
            self.error_count += 1
            error_message = f"Memory query failed: {event.error}. Query: '{event.query}'"
            logger.error(error_message)

            if self.notify_email and self.error_count % 5 == 0:
                self._send_notification(error_message)

    def _send_notification(self, message):
        # Implement your notification system (email, Slack, etc.)
        print(f"[NOTIFICATION] Would send to {self.notify_email}: {message}")

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an instance of your listener](./254-create-an-instance-of-your-listener.md)

**Next:** [Create an instance of your listener →](./256-create-an-instance-of-your-listener.md)
