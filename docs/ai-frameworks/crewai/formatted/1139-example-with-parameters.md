---
title: "Crewai: Example with Parameters"
description: "Example with Parameters section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example with Parameters


Here is an example demonstrating how to use the tool with additional parameters:

```python Code theme={null}
from crewai_tools import SerperDevTool

tool = SerperDevTool(
    search_url="https://google.serper.dev/scholar",
    n_results=2,
)

print(tool.run(search_query="ChatGPT"))

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Parameters](./1138-parameters.md)

**Next:** [Using Tool: Search the internet →](./1140-using-tool-search-the-internet.md)
