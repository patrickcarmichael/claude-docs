---
title: "Crewai: Create an agent that uses the tool"
description: "Create an agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent that uses the tool

extractor_agent = Agent(
    role='Web Content Extractor',
    goal='Extract key information from specified web pages',
    backstory='You are an expert at extracting relevant content from websites using the Tavily API.',
    tools=[tavily_tool],
    verbose=True
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool](./1155-initialize-the-tool.md)

**Next:** [Define a task for the agent →](./1157-define-a-task-for-the-agent.md)
