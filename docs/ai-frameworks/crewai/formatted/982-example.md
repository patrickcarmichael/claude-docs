---
title: "Crewai: Example"
description: "Example section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example


```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import OCRTool

tool = OCRTool()

agent = Agent(
    role="OCR Specialist",
    goal="Extract text from images",
    backstory="Vision‑enabled analyst",
    tools=[tool],
    verbose=True,
)

task = Task(
    description="Extract text from https://example.com/receipt.png",
    expected_output="All detected text in plain text",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Notes](./981-notes.md)

**Next:** [Overview →](./983-overview.md)
