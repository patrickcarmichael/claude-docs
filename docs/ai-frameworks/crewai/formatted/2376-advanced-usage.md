---
title: "Crewai: Advanced Usage"
description: "Advanced Usage section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Advanced Usage


### Custom Input Schema with Dynamic Parameters

```python {2, 4-15} theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import InvokeCrewAIAutomationTool
from pydantic import Field

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Environment Variables](./2375-environment-variables.md)

**Next:** [Define custom input schema →](./2377-define-custom-input-schema.md)
