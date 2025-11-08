---
title: "Langgraph: Resuming Workflows"
description: "Resuming Workflows section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Resuming Workflows


Once you have enabled durable execution in your workflow, you can resume execution for the following scenarios:

- **Pausing and Resuming Workflows:** Use the [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Interrupt) function to pause a workflow at specific points and the [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command) primitive to resume it with updated state. See [**Human-in-the-Loop**](./human_in_the_loop.md) for more details.
- **Recovering from Failures:** Automatically resume workflows from the last successful checkpoint after an exception (e.g., LLM provider outage). This involves executing the workflow with the same thread identifier by providing it with a `None` as the input value (see this [example](../how-tos/use-functional-api.md#resuming-after-an-error) with the functional API).

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Using tasks in nodes](./418-using-tasks-in-nodes.md)

**Next:** [Starting Points for Resuming Workflows →](./420-starting-points-for-resuming-workflows.md)
