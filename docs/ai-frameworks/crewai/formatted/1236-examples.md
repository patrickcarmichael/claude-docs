---
title: "Crewai: Examples"
description: "Examples section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Examples


### SERP Search

```python Code theme={null}
from crewai_tools import BrightDataSearchTool

tool = BrightDataSearchTool(
    query="CrewAI", 
    country="us",
)

print(tool.run())
```

### Web Unlocker

```python Code theme={null}
from crewai_tools import BrightDataWebUnlockerTool

tool = BrightDataWebUnlockerTool(
    url="https://example.com", 
    format="markdown",
)

print(tool.run(url="https://example.com"))
```

### Dataset API

```python Code theme={null}
from crewai_tools import BrightDataDatasetTool

tool = BrightDataDatasetTool(
    dataset_type="ecommerce", 
    url="https://example.com/product",
)

print(tool.run())
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Included Tools](./1235-included-tools.md)

**Next:** [Troubleshooting →](./1237-troubleshooting.md)
