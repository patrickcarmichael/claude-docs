---
title: "Crewai: How It Works"
description: "How It Works section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## How It Works


When reasoning is enabled, before executing a task, the agent will:

1. Reflect on the task and create a detailed plan
2. Evaluate whether it's ready to execute the task
3. Refine the plan as necessary until it's ready or max\_reasoning\_attempts is reached
4. Inject the reasoning plan into the task description before execution

This process helps the agent break down complex tasks into manageable steps and identify potential challenges before starting.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage](./273-usage.md)

**Next:** [Configuration Options →](./275-configuration-options.md)
