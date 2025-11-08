---
title: "Crewai: Define an agent that uses the tool"
description: "Define an agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define an agent that uses the tool

channel_researcher = Agent(
    role="Channel Researcher",
    goal="Extract relevant information from a specific YouTube channel",
    backstory="An expert researcher who specializes in analyzing YouTube channel content.",
    tools=[youtube_channel_tool],
    verbose=True,
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool with a specific YouTube channel handle](./1200-initialize-the-tool-with-a-specific-youtube-channe.md)

**Next:** [Parameters →](./1202-parameters.md)
