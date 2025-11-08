---
title: "Crewai: Define an agent that uses the tool"
description: "Define an agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define an agent that uses the tool

video_researcher = Agent(
    role="Video Researcher",
    goal="Extract relevant information from a specific YouTube video",
    backstory="An expert researcher who specializes in analyzing video content.",
    tools=[youtube_search_tool],
    verbose=True,
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool with a specific YouTube video URL](./1220-initialize-the-tool-with-a-specific-youtube-video-.md)

**Next:** [Parameters →](./1222-parameters.md)
