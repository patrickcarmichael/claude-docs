---
title: "Crewai: Create and run the crew"
description: "Create and run the crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create and run the crew

crew = Crew(agents=[video_researcher], tasks=[research_task])
result = crew.kickoff(inputs={"youtube_video_url": "https://youtube.com/watch?v=example"})
```

You can also initialize the tool with a specific YouTube video URL:

```python Code theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example task to search for information in a specific video](./1218-example-task-to-search-for-information-in-a-specif.md)

**Next:** [Initialize the tool with a specific YouTube video URL →](./1220-initialize-the-tool-with-a-specific-youtube-video-.md)
