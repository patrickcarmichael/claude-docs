---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example

```python
  import os
  from crewai import LLM, Task, Agent, Crew

  llm = LLM(
      model="together_ai/meta-llama/Llama-3.3-70B-Instruct-Turbo",
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  research_agent = Agent(
      llm=llm,
      role="Research Analyst",
      goal="Find and summarize information about specific topics",
      backstory="You are an experienced researcher with attention to detail",
      verbose=True,  # Enable logging for debugging

  )

  research_task = Task(
      description="Conduct a thorough research about AI Agents.",
      expected_output="A list with 10 bullet points of the most relevant information about AI Agents",
      agent=research_agent,
  )

  # Execute the crew

  crew = Crew(
      agents=[research_agent],
      tasks=[research_task],
      verbose=True,
  )

  result = crew.kickoff()

  # Accessing the task output

  task_output = research_task.output

  print(task_output)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
