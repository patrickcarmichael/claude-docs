---
title: "Crewai: Example"
description: "Example section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example


```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import PDFTextWritingTool

tool = PDFTextWritingTool()

agent = Agent(
    role="PDF Editor",
    goal="Annotate PDFs",
    backstory="Documentation specialist",
    tools=[tool],
    verbose=True,
)

task = Task(
    description="Write 'CONFIDENTIAL' at (72, 720) on page 1 of ./sample.pdf",
    expected_output="Confirmation message",
    agent=agent,
)

crew = Crew(
    agents=[agent], 
    tasks=[task],
    verbose=True,
)

result = crew.kickoff()
```

### Direct usage

```python Code theme={null}
from crewai_tools import PDFTextWritingTool

PDFTextWritingTool().run(
  pdf_path="./input.pdf",
  text="CONFIDENTIAL",
  position=(72, 720),
  font_size=18,
  page_number=0,
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Parameters](./993-parameters.md)

**Next:** [Tips →](./995-tips.md)
