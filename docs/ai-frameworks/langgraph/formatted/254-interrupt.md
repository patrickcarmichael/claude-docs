---
title: "Langgraph: Interrupt"
description: "Interrupt section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Interrupt


This option interrupts the current execution but saves all the work done up until that point. 
It then inserts the user input and continues from there. 

If you enable this option, your graph should be able to handle weird edge cases that may arise. 
For example, you could have called a tool but not yet gotten back a result from running that tool.
You may need to remove that tool call in order to not have a dangling tool call.

See the [how-to guide](../cloud/how-tos/interrupt_concurrent.md) for configuring the interrupt double text option.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Enqueue](./253-enqueue.md)

**Next:** [Rollback →](./255-rollback.md)
