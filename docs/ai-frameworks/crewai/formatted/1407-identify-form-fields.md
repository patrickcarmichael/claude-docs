---
title: "Crewai: Identify form fields"
description: "Identify form fields section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Identify form fields

result = stagehand_tool.run(
    instruction="Identify all the input fields in the registration form", 
    url="https://example.com/register",
    command_type="observe",
    selector="#registration-form"
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Find interactive elements](./1406-find-interactive-elements.md)

**Next:** [Configuration Options →](./1408-configuration-options.md)
