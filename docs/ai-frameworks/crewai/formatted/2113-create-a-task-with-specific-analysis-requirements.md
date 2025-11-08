---
title: "Crewai: Create a task with specific analysis requirements"
description: "Create a task with specific analysis requirements section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a task with specific analysis requirements

inspection_task = Task(
    description="""
    Analyze the product image at https://example.com/product.jpg with focus on:
    1. Quality of materials
    2. Manufacturing defects
    3. Compliance with standards
    Provide a detailed report highlighting any issues found.
    """,
    expected_output="A detailed report highlighting any issues found",
    agent=expert_analyst
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create a multimodal agent for detailed analysis](./2112-create-a-multimodal-agent-for-detailed-analysis.md)

**Next:** [Create and run the crew →](./2114-create-and-run-the-crew.md)
