---
title: "Crewai: Create specialized agents"
description: "Create specialized agents section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create specialized agents

data_collector = Agent(
    role='Data Collection Specialist',
    goal='Gather and preprocess data from various sources',
    backstory='I specialize in collecting and cleaning data from multiple sources.',
    tools=[data_collection_tool]
)

data_analyst = Agent(
    role='Data Analysis Expert',
    goal='Perform advanced analysis on collected data',
    backstory='I am an expert in statistical analysis and machine learning.',
    tools=[analysis_tool]
)

report_generator = Agent(
    role='Report Generation Specialist',
    goal='Create comprehensive reports and visualizations',
    backstory='I excel at creating clear, actionable reports from complex data.',
    tools=[reporting_tool]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize different automation tools](./2381-initialize-different-automation-tools.md)

**Next:** [Create sequential tasks →](./2383-create-sequential-tasks.md)
