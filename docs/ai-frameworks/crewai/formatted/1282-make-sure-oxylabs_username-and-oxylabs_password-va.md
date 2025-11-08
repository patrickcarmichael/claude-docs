---
title: "Crewai: make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set"
description: "make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set

tool = OxylabsAmazonProductScraperTool(
    config={
        "domain": "com",
        "parse": True,
        "context": [
            {
                "key": "autoselect_variant",
                "value": True
            }
        ]
    }
)

result = tool.run(query="AAAAABBBBCC")

print(result)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set](./1281-make-sure-oxylabs_username-and-oxylabs_password-va.md)

**Next:** [`OxylabsAmazonSearchScraperTool` →](./1283-oxylabsamazonsearchscrapertool.md)
