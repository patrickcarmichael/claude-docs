---
title: "Crewai: The Simplest Way to Customize Prompts"
description: "The Simplest Way to Customize Prompts section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## The Simplest Way to Customize Prompts


One straightforward approach is to create a JSON file for the prompts you want to override and then point your Crew at that file:

1. Craft a JSON file with your updated prompt slices.
2. Reference that file via the `prompt_file` parameter in your Crew.

CrewAI then merges your customizations with the defaults, so you don't have to redefine every prompt. Here's how:

### Example: Basic Prompt Customization

Create a `custom_prompts.json` file with the prompts you want to modify. Ensure you list all top-level prompts it should contain, not just your changes:

```json  theme={null}
{
  "slices": {
    "format": "When responding, follow this structure:\n\nTHOUGHTS: Your step-by-step thinking\nACTION: Any tool you're using\nRESULT: Your final answer or conclusion"
  }
}
```

Then integrate it like so:

```python  theme={null}
from crewai import Agent, Crew, Task, Process

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Best Practices for Managing Prompt Files](./364-best-practices-for-managing-prompt-files.md)

**Next:** [Create agents and tasks as normal →](./366-create-agents-and-tasks-as-normal.md)
