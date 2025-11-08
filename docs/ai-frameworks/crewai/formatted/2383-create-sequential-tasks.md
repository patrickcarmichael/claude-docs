---
title: "Crewai: Create sequential tasks"
description: "Create sequential tasks section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create sequential tasks

collection_task = Task(
    description="Collect market data for Q4 2024 analysis",
    agent=data_collector
)

analysis_task = Task(
    description="Analyze collected data to identify trends and patterns",
    agent=data_analyst
)

reporting_task = Task(
    description="Generate executive summary report with key insights and recommendations",
    agent=report_generator
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create specialized agents](./2382-create-specialized-agents.md)

**Next:** [Create a crew with sequential processing →](./2384-create-a-crew-with-sequential-processing.md)
