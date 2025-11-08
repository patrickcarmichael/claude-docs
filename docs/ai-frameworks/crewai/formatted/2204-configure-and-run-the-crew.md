---
title: "Crewai: Configure and run the crew"
description: "Configure and run the crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Configure and run the crew

crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=True
)

try:
    result = crew.kickoff()
finally:
    maxim.cleanup()  # Ensure cleanup happens even if errors occur
```

That's it! All your CrewAI agent interactions will now be logged and available in your Maxim dashboard.

Check this Google Colab Notebook for a quick reference - [Notebook](https://colab.research.google.com/drive/1ZKIZWsmgQQ46n8TH9zLsT1negKkJA6K8?usp=sharing)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define the task](./2203-define-the-task.md)

**Next:** [Viewing Your Traces →](./2205-viewing-your-traces.md)
