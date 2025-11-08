---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Export tool specifications for manual testing

reward-kit agent-eval --task-dir examples/your_agent_task_bundle/ --export-tools ./tool_specs
```

### Task Bundle Structure

A task bundle is a directory containing the following files:

* `reward.py`: Reward function with @reward\_function decorator
* `tools.py`: Tool registry with tool definitions
* `task.jsonl`: Dataset rows with task specifications
* `seed.sql` (optional): Initial database state

See the [Agent Evaluation](/evaluators/developer_guide/agent_evaluation) guide for more details.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
