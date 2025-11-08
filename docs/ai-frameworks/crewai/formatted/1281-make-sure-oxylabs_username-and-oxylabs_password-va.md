---
title: "Crewai: make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set"
description: "make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set

tool = OxylabsAmazonProductScraperTool()

result = tool.run(query="AAAAABBBBCC")

print(result)
```

### Parameters

* `query` - 10-symbol ASIN code.
* `domain` - domain localization for Amazon.
* `geo_location` - the *Deliver to* location.
* `user_agent_type` - device type and browser.
* `render` - enables JavaScript rendering when set to `html`.
* `callback_url` - URL to your callback endpoint.
* `context` - Additional advanced settings and controls for specialized requirements.
* `parse` - returns parsed data when set to true.
* `parsing_instructions` - define your own parsing and data transformation logic that will be executed on an HTML scraping result.

### Advanced example

```python  theme={null}
from crewai_tools import OxylabsAmazonProductScraperTool

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← `OxylabsAmazonProductScraperTool`](./1280-oxylabsamazonproductscrapertool.md)

**Next:** [make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set →](./1282-make-sure-oxylabs_username-and-oxylabs_password-va.md)
