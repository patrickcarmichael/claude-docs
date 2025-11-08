---
title: "Crewai: Parameters"
description: "Parameters section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Parameters


The `ScrapegraphScrapeTool` accepts the following parameters during initialization:

* **api\_key**: Optional. Your Scrapegraph API key. If not provided, it will look for the `SCRAPEGRAPH_API_KEY` environment variable.
* **website\_url**: Optional. The URL of the website to scrape. If provided during initialization, the agent won't need to specify it when using the tool.
* **user\_prompt**: Optional. Custom instructions for content extraction. If provided during initialization, the agent won't need to specify it when using the tool.
* **enable\_logging**: Optional. Whether to enable logging for the Scrapegraph client. Default is `False`.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool with predefined parameters](./1320-initialize-the-tool-with-predefined-parameters.md)

**Next:** [Usage →](./1322-usage.md)
