---
title: "Crewai: Define the task with output_json set to the Blog model"
description: "Define the task with output_json set to the Blog model section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define the task with output_json set to the Blog model

task1 = Task(
    description="""Create a blog title and content on a given topic. Make sure the content is under 200 words.""",
    expected_output="A JSON object with 'title' and 'content' fields.",
    agent=blog_agent,
    output_json=Blog,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define the agent](./306-define-the-agent.md)

**Next:** [Instantiate the crew with a sequential process →](./308-instantiate-the-crew-with-a-sequential-process.md)
