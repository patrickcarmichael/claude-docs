---
title: "Crewai: Fill out a form"
description: "Fill out a form section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Fill out a form

result = stagehand_tool.run(
    instruction="Fill the contact form with name 'John Doe', email 'john@example.com', and message 'Hello world'", 
    url="https://example.com/contact"
)
```

### 2. Extract Command

The `extract` command type retrieves structured data from webpages.

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Perform an action (default behavior)](./1402-perform-an-action-default-behavior.md)

**Next:** [Extract all product information →](./1404-extract-all-product-information.md)
