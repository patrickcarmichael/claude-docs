---
title: "Crewai: Example task to search for information in a specific channel"
description: "Example task to search for information in a specific channel section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example task to search for information in a specific channel

research_task = Task(
    description="Search for information about machine learning tutorials in the YouTube channel {youtube_channel_handle}",
    expected_output="A summary of the key machine learning tutorials available on the channel.",
    agent=channel_researcher,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./1197-define-an-agent-that-uses-the-tool.md)

**Next:** [Create and run the crew →](./1199-create-and-run-the-crew.md)
