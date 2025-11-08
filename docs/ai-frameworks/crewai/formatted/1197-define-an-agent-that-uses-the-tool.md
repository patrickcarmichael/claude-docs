---
title: "Crewai: Define an agent that uses the tool"
description: "Define an agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define an agent that uses the tool

channel_researcher = Agent(
    role="Channel Researcher",
    goal="Extract relevant information from YouTube channels",
    backstory="An expert researcher who specializes in analyzing YouTube channel content.",
    tools=[youtube_channel_tool],
    verbose=True,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool for general YouTube channel searches](./1196-initialize-the-tool-for-general-youtube-channel-se.md)

**Next:** [Example task to search for information in a specific channel →](./1198-example-task-to-search-for-information-in-a-specif.md)
