---
title: "Crewai: **Max Usage Count**"
description: "**Max Usage Count** section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## **Max Usage Count**


You can set a maximum usage count for a tool to prevent it from being used more than a certain number of times.
By default, the max usage count is unlimited.

```python  theme={null}
from crewai_tools import FileReadTool

tool = FileReadTool(max_usage_count=5, ...)
```

Ready to explore? Pick a category above to discover tools that fit your use case!

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Add tools to your agent](./1030-add-tools-to-your-agent.md)

**Next:** [Arxiv Paper Tool →](./1032-arxiv-paper-tool.md)
