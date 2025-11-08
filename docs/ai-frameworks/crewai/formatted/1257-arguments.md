---
title: "Crewai: Arguments"
description: "Arguments section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Arguments


* `api_key`: Optional. Specifies Firecrawl API key. Defaults is the `FIRECRAWL_API_KEY` environment variable.
* `url`: The URL to scrape.
* `page_options`: Optional.
  * `onlyMainContent`: Optional. Only return the main content of the page excluding headers, navs, footers, etc.
  * `includeHtml`: Optional. Include the raw HTML content of the page. Will output a html key in the response.
* `extractor_options`: Optional. Options for LLM-based extraction of structured information from the page content
  * `mode`: The extraction mode to use, currently supports 'llm-extraction'
  * `extractionPrompt`: Optional. A prompt describing what information to extract from the page
  * `extractionSchema`: Optional. The schema for the data to be extracted
* `timeout`: Optional. Timeout in milliseconds for the request

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example](./1256-example.md)

**Next:** [Hyperbrowser Load Tool →](./1258-hyperbrowser-load-tool.md)
