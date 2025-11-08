---
title: "Crewai: Example with multiple URLs and advanced extraction"
description: "Example with multiple URLs and advanced extraction section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example with multiple URLs and advanced extraction

multi_extract_task = Task(
    description='Extract content from https://example.com and https://anotherexample.org using advanced extraction.',
    expected_output='A JSON string containing the extracted content from both URLs.',
    agent=extractor_agent
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Advanced Usage](./1160-advanced-usage.md)

**Next:** [Configure the tool with custom parameters →](./1162-configure-the-tool-with-custom-parameters.md)
