---
title: "Crewai: Configure logging"
description: "Configure logging section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Configure logging

logger = logging.getLogger('memory_events')

class MemoryLogger(BaseEventListener):
    def setup_listeners(self, crewai_event_bus):
        @crewai_event_bus.on(MemorySaveStartedEvent)
        def on_memory_save_started(source, event: MemorySaveStartedEvent):
            if event.agent_role:
                logger.info(f"Agent '{event.agent_role}' saving memory: {event.value[:50]}...")
            else:
                logger.info(f"Saving memory: {event.value[:50]}...")

        @crewai_event_bus.on(MemoryQueryStartedEvent)
        def on_memory_query_started(source, event: MemoryQueryStartedEvent):
            logger.info(f"Memory query started: '{event.query}' (limit: {event.limit})")

        @crewai_event_bus.on(MemoryRetrievalCompletedEvent)
        def on_memory_retrieval_completed(source, event: MemoryRetrievalCompletedEvent):
            if event.task_id:
                logger.info(f"Memory retrieved for task {event.task_id} in {event.retrieval_time_ms:.2f}ms")
            else:
                logger.info(f"Memory retrieved in {event.retrieval_time_ms:.2f}ms")
            logger.debug(f"Memory content: {event.memory_content}")

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an instance of your listener](./252-create-an-instance-of-your-listener.md)

**Next:** [Create an instance of your listener →](./254-create-an-instance-of-your-listener.md)
