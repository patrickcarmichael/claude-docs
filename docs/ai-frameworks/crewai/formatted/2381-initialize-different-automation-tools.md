---
title: "Crewai: Initialize different automation tools"
description: "Initialize different automation tools section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Initialize different automation tools

data_collection_tool = InvokeCrewAIAutomationTool(
    crew_api_url="https://data-collection-crew-[...].crewai.com",
    crew_bearer_token="your_bearer_token_here",
    crew_name="Data Collection Automation",
    crew_description="Collects and preprocesses raw data"
)

analysis_tool = InvokeCrewAIAutomationTool(
    crew_api_url="https://analysis-crew-[...].crewai.com",
    crew_bearer_token="your_bearer_token_here",
    crew_name="Analysis Automation",
    crew_description="Performs advanced data analysis and modeling"
)

reporting_tool = InvokeCrewAIAutomationTool(
    crew_api_url="https://reporting-crew-[...].crewai.com",
    crew_bearer_token="your_bearer_token_here",
    crew_name="Reporting Automation",
    crew_description="Generates comprehensive reports and visualizations"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create and execute a task with custom parameters](./2380-create-and-execute-a-task-with-custom-parameters.md)

**Next:** [Create specialized agents →](./2382-create-specialized-agents.md)
