---
title: "Crewai: Define an agent that uses the tool"
description: "Define an agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define an agent that uses the tool

video_researcher = Agent(
    role="Video Researcher",
    goal="Extract relevant information from YouTube videos",
    backstory="An expert researcher who specializes in analyzing video content.",
    tools=[youtube_search_tool],
    verbose=True,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool for general YouTube video searches](./1216-initialize-the-tool-for-general-youtube-video-sear.md)

**Next:** [Example task to search for information in a specific video →](./1218-example-task-to-search-for-information-in-a-specif.md)
