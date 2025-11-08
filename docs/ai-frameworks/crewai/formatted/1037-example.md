---
title: "Crewai: Example"
description: "Example section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example


```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import ArxivPaperTool

tool = ArxivPaperTool(
    download_pdfs=False,
    save_dir="./arxiv_pdfs",
    use_title_as_filename=True,
)

agent = Agent(
    role="Researcher",
    goal="Find relevant arXiv papers",
    backstory="Expert at literature discovery",
    tools=[tool],
    verbose=True,
)

task = Task(
    description="Search arXiv for 'transformer neural network' and list top 5 results.",
    expected_output="A concise list of 5 relevant papers with titles, links, and summaries.",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```

### Direct usage (without Agent)

```python Code theme={null}
from crewai_tools import ArxivPaperTool

tool = ArxivPaperTool(
    download_pdfs=True, 
    save_dir="./arxiv_pdfs",
)
print(tool.run(search_query="mixture of experts", max_results=3))
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Steps to Get Started](./1036-steps-to-get-started.md)

**Next:** [Parameters →](./1038-parameters.md)
