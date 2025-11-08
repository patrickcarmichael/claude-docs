---
title: "Crewai: Example task to search for information in a specific video"
description: "Example task to search for information in a specific video section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example task to search for information in a specific video

research_task = Task(
    description="Search for information about machine learning frameworks in the YouTube video at {youtube_video_url}",
    expected_output="A summary of the key machine learning frameworks mentioned in the video.",
    agent=video_researcher,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./1217-define-an-agent-that-uses-the-tool.md)

**Next:** [Create and run the crew →](./1219-create-and-run-the-crew.md)
