---
title: "Crewai: Arguments"
description: "Arguments section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Arguments


The following parameters can be used to customize the `BrowserbaseLoadTool`'s behavior:

| Argument          | Type     | Description                                                                           |
| :---------------- | :------- | :------------------------------------------------------------------------------------ |
| **api\_key**      | `string` | *Optional*. Browserbase API key. Default is `BROWSERBASE_API_KEY` env variable.       |
| **project\_id**   | `string` | *Optional*. Browserbase Project ID. Default is `BROWSERBASE_PROJECT_ID` env variable. |
| **text\_content** | `bool`   | *Optional*. Retrieve only text content. Default is `False`.                           |
| **session\_id**   | `string` | *Optional*. Provide an existing Session ID.                                           |
| **proxy**         | `bool`   | *Optional*. Enable/Disable Proxies. Default is `False`.                               |

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool with the Browserbase API key and Project ID](./1244-initialize-the-tool-with-the-browserbase-api-key-a.md)

**Next:** [Firecrawl Crawl Website →](./1246-firecrawl-crawl-website.md)
