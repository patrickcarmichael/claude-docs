---
title: "Crewai: Parameters"
description: "Parameters section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Parameters


The `HyperbrowserLoadTool` accepts the following parameters:

### Constructor Parameters

* **api\_key**: Optional. Your Hyperbrowser API key. If not provided, it will be read from the `HYPERBROWSER_API_KEY` environment variable.

### Run Parameters

* **url**: Required. The website URL to scrape or crawl.
* **operation**: Optional. The operation to perform on the website. Either 'scrape' or 'crawl'. Default is 'scrape'.
* **params**: Optional. Additional parameters for the scrape or crawl operation.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./1265-define-an-agent-that-uses-the-tool.md)

**Next:** [Supported Parameters →](./1267-supported-parameters.md)
