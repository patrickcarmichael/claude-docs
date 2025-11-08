---
title: "Crewai: Parameters"
description: "Parameters section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Parameters


The `SeleniumScrapingTool` accepts the following parameters during initialization:

* **website\_url**: Optional. The URL of the website to scrape. If provided during initialization, the agent won't need to specify it when using the tool.
* **css\_element**: Optional. The CSS selector for the elements to extract. If provided during initialization, the agent won't need to specify it when using the tool.
* **cookie**: Optional. A dictionary containing cookie information, useful for simulating a logged-in session to access restricted content.
* **wait\_time**: Optional. Specifies the delay (in seconds) before scraping, allowing the website and any dynamic content to fully load. Default is `3` seconds.
* **return\_html**: Optional. Whether to return the HTML content instead of just the text. Default is `False`.

When using the tool with an agent, the agent will need to provide the following parameters (unless they were specified during initialization):

* **website\_url**: Required. The URL of the website to scrape.
* **css\_element**: Required. The CSS selector for the elements to extract.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./1378-define-an-agent-that-uses-the-tool.md)

**Next:** [Agent Integration Example →](./1380-agent-integration-example.md)
