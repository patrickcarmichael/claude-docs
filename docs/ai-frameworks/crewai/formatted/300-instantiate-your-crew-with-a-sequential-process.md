---
title: "Crewai: Instantiate your crew with a sequential process"
description: "Instantiate your crew with a sequential process section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Instantiate your crew with a sequential process

crew = Crew(
    agents=[blog_agent],
    tasks=[task1],
    verbose=True,
    process=Process.sequential,
)

result = crew.kickoff()

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Getting Structured Consistent Outputs from Tasks](./299-getting-structured-consistent-outputs-from-tasks.md)

**Next:** [Option 1: Accessing Properties Using Dictionary-Style Indexing →](./301-option-1-accessing-properties-using-dictionary-sty.md)
