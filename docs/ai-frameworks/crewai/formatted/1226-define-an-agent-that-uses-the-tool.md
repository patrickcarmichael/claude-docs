---
title: "Crewai: Define an agent that uses the tool"
description: "Define an agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define an agent that uses the tool

video_researcher = Agent(
    role="Video Researcher",
    goal="Extract and analyze information from YouTube videos",
    backstory="""You are an expert video researcher who specializes in extracting 
    and analyzing information from YouTube videos. You have a keen eye for detail 
    and can quickly identify key points and insights from video content.""",
    tools=[youtube_search_tool],
    verbose=True,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool](./1225-initialize-the-tool.md)

**Next:** [Create a task for the agent →](./1227-create-a-task-for-the-agent.md)
