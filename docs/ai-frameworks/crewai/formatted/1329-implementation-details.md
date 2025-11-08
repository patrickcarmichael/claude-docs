---
title: "Crewai: Implementation Details"
description: "Implementation Details section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Implementation Details


The `ScrapegraphScrapeTool` uses the Scrapegraph Python client to interact with the SmartScraper API:

```python Code theme={null}
class ScrapegraphScrapeTool(BaseTool):
    """
    A tool that uses Scrapegraph AI to intelligently scrape website content.
    """
    
    # Implementation details...
    
    def _run(self, **kwargs: Any) -> Any:
        website_url = kwargs.get("website_url", self.website_url)
        user_prompt = (
            kwargs.get("user_prompt", self.user_prompt)
            or "Extract the main content of the webpage"
        )

        if not website_url:
            raise ValueError("website_url is required")

        # Validate URL format
        self._validate_url(website_url)

        try:
            # Make the SmartScraper request
            response = self._client.smartscraper(
                website_url=website_url,
                user_prompt=user_prompt,
            )

            return response
        # Error handling...
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Rate Limiting](./1328-rate-limiting.md)

**Next:** [Conclusion →](./1330-conclusion.md)
