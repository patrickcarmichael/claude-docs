---
title: "Crewai: Extract specific information with a selector"
description: "Extract specific information with a selector section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Extract specific information with a selector

result = stagehand_tool.run(
    instruction="Extract the main article title and content", 
    url="https://example.com/blog/article",
    command_type="extract",
    selector=".article-container"  # Optional CSS selector
)
```

### 3. Observe Command

The `observe` command type identifies and analyzes webpage elements.

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Extract all product information](./1404-extract-all-product-information.md)

**Next:** [Find interactive elements →](./1406-find-interactive-elements.md)
