---
title: "Crewai: Define custom input schema"
description: "Define custom input schema section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define custom input schema

custom_inputs = {
    "year": Field(..., description="Year to retrieve the report for (integer)"),
    "region": Field(default="global", description="Geographic region for analysis"),
    "format": Field(default="summary", description="Report format (summary, detailed, raw)")
}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Advanced Usage](./2376-advanced-usage.md)

**Next:** [Create tool with custom inputs →](./2378-create-tool-with-custom-inputs.md)
