---
title: "Crewai: Create tool with custom inputs"
description: "Create tool with custom inputs section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create tool with custom inputs

market_research_tool = InvokeCrewAIAutomationTool(
    crew_api_url="https://state-of-ai-report-crew-[...].crewai.com",
    crew_bearer_token="your_bearer_token_here",
    crew_name="State of AI Report",
    crew_description="Retrieves a comprehensive report on state of AI for a given year and region",
    crew_inputs=custom_inputs,
    max_polling_time=15 * 60  # 15 minutes timeout
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define custom input schema](./2377-define-custom-input-schema.md)

**Next:** [Create an agent with the tool →](./2379-create-an-agent-with-the-tool.md)
