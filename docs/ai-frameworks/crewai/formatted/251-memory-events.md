---
title: "Crewai: Memory Events"
description: "Memory Events section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Memory Events


CrewAI's event system provides powerful insights into memory operations. By leveraging memory events, you can monitor, debug, and optimize your memory system's performance and behavior.

### Available Memory Events

CrewAI emits the following memory-related events:

| Event                             | Description                                                 | Key Properties                                                  |
| :-------------------------------- | :---------------------------------------------------------- | :-------------------------------------------------------------- |
| **MemoryQueryStartedEvent**       | Emitted when a memory query begins                          | `query`, `limit`, `score_threshold`                             |
| **MemoryQueryCompletedEvent**     | Emitted when a memory query completes successfully          | `query`, `results`, `limit`, `score_threshold`, `query_time_ms` |
| **MemoryQueryFailedEvent**        | Emitted when a memory query fails                           | `query`, `limit`, `score_threshold`, `error`                    |
| **MemorySaveStartedEvent**        | Emitted when a memory save operation begins                 | `value`, `metadata`, `agent_role`                               |
| **MemorySaveCompletedEvent**      | Emitted when a memory save operation completes successfully | `value`, `metadata`, `agent_role`, `save_time_ms`               |
| **MemorySaveFailedEvent**         | Emitted when a memory save operation fails                  | `value`, `metadata`, `agent_role`, `error`                      |
| **MemoryRetrievalStartedEvent**   | Emitted when memory retrieval for a task prompt starts      | `task_id`                                                       |
| **MemoryRetrievalCompletedEvent** | Emitted when memory retrieval completes successfully        | `task_id`, `memory_content`, `retrieval_time_ms`                |

### Practical Applications

#### 1. Memory Performance Monitoring

Track memory operation timing to optimize your application:

```python  theme={null}
from crewai.events import (
    BaseEventListener,
    MemoryQueryCompletedEvent,
    MemorySaveCompletedEvent
)
import time

class MemoryPerformanceMonitor(BaseEventListener):
    def __init__(self):
        super().__init__()
        self.query_times = []
        self.save_times = []

    def setup_listeners(self, crewai_event_bus):
        @crewai_event_bus.on(MemoryQueryCompletedEvent)
        def on_memory_query_completed(source, event: MemoryQueryCompletedEvent):
            self.query_times.append(event.query_time_ms)
            print(f"Memory query completed in {event.query_time_ms:.2f}ms. Query: '{event.query}'")
            print(f"Average query time: {sum(self.query_times)/len(self.query_times):.2f}ms")

        @crewai_event_bus.on(MemorySaveCompletedEvent)
        def on_memory_save_completed(source, event: MemorySaveCompletedEvent):
            self.save_times.append(event.save_time_ms)
            print(f"Memory save completed in {event.save_time_ms:.2f}ms")
            print(f"Average save time: {sum(self.save_times)/len(self.save_times):.2f}ms")

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Benefits of Using CrewAI's Memory System](./250-benefits-of-using-crewais-memory-system.md)

**Next:** [Create an instance of your listener →](./252-create-an-instance-of-your-listener.md)
