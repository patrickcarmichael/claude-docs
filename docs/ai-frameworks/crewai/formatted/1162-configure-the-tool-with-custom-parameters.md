---
title: "Crewai: Configure the tool with custom parameters"
description: "Configure the tool with custom parameters section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Configure the tool with custom parameters

custom_extractor = TavilyExtractorTool(
    extract_depth='advanced',
    include_images=True,
    timeout=120
)

agent_with_custom_tool = Agent(
    role="Advanced Content Extractor",
    goal="Extract comprehensive content with images",
    tools=[custom_extractor]
)
```

### Tool Parameters

You can customize the tool's behavior by setting parameters during initialization:

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example with multiple URLs and advanced extraction](./1161-example-with-multiple-urls-and-advanced-extraction.md)

**Next:** [Initialize with custom configuration →](./1163-initialize-with-custom-configuration.md)
