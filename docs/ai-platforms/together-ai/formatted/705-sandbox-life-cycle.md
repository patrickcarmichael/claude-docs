---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Sandbox life-cycle

By default a Sandbox will be created from a template. A template is a memory/fs snapshot of a Sandbox, meaning it will be a direct continuation of the template. If the template was running a dev server, that dev server is running when the Sandbox is created.

When you create, resume or restart a Sandbox you can access its `bootupType`. This value indicates how the Sandbox was started.

**FORK**: The Sandbox was created from a template. This happens when you call `create` successfully.\
**RUNNING**: The Sandbox was already running. This happens when you call `resume` and the Sandbox was already running.\
**RESUME**: The Sandbox was resumed from hibernation. This happens when you call `resume` and the Sandbox was hibernated.\
**CLEAN**: The Sandbox was created or resumed from scratch. This happens when you call `create` or `resume` and the Sandbox was not running and was missing a snapshot. This can happen if the Sandbox was shut down, restarted, the snapshot was expired (old snapshot) or if something went wrong.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
