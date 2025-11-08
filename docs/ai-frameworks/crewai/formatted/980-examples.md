---
title: "Crewai: Examples"
description: "Examples section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Examples


### Direct usage

```python Code theme={null}
from crewai_tools import OCRTool

print(OCRTool().run(image_path_url="/tmp/receipt.png"))
```

### With an agent

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import OCRTool

ocr = OCRTool()

agent = Agent(
    role="OCR", 
    goal="Extract text", 
    tools=[ocr],
)

task = Task(
    description="Extract text from https://example.com/invoice.jpg", 
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

**Previous:** [← Parameters](./979-parameters.md)

**Next:** [Notes →](./981-notes.md)
