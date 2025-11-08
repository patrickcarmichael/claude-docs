---
title: "Crewai: make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set"
description: "make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set

tool = OxylabsGoogleSearchScraperTool(
    config={
        "parse": True,
        "geo_location": "Paris, France",
        "user_agent_type": "tablet",
    }
)

result = tool.run(query="iPhone 16")

print(result)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set](./1287-make-sure-oxylabs_username-and-oxylabs_password-va.md)

**Next:** [`OxylabsUniversalScraperTool` →](./1289-oxylabsuniversalscrapertool.md)
