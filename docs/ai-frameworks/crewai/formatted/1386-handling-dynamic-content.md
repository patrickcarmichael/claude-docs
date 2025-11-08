---
title: "Crewai: Handling Dynamic Content"
description: "Handling Dynamic Content section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Handling Dynamic Content


The `SeleniumScrapingTool` is particularly useful for scraping websites with dynamic content that is loaded via JavaScript. By using a real browser instance, it can:

1. Execute JavaScript on the page
2. Wait for dynamic content to load
3. Interact with elements if needed
4. Extract content that would not be available with simple HTTP requests

You can adjust the `wait_time` parameter to ensure that all dynamic content has loaded before extraction.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Implementation Details](./1385-implementation-details.md)

**Next:** [Conclusion →](./1387-conclusion.md)
