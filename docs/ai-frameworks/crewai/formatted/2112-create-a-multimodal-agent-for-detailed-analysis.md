---
title: "Crewai: Create a multimodal agent for detailed analysis"
description: "Create a multimodal agent for detailed analysis section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a multimodal agent for detailed analysis

expert_analyst = Agent(
    role="Visual Quality Inspector",
    goal="Perform detailed quality analysis of product images",
    backstory="Senior quality control expert with expertise in visual inspection",
    multimodal=True  # AddImageTool is automatically included
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create and run the crew](./2111-create-and-run-the-crew.md)

**Next:** [Create a task with specific analysis requirements →](./2113-create-a-task-with-specific-analysis-requirements.md)
