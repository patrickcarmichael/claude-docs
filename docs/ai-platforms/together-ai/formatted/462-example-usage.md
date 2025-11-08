---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example Usage

```py
  task = """
  Implement a Stack with:
  1. push(x)
  2. pop()
  3. getMin()
  All operations should be O(1).
  """

  loop_workflow(task, EVALUATOR_PROMPT, GENERATOR_PROMPT)
```
```typescript
  const task = dedent`
    Implement a Stack with:

      1. push(x)
      2. pop()
      3. getMin()

    All operations should be O(1).
  `;

  loopWorkflow(task, EVALUATOR_PROMPT, GENERATOR_PROMPT);
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
