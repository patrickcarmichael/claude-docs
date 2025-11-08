---
title: "Crewai: Error Handling"
description: "Error Handling section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Error Handling


The `ScrapegraphScrapeTool` may raise the following exceptions:

* **ValueError**: When API key is missing or URL format is invalid.
* **RateLimitError**: When API rate limits are exceeded.
* **RuntimeError**: When scraping operation fails (network issues, API errors).

It's recommended to instruct agents to handle potential errors gracefully:

```python Code theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1325-run-the-task.md)

**Next:** [Create a task that includes error handling instructions →](./1327-create-a-task-that-includes-error-handling-instruc.md)
