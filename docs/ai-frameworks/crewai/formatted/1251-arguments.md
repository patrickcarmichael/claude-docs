---
title: "Crewai: Arguments"
description: "Arguments section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Arguments


* `api_key`: Optional. Specifies Firecrawl API key. Defaults is the `FIRECRAWL_API_KEY` environment variable.
* `url`: The base URL to start crawling from.
* `page_options`: Optional.
  * `onlyMainContent`: Optional. Only return the main content of the page excluding headers, navs, footers, etc.
  * `includeHtml`: Optional. Include the raw HTML content of the page. Will output a html key in the response.
* `crawler_options`: Optional. Options for controlling the crawling behavior.
  * `includes`: Optional. URL patterns to include in the crawl.
  * `exclude`: Optional. URL patterns to exclude from the crawl.
  * `generateImgAltText`: Optional. Generate alt text for images using LLMs (requires a paid plan).
  * `returnOnlyUrls`: Optional. If true, returns only the URLs as a list in the crawl status. Note: the response will be a list of URLs inside the data, not a list of documents.
  * `maxDepth`: Optional. Maximum depth to crawl. Depth 1 is the base URL, depth 2 includes the base URL and its direct children, and so on.
  * `mode`: Optional. The crawling mode to use. Fast mode crawls 4x faster on websites without a sitemap but may not be as accurate and shouldn't be used on heavily JavaScript-rendered websites.
  * `limit`: Optional. Maximum number of pages to crawl.
  * `timeout`: Optional. Timeout in milliseconds for the crawling operation.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example](./1250-example.md)

**Next:** [Firecrawl Scrape Website →](./1252-firecrawl-scrape-website.md)
