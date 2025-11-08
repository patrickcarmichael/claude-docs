---
title: "Crewai: Create a task for the agent"
description: "Create a task for the agent section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a task for the agent

research_task = Task(
    description="""
    Search for information about recent advancements in artificial intelligence 
    in the YouTube video at {youtube_video_url}. 
    
    Focus on:
    1. Key AI technologies mentioned
    2. Real-world applications discussed
    3. Future predictions made by the speaker
    
    Provide a comprehensive summary of these points.
    """,
    expected_output="A detailed summary of AI advancements, applications, and future predictions from the video.",
    agent=video_researcher,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./1226-define-an-agent-that-uses-the-tool.md)

**Next:** [Run the task →](./1228-run-the-task.md)
