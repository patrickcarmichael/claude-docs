---
title: "Crewai: Understanding CrewAI's Prompt System"
description: "Understanding CrewAI's Prompt System section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Understanding CrewAI's Prompt System


Under the hood, CrewAI employs a modular prompt system that you can customize extensively:

* **Agent templates** – Govern each agent's approach to their assigned role.
* **Prompt slices** – Control specialized behaviors such as tasks, tool usage, and output structure.
* **Error handling** – Direct how agents respond to failures, exceptions, or timeouts.
* **Tool-specific prompts** – Define detailed instructions for how tools are invoked or utilized.

Check out the [original prompt templates in CrewAI's repository](https://github.com/crewAIInc/crewAI/blob/main/src/crewai/translations/en.json) to see how these elements are organized. From there, you can override or adapt them as needed to unlock advanced behaviors.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Why Customize Prompts?](./354-why-customize-prompts.md)

**Next:** [Understanding Default System Instructions →](./356-understanding-default-system-instructions.md)
