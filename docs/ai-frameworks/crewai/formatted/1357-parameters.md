---
title: "Crewai: Parameters"
description: "Parameters section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Parameters


The `ScrapflyScrapeWebsiteTool` accepts the following parameters:

### Initialization Parameters

* **api\_key**: Required. Your Scrapfly API key.

### Run Parameters

* **url**: Required. The URL of the website to scrape.
* **scrape\_format**: Optional. The format in which to extract the web page content. Options are "raw" (HTML), "markdown", or "text". Default is "markdown".
* **scrape\_config**: Optional. A dictionary containing additional Scrapfly scraping configuration options.
* **ignore\_scrape\_failures**: Optional. Whether to ignore failures during scraping. If set to `True`, the tool will return `None` instead of raising an exception when scraping fails.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← }](./1356-.md)

**Next:** [Scrapfly Configuration Options →](./1358-scrapfly-configuration-options.md)
