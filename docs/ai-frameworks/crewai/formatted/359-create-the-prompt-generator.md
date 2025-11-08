---
title: "Crewai: Create the prompt generator"
description: "Create the prompt generator section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create the prompt generator

prompt_generator = Prompts(
    agent=agent,
    has_tools=len(agent.tools) > 0,
    use_system_prompt=agent.use_system_prompt
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create a sample task](./358-create-a-sample-task.md)

**Next:** [Generate and inspect the actual prompt →](./360-generate-and-inspect-the-actual-prompt.md)
