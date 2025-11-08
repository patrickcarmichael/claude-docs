---
title: "Crewai: make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set"
description: "make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set

tool = OxylabsUniversalScraperTool()

result = tool.run(url="https://ip.oxylabs.io")

print(result)
```

### Parameters

* `url` - website url to scrape.
* `user_agent_type` - device type and browser.
* `geo_location` - sets the proxy's geolocation to retrieve data.
* `render` - enables JavaScript rendering when set to `html`.
* `callback_url` - URL to your callback endpoint.
* `context` - Additional advanced settings and controls for specialized requirements.
* `parse` - returns parsed data when set to `true`, as long as a dedicated parser exists for the submitted URL's page type.
* `parsing_instructions` - define your own parsing and data transformation logic that will be executed on an HTML scraping result.

### Advanced example

```python  theme={null}
from crewai_tools import OxylabsUniversalScraperTool

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← `OxylabsUniversalScraperTool`](./1289-oxylabsuniversalscrapertool.md)

**Next:** [make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set →](./1291-make-sure-oxylabs_username-and-oxylabs_password-va.md)
