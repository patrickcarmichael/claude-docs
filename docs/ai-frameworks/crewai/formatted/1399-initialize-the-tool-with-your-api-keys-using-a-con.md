---
title: "Crewai: Initialize the tool with your API keys using a context manager"
description: "Initialize the tool with your API keys using a context manager section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Initialize the tool with your API keys using a context manager

with StagehandTool(
    api_key="your-browserbase-api-key",
    project_id="your-browserbase-project-id",
    model_api_key="your-llm-api-key",  # OpenAI or Anthropic API key
    model_name=AvailableModel.CLAUDE_3_7_SONNET_LATEST,  # Optional: specify which model to use
) as stagehand_tool:
    # Create an agent with the tool
    researcher = Agent(
        role="Web Researcher",
        goal="Find and summarize information from websites",
        backstory="I'm an expert at finding information online.",
        verbose=True,
        tools=[stagehand_tool],
    )

    # Create a task that uses the tool
    research_task = Task(
        description="Go to https://www.example.com and tell me what you see on the homepage.",
        agent=researcher,
    )

    # Run the crew
    crew = Crew(
        agents=[researcher],
        tasks=[research_task],
        verbose=True,
    )

    result = crew.kickoff()
    print(result)
```

#### 2. Manual Resource Management

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import StagehandTool
from stagehand.schemas import AvailableModel

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage](./1398-usage.md)

**Next:** [Initialize the tool with your API keys →](./1400-initialize-the-tool-with-your-api-keys.md)
