---
title: "Crewai: Run the crew"
description: "Run the crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the crew

result = crew.kickoff()
```

### Example: Using `kickoff()` with Repository Agents

You can also use repository agents directly with the `kickoff()` method for simpler interactions:

```python  theme={null}
from crewai import Agent
from pydantic import BaseModel
from typing import List

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create the crew](./1424-create-the-crew.md)

**Next:** [Define a structured output format →](./1426-define-a-structured-output-format.md)
