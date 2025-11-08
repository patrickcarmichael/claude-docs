---
title: "Crewai: Consider creating new state:"
description: "Consider creating new state: section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Consider creating new state:

from pydantic import BaseModel
from typing import List

class ItemState(BaseModel):
    items: List[str] = []

class ImmutableFlow(Flow[ItemState]):
    @start()
    def add_item(self):
        # Create new list with the added item
        self.state.items = [*self.state.items, "new item"]
        return "Item added"
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Instead of modifying lists in place:](./506-instead-of-modifying-lists-in-place.md)

**Next:** [Debugging Flow State →](./508-debugging-flow-state.md)
