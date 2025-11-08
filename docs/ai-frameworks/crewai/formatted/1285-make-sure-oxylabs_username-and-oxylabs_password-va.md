---
title: "Crewai: make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set"
description: "make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set

tool = OxylabsAmazonSearchScraperTool(
    config={
        "domain": 'nl',
        "start_page": 2,
        "pages": 2,
        "parse": True,
        "context": [
            {'key': 'category_id', 'value': 16391693031}
        ],
    }
)

result = tool.run(query='nirvana tshirt')

print(result)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set](./1284-make-sure-oxylabs_username-and-oxylabs_password-va.md)

**Next:** [`OxylabsGoogleSearchScraperTool` →](./1286-oxylabsgooglesearchscrapertool.md)
