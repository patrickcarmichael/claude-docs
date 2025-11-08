---
title: "Crewai: Create an Agent using Llama-specific layouts"
description: "Create an Agent using Llama-specific layouts section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an Agent using Llama-specific layouts

principal_engineer = Agent(
    role="Principal Engineer",
    goal="Oversee AI architecture and make high-level decisions",
    backstory="You are the lead engineer responsible for critical AI systems",
    verbose=True,
    llm="groq/llama-3.3-70b-versatile",  # Using the Llama 3 model
    system_template=system_template,
    prompt_template=prompt_template,
    response_template=response_template,
    tools=[DirectoryReadTool(), FileReadTool()]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define templates for system, user (prompt), and assistant (response) messages](./370-define-templates-for-system-user-prompt-and-assist.md)

**Next:** [Define a sample task →](./372-define-a-sample-task.md)
