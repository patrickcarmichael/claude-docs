---
title: "Crewai: 2. External Memory"
description: "2. External Memory section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## 2. External Memory


External Memory provides a standalone memory system that operates independently from the crew's built-in memory. This is ideal for specialized memory providers or cross-application memory sharing.

### Basic External Memory with Mem0

```python  theme={null}
import os
from crewai import Agent, Crew, Process, Task
from crewai.memory.external.external_memory import ExternalMemory

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Compare performance](./239-compare-performance.md)

**Next:** [Create external memory instance with local Mem0 Configuration →](./241-create-external-memory-instance-with-local-mem0-co.md)
