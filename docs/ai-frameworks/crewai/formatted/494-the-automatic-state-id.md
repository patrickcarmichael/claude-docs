---
title: "Crewai: The Automatic State ID"
description: "The Automatic State ID section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## The Automatic State ID


Both unstructured and structured states automatically receive a unique identifier (UUID) to help track and manage state instances.

### How It Works

* For unstructured state, the ID is accessible as `self.state["id"]`
* For structured state, the ID is accessible as `self.state.id`
* This ID is generated automatically when the flow is created
* The ID remains the same throughout the flow's lifecycle
* The ID can be used for tracking, logging, and retrieving persisted states

This UUID is particularly valuable when implementing persistence or tracking multiple flow executions.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the flow](./493-run-the-flow.md)

**Next:** [Dynamic State Updates →](./495-dynamic-state-updates.md)
