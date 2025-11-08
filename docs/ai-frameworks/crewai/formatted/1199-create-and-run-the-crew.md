---
title: "Crewai: Create and run the crew"
description: "Create and run the crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create and run the crew

crew = Crew(agents=[channel_researcher], tasks=[research_task])
result = crew.kickoff(inputs={"youtube_channel_handle": "@exampleChannel"})
```

You can also initialize the tool with a specific YouTube channel handle:

```python Code theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example task to search for information in a specific channel](./1198-example-task-to-search-for-information-in-a-specif.md)

**Next:** [Initialize the tool with a specific YouTube channel handle →](./1200-initialize-the-tool-with-a-specific-youtube-channe.md)
