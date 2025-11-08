---
title: "Crewai: Referring to Other Tasks"
description: "Referring to Other Tasks section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Referring to Other Tasks


In CrewAI, the output of one task is automatically relayed into the next one, but you can specifically define what tasks' output, including multiple, should be used as context for another task.

This is useful when you have a task that depends on the output of another task that is not performed immediately after it. This is done through the `context` attribute of the task:

```python Code theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← to perform a semantic search for a specified query from a text's content across the internet](./314-to-perform-a-semantic-search-for-a-specified-query.md)

**Next:** [... →](./316-.md)
