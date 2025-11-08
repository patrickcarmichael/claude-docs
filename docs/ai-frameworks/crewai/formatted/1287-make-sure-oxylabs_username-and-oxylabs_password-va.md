---
title: "Crewai: make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set"
description: "make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set

tool = OxylabsGoogleSearchScraperTool()

result = tool.run(query="iPhone 16")

print(result)
```

### Parameters

* `query` - search keyword.
* `domain` - domain localization for Google.
* `start_page` - starting page number.
* `pages` - number of pages to retrieve.
* `limit` - number of results to retrieve in each page.
* `locale` - `Accept-Language` header value which changes your Google search page web interface language.
* `geo_location` - the geographical location that the result should be adapted for. Using this parameter correctly is extremely important to get the right data.
* `user_agent_type` - device type and browser.
* `render` - enables JavaScript rendering when set to `html`.
* `callback_url` - URL to your callback endpoint.
* `context` - Additional advanced settings and controls for specialized requirements.
* `parse` - returns parsed data when set to true.
* `parsing_instructions` - define your own parsing and data transformation logic that will be executed on an HTML scraping result.

### Advanced example

```python  theme={null}
from crewai_tools import OxylabsGoogleSearchScraperTool

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← `OxylabsGoogleSearchScraperTool`](./1286-oxylabsgooglesearchscrapertool.md)

**Next:** [make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set →](./1288-make-sure-oxylabs_username-and-oxylabs_password-va.md)
