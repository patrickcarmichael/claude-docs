---
title: "Crewai: Custom Input Schema"
description: "Custom Input Schema section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Custom Input Schema


When defining `crew_inputs`, use Pydantic Field objects to specify the input parameters:

```python  theme={null}
from pydantic import Field

crew_inputs = {
    "required_param": Field(..., description="This parameter is required"),
    "optional_param": Field(default="default_value", description="This parameter is optional"),
    "typed_param": Field(..., description="Integer parameter", ge=1, le=100)  # With validation
}
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Use Cases](./2385-use-cases.md)

**Next:** [Error Handling →](./2387-error-handling.md)
