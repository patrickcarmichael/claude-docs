---
title: "Crewai: make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set"
description: "make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set

tool = OxylabsUniversalScraperTool(
    config={
        "render": "html",
        "user_agent_type": "mobile",
        "context": [
            {"key": "force_headers", "value": True},
            {"key": "force_cookies", "value": True},
            {
                "key": "headers",
                "value": {
                    "Custom-Header-Name": "custom header content",
                },
            },
            {
                "key": "cookies",
                "value": [
                    {"key": "NID", "value": "1234567890"},
                    {"key": "1P JAR", "value": "0987654321"},
                ],
            },
            {"key": "http_method", "value": "get"},
            {"key": "follow_redirects", "value": True},
            {"key": "successful_status_codes", "value": [808, 909]},
        ],
    }
)

result = tool.run(url="https://ip.oxylabs.io")

print(result)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set](./1290-make-sure-oxylabs_username-and-oxylabs_password-va.md)

**Next:** [Scrape Element From Website Tool →](./1292-scrape-element-from-website-tool.md)
