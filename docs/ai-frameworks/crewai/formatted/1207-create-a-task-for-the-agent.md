---
title: "Crewai: Create a task for the agent"
description: "Create a task for the agent section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a task for the agent

research_task = Task(
    description="""
    Search for information about data science projects and tutorials 
    in the YouTube channel {youtube_channel_handle}. 
    
    Focus on:
    1. Key data science techniques covered
    2. Popular tutorial series
    3. Most viewed or recommended videos
    
    Provide a comprehensive summary of these points.
    """,
    expected_output="A detailed summary of data science content available on the channel.",
    agent=channel_researcher,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./1206-define-an-agent-that-uses-the-tool.md)

**Next:** [Run the task →](./1208-run-the-task.md)
