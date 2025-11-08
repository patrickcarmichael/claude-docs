---
title: "Crewai: Configuration Options"
description: "Configuration Options section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Configuration Options


Customize the StagehandTool behavior with these parameters:

```python  theme={null}
stagehand_tool = StagehandTool(
    api_key="your-browserbase-api-key",
    project_id="your-browserbase-project-id",
    model_api_key="your-llm-api-key",
    model_name=AvailableModel.CLAUDE_3_7_SONNET_LATEST,
    dom_settle_timeout_ms=5000,  # Wait longer for DOM to settle
    headless=True,  # Run browser in headless mode
    self_heal=True,  # Attempt to recover from errors
    wait_for_captcha_solves=True,  # Wait for CAPTCHA solving
    verbose=1,  # Control logging verbosity (0-3)
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Identify form fields](./1407-identify-form-fields.md)

**Next:** [Best Practices →](./1409-best-practices.md)
