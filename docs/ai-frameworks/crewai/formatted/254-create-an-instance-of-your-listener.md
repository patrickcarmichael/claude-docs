---
title: "Crewai: Create an instance of your listener"
description: "Create an instance of your listener section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an instance of your listener

memory_logger = MemoryLogger()
```

#### 3. Error Tracking and Notifications

Capture and respond to memory errors:

```python  theme={null}
from crewai.events import (
    BaseEventListener,
    MemorySaveFailedEvent,
    MemoryQueryFailedEvent
)
import logging
from typing import Optional

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Configure logging](./253-configure-logging.md)

**Next:** [Configure logging →](./255-configure-logging.md)
