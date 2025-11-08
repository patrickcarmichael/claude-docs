---
title: "Crewai: Features"
description: "Features section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Features


* Weave automatically captures all CrewAI operations: agent interactions and task executions; LLM calls with metadata and token usage; tool usage and results.
* The integration supports all CrewAI execution methods: `kickoff()`, `kickoff_for_each()`, `kickoff_async()`, and `kickoff_for_each_async()`.
* Automatic tracing of all [crewAI-tools](https://github.com/crewAIInc/crewAI-tools).
* Flow feature support with decorator patching (`@start`, `@listen`, `@router`, `@or_`, `@and_`).
* Track custom guardrails passed to CrewAI `Task` with `@weave.op()`.

For detailed information on what's supported, visit the [Weave CrewAI documentation](https://weave-docs.wandb.ai/guides/integrations/crewai/#getting-started-with-flow).

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setup Instructions](./2293-setup-instructions.md)

**Next:** [Resources →](./2295-resources.md)
