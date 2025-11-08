---
title: "Crewai: Arguments"
description: "Arguments section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Arguments


| Argument                | Type     | Description                                                                                                                       |
| :---------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| **api\_key**            | `string` | Specifies Spider API key. If not specified, it looks for `SPIDER_API_KEY` in environment variables.                               |
| **params**              | `object` | Optional parameters for the request. Defaults to `{"return_format": "markdown"}` to optimize content for LLMs.                    |
| **request**             | `string` | Type of request to perform (`http`, `chrome`, `smart`). `smart` defaults to HTTP, switching to JavaScript rendering if needed.    |
| **limit**               | `int`    | Max pages to crawl per website. Set to `0` or omit for unlimited.                                                                 |
| **depth**               | `int`    | Max crawl depth. Set to `0` for no limit.                                                                                         |
| **cache**               | `bool`   | Enables HTTP caching to speed up repeated runs. Default is `true`.                                                                |
| **budget**              | `object` | Sets path-based limits for crawled pages, e.g., `{"*":1}` for root page only.                                                     |
| **locale**              | `string` | Locale for the request, e.g., `en-US`.                                                                                            |
| **cookies**             | `string` | HTTP cookies for the request.                                                                                                     |
| **stealth**             | `bool`   | Enables stealth mode for Chrome requests to avoid detection. Default is `true`.                                                   |
| **headers**             | `object` | HTTP headers as a map of key-value pairs for all requests.                                                                        |
| **metadata**            | `bool`   | Stores metadata about pages and content, aiding AI interoperability. Defaults to `false`.                                         |
| **viewport**            | `object` | Sets Chrome viewport dimensions. Default is `800x600`.                                                                            |
| **encoding**            | `string` | Specifies encoding type, e.g., `UTF-8`, `SHIFT_JIS`.                                                                              |
| **subdomains**          | `bool`   | Includes subdomains in the crawl. Default is `false`.                                                                             |
| **user\_agent**         | `string` | Custom HTTP user agent. Defaults to a random agent.                                                                               |
| **store\_data**         | `bool`   | Enables data storage for the request. Overrides `storageless` when set. Default is `false`.                                       |
| **gpt\_config**         | `object` | Allows AI to generate crawl actions, with optional chaining steps via an array for `"prompt"`.                                    |
| **fingerprint**         | `bool`   | Enables advanced fingerprinting for Chrome.                                                                                       |
| **storageless**         | `bool`   | Prevents all data storage, including AI embeddings. Default is `false`.                                                           |
| **readability**         | `bool`   | Pre-processes content for reading via [Mozilla’s readability](https://github.com/mozilla/readability). Improves content for LLMs. |
| **return\_format**      | `string` | Format to return data: `markdown`, `raw`, `text`, `html2text`. Use `raw` for default page format.                                 |
| **proxy\_enabled**      | `bool`   | Enables high-performance proxies to avoid network-level blocking.                                                                 |
| **query\_selector**     | `string` | CSS query selector for content extraction from markup.                                                                            |
| **full\_resources**     | `bool`   | Downloads all resources linked to the website.                                                                                    |
| **request\_timeout**    | `int`    | Timeout in seconds for requests (5-60). Default is `30`.                                                                          |
| **run\_in\_background** | `bool`   | Runs the request in the background, useful for data storage and triggering dashboard crawls. No effect if `storageless` is set.   |

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example](./1392-example.md)

**Next:** [Stagehand Tool →](./1394-stagehand-tool.md)
