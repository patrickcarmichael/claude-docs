---
title: "Crewai: Getting Structured Consistent Outputs from Tasks"
description: "Getting Structured Consistent Outputs from Tasks section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Getting Structured Consistent Outputs from Tasks


<Note>
  It's also important to note that the output of the final task of a crew becomes the final output of the actual crew itself.
</Note>

### Using `output_pydantic`

The `output_pydantic` property allows you to define a Pydantic model that the task output should conform to. This ensures that the output is not only structured but also validated according to the Pydantic model.

Here's an example demonstrating how to use output\_pydantic:

```python Code theme={null}
import json

from crewai import Agent, Crew, Process, Task
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    content: str

blog_agent = Agent(
    role="Blog Content Generator Agent",
    goal="Generate a blog title and content",
    backstory="""You are an expert content creator, skilled in crafting engaging and informative blog posts.""",
    verbose=False,
    allow_delegation=False,
    llm="gpt-4o",
)

task1 = Task(
    description="""Create a blog title and content on a given topic. Make sure the content is under 200 words.""",
    expected_output="A compelling blog title and well-written content.",
    agent=blog_agent,
    output_pydantic=Blog,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task Guardrails](./298-task-guardrails.md)

**Next:** [Instantiate your crew with a sequential process →](./300-instantiate-your-crew-with-a-sequential-process.md)
