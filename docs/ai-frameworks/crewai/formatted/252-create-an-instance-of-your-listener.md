---
title: "Crewai: Create an instance of your listener"
description: "Create an instance of your listener section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an instance of your listener

memory_monitor = MemoryPerformanceMonitor()
```

#### 2. Memory Content Logging

Log memory operations for debugging and insights:

```python  theme={null}
from crewai.events import (
    BaseEventListener,
    MemorySaveStartedEvent,
    MemoryQueryStartedEvent,
    MemoryRetrievalCompletedEvent
)
import logging

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Memory Events](./251-memory-events.md)

**Next:** [Configure logging →](./253-configure-logging.md)
