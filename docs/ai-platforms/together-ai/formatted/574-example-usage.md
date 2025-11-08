---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example Usage

```typescript
  async function main() {
    const task = `Write a product description for a new eco-friendly water bottle.
      The target_audience is environmentally conscious millennials and key product
      features are: plastic-free, insulated, lifetime warranty
    `;

    const workerResponses = await orchestratorWorkflow(
      task,
      ORCHESTRATOR_PROMPT,
      WORKER_PROMPT,
    );

    console.log(
      workerResponses
        .map((w) => `## WORKER RESULT (${w.task.type})\n${w.response}`)

        .join("\n\n"),
    );
  }

  main();
```
```typescript
  async function main() {
    const task = `Write a product description for a new eco-friendly water bottle.
      The target_audience is environmentally conscious millennials and key product
      features are: plastic-free, insulated, lifetime warranty
    `;

    const workerResponses = await orchestratorWorkflow(
      task,
      ORCHESTRATOR_PROMPT,
      WORKER_PROMPT,
    );

    console.log(
      workerResponses
        .map((w) => `## WORKER RESULT (${w.task.type})\n${w.response}`)

        .join("\n\n"),
    );
  }

  main();
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
