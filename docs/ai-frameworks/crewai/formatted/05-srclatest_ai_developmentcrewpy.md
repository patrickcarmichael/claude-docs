---
title: "Crewai: src/latest_ai_development/crew.py"
description: "src/latest_ai_development/crew.py section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# src/latest_ai_development/crew.py

from crewai import Agent, Crew, Process
from crewai.project import CrewBase, agent, crew
from crewai_tools import SerperDevTool

@CrewBase
class LatestAiDevelopmentCrew():
  """LatestAiDevelopment crew"""

  agents_config = "config/agents.yaml"

  @agent
  def researcher(self) -> Agent:
    return Agent(
      config=self.agents_config['researcher'], # type: ignore[index]
      verbose=True,
      tools=[SerperDevTool()]
    )

  @agent
  def reporting_analyst(self) -> Agent:
    return Agent(
      config=self.agents_config['reporting_analyst'], # type: ignore[index]
      verbose=True
    )
```

<Note>
  The names you use in your YAML files (`agents.yaml`) should match the method names in your Python code.
</Note>

### Direct Code Definition

You can create agents directly in code by instantiating the `Agent` class. Here's a comprehensive example showing all available parameters:

```python Code theme={null}
from crewai import Agent
from crewai_tools import SerperDevTool

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← src/latest_ai_development/config/agents.yaml](./04-srclatest_ai_developmentconfigagentsyaml.md)

**Next:** [Create an agent with all available parameters →](./06-create-an-agent-with-all-available-parameters.md)
