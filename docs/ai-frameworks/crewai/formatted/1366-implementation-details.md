---
title: "Crewai: Implementation Details"
description: "Implementation Details section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Implementation Details


The `ScrapflyScrapeWebsiteTool` uses the Scrapfly SDK to interact with the Scrapfly API:

```python Code theme={null}
class ScrapflyScrapeWebsiteTool(BaseTool):
    name: str = "Scrapfly web scraping API tool"
    description: str = (
        "Scrape a webpage url using Scrapfly and return its content as markdown or text"
    )
    
    # Implementation details...
    
    def _run(
        self,
        url: str,
        scrape_format: str = "markdown",
        scrape_config: Optional[Dict[str, Any]] = None,
        ignore_scrape_failures: Optional[bool] = None,
    ):
        from scrapfly import ScrapeApiResponse, ScrapeConfig

        scrape_config = scrape_config if scrape_config is not None else {}
        try:
            response: ScrapeApiResponse = self.scrapfly.scrape(
                ScrapeConfig(url, format=scrape_format, **scrape_config)
            )
            return response.scrape_result["content"]
        except Exception as e:
            if ignore_scrape_failures:
                logger.error(f"Error fetching data from {url}, exception: {e}")
                return None
            else:
                raise e
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create a task that instructs the agent to handle errors](./1365-create-a-task-that-instructs-the-agent-to-handle-e.md)

**Next:** [Conclusion →](./1367-conclusion.md)
